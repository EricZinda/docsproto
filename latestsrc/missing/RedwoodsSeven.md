{% raw %}# Background

In November 2010, the Seventh Growth of the Redwoods Treebank was
released; it adds a few new data sets, adding up to a total of some
38,200 annotated trees. Starting with this release, the data is no
longer released as a collection of tar(1) archives, but rather through
the DELPH-IN SVN repository (which is open for anonymous download).

The following is a compact summary of how to obtain a copy of the
Redwoods data proper, as well as of a ready-to-run installation of the
full DELPH-IN toolchain; the software should work on any reasonably
up-to-date Linux installation (on 32- or 64-bit x86 platforms) and,
among other things, allows exporting the internal Redwoods
representations into a variety of easily accessible formats.

      svn co http://www.emmtee.net/tags/paris logon
      cd logon/lingo/terg
      svn switch http://www.emmtee.net/erg/tags/1010
      cd ../..
      cd logon/lingo/redwoods
      svn switch http://www.emmtee.net/extras/paris/lingo/redwoods

Last update: 2010-11-27 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/RedwoodsSeven/_edit)]{% endraw %}