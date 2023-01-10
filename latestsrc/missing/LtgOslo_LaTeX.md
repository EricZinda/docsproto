{% raw %}# Background

People, even within our homogeneous research group, differ in their
aesthetic judgment, specifically when it comes to typography. When
writing collaboratively, it can be beneficial to rely on a set of shared
assumptions and conventions, to help synchronize LaTeX sources from
multiple authors. Following are some suggestions for best practices that
at least some LTG members have found useful in the past.

# General Best Practices

For maximum compatibility across platforms, use Unix-style newlines and
the UTF-8 character encoding. The following may serve as a good template
header for LaTeX (where the specifics of the document class and default
font size are subject to adjustments, naturally):

      % -*- coding: utf-8; -*-
    
      \documentclass[11pt]{article}
      \usepackage[T1]{fontenc}
      \usepackage[utf8]{inputenc}
      \usepackage{apacite}

Limit lines to at most 79 characters. In emacs, use auto-fill mode and
set *fill-column* to 79, in vim set *textwidth* to 79.

When working on a shared set of LaTeX sources, avoid unnecessary, purely
cosmetic edits. For example, to follow the above recommendation it may
be tempting to *re-fill* entire paragraphs, i.e. after inserting a word
somewhere make the editor reaarange line breaks (which have no
significance to LaTeX in running text). Such re-filling will typically
lead to a seeminly large revision in SVN, as it effectively changes
around a large number of lines in the source file (for no logical
change). One technique (advocated by at least some LTG folks) to
mitigate this issue can be starting each *sentence* on a line of its own
in the LaTeX sources, e.g.

      Wikipedia is met with great interest by researchers in (computational)
      linguistics.
      It provides a massive and relatively high-quality collection of text
      and (predominantly unstructured) encyclopedic knowledge.

# Historic Notes (To be Updated)

Following are a few more general LaTeX recommendations (with more to
come, surely):

- For emphasis in running text, use the \\emph{} macro rather than the
deprecated \\em, e.g.
We define \\emph{coverage} as the ratio of ...; the benefit of
\\emph{} over \\em is that it automatically inserts what is know as
*italic correction*, i.e. what would otherwise have to be typeset as
{\\em coverage\\/}.
- Similarly, use the macros \\textit{}, \\textsc{}, and \\textbf{}
instead of the deprecated \\it etc. macros.
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
of QobiTree, that is available too. For TikZ users, there is a drop-in
replacement for qtree, tikz-qtree, that draws trees using TikZ and
supports some additional TikZ features.

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
style file [\`mrs.sty\`](http://svn.emmtee.net/ltg/tex/mrs.sty) for more
examples and the full inventory of MRS macros. Two boolean toggles
control whether role labels (ARG0 et al.) and variable properties (e.g.
TENSE) are included in the output. The defaults are \\rolesfalse and
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

The package gb4e turns the \\automath feature on making symbols \_
(underline) and ^ (caret) active. This means you can get sub- and
super-scripting outside maths mode, e.g. write foo\_i instead of
foo$\_i$. However this can cause errors such as ! TeX capacity exceeded,
sorry \[parameter stack size=10000\]. You can turn off the \\automath
feature by putting \\noautomath in your preamble.

The gb4e package is incompatible with the beamer class. A more modern
package providing the same features as gb4e, but also compatible with
beamer, is expex.

# Tables

The default support for creating tables in LaTeX is not optimal and much
better results can be produced using the
[booktabs](http://www.ctan.org/tex-archive/macros/latex/contrib/booktabs/)
package of Simon Fear. The
[documentation](http://mirrors.ctan.org/macros/latex/contrib/booktabs/booktabs.pdf)
that comes with it also serves as an excellent style guide for tables.
The following is an example of a simple table using booktabs. (Note how
the table is structured around the commands \\toprule, \\midrule and
\\bottomrule, which will insert appropriate vertical spacing. Should you
need additional spacing use \\addlinespace.)

      \begin{table}[t!]
        \begin{center}
        \begin{tabular}{@{}lcc@{}}
          \toprule
          &\multicolumn{2}{c}{\textbf{Judgement}}\\
          \cmidrule{2-3}
          \textbf{Element}     &\textbf{Yay}&\textbf{Nay}\\
          \midrule
          Vertical rules   &        & X \\
          Double rules     &        & X \\
          Horizontal rules &  X     &   \\
          Single rules     &  X     &   \\
          \bottomrule
        \end{tabular}
        \caption{This is a simple table.}
        \label{tb:mytable}
      \end{center}
      \end{table}

The package ctable is extends booktabs to a simple but flexible command
\\ctable, and abbreviates the rule commands to \\FL, \\ML, \\LL (first,
middle, last). The package has useful options for things like notes in
the table and landscape tables as well. Using ctable, the table above
becomes:

    \ctable[botcap,
    caption={This is a simple table},
    label=tb:mytable,
    pos=t!]{@{}lcc@{}}{}{
         \FL
          &\multicolumn{2}{c}{\textbf{Judgement}}\NN
          \cmidrule{2-3}
          \textbf{Element}     &\textbf{Yay}&\textbf{Nay}\ML
          Vertical rules   &        & X \NN
          Double rules     &        & X \NN
          Horizontal rules &  X     &   \NN
          Single rules     &  X     &   \LL
    }

## Tables of Numbers

In our line of work, tables of numbers are quite frequent. In
particular, tables of decimal numbers are very common. Ideally, this
kind of table should have the numbers aligned on the decimal point with
either the widest number centered or right-aligned (according to CMS16,
anyways). There are various hacks to get this right, but the best
solution is to use the siunitx package. This package supports both ways
of formatting columns. For a right-aligned column of numbers,
automatically rounded to three significant digits, with a maximum of 1
digit before the period and a maximum of 3 after, use the following:

    % In the preamble:
    \usepackage{siunitx}
    \sisetup{table-number-alignment=right,                                  
             table-text-alignment=right,
             detect-mode=true}
    
    % And then in the document:
    \ctable{lS[table-figures-integer=1,table-figures-decimal=3,round-mode=figures,round-precision=3]}{}{
        \FL
    Header 1 & {Header 2} \ML
    Label & 1.23456 \NN
    Label & 12.3678
       \LL
    }

Note the braces around the header of the numerical column. These are
required to prevent siunitx from parsing the text as a number. This will
result in a typeset value of "1.23" in the first row and "12.4" in the
second. Since the S column specifier is rather verbose, I recommend
wrapping it in a custom column type, like so:

    \newcolumntype{R}[2]{S[table-figures-integer=#1,table-figures-decimal=#2,round-mode=figures,round-precision=3]}

This lets the example above use the column spec lR{1}{3} instead of the
overlong S\[...\] spec. For centered numbers, the table-\* options to
\\sisetup and the S specifier can be omitted. For chapter and verse on
this (and many other neat features), see the siunitx documentation.

# Squeezing under the Page Limit

A well-known tribulation in academia is the dreaded page limit.
Sometimes, you just have too much to say and not quite enough space on
the page to say it. The first thing to look for is paragraphs whose last
lines are very short. Reword them so that you can squeeze them into one
line less.

If you still need to squeeze a bit, there are some slightly more naughty
things that can be done:

- The amount of space between the title and author info and the start
of the text: \\titlebox3.5cm
- Spacing after a floating figure: \\setlength\\textfloatsep{2.5mm}
- If you have enumerations or itemizes, use the enumitem package
remove the spacing between items: \\setlist{nolistsep}

The exact spacings above can be tweaked to taste; and remember to not
make it *too* blatant that you're squeezing.

**Warning! This last option is truly the nuclear option. It is more than
a little shady, and if you're caught it can be grounds for outright
rejection of your paper. Here be dragons, caveat emptor, cave canem,
etc, etc, etc.**

Finally, if you just can't get rid of those last few lines, you can
reduce the amount of space between lines:
\\renewcommand\\baselinestretch{0.95}. Note that this parameter is very
sensitive, and can make your paper look very funny indeed. Use with
care.
<update date omitted for speed>{% endraw %}