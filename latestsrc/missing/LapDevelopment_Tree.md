{% raw %}# Background

The LAP Tree is a repository of *tools*, i.e. ready-to-run installations
of processing components used by LAP. Key design desiderata are
replicability (versioning) and relocatability (in terms of filesystem
locations), such that central installation on compute nodes is
completely avoided. Instead, the LAP Tree is realized as a
version-controlled SVN repository, where (in principle) individual
components can be checked out by an arbitrary user and into an abritrary
location, for immediate use through Galaxy. The general philosophy is to
include all ‘non-standard’ binaries and libraries in the LAP Tree,
including command interpreters (like Perl, Python, and Java) that
transcend the ‘basic’ operating system.

At present, all users use the *trunk* of the LAP tree (which is checked
out to /projects/lap/development/tree/trunk/) and updated manually (on
an as-need basis) by LAP developers. The mid-term goal is to enable
users to request individual revisions of components directly in Galaxy,
and then dynamically populate a user-specific instance of (relevant
parts of) the LAP Tree. To approach this vision (sometime in mid- to
late-2015, hopefully), we will need to be more careful about making
explicit the provenance of tool versions and inter-tool dependencies,
such that we can statically ‘reason’ over requested versions in a given
workflow.

To maintain an inventory of tools, versions, and licenses integrated in
LAP, the list below needs to be extended with full and up-to-date
information (mostly copying from the build directories).

# Interpreters

- Java (7u65); [OBCL](http://java.com/license): validated
- Perl (5.20.1);
[GPL 1.0](http://svn.emmtee.net/lap/trunk/tree/perl/LICENSE):
validated
- Python (2.7.6); [PSFL
2.0](http://svn.emmtee.net/lap/trunk/tree/python/LICENSE): validated
- Ruby (2.2.2);
[BSDL](http://svn.emmtee.net/lap/trunk/tree/ruby/LICENSE):

# Labeling

- langid.py

# Segmentation (Sentences and Tokens)

- NLTK Punkt: validated (twice)
- NLTK Tokenizer: wrapped (not validated)
- Tokenizer Segmenter : validated
- REPP Tokenizer (trunk): validated

# Tagging

- NLTK Tagger: validated
- HunPos (1.0): validated
- HFST: validated
- VislCG: validated
- Giellatekno:
- Oslo-Bergen Tagger;

# Parsing

- MaltParser (1.7.2): validated
- Bohnet & Nivre (2012):
- VislCG: validated

# Interfacing

- RESA Alignment: to be validated
- Corpus Import: to be revisited
- CoNLL Export: validated
- RDF Export:
- CG3 Export:

Last update: 2016-09-06 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_Tree/_edit)]{% endraw %}