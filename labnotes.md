### Updates to config
- Need to set defaults so that yml front matter is not required on every page
    defaults:
    # _pages
    - scope:
        path: ""
        type: pages
        values:
        layout: single
- Need to create a custom layout because the default layout includes the page title on the page which means it shows twice (since the page title is generated from the top heading in the MD)