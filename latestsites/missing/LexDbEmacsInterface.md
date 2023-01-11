{% raw %}Contents

1. [LexDB Emacs Interface
(lexdb-mode)](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
   1. [HOW TO edit entries in the
LexDB](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
   2. [Searching the Lexicon](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
      1. [Moving around within a search
result](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
   3. [Changing the Lexicon](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
      1. [Redisplaying a Changed
Entry](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
   4. [Saving/Restoring the Lexicon](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
   5. [Starting the Lexicon Editing
Mode](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)
2. [Installation](https://blog.inductorsoftware.com/docsproto/missing/LexDbEmacsInterface)

# LexDB Emacs Interface (lexdb-mode)

## HOW TO edit entries in the LexDB

The LexDB-Emacs interface allows editing of lexical entries from within
an Emacs environment (with browsing functionality, field completion,
etc.). New revision entries are first stored in the users private
schema, and hence are visible only to the particular user.

0\. Add the following (path adjusted for your setup) to your .emacs
file:

    (add-to-list 'load-path "/path/to/delphin/lkb/lexdb")
    (load "pg-interface")

1\. In [GNU Emacs](http://www.gnu.org/software/emacs/emacs.html): *M-x
lexdb* to enter LexDB major mode. Then see the PG menu.

Available commands in LexDB major mode are:

*C-l* : load (active revision of lexical entry) into Emacs

*C-c C-c* : commit (edited/new revision of) lexical entry into LexDB

*TAB* : field completion

*M-TAB l* : get (ring of) entries in table lex where value of current
field matches that in buffer

*M-TAB r* : get (ring of) entries in union of rev tables where value of
current field matches that in buffer

*M-n* : cycle through ring of entries obtained above

*M-s* : as M-TAB, but explicitly specify field value

*M-va* : view entries added in merge operation from dump file

*M-vs* : view entries in user's privat rev

To remove a lexical entry from the current lexicon *lex*, create a
(head) revision where the dead field is set to t (true) rather than f
(false). In this manner we keep a revision history even for entries
which are no longer used (and such entries can be reactivated if
necessary). No revision entry should ever be deleted from the lexical
database itself.

## Searching the Lexicon

- Search by lexical-id (**Load record: C-l**)
- Search by orthography (**Search Orth: C-c C-s**)
- Search by the value of an attribute (**search: M-s**)
- Cross Reference

### Moving around within a search result

## Changing the Lexicon

- Edit then Commit Changes (**Commit Record: C-c C-c**)
- Change lexical-id (**Rename Record: C-c C-r**)
- Delete (**Delete Record: C-c C-d**)

### Redisplaying a Changed Entry

- Normalize

## Saving/Restoring the Lexicon

## Starting the Lexicon Editing Mode

- M-X lexdb

**Note:** the interface talks to the database through the lkb, so you
have to have the lkb and the relevant grammar loaded to do anything.

# Installation

You can install the emacs interface by adding the following lines (or
something similar) to your .emacs:

      (autoload 'lexdb 
         "/home/bond/delphin/lkb/lexdb/pg-interface.el" 
         "LexDB interface for the LKB" t)
<update date omitted for speed>{% endraw %}