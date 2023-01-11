{% raw %}# Background

In July 2012, on the occasion of the 50th anniversary of the
[Association for Computational Linguistics](http://www.aclweb.org/)
(ACL), a [special workshop](http://translit.i2r.a-star.edu.sg/r50/) was
devoted to “issues related to preserving, analysing and exploiting the
scientific heritage of the ACL”. Spurred by this event, a community
effort emerged, aiming to provide the full [ACL
Anthology](http://aclweb.org/anthology-new/index.html) as a high-quality
corpus with rich markup, following the TEI P5 guidelines. The goals of
this initiative are threefold: (a) to provide a shared resource for
experimentation on scientific text; (b)to serve as a basis for advanced
search over the ACL Anthology, based on textual content and citations;
and, by combining the aforementioned goals, (c)\~to present a showcase
of the benefits of natural language processing to a broader audience.

This community effort, dubbed the *ACL Anthology Corpus (AAC)*,
continues the tradition of projects like the [ACL Anthology Reference
Corpus](http://acl-arc.comp.nus.edu.sg/) (ACL ARC), [ACL Anthology
Network](http://clair.si.umich.edu/clair/anthology/index.cgi) (ANN), or
the [ACL Anthology Searchbench](http://aclasb.dfki.de/) (ACL ASB).

As of mid-2012 at least, AAC is in its early stages in many respects.
This page aims to provide a stable on-line access point to AAC-related
information, launched at the time of the 2012 Annual Meeting of the ACL.

# Canonical URL

For the time being, this page has been redirected into the wiki of the
[DELPH-IN](http://www.delph-in.net) community (whose members stand
behind the ACL Anthology Searchbench). However, for long-term validity,
please always refer to the canonical URL for the AAC initiative as:
<http://www.delph-in.net/aac/>.

# The 2012 Contributed Task

The main idea behind what was called a [Contributed
Task](http://translit.i2r.a-star.edu.sg/r50/taskintro/) at ACL 2012 was
to combine techniques from Optical Character Recognition (OCR) and
‘native’ text stream extraction from born-digital PDF documents, to let
alternate approaches complement each other and aim for the creation of a
rich XML format. This method would rely on OCR exclusively only in cases
where no born-digital PDFs are available—in case of the ACL Anthology
mostly papers published before the year 2000.

Details on specific sub-tasks and examples of challenges to high-quality
text and format extraction from the ACL Anthology, for the time being,
remain available from the [ACL 2012
pages](http://translit.i2r.a-star.edu.sg/r50/taskintro/). However, we
expect to migrate all relevant information and files to a more permanent
communication infrastructure (see below), hence please monitor this page
for updates.

Although many of the subtasks sketched above did not find volunteers in
this round, the 2012 Contributed Task, in our view, is an on-going,
long-term community endeavor. Results to date, if nothing else, confirm
the general suitability of (a) using TEI P5 markup as a shared target
representation and (b) exploiting the complementarity of OCR-based
techniques ([Schäfer & Weitz,
2012](http://www.aclweb.org/anthology/W12-3212.pdf)), on the one hand,
and direct interpretation of born-digital PDF files ([Berg, et al.,
2012](http://www.aclweb.org/anthology/W12-3211.pdf)), on the other hand.
Combining these approaches has the potential to solve the venerable
challenges that stem from inhomogeneous sources in the ACL
Anthology—e.g. scanned, older papers and digital newer papers, generated
from a broad variety of typesetting tools.

However, as of mid-2012 there still is no ready-to-use, high-quality
corpus that could serve as a shared starting point for a broad range of
Anthology-based NLP activities. In fact, we remain slighly ambivalent
about our recommendations for utilizing the current state of affairs and
expected next steps—as we would like to avoid much work getting underway
with a version of the corpus that we know is unsatisfactory. Further,
obviously, versioning and well-defined release cycles will be a
prerequisite to making the corpus useful for comparable research, as
discussed by Bird, et al. (2008).

In a nutshell, we see several possible avenues forward. For the ACL 2012
Contributed Task, we collected various views on the corpus data (as well
as some of the source code used in its production) in a unified SVN
repository. Following the open-source, crowd-sourcing philosophy, we
make this repository openly available to all interested parties for
future development (seel below), further augmenting it with support
infrastructure like, for example, a mailing list and shared wiki.

At the same time, our experience from the past months suggests that it
is hard to reach sufficient momentum and critical mass to make
substantial progress towards our long-term goals, while contributions
are limited to loosely organized volunteer work. A possibility we
believe might overcome these limitations would be an attempt at
formalizing work in this spirit further, for example through a funded
project (with endorsement and maybe financial support from organisations
like the ACL, ICCL, AFNLP, ELRA, or LDC). To decide on the way forward,
we will solicit comments and expressions of interest during ACL 2012,
including of course from the R50 workshop audience and participants in
the Contributed Task.

# SVN Access

All supporting files (documents and software) for the AAC initiate are
distributed through a shared [Subversion](http://subversion.apache.org/)
(SVN) repository. For read-only access, please use a command like the
following:

      svn co http://svn.delph-in.net/aac/trunk aac

Note that the repository, in mid-2012, contains some 55,000 files, so
please allow adequate time (between ten minutes and a couple of hours,
depending on network throughput) for the initial checkout.

Use of SVN is intended to ease the creation of stable release snapshots
or development branches for individuals or groups of collaborating
developers. To gain write access to the repository, please contact
[Stephan Oepen](http://emmtee.net/oe).

# Mailing List

In case you would like to participate in on-going and future AAC-related
efforts, please contact [Ulrich
Schäfer](http://www.dfki.de/~uschaefer/).

To receive updates on the ACL Anthology Corpus initiative, please
subscribe to our (very low-traffic) [mailing
list](http://lists.delph-in.net/mailman/listinfo/aac).

Last update: 2012-12-29 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/AclAnthologyCorpus/_edit)]{% endraw %}