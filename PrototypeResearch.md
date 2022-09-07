# Github pages
- Basic overview: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

# How to copy pages from other repositories
https://stackoverflow.com/questions/59408320/github-action-to-copy-a-file-from-one-repo-to-another
Probably the best action to start with: https://github.com/marketplace/actions/copy-anywhere-action

check out both repositories under different paths:
https://github.com/actions/checkout

literally do a file copy of one into the other

check it back in

# How to checkin using github actions

https://github.com/marketplace/actions/simple-commit
    - doesn't push

https://github.com/marketplace/actions/commit-and-push-branch
    - does a commit and push


https://github.com/ad-m/github-push-action
    - best reviewed for push


# Create Indexes
https://github.com/marketplace/actions/markdown-action-create-indexes

# How does versioning work?
- https://justwriteclick.com/2017/07/30/investigating-jekyll-for-versioned-content/#:~:text=Setting%20a%20version%20value%20in%20the%20source%20With,%E2%80%9Cbase%E2%80%9D%20_config.yml%20file%20and%20the%20versioned%20config%20file.

# Configuring Jekyll correctly
http://downtothewire.io/2015/08/15/configuring-jekyll-for-user-and-project-github-pages/

# Minimal Mistakes Theme
https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/

## Initial config file
https://github.com/mmistakes/minimal-mistakes/blob/master/_config.yml

## Config documentation
https://mmistakes.github.io/minimal-mistakes/docs/configuration/

### Updates to config
- Need to set defaults so that yml front matter is not required on every page
    defaults:
    # _pages
    - scope:
        path: ""
        type: pages
        values:
        layout: single

## Overriding theme defaults
https://mmistakes.github.io/minimal-mistakes/docs/overriding-theme-defaults/
- includes how to create new layouts if theirs don't work for us
