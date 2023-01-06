{% raw %}# Page Status

This page presents user-supplied information, hence may be inaccurate in
some details, or not necessarily reflect use patterns anticipated by the
LOGON developers. The functionality documented here is not officially
supported and may still change. This page was initiated by
EmilyBender; please feel free to make additions or
corrections as you see fit. However, before revising this page, one
should be reasonably confident of the information given being correct.

# Running a web demo

The script \`www', found in the root directory of the LOGON
distribution, creates web accessible demos of parsing, generation, or
translation systems. The script as distributed contains appropriate
customization for all grammars distributed with logon:

    LOGONROOT=`pwd` ./www --binary --erg --port 8888

The above should result in an on-line web demo at port 8888 of your web
server. Note, however, that many firewalls block access to user ports,
so at least for external access you may have to talk to the IT crowd.

# Adding a grammar

- add a command line option and startup code to the \`www' script;
- create three additional files for each grammar:
  - lingo/lkb/src/tsdb/html/language.html: html boilerplate with
information about the grammar
  - lingo/lkb/src/tsdb/js/language.js: sample sentences
  - language.lisp, if your cpu definition makes reference to one
- make sure that logon/dot.tsdbrc has appropriate cpu definitions
- edit lingo/lkb/src/tsdb/lisp/www.lisp to add new language to
www-initialize

# Exporting data from an \[incr tsdb()\] profile for a .js file

1. Select the [itsdb](/itsdb) profile you want to work from in the
[itsdb](/itsdb) podium.
2. In the common lisp buffer (in the tsdb package), do something like
the following:

<!-- -->


    (loop for item in (analyze *tsdb-data* :condition "readings > 0 && 
                         readings < 10 && i-length < 10")
                  do (let ((i-id (get-field :i-id item))
                           (i-input (get-field :i-input item))
                           (readings (get-field :readings item)))
                       (format t "  { id: ~a, item: \"~a\", readings: ~a},~%" 
                               i-id i-input readings)))

The condition string should be customized to select the examples you
want for the sample data file. The format string matches what is
required by the javascript system.

# Other observations

A few other quirks we noted setting this up at UW:

- The user starting the demo has to have write (not just read)
permission on the grammar. (At UW, we have a separate user for this
web process, which means we end up making the grammar group
writable.)
- There of course has to be a \~/tmp directory. (We're running the web
demos as a separate user, so this needed to be created a new).
- pvmd3 has to be running
<update date omitted for speed>{% endraw %}