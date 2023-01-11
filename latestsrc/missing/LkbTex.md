{% raw %}# Overview

This page describes the use of LaTeX/PostScript with the DELPH-IN tools.

# LKB

The LKB allows you to print postscript snapshots of many
windows by clicking on the **print** button. This may not work for
non-ascii scripts.

There are also macros for creating LaTeX from the xml output, developed
as part of the Heart of Gold.

# LUI

You can export postscript from the Linguistic User Interface
(LUI) by pressing **p** and LaTeX by pressing **l**. The
postscript may not work for non-ascii scripts.

The LaTeX export from LUI uses
[avm.sty](http://nlp.stanford.edu/~manning/tex/avm.sty) for AVMs, and
[qtree.sty](http://www.ctan.org/tex-archive/macros/latex/contrib/qtree/)
for trees.

# LOGON web demonstrator

The LOGON web demonstrator allows you to export LaTeX
parse and derivation trees, as well as MRS.

The LaTeX export from these demonstrators assumes a set of [custom
macros](http://svn.emmtee.net/trunk/lingo/lkb/tex/mrs.sty) for MRS
formatting (mrs.sty), and further the standard LaTeX package
[qtree.sty](http://www.ctan.org/tex-archive/macros/latex/contrib/qtree/),
for the syntax trees. Further, qtree.sty requires pict2e.sty (which it
will load automatically) and mrs.sty assumes relsize.sty has been
loaded, and some commands use pstricks.

## delphin.sty

A vain attempt to gather some macros that may be generally useful for
describing systems.

e.g.:  \\newcommand{\\itsdb}{\\textsf{\\lbrack incr tsdb()\\rbrack}} 
for [\[incr tsdb()\]](http://www.delph-in.net/itsdb).

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/LkbTex/_edit)]{% endraw %}