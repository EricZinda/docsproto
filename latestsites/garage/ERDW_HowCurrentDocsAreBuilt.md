{% raw %}When done, this page should describe how the current (as of 8/15/22) docs are built so we can decide what to do next.

# Delph-in Wiki
The ["official" Delph-in wiki](https://github.com/delph-in/docs/wiki) uses the [Github wiki feature](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis).  That means that it is a special wiki repository tied to a "regular" github repository: https://github.com/delph-in/docs. 

If you go to the docs repository and look at the source in it, there is very little. To see the actual source for the wiki pages, you have to find the wiki repository: Click on the "wiki" link on top of the docs repository, look at the bottom of the right hand column on that new page. You'll see UI for "Clone this wiki locally". If you clone it, you'll see all the wiki pages there. I haven't found a way to actually browse the source using the normal github repository browser, I think you just have to clone it.

# delph-in.github.io/docs/
The "official docs" are created using [Github Pages](https://pages.github.com/) and are hosted at https://delph-in.github.io/docs/. If you go to that page, you'll see the (small number of) pages from the https://github.com/delph-in/docs repository there. These get built and pushed to https://delph-in.github.io/docs/ by Github automatically whenever anyone pushes a change to the delph-in/docs repository. 

One "trick" that happens on the https://delph-in.github.io/docs/ page is the search box. This is set up to post to the same URL the wiki uses for its search.

<update date omitted for speed>{% endraw %}