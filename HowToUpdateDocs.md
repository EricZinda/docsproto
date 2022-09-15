# How the DELPH-IN Docs work
The documentation system is designed to be able to combine documentation from any publicly accessible git repository into an arbitrary set of sites.  Pages from one repository can be put into different sites and will automatically keep their links valid. Furthermore, documentation can be generated from, for example, grammar source and included as well.  The definition of the sites created is copied into the docs repository so that git can be used to see what changed and observe the history.  Branches can be used to test, etc.

It does this by using a [GitHub Workflow](https://docs.github.com/en/actions/using-workflows/about-workflows) which is located in the /.github/workflows folder of the DELPH-IN repository to build the docs. A workflow is simply a way of defining computer code that can run on GitHub's servers.  The workflow runs on an actual computer at GitHub, it has access to a file system, and it can run any command you can run from a linux shell (including git commands), etc.  It is just a large script running on a Linux server.

It uses a [system called Jekyll to create a set of sites and then uses GitHub pages to publish the sites.](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)

In a nutshell the workflow does the following to build the documentation site:
1. Clone (in a git sense, i.e. git clone ...) every repository that has any content we want to use in the ultimate documentation. This will make a copy of it available on the GitHub server the script is running on. We will selectively choose which files to include in later steps. Step 1 simply grabs the entire set of repositories we want access to.

Run the `createdocs.py` script that is in the root of the docs repository. This script does the following:

2. Load in the file called `sitesdefinitions.json` in the root of the docs repository.  This file defines all of the sites that will be created, and all of the files that will be copied from the repositories we cloned in step 1.  This is how the structure of the documentation sites and the docs that populate them are defined.
3. Create blank template site definitions for everything in the `Sites` section of `sitesdefinitions.json`. These site definitions are for Jekyll to use. Jekyll will actually turn them into valid HTML pages that Github Pages can serve.  See [the Github Pages docs](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll) for more information.
4. Copy all of the pages in the `Pages` section of `sitesdefinitions.json` to the proper site definition where they should be displayed.  In the process, `createdocs.py` reads each file and fixes up its links to point to the proper place in the new site structure.  This is so pages that link to other pages in the same repository will continue to work in the final documentation, even if the pages fall in different sites.

After the `createdocs.py` script is finished, control goes back to the workflow:

5. Actually run Jekyll on all of the site definitions to build the real HTML
6. Publish the sites to GitHub pages so they can be served

## Defining the Documentation Structure
`sitesdefinitions.json` is the key file in this whole process. It looks like this:

~~~
{
  "Sites":
  [
    {"SiteFullName": "DELPH-IN Conceptual Docs", "SiteNavigationName": "Concepts", "Site": "concept", "HomePage": "ErgSemantics.md"},
    {"SiteFullName": "DELPH-IN Tools", "SiteNavigationName": "Tools", "Site": "tools"}
  ],
  "Pages":
  {
    "concept": [
      {"Section": "Erg Semantics", "Pages": [
        {"Page": "Overview", "SrcDir": "docswiki", "SrcFile": "ErgSemantics.md"},
        {"Page": "Essence", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Essence.md"}
      ]},
      {"Section": "More Semantics", "Pages": [
        {"Page": "Basics", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Basics.md"},
        {"Page": "Basics", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Design.md"}
      ]}
    ],
    "tools": [
      {"Section": "Tools", "Pages": [
        {"Page": "Overview", "SrcDir": "docswiki", "SrcFile": "ToolsTop.md"},
        {"Page": "Logon", "SrcDir": "docswiki", "SrcFile": "LogonTop.md"},
        {"Page": "matrixdef File Syntax", "SrcDir": "docswiki", "SrcFile": "matrixdef_File_Syntax.md", "Referrer": "concept/Updating_the_Customization_System.md"}
      ]}
    ]
  }
}
~~~

The `Sites` section declares what top level sites exist to hold content. Think of these like chapters in a book. 
- "SiteFullName" is the descriptive name that will be shown for the site when you are in that site.
- "SiteNavigationName" is what shows up in the menu to change between sites
- "Site" is not shown to the user but is used in the `Pages` section to identify the site
- "HomePage" is optional. If included, that will be the first page displayed when you go to the site. If missing, the very first page in the site will be shown.
~~~
{"SiteFullName": "DELPH-IN Conceptual Docs", "SiteNavigationName": "Concepts", "Site": "concept", "HomePage": "ErgSemantics.md"}
~~~

The `Pages` section declares which pages from the different repositories we cloned should be included in the site, and where. It is in a tree structure so that pages can be easily moved around. The page definitions themselves don't have information about where they are. Their location is set by their location in the tree.  

So, to include 2 pages in the "concept" site in a structure like this:
~~~
concept
    Erg Semantics
        ErgSemantics.md
    More Semantics
        ErgSemantics_Basics.md
~~~
You would use the definition below:
~~~
  "Pages":
  {
    "concept": [
      {"Section": "Erg Semantics", "Pages": [
        {"Page": "Overview", "SrcDir": "docswiki", "SrcFile": "ErgSemantics.md"},
      ]},
      {"Section": "More Semantics", "Pages": [
        {"Page": "Basics", "SrcDir": "docswiki", "SrcFile": "ErgSemantics_Basics.md"},
      ]}
    ]
  }
~~~
The `Page` definition fields are:
- "Page": The name that should be shown to the user for the page
- "SrcDir": the name of the directory that contains the repository that contains it. This directory name is defined in the workflow.
- "SrcFile": the filename and path to the file in the directory that should be included in the documentation.

Simply creating a new `Section` definition and putting pages inside it causes them to be included in the site, and in that section of the docs.

The format is designed to make it easy to move files around, redefine sections, sites, etc. Just running the workflow again will create the new site structure.

## Running the Workflow
To run the workflow:
1. Click on the `Actions` tab at the top of the DELPH-IN docs repository on GitHub.  
2. Then click `BuildDocs` on the left side of the page. At this point you'll see a record of previous runs (if they weren't deleted)
3. Finally, click the `Run Workflow` button the right side and then `Run Workflow` on the UI that appears

At this point the workflow will begin running and you'll see its status.  When done, it will have a green checkmark for success or a red X for failure.

If it was successful the docs have been immediately published and you can browse them live. It takes about 2 minutes to run. 

You can also click on the row that represents the run you just did and you'll see an "Artifacts" section at the bottom. This gives you files that get output by the run:
- "All Links": A Json file that lists every link in every document included in every site. Useful for debugging.
- "All Pages": Lists every page in every site.
- "Broken Links": Lists files that were linked to but not included in the documentation. I.e. they will be broken. This is in a format that allows you to simply copy the `File` definition to the `sitesdefinition.json` file to include it and fix the broken link.
- "Transitive Broken Links": Lists the transitive closure of all broken links, and the links from those files to other files that aren't included, and so on.  If you included all of these files in `sitesdefinition.json`, there would be no broken links!

Note that the Broken Links files are only for links to other docs in the repositories, not for public web URLs.

If it failed, click on the row that represents the run you just did and you'll see an error file. If you open this file, all of the errors encountered will be listed.  Fix those, and rerun the workflow.
