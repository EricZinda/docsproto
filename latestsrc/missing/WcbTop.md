{% raw %}# Background

The *Wikipedia Corpus Builder* (WCB) is a toolkit for extracting
relevant linguistic content from Wikipedia. It was used in the creation
of the 2012 versions of WeScience and
WikiWoods, through the MSc thesis of Lars Jørgen Solberg at
the Department of Informatics at the University of Oslo.

# Installation

Make sure that the following prerequisites are installed:

- mwlib - <http://pediapress.com/code/>
- mwlib.cdb - <http://pypi.python.org/pypi/mwlib.cdb/0.1.1>
- tokenizer - <http://www.cis.uni-muenchen.de/~wastl/misc/>
- srilm - <http://www.speech.sri.com/projects/srilm/>

The environment variable PYTHONIOENCODING should be set to utf-8 (for
instance by running export PYTHONIOENCODING=utf-8)

If the command python -c 'from mwlib.cdb import cdbwiki' does not give
any error message and your shell is able to find tokenizer and ngram you
should be in good shape.

WCB itself can be downloaded from
<https://github.com/larsjsol/wcb/archive/master.tar.gz>.

# Running on the English Wikipedia

The setup used in the creation of WikiWoods 2.0 is included
in the wcb/enwiki-20080727 directory. It should be usable on newer
snapshots as well.

First prepare a database snapshot:

1. Download a snapshot from either from the WikiWoods page
or from <http://dumps.wikimedia.org/>.
2. Decompress the the snapshot:
bunzip enwiki-20080727-pages-articles.xml.bz2
3. Create a Constant Database:
mw-buildcdb --input enwiki-20080727-pages-articles.xml --output OUTDIR
4. Change the wikiconf entry in wcb/enwiki-20080727/paths.txt so it
points to the file wikiconf.txt created in the previous step.

Most of the modules in WCB need access to a paths.txt-file and
determines its location by examining the environment variable PATHSFILE.
This variable can be set by doing something like
export PATHSFILE=./wcb/enwiki-20080727/paths.txt.

As a test run ./wcb/scripts/gml.py --senseg 'Context-free language',
which should print some GML to stdout. The first invocation of
this command will take some time as it will examine all templates in the
snapshot.

WCB can create corpora directly from a snapshot or from files containing
wiki markup by using the scripts build\_corpus.py (snapshot) or
build\_corpus\_files.py (plain files). The following example shows the
creation a corpus containing all articles in a snapshot using 20
parallel processes:

    mkdir out-dir
    ./wcb/scripts/build_corpus.py -p 20 out-dir

Details on the command line parameters for these scripts can be found by
using the --help switch.

# Adaptations to Other Languages / Wikis

In addition to the preparations described in the above section, a few
extra steps necessary to run WCB on a snapshot from a non-Engish
Wikipedia or from a different wiki.

## Rules For Template Inclusions

Mediawiki templates are pages that are intended to be included in other
pages. Many of them are used to insert boilerplate text (e.g.
"\[citation needed\]"), while others can act as clues when performing
linguistic analysis by, for instance, declaring that a span of text is
in a foreign language (e.g. {{lang-no\|Universitetet i Oslo}}). Due to
the way templates interacts with other markup, aggressively removing all
templates will insert noise into the corpus.

How certain templates should be treated are specified in a comma
separated file (actually "underscore separated") where each row starts
with the name of a template (or a regular expression) followed by one of
the actions keep, remove or expand. Templates not listed in the rules
file is expanded as normal. The template rules used in the creation of
WikiWoods 2.0 can be seen here:
<https://github.com/larsjsol/wcb/blob/master/enwiki-20080727/templaterules.csv>
.

Since large wikis often have a large number of templates it usually
makes sense to pick those that are used most and write rules for those.
The script templatecount.py counts of often each template is included
either directly or via another template, while the script
templatesubsr.py tries to find naming conventions.

The "templaterules" entry in paths.txt should point to this file.

## Downloading "Siteinfo"

A "siteinfo file" contains information about the configuration (e.g.
active namespaces, links to other localized versions of this wiki) of a
Mediawiki instance and is bundled with mwlib for several of the
translations of Wikipeida (see
<https://github.com/pediapress/mwlib/tree/master/mwlib/siteinfo> for a
list).

If a fitting siteinfo file is not bundled, it can be downloaded directly
from the wiki in question:

- <http://nn.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=general%7Cnamespaces%7Cnamespacealiases%7Cmagicwords%7Cinterwikimap&format=json>
- <http://buffy.wikia.com/api.php?action=query&meta=siteinfo&siprop=general%7Cnamespaces%7Cnamespacealiases%7Cmagicwords%7Cinterwikimap&format=json>
- ...

The "siteinfo" entry in paths.txt should point to the location of this
file.

## Re-training the Language Models

The classifier in WCB uses two character-level n-gram models. As these
are trained on sections from the English Wikipedia they probably do not
perform very well on non-English wikis. They may or may not be good
enough for other English wikis.

### Collecting Training and Test Sets

The classifier included in WCB is trained on article sections collected
using heuristic rules from the English Wikipedia. These rules probably
do not translate well to other wikis, but they can serve as a decent
starting point.

The following commands will create a directory sets and fill it with
training data for the "clean" and "dirty" language model.

    mkdir sets
    ./wcb/scripts/sectioncount.py > sections.csv
    ./wcb/scripts/trainingdata.py sections.csv sets

The script sectioncount.py produces a list with the frequency and
average length of all section headings, which is then referenced by the
script that collects the training data (trainingdata.py). The latter is
the script you would want to modify so it fits the wiki you are working
on. Redefining the functions is\_clean() and is\_dirty() should be
enough. It might be necessary to do a few iterations of manually
inspecting the collected training data (use unexplode.py to make it
human readable) and adjusting the heuristics.

### Training and Tuning

The data collected by trainingdata.py must be manually partitioned into
different sets (training, test, etc.). Testing on sets created with the
same heuristics as the training set does not give a good indication of
classifier performance. Consider instead creating a gold standard by
manually classifying a few sections (the script trainingdata\_all.py
collects sections from randomly selected articles).

The script build\_lms.py creates n-gram models with different orders and
smoothing algorithms and training sets. It assumes that your traning
sets use the following naming convention: "clean\_1, dirty\_1, clean\_2,
dirty\_2, ...".

    mkdir lm
    ./wcb/scripts/build_lms.py

You can then see how the different configurations perform on a test set
by using
tune\_classifiers.py &lt;cleant test set&gt; &lt;dirty test set&gt; &lt;location of n-gram models&gt;.
It is also possible to use the ngram-count utility from SRILM directly.

The models included in WCB are add-one smoothed 4-gram models.

The entries "clean lm" and "dirty lm" in paths.txt should point to the
n-gram models you wish to use.

# Construction of WeScience 2.0
<update date omitted for speed>{% endraw %}