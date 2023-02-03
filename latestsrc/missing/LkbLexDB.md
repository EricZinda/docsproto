{% raw %}# LexDB Usage Instructions

(Please note: POWER USERS only.)

**NEW: The LKB/LexDB module now runs under both Linux and M$ Windows
(and presumably Solaris also).**

If running the LKB runtime binary:

- Download and install ([LkbInstallation](https://blog.inductorsoftware.com/docsproto/tools/LkbInstallation)) the latest
LKB, taking care to install/extract the lkb\_data.tgz archive into
the lkb installation directory (henceforth \[Linux\] \~/lkb).
- Ensure the environment variable PSQL is set: e.g. \[Linux\] set
export PSQL=t in .bashrc.

If running the LKB from source:

- Download and compile ([LkbCompilation](https://blog.inductorsoftware.com/docsproto/tools/LkbCompilation)) the LKB,
ensuring that
  
  - your .clinit.cl file contains (pushnew :psql \*features\*)
  - your .lkbrc file contains (psql-initialize)

Now initialize the database server
([LexDbPsqlInitialize](https://blog.inductorsoftware.com/docsproto/tools/LexDbPsqlInitialize)) and the lexical database
itself ([LexDbInitialize](https://blog.inductorsoftware.com/docsproto/tools/LexDbInitialize)).

## HOW TO set the filter

*LexDB -&gt; Filter*

The filter specified will be interpreted as an SQL WHERE clause.

Eg.

         userid = 'danf'
         userid = 'danf' AND dialect = 'my_dialect'
         userid IN ('danf', 'aac')
         confidence > 0.5

(Note: the default is TRUE. This represents the empty condition and will
select all available entries.)

The lexicon as seen by the login user is determined by that user's
database filter. Only revision entries matching the conditions in filter
can form part of the lexicon. In general multiple revisions for a given
entry will be returned; the most recent will become part of the visible
lexicon.

## HOW TO store LexDB in CVS

The LexDB may be dumped to text files which can then be uploaded to
storage in CVS.

1\. *LexDB -&gt; Dump*

(This will dump public schema tables to text files -- eg. lexdb.rev,
lexdb.rev\_key, lexdb.dfn, lexdb.fld, lexdb.meta) [BR](/BR)(Note: a TDL
dump will be performed also if \*lexdb-dump-tdl\* is set to t)
[BR](/BR)(Note: the database dump files are tab-separated with null as
\\N)

2\. Run the cvs commit command. E.g. \[Linux\]

- cvs commit \~/erg/lexdb.\*

## HOW TO retrieve LexDB from CVS

1\. Run the cvs update command to retrieve the latest dump file. E.g.
\[Linux\]

- cvs update \~/erg/lexdb.\*

2\. *LexDB -&gt; Merge new entries*

These steps update the LexDB (public schema) to include all new
revisions stored in a CVS dump file. The new entries will be copied to
the table public.rev\_new. Any changes made to your copy of the LexDB
since the last update will be preserved.

## HOW TO dump LexDB as TDL file

*LexDB -&gt; Dump (TDL format)*

Dumps active LexDB entries (see filter) to .tdl file.

## HOW TO edit entries in the LexDB

The LexDB-Emacs interface allows editing of lexical entries from within
an Emacs environment (with browsing functionality, field completion,
etc.). New revision entries are first stored in the users private
schema, and hence are visible only to the particular user. To commit the
entries to the public table (*public.rev*):

0\. Add the following line to your .emacs file:

(load "pg-interface")

1\. In \[<http://www.gnu.org/software/emacs/emacs.html> GNU Emacs\]:
*M-x lexdb* to enter LexDB major mode. Then see the PG menu.

Available commands in LexDB major mode are:

*C-l* : load (active revision of lexical entry) into Emacs

*C-c* : commit (edited/new revision of) lexical entry into LexDB

*TAB* : field completion

*M-TAB* : get (ring of) (active) entries in LexDB where value of current
field matches that in buffer

*M-n* : cycle through ring of entries obtained above

*M-s* : as M-TAB, but explicitly specify field value

*M-va* : view entries added in merge operation from dump file

*M-vs* : view entries in user's privat rev

Note: To remove a lexical entry from the current lexicon *lex*, create a
(head) revision where the dead field is set to t (true) rather than f
(false). In this manner we keep a revision history even for entries
which are no longer used (and such entries can be reactivated if
necessary). No revision entry should ever be deleted from the lexical
database itself.)

## HOW TO load TDL entries into private rev

To add a small number of new (revision) entries from a .tdl file: *LexDB
-&gt; Import TDL entries*. The grammatical fields of the LexDB will be
obtained from the TDL code. You will be queried to provide values for
other necessary fields.

## HOW TO commit entries to public rev

The LexDB consists of a single public schema and a set of private
schemas, one per user. New (revision) entries are placed initially in
your private schema. To commit (all) entries in your private schema to
the public table: *LexDB -&gt; Commit private rev*

## HOW TO list entries in private rev

From LKB: *LexDB -&gt; View private rev*

or

from Emacs LexDB major mode: *M-vs*

## HOW TO clear entries in private rev

*LexDB -&gt; Clear private rev*

## Further Topics

[LexDbInternals](https://blog.inductorsoftware.com/docsproto/missing/LexDbInternals) [BR](/BR)\["MWEs and Idiomatic
Expressions"\] [BR](/BR) \[<http://www.cl.cam.ac.uk/~bmw20/DT/Papers/>
Papers\]
<update date omitted for speed>{% endraw %}