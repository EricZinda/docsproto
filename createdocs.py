import json
import os
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
    with open(src_file_path, "r") as txtFile:
        result = parser.parse(txtFile.read())
        convert_child(result)

    with open(dst_file_path, "w") as txtFile:
        final_result = parser.render(result)
        txtFile.write(final_result)


def convert_child(node):
    if isinstance(node, Link):
        split_url = urllib.parse.urlsplit(node.dest)
        if split_url.scheme == "" and split_url.netloc == "" and split_url.query == "" and split_url.fragment == "":
            parts = split_url.path.split('/')
            if len(parts) == 1 and parts[0] != "":
                node.dest = "../" + node.dest
    elif hasattr(node, "children"):
        for child in node.children:
            convert_child(child)


# Given a definition file that contains all the site defininitions create the latestsrc folder structure
# We do it all at once so we can check for broken links
def create_sites_src(src_root, dst_root, sites_definitions_path):
    parser = Markdown(Parser, MarkdownRenderer)
    with open(sites_definitions_path, "r") as txtFile:
        sites_definition = json.loads(txtFile.read())
        for fileDefinition in sites_definition["Sites"]:
            src_file = os.path.join(src_root, fileDefinition["SrcDir"], fileDefinition["SrcFile"])
            dst_file = os.path.join(dst_root, fileDefinition["Site"], fileDefinition["SrcFile"])
            convert_and_copy_doc(parser, src_file, dst_file)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        src_root = sys.argv[1]
        dst_root = sys.argv[2]
        sites_definitions_path = sys.argv[3]
        create_sites_src(src_root, dst_root, sites_definitions_path)

    else:
        print("Error: Requires 3 arguments: 1) full path to where repositories containing docs are stored, 2) full path to the latestsrc directory of the docs repository, 3) full path and filename of the json file that defines the docs")

    # parser = Markdown(Parser, MarkdownRenderer)
    # parser.use(GFM)
    # print(parser.convert("This is a test [foo](bar)\ntest"))

    # from marko.ext.gfm import gfm, GFM
    #
    # print(gfm("[foo](bar)"))