{% raw %}# DELPH-IN Docs Reference Guide
The documentation system is designed to be able to combine documentation from any publicly accessible git repository into an arbitrary set of sites.  Pages from one repository can be put into different sites and will automatically keep their links valid. Furthermore, documentation can be generated from, for example, grammar source and included as well.  The definition of the sites created is copied into the docs repository so that git can be used to see what changed and observe the history.  Branches can be used to test, etc.

It does this by using a [GitHub Workflow](https://docs.github.com/en/actions/using-workflows/about-workflows) which is located in the [/.github/workflows folder](https://github.com/EricZinda/docsproto/tree/main/.github/workflows) of the DELPH-IN docs repository to build the docs. A workflow is simply a way of defining computer code that can run on GitHub's servers.  The workflow runs on an actual computer at GitHub, it has access to a file system and it can run any command you can run from a linux shell (including git commands), etc.  It is just a large script running on a Linux server. It uses a [system called Jekyll to create a set of sites and then uses GitHub pages to publish the sites.](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)

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
`sitesdefinitions.json` is the key file in this whole process. A simplified version looks like this:

```
{
  "Comments": [
    "This comments section is solely for comments that describe this json file"
  ],
  "SourceRepositories":
    {
      "docswiki": {"Repository": "delph-in/docs/wiki"},
      "websitewiki": {"Repository": "ericzinda/docsproto/wiki"}
    },
  "Sites":
  [
    {"SiteFullName": "DELPH-IN Docs", "SiteNavigationName": "Home", "Site": "home", "HomePage": "Home.md"},
    {"SiteFullName": "DELPH-IN How-to", "SiteNavigationName": "How-to", "Site": "howto"}
  ],
  "Pages":
  {
    "home": [
      {"Section": "DELPH-IN", "Pages": [
        {"Page": "Overview", "SrcDir": "docswiki", "SrcFile": "Home.md"},
        {"Page": "Welcome", "SrcDir": "docswiki", "SrcFile": "DelphinWelcome.md", "Referrer": "home/Home.md"},
        {"Page": "Applications", "SrcDir": "docswiki", "SrcFile": "DelphinApplications.md", "Referrer": "home/Home.md"}
      ]},
      {"Section": "Projects", "Pages": [
        {"Page": "DeepBank", "SrcDir": "docswiki", "SrcFile": "DeepBank.md"}
      ]}
    ],
    "howto": [
      {"Section": "DELPH-IN", "Pages": [
        {"Page": "Welcome", "SrcDir": "docswiki", "SrcFile": "DelphinWelcome.md", "Referrer": "home/Home.md"}
      ]},
      {"Section": "Tutorials", "Pages": [
        {"Page": "DelphinTutorial", "SrcDir": "docswiki", "SrcFile": "DelphinTutorial.md", "Referrer": "summits/SaarlandSchedule.md"},
        {"Page": "DelphinTutorial_Formalisms", "SrcDir": "docswiki", "SrcFile": "DelphinTutorial_Formalisms.md" 
      ]}
   ]}
  }
}
```
### SourceRepositories
The `SourceRepositories` section declares what repositories will be used to populate the content of the site. Not everything from these repositories is included, just the files listed in `sitedefinitions.json`. 
- `key` is the name that will be used by the `SrcDir` field in every page in the `Pages` section to refer to the repository.  It must match the directory name where the repository got cloned by the workflow.
- `Repository` is the name of the repository in Github.  If it is a Wiki, replace the dot in the name (delph-in/docs.wiki) with a slash (delph-in/docs/wiki)

To add a new repository, a row must be added here *and* the [workflow](https://github.com/EricZinda/docsproto/blob/main/.github/workflows/BuildDocs.yml) must be modified to also clone it so the data is available. You can see how this is done in the workflow by looking for where the existing repositories are cloned and adding a new section.
```
  ...
  
  "SourceRepositories":
    {
      "docswiki": {"Repository": "delph-in/docs/wiki"},
      "websitewiki": {"Repository": "ericzinda/docsproto/wiki"}
    },
  
  ...
```

### Sites
The `Sites` section declares what top level sites exist to hold content. Think of these like chapters in a book. These create the top level navigation on the site.
- `SiteFullName` is the descriptive name that will be shown for the site when you are in that site.
- `SiteNavigationName` is what shows up in the menu to change between sites
- `Site` is not shown to the user but is used as the *key* in the `Pages` section to identify the site
- `HomePage` is optional. If included, that will be the first page displayed when you go to the site. If missing, the very first page listed in the site will be shown.
```
  ...
  
  "Sites":
  [
    {"SiteFullName": "DELPH-IN Docs", "SiteNavigationName": "Home", "Site": "home", "HomePage": "Home.md"},
    {"SiteFullName": "DELPH-IN How-to", "SiteNavigationName": "How-to", "Site": "howto"}
  ],
  
  ...
```

### Pages
The `Pages` section declares which pages from the different repositories should actually be included in the site, and where. It is in a tree structure so that pages can easily be moved around. The page definitions themselves don't have information about where they are. Their location is set by their location in the tree.  

So, to include 2 pages in the "concept" site in a structure like this:
```
concept
    Erg Semantics
        ErgSemantics.md
    More Semantics
        ErgSemantics_Basics.md
```
You would use the definition below:
```
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
```
The `Page` definition fields are:
- `Page`: The name that should be shown to the user for the page
- `SrcDir`: The name of the directory that contains the repository that contains it. This directory name is defined in the workflow.
- `SrcFile`: The filename and path to the file in the directory that should be included in the documentation.
- `DstFile`: (optional) this field can be included if the name of the original page needs to be changed when it is included in the documentation (e.g. to avoid a conflict) or if the file needs to be put in a location different from its default.  If `DstFile` is not included, the default location in the documentation site will be the same as the relative location in the original. For example, if the file was in the root of its source repository, it will be in the root of the documentation site too. If it was in the `foo/bar/goo` directory, that is where it will get put in the documentation site as well. NOTE: Any directory structure deeper than one directory seems to be ignored by the Jekyll system, so use this field to copy files into a structure that is only one directory deep.
- `Referrer`: Not used by the system but included sometimes to indicate what is linking to the file.  Any other fields can be added to the page definition and they will be ignored, as this field is.  Just informational. 

Simply creating a new `Section` definition and putting pages inside it causes them to be included in the site, and in that section of the docs.

The format is designed to make it easy to move files around, redefine sections, sites, etc. Just running the workflow again will create the new site structure.

## Running the Workflow
To run the workflow:
1. Click on the `Actions` tab at the top of the DELPH-IN docs repository on GitHub.  
2. Then click `BuildDocs` on the left side of the page. At this point you'll see a record of previous runs (if they weren't deleted)
3. Finally, click the `Run Workflow` button the right side and then `Run Workflow` on the UI that appears

At this point the workflow will begin running and you'll see its status.  When done, it will have a green checkmark for success or a red X for failure.  If it was successful the docs have been immediately published and you can browse them live. It takes about 10 minutes to run. 

You can also click on the row that represents the run you just did and you'll see an "Artifacts" section at the bottom. This gives you files that get output by the run:
- `All Links`: A Json file that lists every link in every document included in every site and whether they are broken, valid, etc. Useful for debugging. If you chose to check external links (which takes about 1.5 hours) the validity of those will be included. Otherwise only internal links between wiki pages are checked.
- `All Pages`: Lists every page in every site.
- `Fixes for Broken Links to Pages`: Creates page definitions suitable for including in `sitesdefinition.json` for every broken link. Note that this includes adding entries for wiki pages that *don't exist* (those will have the `FileMissing` field set in their definition). This allows you to simply copy the `File` definition to the `sitesdefinition.json` file to include it and fix the broken link. It includes the transitive closure of all broken links (i.e. the links from those files to other files that aren't included, and so on).  If you included all of these files in `sitesdefinition.json`, there would be no broken (Wiki) links!

> Note that a file that was linked to but didn't exist will have a definition in `Fixes for Broken Links to Pages` as well, but will include a `"FileMissing": True` field. Obviously don't add this to the site without also creating the file that was missing!


If it failed, click on the row that represents the run you just did and you'll see an error file. If you open this file, all of the errors encountered will be listed.  Fix those and rerun the workflow.  In rare cases, you might need to click on the run, and then on the box that represents the "build" part of the workflow. That will expand all the details of the run and show you why it failed.  The biggest source of failure is not formatting the JSON file correctly.

## The `<todo>` Section
Note that any section named `<todo>` that is included in the docs will *not* be included in the output.  However, any pages in it will be counted as "valid" when linked to, even if they don't exist in the site. This is a mechanism for removing them from being added to the "Fixes for Broken Links to Wiki Pages" output file that the build generates.

Last update: 2023-01-04 by EricZinda [[edit](https://github.com/ericzinda/docsproto/edit/main/DelphinDocsReference.md)]{% endraw %}