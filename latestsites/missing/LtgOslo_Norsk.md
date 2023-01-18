{% raw %}# Background

LTG-internal notes on available data and software resources for the
morpho-syntactic analysis of Norwegian text.

# History

- Norsk Ordbank
- OBT
- NorGram
- NDT
- INESS
- UD
- UDPipe

# Data

LTG maintains its own copy of NDT in SVN:

      svn co http://svn.emmtee.net/ltg/ndt

Main differences in this version are an organization of the directory
and file structure that makes explicit the correspondences between raw
text files and the annotated versions. Furthermore
[FredrikJørgensen](/FredrikJ%C3%B8rgensen) has provided a version of the
raw texts aligned to the sentence segmentation in the gold standard.

# Segmentation

Segmentation of raw, running text into (a) *splitting* into ‘sentences’
(i.e. root-level utterances) and (b) *tokenization* into ‘word’-like
units. Two to three known de-facto strandards: OBT-style, NorGram-style,
and NDT-style.

The mtag tool is the first component in the OBT pipeline and implements
sentence spilitting, tokenization, and multi-tagging (morphological
analysis). OBT tokens at times comprise multi-words, presumably for
‘words with spaces’ (*for eksempel*) and maybe for some names?

NDT tokenization (I believe) resembles PTB-style tokens, e.g. splitting
at hyphens and slashes. StephanOepen has started to
develop an NDT-compatible tokenizer in the [REPP
framework](http://moin.delph-in.net/ReppTop) (through adaptation of
PTB-style rules); he would also be interested in using REPP to devise a
rule-based sentence splitter. One main advantage of REPP is its output
of character offset pointers, which are often useful in applications.

The Punkt implementation in NLTK includes a pre-trained sentence
splitting model for Norwegian.

The LAP team has been discussing integration of NorGram parsing, which
would most likely make available the NorGram sentence splitter and
tokenizer as stand-alone components; however, they require licensing of
the proprietary XFST toolkit.

UDPipe implements a classification-based approach to splitting and
tokenization and ships with pre-trained models for Norwegian. While the
current release of the Norwegian UD treebank lacked information on
whitespace boundaries, a forthcoming new version will address this
problem.

# Morphology

By *morphology* we mean all sub-tasks of analyzing word-internal
structure, including PoS tagging and lemmatization.

# Syntax
<update date omitted for speed>{% endraw %}