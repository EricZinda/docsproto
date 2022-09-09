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


def convert_and_copy_doc(parser, src_file_path, dst_file_path):
    file_name, file_extension = os.path.splitext(src_file_path)
    if file_extension.lower() == ".md":
        with open(src_file_path, "r") as txtFile:
            result = parser.parse(txtFile.read())
            links = convert_child(src_file_path, result)

        with open(dst_file_path, "w") as txtFile:
            final_result = parser.render(result)
            txtFile.write(final_result)
            print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")

    else:
        shutil.copy2(src_file_path, dst_file_path)
        print(f"copy {file_extension}: {src_file_path} to {dst_file_path}")
        links = []

    return links


def convert_child(docpath, node):
    links = []
    if isinstance(node, Link):
        links.append({"Doc": docpath, "Link": node.dest})
        split_url = urllib.parse.urlsplit(node.dest)
        if split_url.scheme == "" and split_url.netloc == "" and split_url.query == "" and split_url.fragment == "":
            parts = split_url.path.split('/')
            if len(parts) == 1 and parts[0] != "":
                node.dest = "../" + node.dest
    elif hasattr(node, "children"):
        for child in node.children:
            links += convert_child(docpath, child)

    return links


# Given a definition file that contains all the site defininitions create the latestsrc folder structure
# We do it all at once so we can check for broken links
def create_sites_src(src_root, dst_root, sites_definitions_path):
    parser = Markdown(Parser, MarkdownRenderer)
    with open(sites_definitions_path, "r") as txtFile:
        sites_definition = json.loads(txtFile.read())
        links = []
        docs = []
        tocs = {}
        for fileDefinition in sites_definition["Sites"]:
            src_file = os.path.join(src_root, fileDefinition["SrcDir"], fileDefinition["SrcFile"])
            dst_file = os.path.join(dst_root, fileDefinition["Site"], fileDefinition["SrcFile"])
            docs.append(dst_file)
            links += convert_and_copy_doc(parser, src_file, dst_file)
            if fileDefinition["Site"] not in tocs:
                tocs[fileDefinition["Site"]] = []
            tocs[fileDefinition["Site"]].append({"Section": fileDefinition["Section"], "Page": fileDefinition["Page"], "Link": fileDefinition["SrcFile"]})

    return docs, links, tocs


def create_tocs(dst_root, tocs):
    for site in tocs.items():
        sections = {}
        for entry in site[1]:
            if entry["Section"] not in sections:
                sections[entry["Section"]] = []
            sections[entry["Section"]].append({"Name": entry["Page"], "Link": entry["Link"]})

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
        index_link = list(sections.items())[0][1][0]["Link"]
        with open(index_file_path, "a") as txtFile:
            include_text = '{% include_relative ' + index_link + ' %}'
            txtFile.write(include_text)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        src_root = sys.argv[1]
        dst_root = sys.argv[2]
        sites_definitions_path = sys.argv[3]
        docs, links, tocs = create_sites_src(src_root, dst_root, sites_definitions_path)
        create_tocs(dst_root, tocs)
        print(docs)
        print(links)

    else:
        print("Error: Requires 3 arguments: 1) full path to where repositories containing docs are stored, 2) full path to the latestsrc directory of the docs repository, 3) full path and filename of the json file that defines the docs")

    # parser = Markdown(Parser, MarkdownRenderer)
    # parser.use(GFM)
    # print(parser.convert("This is a test [foo](bar)\ntest"))

    # from marko.ext.gfm import gfm, GFM
    #
    # print(gfm("[foo](bar)"))