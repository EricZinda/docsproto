import os
import posixpath
import shutil
import urllib

script_path = os.path.dirname(os.path.realpath(__file__))


def create_blank_sites(root_address, latest_src_path, latest_sites_path, site_definitions):
    reset_sites(latest_src_path, latest_sites_path)
    navigation_content = generate_shared_navigation(root_address, site_definitions)
    for site in site_definitions:
        create_blank_site(site, root_address, site["Site"], latest_src_path, navigation_content)


# Remove all pages from "latest" so we don't carry over removed pages
def reset_sites(latest_src_path, latest_sites_path):
    shutil.rmtree(latest_src_path)
    os.mkdir(latest_src_path)
    shutil.rmtree(latest_sites_path)
    os.mkdir(latest_sites_path)


# # Create blank site
def create_blank_site(site_definition, root_address, site_name, latest_src_path, navigation_content):
    site_template_path = os.path.join(script_path, "site_template_standard")
    site_path = os.path.join(latest_src_path, site_name)

    # Copy the initial template over
    shutil.copytree(site_template_path, site_path)

    # Add top level navigation
    write_template(site_path, "_data/navigation.yml", navigation_content)

    # Add the configuration
    create_site_configuration(site_path, root_address, site_definition)


def get_template(name):
    file_path = os.path.join(script_path, name)
    with open(file_path, "r") as txt_file:
        return txt_file.read()


def write_template(site_path, relative_path, value):
    file_path = os.path.join(site_path, relative_path)
    with open(file_path, "a") as txt_file:
        txt_file.write(value)


def create_site_configuration(site_path, root_address, site_definition):
    template = get_template("template_config.txt")
    split_url = urllib.parse.urlparse(root_address)
    path_parts = split_url.path.split('/')
    base_url = "/" + "/".join(path_parts[1:])
    final_base_url = posixpath.join(base_url, site_definition["Site"])
    value = template.format(SiteFullName=site_definition["SiteFullName"], SiteBaseUrl=final_base_url)
    write_template(site_path, "_config.yml", value)


def generate_shared_navigation(root_address, site_definitions):
    template = get_template("template_navigation.txt")
    navigation_content = ""
    for site_definition in site_definitions:
        site_root = posixpath.join(root_address, site_definition["Site"])
        navigation_content += template.format(SiteNavigationName=site_definition["SiteNavigationName"], SiteAbsoluteUrl=site_root)
    return navigation_content

