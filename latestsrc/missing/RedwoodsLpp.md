{% raw %}# Data/Software Companion for Layers of Interpretation: On Grammar and Compositionality

Bender, Emily M., Dan Flickinger, Stephan Oepen, Woodley Packard and Ann Copestake. 2015. [Layers of Interpretation: On Grammar and Compositionality](https://aclanthology.org/W15-0128/). In Proceedings of the 11th International Conference on Computational Semantics (IWCS 2015), London.

## Data

The inter-annotator agreement study in Bender et al 2015 draws its data
from Antoine de Saint-Exupéry's *The Little Prince*. The data is in two
collections: a 50-item trial set, for annotator training and guidelines
refinement, and a 150-item sample set for measuring IAA. The links below
provide access to the individual and adjudicated profiles for the
150-item sample set:

|              |                                                                            |                                                                            |                                                                            |                                                                               |
|--------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Sample (150) | [Annotator A](http://svn.delph-in.net/snug/starsem14/iwcs15/public/tsdb/a) | [Annotator B](http://svn.delph-in.net/snug/starsem14/iwcs15/public/tsdb/b) | [Annotator C](http://svn.delph-in.net/snug/starsem14/iwcs15/public/tsdb/c) | [Adjudicated](http://svn.delph-in.net/snug/starsem14/iwcs15/public/tsdb/gold) |

In addition, the 150 adjudicated items are included in the treebanks for
the 1214 release of the ERG (as ‘lpps’). Those also interested in the
50-item trial set should contact the authors for access.

## Software

**Grammar and Parser** The profiles for treebanking were prepared with
the English Resource Grammar, in its [1214
release](http://svn.delph-in.net/erg/tags/1214), and the [ACE
parser](), in its [0.9.19
release](http://sweaglesw.org/svn/ace/tags/ace-0.9.19/).

**Treebanking** The annotation was done with the [Full Forest
Treebanker](), at tagged version
<http://sweaglesw.org/svn/treebank/tags/packard-2015/>

**Inter-Annotator Agreement** IAA statistics were computed using the
code in
[iaa.lisp](http://svn.delph-in.net/snug/starsem14/iwcs15/public/iaa.lisp)
and can be invoked in the LOGON system (see the
LogonInstallation page for installation
instructions) as follows:

      $LOGONROOT/redwoods --binary --erg --run iaa.lisp

**Export** In addition to the native representations, the analyses in
the annotated profiles can be exported into different formats (see the
ErgProcessing page for general background and further
pointers), e.g.

      $LOGONROOT/redwoods --binary --erg --home `pwd` --increment none \
        --export tree,mrs,eds --target /tmp gold

Note, however, that some components of ‘classic’ ERG profiles are
missing in this data for technical reasons, including for example an
explicit account of input and internal tokens and sub-node identifiers
in the recorded derivation trees; thus, not all [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) analysis and post-processing
functionality will be applicable to these profiles.

## Guidelines

We adopted the following annotation guidelines in our IAA study. The
versions linked here were refined on the basis of discussion of the
50-item trial set and then used in the annotation of the 150-item sample
set. Note that this was done in two passes: One pass annotating and
adjudicating the sample and then trial without any bridging rules and
then a second pass (sample first, then trial) for the items that were
rejected in the initial adjudicated gold standard with the bridging
rules turned on. The guidelines for treebanking with bridges were
initially developed in the course of this study; the other guidelines
predate this study and have been developed in the context of
ErgTreebanking more generally.

- [General heuristics for ERG Treebanking](/delph-in/docs/wiki/ErgTreebankingGuidelines) (updated after sample adjudication without bridges)
- [Notes on rule distinctions](/delph-in/docs/wiki/ErgTreebankingRules) (not updated during this study)
- [Heuristics for treebanking with bridges](/delph-in/docs/wiki/ErgTreebankingBridges) (updated after sample adjudication with bridges)
- [Lexical type database](http://compling.hss.ntu.edu.sg/ltdb/cgi/ERG_1214/ltypes.cgi) (not updated during this study; automatically generated from ERG 1214)
- [Notes on lexical types](/delph-in/docs/wiki/ErgLeTypes) (not updated during this study)

Last update: 2022-02-14 by Alexandre Rademaker [[edit](https://github.com/delph-in/docs/wiki/RedwoodsLpp/_edit)]{% endraw %}