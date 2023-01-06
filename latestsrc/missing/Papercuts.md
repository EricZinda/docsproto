{% raw %}
In the Ubuntu Linux-based operating system a paper cut bug is defined as
"a trivially fixable usability bug that the average user would encounter
on his/her first day of using a brand new installation of the latest
version of Ubuntu Desktop Edition." The analogy is with a paper cut;
small, not seriously damaging, but surprisingly painful. [Wikipedia
Paper Cut Bug](http://en.wikipedia.org/wiki/Paper_cut_bug).

This page is for DELPH-IN paper cut bugs. The goal is to make the
experience of using our wonderful software slightly more pleasant.

- Knoppix lkb
  - you can't load the erg as Version.lsp is not writable by default
(I get this all of the time)
    - solution: make it world writable (or stop writing to it)
  - you can't load the erg as it complains it can't find the lexdb
    - solution: in .lkbrc (setf \*lexdb-params\* nil)
  - you cannot load gg (even with \*lexdb-params\* nil)
    - solution: fiddle with the script file
- General
  - The default treebanking interface is not the most common one.
    - solution: give it some time.
  - I find the the open grammar dialogue box thing from the LKB far
too painful. (Ned)
    - My workarounds for this have been creating .1GRAMMAR etc
symlinks in my home directory so they will be at the top of
the open file dialogue. More recently it occurred to me that
I could just add individual emacs key bindings to load each
grammar I use regularly.
    - You can use C-g to get a template to do this in emacs
    - (rsa) will load some grammars
    - a little snippet for loading a grammar (and setting home,
skeletons and languages)
      - [[JacyInstallation#calling-jacy-from-emacs]]
    - Trollet avoids this
  - Num Lock On interferes with the LKB/tsdb++ GUI
  - Asian fonts in LKB top window with DELPH-IN build
    - solution: switch to LOGON build
<update date omitted for speed>{% endraw %}