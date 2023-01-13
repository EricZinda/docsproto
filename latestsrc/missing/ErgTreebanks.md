{% raw %}# Background

Each ERG release is accompanied by a collection of treebanks, text
corpora that are manually annotated with gold-standard ERG analyses.
These treebanks are constructed through the Redwoods approach, where an
expert annotator (often the main grammar engineer) searches the space of
candidate analyses provided by the grammar (i.e. a large n-best list or
the full parse forest) for the intended reading. This search is made
possible through what is called discriminant-based annotation, where
what annotators judge are minimal contrasts between analyses, e.g.
lexical choices, syntactic constructions, or attachment sites.

Coordinated with the 1212 version of the ERG (released in mid-2013),
there are two large collections of gold-standard ERG analyses: the
Eighth Growth of the [Redwoods
Treebank](https://blog.inductorsoftware.com/docsproto/garage/RedwoodsTop), and [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank)
1.0—the first release of the new ERG annotation of (most of) the
venerable WSJ text originally annotated in the Penn Treebank.

Redwoods comprises some 400,000 tokens of annotated text from various
domains and genres (including transcribed dialogues, ecommerce email,
tourism information, Wikipedia, and user-generated content; see the
Redwoods web page for details). The 1.0 release of [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank)
encompasses WSJ Sections 00–21, for about 750,000 tokens of annotated
text. An exact summary of the various sections in Redwoods and
[DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank), recommendations for splitting out development and
testing sections, and sentence and token counts are available in the
form of an [on-line
spreadsheet](http://svn.delph-in.net/erg/tags/1212/etc/redwoods.xls).

This page was predominantly authored by StephanOepen,
who jointly with DanFlickinger (the principal grammar
engineer and benevolent ERG царь for life) administers the ERG release
and treebank maintenance cycle. Please do not make substantial changes
to this page unless you are reasonably sure of the technical correctness
of your revisions and expect your changes to be compatible with the
goals of the ERG developers and of this page.

# Obtaining the Treebanks and Supporting Software

Both the Redwoods and [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank) annotations are natively
recorded and distributed as what is called [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) profiles, essentially database
snapshots that record exactly how the ERG parser arrived at the intended
analysis and the annotator decisions that led to its identification.
These profiles can be exported and converted into a variety of formats
using the DELPH-IN toolchain. These tools are easy to install and run on
any reasonably recent Linux installation (on 32- or 64-bit x86
architectures, where 32-bit compatibility libraries need to be installed
in a 64-bit environment), provided one has available some six gigabytes
of disk space.

Technical details are available on the [LogonTop](https://blog.inductorsoftware.com/docsproto/tools/LogonTop) and
[LogonInstallation](https://blog.inductorsoftware.com/docsproto/tools/LogonInstallation) pages, but it should just work to
execute the following:

      svn co http://svn.emmtee.net/trunk logon

The initial check-out from SVN will install a complete DELPH-IN
toolchain (including many pieces irrelevant to manipulation of ERG
treebanks, but network bandwidth and disk space should be cheap);
depending on the quality of your link, this one-time preparatory step
might take between a few minutes and a couple of hours.

# Export and Conversion of ERG Treebanks

The LOGON tree includes a copy of the ERG, which in turn brings with it
the Redwoods [\[incr tsdb()\]](http://www.delph-in.net/itsdb) profiles.
The following command will invoke the DELPH-IN toolchain to export (into
a textual format, aiming to balance human and machine readability) a
range of derived representations for a given profile:

      cd logon
      ./redwoods --binary --erg --binary --target /tmp \
        --export input,derivation,tree,mrs,eds cb

For a brief discussion of what the individual export formats are, please
look towards the bottom of the [ErgProcessing](https://blog.inductorsoftware.com/docsproto/erg/ErgProcessing) page and
links from there. The procedure above should create a new directory
/tmp/cb/ (for the advocacy essay *The Cathedral and the Bazaar*, in this
case, which is commonly used as out-of-domain test data with the ERG);
this export directory will contain a collection of compressed files,
each providing the various syntactic and semantic views requested during
the export of one sentence at a time.

To further reduce a collection of exported ERG analyses into bi-lexical
syntacto-semantic dependencies, a second step of conversion (and loss of
information) is required. Still within the top-level LOGON directory,
execute the following:

      ./bin/dtm --grammar ./lingo/erg --data /tmp/cb --tok ptb --dtm /tmp

The result should be a new tab-separated file in /tmp/ (called
cb.ptb.dtm, for our running example), containing both syntactic and
semantic bi-lexical dependencies in CoNLL-08 format. While the ERG makes
its own (linguistically motivated) internal tokenization assumptions,
this final step also can convert to the venerable PTB-style tokenization
conventions (see [ErgTokenization](https://blog.inductorsoftware.com/docsproto/erg/ErgTokenization) for background).
[Ivanova et al. (2012)](http://aclweb.org/anthology/W/W12/W12-3602.pdf)
provides more background to this final conversion.

# Adding DeepBank to the LOGON Tree

Once [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank) 1.0 is publicly released (which is imminent in
September 2013), the same formats and procedures documented above will
be applicable to the ERG WSJ annotations too. Furthermore,
[DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank) will make available pre-packaged exports and
conversion into bi-lexical syntactic and semantic dependencies. Please
watch this page for updates.

# Known Bugs and Caveats

This set of recommendations was first created in the fall of 2013. The
tools and procedures described here have been frequently used by ERG and
DELPH-IN developers for about one decade, but so far they have not been
subjected to testing by a more diverse user community. When in doubt,
please contact DanFlickinger and
StephanOepen for assistance.

# Querying Treebanks

- Some of the ERG treebank data can be searched via semantic
‘fingerprints’ using the [WeSearch
Interface](http://wesearch.delph-in.net); for information on
fingerprinting, please see the [ErgSemantics](https://blog.inductorsoftware.com/docsproto/erg/ErgSemantics)
documentation.
- [Fangorn](http://hum.csse.unimelb.edu.au/ts/index) provides a
syntactic search interface to a subset of Redwoods.
- The [INESS Treebank Infrastructure](http://clarino.uib.no/iness)
also facilitates search over syntactic derivations and labeled
constituent trees of Redwoods and [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank).
- [Some further thoughts on kinds of searches to
enable](https://blog.inductorsoftware.com/docsproto/missing/TreebankQueryIdeas)

Last update: 2021-07-20 by Alexandre Rademaker [[edit](https://github.com/delph-in/docs/wiki/ErgTreebanks/_edit)]{% endraw %}