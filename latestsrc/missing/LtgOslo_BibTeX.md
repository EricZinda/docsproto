{% raw %}# Background

When writing jointly, with various sub-groups of people, one of the more
time-consuming tasks can be the unification of BibTeX entries from
multiple sources. To avoid duplicate entries in bibliographic
references, it can be helpful to use a common scheme for generating
citation keys, i.e. the unique strings used in \\cite{} commands.
Furthermore, there is some stylistic variation in how to typeset
bibliographic references, and there can even be discrepancies between
different so-called BibTeX styles, for example in the range of entry
types that they support and which files they allow (or require). Thus,
it can further be useful to converge on a small-ish subset of common
BibTeX styles and make sure to operate within their parameters.

# Towards a Shared References Collection

All LTG staff should be able to access an emerging collection of shared
LaTeX and BibTeX files in SVN:

      svn co http://svn.nlpl.eu/ltg/tex ltg

Inside the bib/ sub-directory, there is a hierarchy of folders to hold a
(future) file-based database of BibTeX entries. The main reason to keep
each entry in a file of its own is version control in SVN, where there
will be a natural notion of (original) authorship and revision history
for each individual entry. With the exception of files in the etc/
folder, each entry should be in a file of its own, named according to
its unique citation key (see below) and, for ease of retrieval, stored
in the sub-directory of the first letter of the citation key.

We envision various ways of taking into use this database, ranging from
merely copying individual entries into a personal BibTeX file,
concatenating all entries into a single file (for inclusion in a
specific writing project), or using entries directly from the SVN
database. Over time, we will have more to say an possible use cases.

The most common pattern of use so far appears to check out the LTG
BibTeX database as a sub-directory called ltg with each writing project.
Then, folks often use a Makefile as follows:

    submission.pdf: submission.tex ltg.bib
            -/bin/rm submission.bbl
            pdflatex submission
            bibtex submission
            pdflatex submission
            pdflatex submission
    
    ltg.bib:
            cat ./ltg/bib/etc/general.bib ./ltg/bib/etc/conferences.bib \
              ./ltg/bib/etc/journals.bib ./ltg/bib/etc/addresses.bib \
              ./ltg/bib/?/*.bib > ltg.bib

The above will concatenate the complete BibTeX database into a file
ltg.bib, which can then be used in the actual paper (here, we are
assuming that the master file is called submission.tex), e.g.

      \input{ltg/macros.tex}
      \usepackage{apacite}
      ...
      \bibliographystyle{apacite}
      \bibliography{ltg,local}

In the above, ltg.bib is (optionally) combined with an ad-hoc collection
of BibTeX entries in a file called local.bib.

# Naming Conventions for Citation Keys

Please consult the files below ltg/bib/ (in the above SVN repository)
for existing entries and inspiration in creating new entries.
Specifically, please obey the following format in creating citation
keys:

- for references with a single author, use the last name suffixed with
the last two digits of the year of publication, e.g. Alshawi:92. In
case there are multiple entries by the same name in any given year,
add additional letter suffices, e.g. Erbach:91a.
- for multi-authored references, compose the first three letter of the
first three authors, plus the two-digit year, e.g. Ber:Hel:04 for
Beermann and Hellan (2004) and Bon:Oep:Sie:05 for Bond, Oepen,
Siegel, Copestake, and Flickinger (2005).

We plan to continually grow our collection of BibTeX entries and share
it within the group (and possibly external collaborators), therefore
consistency of entries is important. Also, note that there is a set of
pre-defined strings in the etc/ sub-directory, e.g. for the names of
conferences and institutions. Where applicable, please make good use of
these or add additional ones, for example:

      @string{MONS:04 = {Rapport fra det 10. møte om norsk språk}}
      @string{L:MONS:04 = {Kristiansand, Norway}}
    
      @inproceedings{Joh:Nyg:04b,
        author = {Johannessen, Janne Bondi and Nygaard, Lars},
        title = {Oslo-skogen. {E}n trebank for norsk},
        booktitle = MONS:04,
        address = L:MONS:04,
        pages = {},
        year = 2004
      }

# Conventions for Individual BibTeX Fields

In crafting individual BibTeX entries, there are a number of choices
regarding the values to individual fields to be made. Inevitably,
different publishing channels will have different requirements.
Following are some reflections and recommendations, to maximize
portability and reuse across channels.

In terms of names, some channels encourage full given names while others
abbreviate first names to just initials. In principle, this choice
should be made by a specific BibTeX style, but for there to be a choice,
the *raw* data needs to make available the necessary information. Hence,
our recommendation is to write out given names in shared BibTeX entries,
for example:

      author = {Toutanova, Kristina and Manning, Christoper D.
                and Flickinger, Dan and Oepen, Stephan}

In a few corner cases, it may be appropriate to resort to variant ways
of structuring a list of authors, for example:

      author = {Rosén, Victoria and De~Smedt, Koenraad and Meurer, Paul},

We also recommend specifying names in the format ‘Flickinger, Dan’, i.e.
letting the given name(s) follow the family name, separated by a comma.
This way the part that is the family name is explicit, which means we
encode more information (partly in anticipation of BibTeX someday
handling Asian-style names).

In terms of capitalization of (book) titles, again there will be
different demands for different channels, and control should largely be
delegated to the BibTeX style. To support the wides possible range of
use cases, use so-called *[title
case](http://en.wikipedia.org/wiki/Letter_case)* (rather than standard
capitalization rules for running text, so-called *sentence case*), e.g.

      title = {Paraphrasing Treebanks for Stochastic Realization Ranking}

When using BibTeX styles that automatically downcase, it is important to
protect capital letters or acronyms that must never be spelled in lower
case. For example:

      title = {Stochastic {HPSG} Parse Selection using the {R}edwoods Corpus}

In accordance with the BibTeX manual (and the APA recommendations; see
below) the address field for conference and workshop proceedings should
record the location of the conference (not the business address of the
publisher). In fact (contrary to many entries in the ACL Anthology)
@inproceedings entries need not include the publisher field for
‘pseudo-’publishers like the ACL, ELRA, EAMT, et al.

# Recommended BibTeX Styles

Several LTG members use the [APA citation
style](http://www.dante.de/CTAN//biblio/bibtex/contrib/apacite/apacite.pdf),
which is very comprehensive, highly customizable, and relatively well
documented. Where the ACL conferences, for example, in principle
prescribe the use of their own BibTeX style, it is usually
straightforward to substitute APAcite and deliver a very convincing
mimicry of the ACL citation style, while avoiding its shortcomings.

# Other Relevant Best Practices

As always, use Unix-style newlines and UTF-8 character encoding. Wrap
all lines at column 80 (i.e. using a *column-width* value of 79 in a
modern editor like emacs). Please finish each file with a closing
newline.

As regards in-text bibliographic references, the APA citation package
provides three basic macros: \\cite{}, \\citeA{}, and \\citeNP{}. The
first form yields a reference enclosed in parenthesis, suitable for
citations that serve as background information, i.e. typically act like
parentheticals to their context of use. The second form only
parenthesizes the year of publication and is suitable for references
that serve a grammatical function in their context of use. Finally, the
third form lacks all parentheses and can be used to avoid double
embedding, i.e. when used within an enclosing set of parentheses.
Consider the following example to see the three distinct forms:

      \citeA{Lon:Oep:Ber:04} sketch the LOGON MT system, which has some superficial similarity
      to the earlier VerbMobil effort \cite{Wahlster:00} and employs semantic transfer in the
      framework of Minimal Recursion Semantics (\MRS; \citeNP{Cop:Fli:Pol:05}).

Once typeset and processed by BibTeX, this will yield:

- *Lønning, et al. (2004) sketch the LOGON MT system, which has some
superficial similarity to the earlier [VerbMobil](/VerbMobil) effort
(Wahlster, 2000) and employs semantic transfer in the framework of
Minimal Recursion Semantics (MRS; Copestake, et al., 2005).*

Last update: 2019-09-24 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LtgOslo_BibTeX/_edit)]{% endraw %}