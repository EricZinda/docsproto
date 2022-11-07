import copy
import json
import os
import posixpath
import shutil
import subprocess
import sys
import urllib.parse
from urllib import request
from urllib.error import HTTPError
from urllib.request import Request

from marko import Markdown
import marko
from marko import Parser
from marko.ext.gfm import GFM
from marko.md_renderer import MarkdownRenderer
from marko.renderer import Renderer
from marko.inline import Link

import createblanksite


# Given a link that was in a document but not included in the site definitions (and thus will be broken in the final site),
# give a proposal for what to include to make it not broken for it and recursively follow *its* links and do the same
def propose_link_recursive(input_content_root, proposals, repositories_definitions, sites_definitions, unique_existing_pages, parser, base_referrer, link_to_check):
    # See if the link is a markdown file
    file_name, file_extension = os.path.splitext(link_to_check["TargetFile"])
    if file_extension.lower() == ".md":
        link_file_identity = link_to_check["SrcDir"] + "/" + link_to_check["TargetFile"]
        if link_file_identity not in unique_existing_pages and link_file_identity not in proposals:
            # The file is not included in the site or proposed yet, add it as a proposal
            link_file_definition = {"Site": link_to_check["Site"], "Section": link_to_check["Section"], "Page": link_to_check["LinkTarget"],
                                    "SrcDir": link_to_check["SrcDir"], "SrcFile": link_to_check["TargetFile"], "BaseReferrer": base_referrer,
                                    "Referrer": f'{link_to_check["Site"]}/{link_to_check["SrcFile"]}'}
            proposals[link_file_identity] = link_file_definition

            link_file_path = os.path.join(input_content_root, link_file_definition["SrcDir"], link_file_definition["SrcFile"])
            if os.path.exists(link_file_path):
                # The link file is a file in the project, scan it
                with open(link_file_path, "r") as txtFile:
                    result = parser.parse(txtFile.read())
                    further_links = convert_child(repositories_definitions, sites_definitions, link_file_definition, result)
                    for further_link in further_links:
                        if further_link["LinkState"] == "relative_broken":
                            # Now check the further links
                            propose_link_recursive(input_content_root, proposals, repositories_definitions,
                                                   sites_definitions, unique_existing_pages, parser, base_referrer,
                                                   further_link)

            else:
                # File doesn't exist
                link_file_definition["FileMissing"] = True


def get_change_text(repositories_definitions, sites_definitions, file_definition, src_file_path):
    global quickAndDirty
    if quickAndDirty:
        return "<update date omitted for speed>"
    else:
        if file_definition["SrcDir"] in repositories_definitions:
            repository = repositories_definitions[file_definition["SrcDir"]]["Repository"]
            file_name, file_extension = os.path.splitext(file_definition["SrcFile"])

            if repository.endswith("/wiki"):
                link = f"https://github.com/{repository}/{file_name}/_edit"
            else:
                link = f"https://github.com/{repository}/edit/main/{file_definition['SrcFile']}"

        else:
            link = ""

        workingDirectory = os.path.dirname(src_file_path)
        # TODO: would running the whole list at once be more efficient? cat filelist.txt | while read filename; do echo "$filename $(git log -s -n1 --pretty='tformat:%an - %cs' $filename)"; done
        result = subprocess.check_output([f"git log -s -n1 --pretty='tformat:%cs by %an' {src_file_path}"], cwd=workingDirectory, shell=True).decode("utf-8")
        final = "\nLast update: " + result.strip() + (f" [[edit]({link})]" if link != "" else "")
        # print(f"Source: {src_file_path} {final}")
        return final


# Convert the links in file src_file_path to properly refer to documents in the new site structure
# Add anything to the file (like "[edit]") that we want to insert as well
# Finally, actually perform the copy into the new site
def convert_and_copy_doc(repositories_definitions, sites_definitions, parser, file_definition, src_file_path, dst_file_path):
    file_name, file_extension = os.path.splitext(src_file_path)

    # Only mess with markdown files, others are copied as is
    if file_extension.lower() == ".md":
        with open(src_file_path, "r") as txtFile:
            try:
                result = parser.parse(txtFile.read())
            except Exception as error:
                raise Exception(f"Markdown parser crashed parsing file: {src_file_path}. See if there are markdown formatting issues in that file or maybe exclude it and report the bug.")

            # Recursively walk the document tree and do any conversion that is needed (e.g. fixing links)
            links = convert_child(repositories_definitions, sites_definitions, file_definition, result)

        with open(dst_file_path, "w") as txtFile:
            final_result = parser.render(result)
            # wrap all markdown with raw/endraw so that Jekyll won't interpret {{ as being a Jekyll liquid expression
            txtFile.write("{% raw %}")
            txtFile.write(final_result)
            txtFile.write(get_change_text(repositories_definitions, sites_definitions, file_definition, src_file_path))
            txtFile.write("{% endraw %}")
            print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")

    else:
        shutil.copy2(src_file_path, dst_file_path)
        print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")
        links = []

    return links


# convert any child node that is a link to have the proper link
# in the new site structure
def convert_child(repositories_definitions, sites_definitions, file_definition, node):
    links = []
    if isinstance(node, Link):
        link_data = copy.deepcopy(file_definition)

        # Remember the original information in the link
        link_data["Link"] = node.dest
        # LinkTarget is the relative URL Address of the link with no adornments (i.e. #fragments)
        link_target, _, _ = parse_relative_link(file_definition["SrcFile"], node.dest)
        link_data["LinkTarget"] = link_target

        link_state, message, target_file, node.dest = get_rerouted_link(repositories_definitions, sites_definitions, file_definition, node.dest)
        link_data["ResolvedLink"] = node.dest
        link_data["TargetFile"] = target_file
        link_data["LinkState"] = link_state
        link_data["LinkStateMessage"] = message
        links.append(link_data)

    elif hasattr(node, "children"):
        for child in node.children:
            links += convert_child(repositories_definitions, sites_definitions, file_definition, child)

    return links


# In the Github wiki:
# 1. links with no beginning slashes are links to other wiki topics in the same wiki
#   - They can have "#" to link to a heading within that page
# 2. links starting with slashes ("root-relative links") link to http://github.com since that is the root they are on
#   - this can be legit for linking to another github project, subproject, etc
#   - They can have "#" to link to a heading within that page
# 3. links with "http(s)" are public websites
#
# See the "ALinkTest.md" file in the project for examples of common mistakes that are made in the wiki
#
# If this is a local link to another wiki topic, it returns information about it (case 1 above)
# Otherwise, it is a link outside the wiki and is ignored
#
# returns the target segment of the link, query, fragment
# returns None if this is not a local link
def parse_relative_link(SrcFile, link):
    split_url = urllib.parse.urlparse(link)
    if split_url.scheme == "" and split_url.netloc == "":
        # This is a local link
        # If the link is on the same page (i.e. "#heading", use the page as the path
        if split_url.path == "":
            file_name, _ = os.path.splitext(SrcFile)
            path = file_name
        else:
            path = split_url.path

        path_parts = path.split('/')
        if path_parts[0] == "":
            # Leading "/" means it is "root relative" and would be interpreted as "http://www.github.com" + <path> when run in the wiki
            # Thus: treat it as an absolute path
            return None, None, None
        elif len(path_parts) > 1:
            # More than one segment won't work in the wiki so treat it as absolute
            return None, None, None

        return path, split_url.query, split_url.fragment
    else:
        return None, None, None


# if a source markdown file has a link like: [this is a link](targetaddress)
# "targetaddress" might be included in the same site OR it might be in a different site
# This function returns the right link that should be embedded in the markdown file
#
# Algorithm:
# The "identity" of a file is a combination of src_dir + src_file because that represents a file in a
# repository (and the repository has been cloned into a source directory: src_dir).  There can be only one of these.
# There is a relative URL for it that other things in the same site can use
# There is an absolute URL for it that anyone can use.
#
# If a different file has a relative md link to something it could be to
# - "targetaddress.md": it is definitely a markdown file, the easy case
# or
# - "targetaddress": it *might* be a markdown file, or it could be something else
#
# Since the markdown file lives in a repository, and the link is *relative*
# the md link must be to a file in that repository
#
# That gives us enough information to determine the identity of the file, and with that we can determine what
# the link *should be* in the new site layout.
#
# Returns: StateOfLink, LinkStateMessage, The file the link is targeting (if any), rerouted link that should be used in new site
def get_rerouted_link(repositories_definitions, sites_definitions, file_definition, original_link):
    src_site = file_definition["Site"]
    src_dir = file_definition["SrcDir"]

    path, query, fragment = parse_relative_link(file_definition["SrcFile"], original_link)
    if path is not None:
        # This is a relative link
        # First convert relative_md_link to have an .md extension if it doesn't have an extension
        # otherwise leave it
        file_name, file_extension = os.path.splitext(path)
        if file_extension.lower() == "":
            # Assume it was a markdown file
            target_file = path + ".md"
        else:
            target_file = path

        # Now we know the identity of the file since it is a relative link and we have a filename AND a src_dir
        # See if we can find that definition
        # Add "../" since jekyll handles relative links by adding them onto the current url, which refers to the current file
        # which is thus one level too deep
        relative_resolved_link = "../" + path + ("?" + query if query != "" else "") + ("#" + fragment if fragment != "" else "")
        for definition in sites_definitions:
            if definition["SrcDir"] == src_dir and definition["SrcFile"] == target_file:
                # Found it! Now return a relative link if it is in the same site or a full link if not
                if definition["Site"] == src_site:
                    return "relative_success", None, target_file, relative_resolved_link
                else:
                    return "relative_success", None, target_file, definition["AbsoluteLink"]

        # If if it doesn't exist, return the proper link that *would have* accessed it
        return "relative_broken", "Wiki page doesn't exist", target_file, relative_resolved_link

    else:
        # non-relative link
        global url_check
        if not url_check:
            return "absolute_unchecked", None, None, original_link

        # Determine what the root for this page was originally
        original_root_url = urllib.parse.urljoin("https://www.github.com", repositories_definitions[src_dir]["Repository"])

        # see if it exists
        result = check_url(original_root_url, original_link)
        if result["Status"] == "success":
            # If it exists at that location, assume it is legit
            return "absolute_success", None, None, original_link
        elif result["Status"] == "connection_failure":
            return "absolute_unknown_due_to_connection_failure", result["Message"], None, original_link
        else:
            # It wasn't found, which means either it truly is broken OR
            # it was a mistyped link that was really supposed to reference a wiki topic
            # See if it references a wiki topic
            if original_link[0] == "/":
                # StateOfLink, The file the link is targeting (if any), rerouted link that should be used in new site
                wiki_link_state, _, wiki_targeted_file, new_link = get_rerouted_link(repositories_definitions, sites_definitions, file_definition, original_link[1:])
                if wiki_link_state == "relative_success":
                    return "absolute_broken_but_valid_misformed_wiki_link", result["Message"], wiki_targeted_file, original_link
                else:
                    # just a plain old broken link
                    return "absolute_broken", result["Message"], None, original_link
            else:
                # just a plain old broken link
                return "absolute_broken", result["Message"], None, original_link


# See if a url would have been valid in the original wiki
def check_url(base_url, url):
    split_url = urllib.parse.urlparse(url)
    # no "http" etc on the front, treat as relative to root
    if split_url.scheme == "":
        url = urllib.parse.urljoin(base_url, url)

    check_data = {"Message": None, "Status": None}
    try:
        # give it 5 seconds
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            the_page = response.read()
            check_data["Message"] = "success"
            check_data["Status"] = "success"

    except HTTPError as http_error:
        if http_error.code == 406:
            # "406: Not acceptable, just means I got the user agent wrong...
            check_data["Message"] = "success"
            check_data["Status"] = "success"
        else:
            check_data["Message"] = f"{http_error.code}: {http_error.msg}"
            check_data["Status"] = "not_found"

    except Exception as err:
        check_data["Status"] = "connection_failure"
        check_data["Message"] = f"Exception: {str(err)}"

    return check_data


def get_site_relative_page_link(site, src_file):
    # if it is an md file, just strip the extension to make a relative link to the site root
    file_name, file_extension = os.path.splitext(src_file)
    if file_extension.lower() == ".md":
        return file_name
    else:
        return src_file


def add_addresses_for_definition(root_address, definition):
    file_name, file_extension = os.path.splitext(definition["SrcFile"])
    definition["RootRelativeLink"] = file_name
    site_root = posixpath.join(root_address, definition["Site"])
    definition["AbsoluteLink"] = posixpath.join(site_root, file_name)


def add_addresses_for_definitions(root_address, sites_definitions):
    for definition in sites_definitions:
        add_addresses_for_definition(root_address, definition)


# Given a definition file that contains all the site definitions create the latestsrc folder structure
# We do it all at once so we can check for broken links
def populate_sites_src(sites_definition, root_address, src_root, dst_root):
    parser = Markdown(Parser, MarkdownRenderer)
    add_addresses_for_definitions(root_address, sites_definition["Pages"])

    errors = []
    links = []
    docs = {}
    tocs = {}
    for fileDefinition in sites_definition["Pages"]:
        src_file = os.path.join(src_root, fileDefinition["SrcDir"], fileDefinition["SrcFile"])
        dst_file = os.path.join(dst_root, fileDefinition["Site"], fileDefinition["SrcFile"])

        # Remember this doc in the site so we can find broken links later
        file_site = fileDefinition["Site"]
        if fileDefinition["Site"] not in docs:
            docs[file_site] = {}
        path_lower = get_site_relative_page_link(file_site, fileDefinition["SrcFile"]).lower()
        docs[file_site][path_lower] = copy.deepcopy(fileDefinition)

        if fileDefinition["Section"] != "<todo>":
            # links += convert_and_copy_doc(sites_definition["Pages"], parser, fileDefinition, src_file, dst_file)
            try:
                links += convert_and_copy_doc(sites_definition["SourceRepositories"], sites_definition["Pages"], parser, fileDefinition, src_file, dst_file)
            except Exception as error:
                errors.append({"Definition": fileDefinition, "Error": str(error)})

            if fileDefinition["Site"] not in tocs:
                tocs[fileDefinition["Site"]] = []
            site_relative_link = get_site_relative_page_link(fileDefinition["Site"], fileDefinition["SrcFile"])
            tocs[fileDefinition["Site"]].append({"Section": fileDefinition["Section"], "Page": fileDefinition["Page"], "Link": site_relative_link, "SrcFile": fileDefinition["SrcFile"]})

    return docs, links, tocs, errors


def create_tocs(dst_root, tocs):
    for site in tocs.items():
        sections = {}
        for entry in site[1]:
            if entry["Section"] not in sections:
                sections[entry["Section"]] = []
            sections[entry["Section"]].append({"Name": entry["Page"], "Link": entry["Link"], "SrcFile": entry["SrcFile"]})

        # Build the TOC text
        toc_text = "toc:\n"
        for section in sections.items():
            toc_text += f'  - title: "{section[0]}"\n'
            toc_text +=  '    children:\n'
            for page in section[1]:
                toc_text += f'      - title: "{page["Name"]}"\n'
                toc_text += f'        url: "/{page["Link"]}/"\n'

        # Write it to the navigation file
        navfile_path = os.path.join(dst_root, site[0], "_data", "navigation.yml")
        with open(navfile_path, "a") as txtFile:
            txtFile.write(toc_text)


# Given the full set of links on all pages propose entries to sitedefinitions.json to fix
# any that are broken
def propose_broken_links(all_links, sites_definitions, input_content_root, unique_existing_pages):
    parser = Markdown(Parser, MarkdownRenderer)
    proposals = {}
    for link in all_links:
        if link["LinkState"] == "relative_broken":
            base_referrer = f'{link["Site"]}/{link["SrcFile"]}'
            propose_link_recursive(input_content_root, proposals, sites_definitions["SourceRepositories"], sites_definitions["Pages"], unique_existing_pages, parser, base_referrer, link)

    return proposals


def log_json_items_to_file(relative_path, list):
    script_path = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(script_path, relative_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, "w") as txt_file:
        txt_file.write("[\n")
        txt_file.write(",\n".join([json.dumps(item) for item in list]))
        txt_file.write("\n]\n")


# {
#     "concept": [
#         {"Section": "ErgSemantics", "Pages": [
#           {"Page": "ErgSemantics_Inventory", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Inventory.md", "Referrer": "concept/ErgSemantics.md"},
#           {"Page": "RedwoodsTop", "SrcDir": "docswiki", "SrcFile": "RedwoodsTop.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgProcessing", "SrcDir": "docswiki", "SrcFile": "ErgProcessing.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgSemantics_Discovery", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Discovery.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "MatrixMrsTestSuite", "SrcDir": "docswiki", "SrcFile": "MatrixMrsTestSuite.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgSemantics_HowToCite", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_HowToCite.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true}
#         ]}
#     ],
#     "tools": [
#         {"Section": "Tools", "Pages": [
#           {"Page": "ErgSemantics_Inventory", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Inventory.md", "Referrer": "concept/ErgSemantics.md"},
#           {"Page": "RedwoodsTop", "SrcDir": "docswiki", "SrcFile": "RedwoodsTop.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgProcessing", "SrcDir": "docswiki", "SrcFile": "ErgProcessing.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgSemantics_Discovery", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Discovery.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "MatrixMrsTestSuite", "SrcDir": "docswiki", "SrcFile": "MatrixMrsTestSuite.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true},
#           {"Page": "ErgSemantics_HowToCite", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_HowToCite.md", "Referrer": "concept/ErgSemantics.md", "FileMissing": true}
#         ]}
#     ]
# }
def convert_pages_flat_to_tree(sites_definition):
    converted = {}
    for page in sites_definition:
        if page["Site"] not in converted:
            converted[page["Site"]] = []
        found = None
        for section in converted[page["Site"]]:
            if section["Section"] == page["Section"]:
                found = section
                break
        if found is None:
            found = {"Section": page["Section"], "Pages": []}
            converted[page["Site"]].append(found)

        page_copy = copy.deepcopy(page)
        page_copy.pop("Site")
        page_copy.pop("Section")
        found["Pages"].append(page_copy)

    return converted


def convert_to_flat_definition(sites_definitions):
    converted = {"Pages": [], "SourceRepositories": {}}
    for top_key in sites_definitions.items():
        if top_key[0] == "Pages":
            for site in top_key[1].items():
                site_name = site[0]
                for section in site[1]:
                    for page in section["Pages"]:
                        page_definition = {"Site": site_name, "Section": section["Section"]}
                        page_definition.update(page)
                        converted["Pages"].append(page_definition)
        else:
            converted[top_key[0]] = top_key[1]

    return converted


def log_json_tree_to_file(relative_path, tree):
    script_path = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(script_path, relative_path)
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w") as txt_file:
        txt_file.write("  {\n")
        sites = []
        for site in tree.items():
            site_text = f'    "{site[0]}": [\n'
            sections = []
            for section in site[1]:
                section_text = f'      {{"Section": "{section["Section"]}", "Pages": [\n'
                section_text += ",\n".join(f'        {json.dumps(page)}' for page in section["Pages"])
                section_text += '\n      ]}'
                sections.append(section_text)
            site_text += ",\n".join(sections)
            site_text += '\n    ]'
            sites.append(site_text)
        txt_file.write(",\n".join(sites))
        txt_file.write("\n  }")


quickAndDirty = False
url_check = False

if __name__ == '__main__':
    # with open("/Users/ericzinda/Enlistments/docsproto/testsitesdefinitions.json", "r") as txtFile:
    #     sites_definition = json.loads(txtFile.read())
    #
    # tree_pages = convert_pages_flat_to_tree(sites_definition["Pages"])
    # log_json_tree_to_file("sitesdefinitions1.json", tree_pages)

    if len(sys.argv) >= 6 and len(sys.argv) <= 8:
        root_address = sys.argv[1]
        input_content_root = sys.argv[2]
        latestsrc_root = sys.argv[3]
        latestsites_root = sys.argv[4]
        sites_definitions_path = sys.argv[5]
        if len(sys.argv) > 6:
            if sys.argv[6].strip() == "true":
                quickAndDirty = True

        if len(sys.argv) > 7:
            if sys.argv[7].strip() == "true":
                url_check = True

        errors = []

        try:
            with open(sites_definitions_path, "r") as txtFile:
                sites_definition_tree = json.loads(txtFile.read())
                sites_definition = convert_to_flat_definition(sites_definition_tree)
        except Exception as error:
            errors.append({"Error": f"Error reading '{sites_definitions_path}': {str(error)}"})

        if len(errors) == 0:
            try:
                # Create the sites
                createblanksite.create_blank_sites(root_address, latestsrc_root, latestsites_root, sites_definition)
            except Exception as error:
                errors.append({"Error": f"Error generating blank sites (before populating pages): {str(error)}"})

        if len(errors) == 0:
            try:
                # Populate the sites with pages
                all_pages, all_links, tocs, errors = populate_sites_src(sites_definition, root_address, input_content_root, latestsrc_root)
                create_tocs(latestsrc_root, tocs)
            except Exception as error:
                errors.append({"Error": f"Error while populating sites with pages: {str(error)}"})

        # Log any errors that occurred and fail the build
        if len(errors) > 0:
            reportErrors = []
            for item in errors:
                print(f'{json.dumps(item)}\n')
                reportErrors.append({"Error": item["Error"]})
            log_json_items_to_file("latestsrc/SiteErrors.json", reportErrors)
            print(f"Errors generating site (see 'latestsrc/SiteErrors.txt'\n")
            assert False

        # Log all the pages that were generated
        combined_pages = []
        unique_pages = {}
        for item in all_pages.items():
            combined_pages += item[1].items()
            unique_pages.update(item[1])
        log_json_items_to_file("latestsrc/AllPages.json", combined_pages)

        # Log all links on all pages in all sites
        log_json_items_to_file("latestsrc/AllLinks.json", all_links)

        # Create a file that proposes fixes to the site definitions for all broken links
        proposed_fixes = propose_broken_links(all_links, sites_definition, input_content_root, unique_pages)

        proposed_fixes_tree = convert_pages_flat_to_tree([item[1] for item in proposed_fixes.items()])
        log_json_tree_to_file("latestsrc/FixesForBrokenLinksToWikiPages.json", proposed_fixes_tree)

    else:
        print("Error: Requires 5 arguments: \n1) Root address of site (i.e. sites will be under that URL address)\n2) Full path to where repositories containing docs to be used as source are stored\n3) Full path to the latestsrc directory of the docs repository\n4) Full path to the latestsites directory of the docs repository\n5) Full path and filename of the json file that defines the docs\n (optional) 6) true or false (default false): run in quick and dirty mode which removes things like timestamps on files that take a while to calculate")
        assert False
