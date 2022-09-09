import copy
import json
import os
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


def convert_and_copy_doc(parser, file_definition, src_file_path, dst_file_path):
    file_name, file_extension = os.path.splitext(src_file_path)
    if file_extension.lower() == ".md":
        with open(src_file_path, "r") as txtFile:
            result = parser.parse(txtFile.read())
            links = convert_child(file_definition, result)

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


def convert_child(file_definition, node):
    links = []
    if isinstance(node, Link):
        _, parts = get_parts_for_local_link(node.dest)
        link_data = copy.deepcopy(file_definition)
        link_data["Link"] = node.dest
        link_data["LinkParts"] = parts
        links.append(link_data)
        if parts is not None:
            if len(parts) == 1 and parts[0] != "":
                node.dest = "../" + node.dest

    elif hasattr(node, "children"):
        for child in node.children:
            links += convert_child(file_definition, child)

    return links


def get_site_relative_page_link_from_src(site, src_file):
    # if it is an md file, just strip the extension to make a relative link to the site root
    file_name, file_extension = os.path.splitext(src_file)
    if file_extension.lower() == ".md":
        return file_name
    else:
        return src_file


# Given a definition file that contains all the site defininitions create the latestsrc folder structure
# We do it all at once so we can check for broken links
def create_sites_src(src_root, dst_root, sites_definitions_path):
    parser = Markdown(Parser, MarkdownRenderer)
    with open(sites_definitions_path, "r") as txtFile:
        sites_definition = json.loads(txtFile.read())
        errors = []
        links = []
        docs = {}
        tocs = {}
        for fileDefinition in sites_definition["Sites"]:
            src_file = os.path.join(src_root, fileDefinition["SrcDir"], fileDefinition["SrcFile"])
            dst_file = os.path.join(dst_root, fileDefinition["Site"], fileDefinition["SrcFile"])

            # Remember this doc in the site so we can find broken links later
            file_site = fileDefinition["Site"]
            if fileDefinition["Site"] not in docs:
                docs[file_site] = {}
            path_lower = get_site_relative_page_link_from_src(file_site, fileDefinition["SrcFile"]).lower()
            docs[file_site][path_lower] = copy.deepcopy(fileDefinition)

            if fileDefinition["Section"] != "<todo>":
                try:
                    links += convert_and_copy_doc(parser, fileDefinition, src_file, dst_file)
                except Exception as error:
                    errors.append({"Definition": fileDefinition, "Error": str(error)})

                if fileDefinition["Site"] not in tocs:
                    tocs[fileDefinition["Site"]] = []
                site_relative_link = get_site_relative_page_link_from_src(fileDefinition["Site"], fileDefinition["SrcFile"])
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


# returns the path and segments of a local link
# returns None if this is not a local link
def get_parts_for_local_link(link):
    split_url = urllib.parse.urlsplit(link)
    if split_url.scheme == "" and split_url.netloc == "" and split_url.query == "" and split_url.fragment == "":
        return split_url.path, split_url.path.split('/')
    else:
        return None, None


# Given the full set of links on all pages:
# 1. Find the ones we think are broken
# 2. Propose entries to sitedefinitions.json to fix them
def propose_broken_links(all_pages, all_links):
    broken_links = find_broken_links(all_pages, all_links)
    proposals = []
    for linkItem in broken_links.items():
        link = linkItem[1]
        proposals.append({"Site": link["Site"], "Section": link["Section"], "Page": link["LinkParts"][-1], "SrcDir": link["SrcDir"], "SrcFile": link["Link"]})

    return proposals


# all_links includes the link that was found in ["Link"] along with the entire record from sitesdefinitions.json
def find_broken_links(all_pages, all_links):
    broken_links = {}
    for link_data in all_links:
        local_path, local_path_parts = get_parts_for_local_link(link_data["Link"])
        if local_path is not None:
            # strip the "../" from the link since that is just a workaround
            if local_path_parts[0] == "..":
                local_path = local_path_parts[-1]
                link_data["Link"] = local_path + ".md"

            # If a link is relative, see if it exists
            link_site_pages = all_pages[link_data["Site"]]
            if local_path.lower() not in link_site_pages:
                # Check to ensure it is not already there
                if link_data["Link"] not in broken_links:
                    broken_links[link_data["Link"]] = link_data

        else:
            # TODO: If a link is to a fully qualified address, test to see if it works
            pass

    return broken_links


if __name__ == '__main__':
    if len(sys.argv) == 4:
        src_root = sys.argv[1]
        dst_root = sys.argv[2]
        sites_definitions_path = sys.argv[3]
        all_pages, all_links, tocs, errors = create_sites_src(src_root, dst_root, sites_definitions_path)
        if len(errors) > 0:
            print(f"Errors generating site:\n{errors}")
            assert False

        create_tocs(dst_root, tocs)
        proposed_fixes = propose_broken_links(all_pages, all_links)
        print("\n\nBroken Links:\n\n")
        for item in proposed_fixes:
            print(f"{json.dumps(item)},")

    else:
        print("Error: Requires 3 arguments: 1) full path to where repositories containing docs are stored, 2) full path to the latestsrc directory of the docs repository, 3) full path and filename of the json file that defines the docs")

    # parser = Markdown(Parser, MarkdownRenderer)
    # parser.use(GFM)
    # print(parser.convert("This is a test [foo](bar)\ntest"))

    # from marko.ext.gfm import gfm, GFM
    #
    # print(gfm("[foo](bar)"))