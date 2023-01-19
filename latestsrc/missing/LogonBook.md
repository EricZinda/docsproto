{% raw %}# Background

This page (or possibly set of pages below LogonBook) serves a purpose
internal to the LOGON project: help contributors to the final LOGON book
coordinate their efforts. We expect to collect a complete initial set of
chapters before the summer of 2007; these pages will be continuously
updated with instructions to authors, specifically style recommendations
and LaTeX information.

# Collaborative Authoring

The LOGON book project will be compiled in LaTeX, with all source files
organized in CVS version control; please consult the pages
LogonInstallation/CvsBasics and
LogonInstallation/InstallationBasics
for background.

The main difference to our use of CVS in past development of the LOGON
demonstrator is the name of the top-level CVS module. Instead of the
module named logon, all book files are organized as a module named book.
Thus, the following should yield a complete initial LaTeX tree:

      cvs -d :pserver:oe@cvs.emmtee.net:/logon/CVS checkout book

Remember to substitute your LOGON work space user name for oe in this
example.

Once the checkout from CVS is complete, there will be a new directory
book/ with sub-directories planning/ and submission/. Initial chapter
versions that will go into the peer reviewing phase reside in the
submission/ directory, with yet another sub-directory for each chapter.
Take a look at the top-level LaTeX file master.tex to understand the
directory structure and naming conventions. The only change(s) you
should have to make to this file is in the \\includeonly section, where
removing the LaTeX comment character (which is the per cent sign) before
each chapter name will activate inclusion of that chapter. When, to get
started, you add an abstract for a chapter for which you are the primary
author, say the chapter named *fundamentals* (with helge as the lead
author), uncomment the corresponding line in master.tex and add your
text to the file fundamentals/chapter.tex.

To typeset and preview your contributions, run latex on the master file,
or (as a short-hand for the sequence of running both LaTeX and BibTeX as
many times as is needed to include bibliographic references et al.)
simply invoke the following within the submission/ directory:

      make

The current setup uses per-chapter bibliographies, which means that
bibtex runs need to be performed for each (active) chapter. The make
command will do that automatically, but it appears that some MacOS TeX
installation do not include all of the command-line utilities. Assuming
that *fundamentals* were your active chapter (by means of an
\\includeonly declaration, see above), the following sequence of
commands should correspond to the effects of running make:

      latex master
      bibtex fundamental
      latex master
      latex master

# Common Acronyms and Abbreviations

People, even within our homogeneous consortium, differ in their
aesthetic judgment, specifically when it comes to typography. The
publishing house and its copy editor(s) will have the final decision on
all aspects of typesetting, including sentence-final spacing, the use of
commas or not following common abbreviations like *e.g.*, *i.e.*, *viz.*
et al., the conventions used for quote marks, spacing around dashes, and
even the choice of font attributes in various contexts. During the final
copy editing phase of the volume, we will all have to devote some effort
to making our LaTeX sources conformant to specific instructions provided
by the copy editors. However, for some known sources of variation, we
can proactively use LaTeX macros to simplify this task. Specifically, we
ask that you use the existing \\eg, \\ie, \\viz, et al. macros, combined
with pre-defined macros for all-caps acronyms for example:

      \MRS\ is the common meaning representation language in \LOGON, \ie\ the
      interface representation between components.

Note the trailing backslash following all macros that are followed by a
space, which is required for the space to appear in the output. In the
case of a non-alpha, non-space character following the macro, there is
no need for the extra backslash, hence the comma follows the \\LOGON
macro directly in this example. This requirement implies that the plural
of macros has to be formed as, say, \\XLE{}s, because without the
intervening empty parameter list {}, the macro name would appear to be
*XLEs*, which is undefined. For convenience, \\MRSs is an exception to
this rule, where we provide a plural form of the macro already, because
it is quite common. Please consult the macro definitions in logon.sty
for the names of existing macros, and please do not hesitate to define
more (typically at the top of your own chapter.tex, though you might
also nominate them for inclusion in the global macro file). For acronyms
that you plan to use only one or a few times, you can also just enclose
them in the globally provided \\acronym macro. For example,
\\acronym{HMM} will display HMM using the globally defined style for
all-caps acronyms.

Following are a few more general LaTeX recommendations (with more to
come, surely):

- For emphasis in running text, use the \\emph{} macro rather than the
deprecated \\em, e.g.
We define \\emph{coverage} as the ratio of ...; the benefit of
\\emph{} over \\em is that it automatically inserts what is know as
*italic correction*, i.e. what would otherwise have to be typeset as
{\\em coverage\\/}.
- Avoid the use of bold face in running text; bold can be suitable in
the keys of itemized definitions or table headings, but it should
not be used in running text for emphasis.
- Avoid simple double quotes ("); use LaTeX-style opening and closing
sequences of back and single quotes, respectively, instead.

# Feature Structures, Trees, and Hierarchies

There is a wide variety of macro packages for linguistic data, and it is
important that we make a consistent selection throughout the book, both
for aesthetic and technical reasons.

Feature structures (including f-structures), should be typeset using the
avm.sty package by Chris Manning; the package provides reasonably
extensive [on-line
documentation](http://nlp.stanford.edu/~manning/tex/avm-doc.pdf). By
default, all \\avmoptions{} are disabled; thus, in case you wanted to
use *active* or *centered* mode, say, you should place a command like

      \avmoptions{active,centered}

at the start of your own file chapter.tex. Note that *active* and
*centered* are enabled by default in the derived package avm+.sty by
Walt Detmar Meurers, so in case you are used to this package, make sure
to add the right \\avmoptions{} to the preamble of you chapter source
file. Please note that your feature structures should *not* contain font
selection instructions, as these are determined globally for the book as
a whole; accordingly, please always typeset feature names in all
uppercase letters (unlike the examples given in the documentation for
this package, which assumes that the font used for features is set to
small caps). For in-text occurences of AVM elements, the LOGON book
setup augments the AVM package by commands \\avmsort{}, \\avmfeature{},
and \\avmvalue{}, which each take one argument and typeset it using the
appropriate font. For example:

      In \begin{avm}\[ \asort{foo} BAR & baz \]\end{avm}, the type of the structure is
      \avmsort{foo}, and it has one feature \avmfeature{BAR} with value \avmvalue{baz}.

For the construction of trees, there are several options, and your
choice may vary according to parameters like the complexity of
individual nodes and your requirements on fine-grained control over node
placement, labeling of arcs, et al. Our default suggestion for tree
drawing is the [QTree](http://www.ling.upenn.edu/advice/latex/qtree/)
package, which strikes a good balance in ease of use and control
options; QTree comes with good
[documentation](http://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf),
including many examples. Note that QTree is an extension of the earlier
[QobiTree](http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=qobitree)
package, and if you prefer the original (somewhat more verbose) syntax
of QobiTree, that is available too.

A fairly traditional tree drawing package that we do *not* want to
include is tree-dvips.sty by Emma Pease (of CSLI). Its main limitations
are the relatively crude node placement and exclusive support for
PostScript generation only. However, we provide two closely related
packages, viz.
[LingTrees](http://arts.anu.edu.au/linguistics/people/averyandrews/software/latex)
by Avery Andrews and the allmighty [PSTricks](http://tug.org/PSTricks)
by Timothy van Zandt. Both packages include comprehensive documentation
(available from the links above); in many respects, LingTrees is a
front-end to PSTricks, aiming to make partially automate the generation
of complex tree descriptions by virtue of a specialized description
language and pre-processor script (named trees.py and included in our
CVS tree). Furthermore, LingTrees provides a legacy layer of
compatibility macros for the most common commands of tree-dvips.sty, so
in some cases you might not even have to adapt existing tree code
(much).

# MRS Expressions

The LOGON book setup includes a new set of macros for typesetting MRSs.
As with many of the other macros we provide, the main goal here is to
separate the structural description of an MRS (or parts of an MRS) from
decisions about typography or aesthetics. Please try to avoid all direct
format control in MRSs (and AVMs, trees, et al.), e.g. do not select a
specific font, font attributes, or size. The MRS macros essentially
provide one command per MRS component type, e.g. (working from the
smaller to the larger) for a single variable, one role--value pair, one
EP, and so on. At the top-level, there is a choice as to whether a full
MRS should be typeset in standard, running-text mode (which is only
feasible for quite short expressions) or in multi-line, aligned mode.
Consider the following sample (see below for details on the example
environment):

      \rolesfalse
      \propertiestrue
      \begin{exe}
        \ex\label{ex:generation:athlete}
        \sblock{\sh{0}}{%
          \slep{0}{proposition\_m}{\srv{ARG0}{e}{0}{}, \srv{MARG}{h}{1}{}},
          \slep{2}{\_run\_v}{%
            \srv{ARG0}{e}{0}{\svp{TENSE}{past}}, \srv{ARG1}{x}{0}{}},\\
          \sep{\srule}{\_the\_q}{%
            \srole{ARG0}{\svar{x}{0}{}}, \srv{RSTR}{h}{4}{}, \srv{BODY}{h}{5}{}},
          \slep{6}{\_athlete\_n}{\srv{ARG0}{x}{0}{}},\\
          \slep{6}{\_young\_a}{\srole{ARG0}{\srule}, \srv{ARG1}{x}{0}{}},
          \slep{6}{\_polish\_a}{\srole{ARG0}{\srule}, \srv{ARG1}{x}{0}{}}%
        }%
        {\sqeq{1}{2}, \sqeq{4}{6}}
      \end{exe}

This example deliberately uses several variants of the macros: the
general command to typeset one EP, for example, is \\sep{}{}{}, where
the three arguments are the handle, predicate, and roles, respectively.
The variant command \\slep{}{}{} is an abbreviation for convenience:
instead of an arbitrary first argument, it expects as its first argument
the variable identifier of the handle, i.e. \\slep{0}{foo}{...}
translates into \\sep{\\sh{0}}{foo}{...}. Likewise, \\sh{0} is an
abbreviation of \\svar{h}{0}{}, i.e. a variable of type *h*, with
identifier 0, and an empty set of variable properties. Please see the
style file mrs.sty in the top-level book directory for more examples and
the full inventory of MRS macros. Two boolean toggles control whether
role labels (ARG0 et al.) and variable properties (e.g. TENSE) are
included in the output. The defaults are \\rolesfalse and
\\propertiestrue, but it is possible to change these at any point (note
that such changes remain in effect until a later declaration, though the
above defaults are restored upon entry to each chapter). For increased
flexibility, please always include role labels in the LaTeX code for
MRSs, even if you believe you never want to activate display of such
labels in your chapter.

# Examples, Glosses, and Such

For numbered linguistic examples and other in-text numbered and
displayed material, we provide the fairly standard package
[gb4e](http://www.ctan.org/tex-archive/macros/latex/contrib/gb4e/gb4e-doc.pdf).
Among other things, it provides nested examples, flexible referencing to
examples or sub-examples, and aligned glosses. For a simple example,
including an in-text reference, consider the following

      Examples \refx{ex:erg:bridge} and \refx{ex:erg:shelter} below are taken from
      the development corpus.
      \begin{exe}
        \ex\label{ex:erg:bridge}
          We asked him about the classic bridge.
        \ex\label{ex:erg:shelter}
          He recommended that the club build a shelter.
      \end{exe}

To provide an aligned gloss, and optionally a translation, there are
some additional commands, e.g.

      \begin{exe}
        \ex\label{ex:erg:vei}
        \gll
          Veien         mot     Bergen er kort.\\
          Road\sub{def} towards Bergen is short.\\
        \trans The road towards Bergen is short.
      \end{exe}

Note that the commands \\refx{} and \\sub{} are LOGON-specific
extensions to the gb4e package.

# Bibliographic References

For all citations and bibliographic references, we will use the BibTeX
facilities, specifically, the [APA citation
style](http://www.dante.de/CTAN//biblio/bibtex/contrib/apacite/apacite.pdf).
Please consult the files logon.bib and master.bib (in the top-level
submission/ directory of the book source tree) for existing entries and
inspiration in creating new entries. Specifically, please obey the
following format in creating citation keys:

- for references with a single author, use the last name suffixed with
the last two
  
  digits of the year of publication, e.g. Alshawi:92. In case there
are multiple entries by the same name in any given year, add
additional letter suffices, e.g. Erbach:91a.
- for multi-authored references, compose the first three letter of the
first three
  
  authors, plus the two-digit year, e.g. Ber:Hel:04 for Beermann and
Hellan (2004) and Bon:Oep:Sie:05 for Bond, Oepen, Siegel, Copestake,
and Flickinger (2005).

We plan to continually grow our collection of BibTeX entries and share
it with all contributors, therefore consistency of entries is important.
Also, note that master.bib provides a set of pre-defined strings, e.g.
for the names of conferences and institutions; where applicable, please
make good use of these or add additional ones, e.g.

      @string{MONS:04 = {Rapport fra det 10. møte om norsk språk}}
    
      @inproceedings{Joh:Nyg:04b,
        author = {Janne Bondi Johannessen and Lars Nygaard},
        title = {Oslo-skogen. {E}n trebank for norsk},
        booktitle = MONS:04,
        address = {Kristiansand, Norway},
        pages = {},
        year = 2004
      }

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
superficial similarity to the earlier VerbMobil effort
(Wahlster, 2000) and employs semantic transfer in the framework of
Minimal Recursion Semantics (MRS; Copestake, et al., 2005).*

As we aim to cross-reference within the book, we will frequently want to
refer to other chapters in the LOGON volume. Our LaTeX set-up includes
mock citation commands for in-volume references analoguous to the APA
citation commands, viz. \\Cite{}, \\CiteA{}, and \\CiteNP{}. Valid
citation keys for these commands, are chapter identifiers (corresponding
to each sub-directory below submission/, e.g. *introduction*,
*fundamentals*, *demonstrator*, *norgram*, *parsing*, *trepil*, *erg*,
*redwoods*, et al. Consider the following example

      This chapter extends the discussion of \CiteA{parsing} and assumes basic notions
      from the \MRS\ overview chapter \Cite{fundamentals}. 

The above code, when typeset, yields:

- *This chapter extends the discussion of Chapter 5 and assumes basic
notions from the MRS overview chapter (Chapter 2).*

To create additional BibTeX entries, please add to the chapter-local
file, within the same sub-directory as the chapter.tex file. The name of
each per-chapter BibTeX file reflects the chapter name, e.g.
introduction/introduction.bib for the first chapter. The editors will
compare per-chapter entries and over time unify new entries into the
shared master.bib.

# Test Suites and Corpora

The are pre-defined macros for the various testsuites and corpora used
in LOGON; please always refer to these data sets by use of these macros,
e.g. \\basets, \\mrsts, \\tur, \\JH, \\PS, \\TG, or \\JHPSTG. For the
development corpus, there are further variants to refer to the test
sets, for example \\JHk (known vocabulary), \\PSu (unknown vocabulary),
or \\JHPSTGt (the union of all test sets, including the known and
unknown vocabulary sub-divisions).

# Labels: Protecting the Global Name Space

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/LogonBook/_edit)]{% endraw %}