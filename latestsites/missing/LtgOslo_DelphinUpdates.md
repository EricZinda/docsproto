{% raw %}# Background

LTG staff actively participates in the informal, multi-national research
collaboration on [Deep Linguistic Processing with HPSG
Initiative](http://www.delph-in.net) (DELPH-IN). At the annual
DELPH-IN Summit (i.e. gathering of the clique), partners often give
overviews of (more or less) relevant developments at individual sites.
This page is intended to develop into a stream of LTG updates related to
DELPH-IN.

# 2013 Site Update

Two funded projects currently use and extend DELPH-IN technologies,
[WeSearch](http://www.mn.uio.no/ifi/english/research/projects/wesearch/)
(on methods for parser adaptation to user-generated content) and
[LAP](http://www.mn.uio.no/ifi/english/research/projects/clarino/) (the
Language Analysis Portal, part of the Norwegian CLARIN(O) initiative).

Work in WeSearch by AngelinaIvanova (on
relating bi-lexical dependency representations and DELPH-IN HPSG
analyses), by RebeccaDridan (on, among things,
ubertagging for faster and more accurate parsing), and by
StephanOepen and off-site collaborators (on working
towards documentation of ERG Semantic Analyses) are presented
individually at the 2013 Summit.

Another WeSearch activity has been collaborative work with
DanFlickinger on enabling the ERG to analyse inputs
annotated (optionally) with (two types of) candidate phrase boundaries,
or candidate target bi-lexical dependencies. Following are some example
inputs (using GML mark-up; see below) that exemplify this functionality:

      She met the ⌊(⌋cat in the hotel.⌊)⌋
      She met the ⌊(⌋cat in the hotel⌊)⌋.
      the cat saw⌊←¦sb-hd⌋ runs.
      the cat saw⌊←¦sb-hd¦<29:34>⌋ runs.

This functionality is not in the 1212 release of the ERG but currently
coming together in the ERG *trunk*; in a first instance, it will be
validated in in-house projects at LTG.

In the LAP context, there now is a [live pilot
portal](http://lap-test.hpc.uio.no) providing Web access to
pre-configured tokenization, PoS tagging, and syntactic dependency
parsing tools for English and Norwegian (running on a Norwegian national
supercomputer, i.e. potentially making available high-performance
computing capabilities to non-technical users). The LAP architecture is
based on the LAF (Linguistic Annotation Framework) data model, but using
a distributed NoSQL database as the annotation store, where components
record and retrieve annotatons from earlier components in complex
workflows. In the year to come, it is expected that the core
DELPH-IN toolchain will be made available through the LAP.

Finally, two

Last update: 2013-07-29 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LtgOslo_DelphinUpdates/_edit)]{% endraw %}