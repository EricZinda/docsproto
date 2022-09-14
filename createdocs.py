import copy
import json
import os
import posixpath
import shutil
import sys
import urllib.parse

from marko import Markdown
import marko
from marko import Parser
from marko.ext.gfm import GFM
from marko.md_renderer import MarkdownRenderer
from marko.renderer import Renderer
from marko.inline import Link

import createblanksite


# Given a page
def gather_broken_links_from_page(input_content_root, proposals, sites_definitions, parser, file_definition, src_file_path):
    file_name, file_extension = os.path.splitext(src_file_path)
    if file_extension.lower() == ".md":
        if os.path.exists(src_file_path):
            this_file_identity = file_definition["SrcDir"] + "/" + file_definition["SrcFile"]

            # If the file is in proposals, it is already scanned
            if this_file_identity not in proposals:
                with open(src_file_path, "r") as txtFile:
                    result = parser.parse(txtFile.read())
                    links = convert_child(sites_definitions, file_definition, result)
                    for link in links:
                        if link["LinkState"] == "invalid_relative":
                            file_identity = link["SrcDir"] + "/" + link["TargetFile"]
                            if file_identity not in proposals:
                                proposals[file_identity] = {"Site": link["Site"],
                                                            "Section": link["Section"],
                                                            "Page": link["LinkParts"][-1],
                                                            "SrcDir": link["SrcDir"],
                                                            "SrcFile": link["TargetFile"],
                                                            "Referrer": f'{link["Site"]}/{link["SrcFile"]}'}
                                new_src_file_path = os.path.join(input_content_root, proposals[file_identity]["SrcDir"], proposals[file_identity]["SrcFile"])
                                gather_broken_links_from_page(input_content_root, proposals, sites_definitions, parser, proposals[file_identity], new_src_file_path)
        else:
            file_definition["FileMissing"] = True


def convert_and_copy_doc(sites_definitions, parser, file_definition, src_file_path, dst_file_path):
    file_name, file_extension = os.path.splitext(src_file_path)
    if file_extension.lower() == ".md":
        with open(src_file_path, "r") as txtFile:
            try:
                result = parser.parse(txtFile.read())
            except Exception as error:
                raise Exception(f"Markdown parser crashed parsing file: {src_file_path}. See if there are markdown formatting issues in that file or maybe exclude it and report the bug.")
            links = convert_child(sites_definitions, file_definition, result)

        with open(dst_file_path, "w") as txtFile:
            final_result = parser.render(result)
            # wrap all markdown with raw/endraw so that Jekyll won't interpret {{ as being a Jekyll liquid expression
            txtFile.write("{% raw %}")
            txtFile.write(final_result)
            txtFile.write("{% endraw %}")
            print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")

    else:
        shutil.copy2(src_file_path, dst_file_path)
        print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")
        links = []

    return links


def convert_child(sites_definitions, file_definition, node):
    links = []
    if isinstance(node, Link):
        _, _, _, parts = parse_relative_link(file_definition["SrcFile"], node.dest)
        link_data = copy.deepcopy(file_definition)
        link_data["Link"] = node.dest
        link_state, target_file, node.dest = get_markdown_link_to_relative_target(sites_definitions, file_definition, node.dest)

        link_data["ResolvedLink"] = node.dest
        link_data["TargetFile"] = target_file
        link_data["LinkParts"] = parts
        link_data["LinkState"] = link_state
        links.append(link_data)

    elif hasattr(node, "children"):
        for child in node.children:
            links += convert_child(sites_definitions, file_definition, child)

    return links


# Format:
# targetaddress could be in one of many forms:
#   - foo
#   - foo.md
#   - foo#bar
#   - #bar
#   - /foo/goo#bar
#
# returns the path, query, fragment, and the separated segments of the path of a local link
# returns None if this is not a local link
def parse_relative_link(SrcFile, link):
    split_url = urllib.parse.urlparse(link)
    if split_url.scheme == "" and split_url.netloc == "" and split_url.path[0:4] != "www.":
        # This is a local link
        # If the link is on the same page, use the page as the path
        if split_url.path == "":
            file_name, _ = os.path.splitext(SrcFile)
            path = file_name
        else:
            path = split_url.path

        # Leading "/" refers to a repository, treat it as an absolute path
        path_parts = path.split('/')
        if path_parts[0] == "":
            return None, None, None, None

        return path, split_url.query, split_url.fragment, path_parts
    else:
        return None, None, None, None


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
def get_markdown_link_to_relative_target(sites_definitions, file_definition, relative_md_link):
    src_site = file_definition["Site"]
    src_dir = file_definition["SrcDir"]

    path, query, fragment, parts = parse_relative_link(file_definition["SrcFile"], relative_md_link)
    if path is not None:
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
        for definition in sites_definitions:
            if definition["SrcDir"] == src_dir and definition["SrcFile"] == target_file:
                # Found it! Now return a relative link if it is in the same site or a full link if not
                if definition["Site"] == src_site:
                    # Add "../" since jekyll handles relative links by adding them onto the current url, which refers to the current file
                    # which is thus one level too deep
                    # return "valid_relative", target_file, definition["RootRelativeLink"] + ("?" + query if query != "" else "") + ("#" + fragment if fragment != "" else "")
                    return "valid_relative", target_file, "../" + definition["RootRelativeLink"] + ("?" + query if query != "" else "") + ("#" + fragment if fragment != "" else "")
                else:
                    return "valid_relative", target_file, definition["AbsoluteLink"]

        return "invalid_relative", target_file, relative_md_link

    else:
        # non-relative link, just return the original, but cleaned up
        return "absolute", None, relative_md_link


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

    # get_markdown_link_to_relative_target(sites_definition["Pages"], sites_definition["Pages"][0], "ErgSemantics")

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
                links += convert_and_copy_doc(sites_definition["Pages"], parser, fileDefinition, src_file, dst_file)
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
                toc_text += f'        url: "{page["Link"]}"\n'

        # Write it to the navigation file
        navfile_path = os.path.join(dst_root, site[0], "_data", "navigation.yml")
        with open(navfile_path, "a") as txtFile:
            txtFile.write(toc_text)

        # Make the index file have the contents of the first item in the index
        index_file_path = os.path.join(dst_root, site[0], "index.md")
        index_file = list(sections.items())[0][1][0]["SrcFile"]
        with open(index_file_path, "a") as txtFile:
            include_text = '{% include_relative ' + index_file + ' %}'
            txtFile.write(include_text)


# Given the full set of links on all pages propose entries to sitedefinitions.json to fix them
def propose_broken_links(all_links, sites_definitions, input_content_root):
    proposals = {}
    for link in all_links:
        if link["LinkState"] == "invalid_relative":
            file_identity = link["SrcDir"] + "/" + link["TargetFile"]
            if file_identity not in proposals:
                proposals[file_identity] = {"Site": link["Site"], "Section": link["Section"], "Page": link["LinkParts"][-1], "SrcDir": link["SrcDir"], "SrcFile": link["TargetFile"], "Referrer": f'{link["Site"]}/{link["SrcFile"]}'} # , "Debug": linkItem})

    # Now do the transitive closure of all links from the missing pages
    parser = Markdown(Parser, MarkdownRenderer)
    transitive_closure = {}
    for proposal in proposals.items():
        file_definition = proposal[1]
        src_file_path = os.path.join(input_content_root, file_definition["SrcDir"], file_definition["SrcFile"])
        gather_broken_links_from_page(input_content_root, transitive_closure, sites_definitions["Pages"], parser, file_definition, src_file_path)

    return proposals, transitive_closure


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
    converted = {"Pages": []}
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


if __name__ == '__main__':
    # with open("/Users/ericzinda/Enlistments/docsproto/testsitesdefinitions.json", "r") as txtFile:
    #     sites_definition = json.loads(txtFile.read())
    #
    # tree_pages = convert_pages_flat_to_tree(sites_definition["Pages"])
    # log_json_tree_to_file("sitesdefinitions1.json", tree_pages)

    if len(sys.argv) == 6:
        root_address = sys.argv[1]
        input_content_root = sys.argv[2]
        latestsrc_root = sys.argv[3]
        latestsites_root = sys.argv[4]
        sites_definitions_path = sys.argv[5]

        with open(sites_definitions_path, "r") as txtFile:
            sites_definition_tree = json.loads(txtFile.read())
            sites_definition = convert_to_flat_definition(sites_definition_tree)

        # Create the sites
        createblanksite.create_blank_sites(root_address, latestsrc_root, latestsites_root, sites_definition["Sites"])

        # Populate the sites with pages
        all_pages, all_links, tocs, errors = populate_sites_src(sites_definition, root_address, input_content_root, latestsrc_root)
        create_tocs(latestsrc_root, tocs)

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
        for item in all_pages.items():
            combined_pages += item[1].items()
        log_json_items_to_file("latestsrc/AllPages.json", combined_pages)

        # Log all links on all pages in all sites
        log_json_items_to_file("latestsrc/AllLinks.json", all_links)

        # Create a file that proposes fixes to the site definitions for all broken links
        proposed_fixes, transitive_closure = propose_broken_links(all_links, sites_definition, input_content_root)

        proposed_fixes_tree = convert_pages_flat_to_tree([item[1] for item in proposed_fixes.items()])
        log_json_tree_to_file("latestsrc/BrokenLinks.json", proposed_fixes_tree)

        transitive_closure_tree = convert_pages_flat_to_tree([item[1] for item in transitive_closure.items()])
        log_json_tree_to_file("latestsrc/TransitiveBrokenLinks.json", transitive_closure_tree)

    else:
        print("Error: Requires 5 arguments: \n1) Root address of site (i.e. sites will be under that URL address)\n2) Full path to where repositories containing docs to be used as source are stored\n3) Full path to the latestsrc directory of the docs repository\n4) Full path to the latestsites directory of the docs repository\n5) Full path and filename of the json file that defines the docs")
        assert False

    # parser = Markdown(Parser, MarkdownRenderer)
    # parser.use(GFM)
    # print(parser.convert("This is a test [foo](bar)\ntest"))

    # from marko.ext.gfm import gfm, GFM
    #
    # print(gfm("[foo](bar)"))