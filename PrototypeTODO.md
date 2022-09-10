Figure out templates using Jekyll and see if they meet our needs
    - can "template" an .md file
    - can change look and feel
    - can build an index

(done) Figure out how to pull pages from the wiki and process them (or not)
    - Start with https://github.com/marketplace/actions/copy-anywhere-action
        - Update it to accept a file that is a list of files to copy    
            - This might work to build one giant filter: https://stackoverflow.com/questions/1133698/using-find-to-locate-files-that-match-one-of-multiple-patterns

- Get some base pages working right
    - (done) Build script to generate sites
        - automatically copy files
        - Do link fixup
    - (done) Build TOC properly
      - It doesn't link properly if you click on it.  Need to strip ".md"? 
    - Some images are broken
      - Github camo is used: https://github.com/atmos/camo by default in WIKI, this doesn't happen on github pages
      - https://github.blog/2014-01-28-proxying-user-images/
      - https://github.com/sionide21/camo-client
    - Some links are broken
      - it is because it is a page in Conceptual linking to a tools page
      - need to support cross site links
        - Fix these bugs:
          - Look through all the ResolvedLinks and see if they make sense
            - There are many that use the format "#ArgumentIdentification" or "ErgSemantics_Design#non-scopal-modification"
            - Link": "/WoodleyPackard.md", "ResolvedLink": "/WoodleyPackard"
              - handle "/"
- Goal Build the current docs using the new process
    - Do the build in a way that allows versioning
    - Include all the current stuff
    - Include an index
    - TODO:
        - How does versioning work?
            - https://justwriteclick.com/2017/07/30/investigating-jekyll-for-versioned-content/#:~:text=Setting%20a%20version%20value%20in%20the%20source%20With,%E2%80%9Cbase%E2%80%9D%20_config.yml%20file%20and%20the%20versioned%20config%20file.

            - There are some pages (the home page, others?) that are shared among all versions they are in the "shared" folder
            - versioned pages are all in a "version" folder, with a version number folder that represents each version