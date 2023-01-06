Figure out templates using Jekyll and see if they meet our needs
    - can "template" an .md file
    - can change look and feel
    - can build an index

(done) Figure out how to pull pages from the wiki and process them (or not)
    - Start with https://github.com/marketplace/actions/copy-anywhere-action
        - Update it to accept a file that is a list of files to copy    
            - This might work to build one giant filter: https://stackoverflow.com/questions/1133698/using-find-to-locate-files-that-match-one-of-multiple-patterns

- Get the list of docs in the wiki that aren't in the sitedefinitions.json

- Put content from different sources in different base directories so they can't overwrite each other.
- Get some base pages working right
    - (done) Build script to generate sites
        - automatically copy files
        - Do link fixup
    - (done) Build TOC properly
      - It doesn't link properly if you click on it.  Need to strip ".md"? 
    - (done) Some links are broken
      - it is because it is a page in Conceptual linking to a tools page
      - (done) need to support cross site links
      - (done) Look through all the ResolvedLinks and see if they make sense
      - (fixed) There are many that use the format "#ArgumentIdentification" or "ErgSemantics_Design#non-scopal-modification"
    - (done) Put an error in siteerrors if we can't parse the site definition
    - (done) relative links don't always work
      - Theory: 
        - I am fixing up the urls to be of the form ../ since they are relative and we want links of the form [text](foo.md) to be in the same directory as the referrer
        - If you just go to https://blog.inductorsoftware.com/docsproto/concept/, and all links are of the form [text](foo.md) it *won't* work since the relative link is added to the URL and goes one level too far up
        - If you go instead to the same page bug using https://blog.inductorsoftware.com/docsproto/concept/ErgSemantics/ it *will* work because it will not be added to that URL it will replace the last segment
        - https://ricostacruz.com/til/relative-paths-in-jekyll
        - https://superdevresources.com/redirects-jekyll-github-pages/#:~:text=JekyllRedirectFrom%20can%20be%20used%20to%20setup%20multiple%20redirects,from%20which%20the%20current%20location%20is%20mapping%20to.
        - Solution:
          - The solution is to make sure going to https://blog.inductorsoftware.com/docsproto/concept redirects to the home page that is defined there
    - Some images are broken
      - Github camo is used: https://github.com/atmos/camo by default in WIKI, this doesn't happen on github pages
      - https://github.blog/2014-01-28-proxying-user-images/
      - https://github.com/sionide21/camo-client
    - Link: "/WoodleyPackard.md", "ResolvedLink": "/WoodleyPackard"
      - handle "/"
      - This refers to a local *repository*
    - Test absolute links to make sure they work
    - Broken links should be removed from the docs? 
    - Add all referrers to the sitedefintions.json automatically after a build
    - Add links on pages on final site to wiki source for editing
- Goal Build the current docs using the new process
    - Do the build in a way that allows versioning
    - Include all the current stuff
    - Include an index
    - TODO:
        - How does versioning work?
            - https://justwriteclick.com/2017/07/30/investigating-jekyll-for-versioned-content/#:~:text=Setting%20a%20version%20value%20in%20the%20source%20With,%E2%80%9Cbase%E2%80%9D%20_config.yml%20file%20and%20the%20versioned%20config%20file.

            - There are some pages (the home page, others?) that are shared among all versions they are in the "shared" folder
            - versioned pages are all in a "version" folder, with a version number folder that represents each version