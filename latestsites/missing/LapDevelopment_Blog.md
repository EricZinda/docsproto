{% raw %}# Week 23

## Monitoring

Milen attended an USIT-internal workshop on monitoring and come home
with [great ideas](https://rt.uio.no/Ticket/Display.html?id=2161812) for
how to set up alerts when critical LAP services are in jeopardy; we
still hope to see at least an initial set of monitors implemented before
the summer break.

## Job Resources

Milen & oe just put the new scheme for [per-tool job defaults and custom
resource
specifications](https://rt.uio.no/Ticket/Display.html?id=2099594) into
production. The USIT-specific drmaa\_usit.py now resides outside of the
Galaxy tree, and the resource specifications from tools/resources.xml
and tools/jobs.xml appear to be taking effect. One way of testing these
is via the new ‘driver’ tool in the ‘test’ category, which simply
invokes the top-level LAP driver and makes it report the run-time
environment, e.g. LAP and SLURM environment variables.

## OBT Action Plan

We (milen and eman) have met and decided on action plan in order to
investigate the [errors in
OBT](https://rt.uio.no/Ticket/Display.html?id=2097066) due to wrong and
strange input. The goal of this plan is to pinpoint failures in one or
more of the following components:

1\) MTag 2) MTag wrapper 3) Rule Based Disambiguator 4) Rule Based
Disambiguator wrapper 5) Statistical Disambiguator 6) Statistical
Disambiguator wrapper.

To do so we have decided to use the Storting Data and parts of AVIS
corpus as a test data. We have discussed also the possibility of using
Norwegian Wikipedia as a source of more strange text input but decided
to postpone this step till the moment that all of the test
infrastructure in place and we have processed the other corpora. The
action plan consists of the following steps:

1\) Export to CG3 the input and output of each of the aforementioned
components. 2) Log the output and error messages corresponding to each
step. 3) Customize the lap script in order to handle a more verbose
output of relevant information.

# Week 24

Eman and Milen worked jointly on the OBT debugging sketched in week 23.
We ran a full OBT workflow on some 15000 input files from the storting
dataset and were able to find a new feature of OBT: for closing
parentheses at the end of a sentence, the pos tag occupies the slot
usually reserved for features, tricking LAP into thinking that the
end-of-sentence symbol "&lt;&lt;&lt;" is a pos and breaking sentence /
token alignment.

LAP is now patched to work with this feature, with several improvements
both in the obt wrappers and the Library (see commit messages for info).

We also started discussing avenues for overcoming the single mongodb
bottleneck in LAP/Galaxy proper. For our backdoor LAP runs, we have now
decided to launch N mongos (for instance 10) to improve performance.
Milen is launching a new batch of jobs as I am writing this, we are
hopeful we won't discover new OBT features on Monday.

# Week 25

During this week the efforts were concentrated in 3 lines 1) OBT
Debugging; 2) Implementing Monitoring tools; 3) Visualization

## OBT Action Plan

We have finished the obt testing and concluded the following:

1\) OBT does not report correctly the EOS tag in cases when the POS tag
is missing. A bug fix for this problem was implemented and tested. It is
not yet uploaded to the SVN until the other problem is fixed as well.

2\) OBT stubles when processing the symbol U+85. Bug for this problem is
not yet implemented. Milen and Stephan decided that we should replace it
with the CR symbol before giving the text to OBT as input.

Overall we are satisfied with OBT robustness. The first bug was the
cause of most of the errors in Storting corpus. On 15,000 examples it
appeared around 300 times mainly due to the nature of the text. The
second appeared seldom only 4 times out of 200,000 examples.

## Monitoring Services

With the assistance of USIT-gid group we have managed to setup the
monitoring infrastructure on at.hpc and lap-test.hpc.

Milen have created a template called "Monitor LAP" a template for
monitoring a LAP installation. Inside this template we have created an
Item called "Galaxy Server" that reports the presence of the Galaxy
service by requesting an output when accessing the port 8080 on the
corresponding machine. Accordingly a trigger "Galaxy Status" was set to
produce an error in case the item reports that the server is not
responding and an email notification "Galaxy Server is Down" was created
in case there are failures. The whole procedure was tested on lap-test.
The work proceeds here according to the plan set in [Monitoring
task](https://rt.uio.no/Ticket/Display.html?id=2161812)

## Visualization

The visualization of receipts has moved forward.

1\) We have integrated brat in the Galaxy infrastructure

2\) We have created a template page file that resides in the
library/python/lap/visualization/ folder.

3\) We have ported various CSS styles scripts from [WESearch
Infrastructure](http://wesearch.delph-in.net/)

4\) We have visualized the morphology using BRAT.

5\) We have decided to use CONLL-X style brat visualization for the
morphology and dependency layers.

6\) We have decided to use export similar style of creating the CONLL-X
export of the structures in the mongo DB.

7\) Fixed various bugs in lafdb.py. The bugs were in legacy code and did
not influence the lap performance.

The action plan for this task was created in this rt thread [Receipt
Visualization](https://rt.uio.no/Ticket/Display.html?id=1839456)

# Week 26-27

Milen was still in vacation. I assume less effort was dedicated on the
project during this time.

# Week 28

Stephan and Eman in vacation. The graphical representation of the
Tickets was completed during this period. Though still up for testing
most of the code was finished during this week. Some considerations:

- The implementation followed the export module code in most of the
case. It is worth noting that it does select the first annotation
available and does not consider different
  - annotations. Adding them as a choice after is something to
consider.
- The morphological layer is visualized only if the dependency layer
is missing because it is redundant.
- The tokenization layer is visualized only of the morphology and
dependency layers are missing because it is redundant
- The sentence segmentation layer is shown hidden if higher layers are
present.
- The original ticket is present hidden
- Brat does not completely support CONLL-X in the version I have now
(maybe the release is complete. Mine has only one function and not
an entire js file dedicated).
  - For example the lemma representation is missing. I used in the
current implementation of CONLL-U to represent the structures.
- While creating the represention I noticed that the output of the
HUNPOS is only pos and not cpos. I have switched the positions in
the TSV export inside the visualization page
  - (BRAT uses cpos and ignores pos). Should we consider to extend
HUNPOS by providing cpos based on the pos?

If we consider this version a good approximation we can push it to
production.

# Week 29

During this week Milen worked on service monitoring, diff and some code
review. Stephan and Eman in vacation

## Service Monitoring

We have implemented the following monitoring items: 1) Apache; 2)
Galaxy; 3) Gold; 4) Memcached(Memcookie); 5) Mongo and 6) Mount of
/projects

The first 5 are implemented by requesting their presence on the assigned
ports. I have thought about some functional tests and started
implementing them. The mount test is done by accessing the following
file:

/projects/lap/production/galaxy/database/info.txt

I have investigated the issue of automatically restarting the services
by sending commands to the server. This is a standard functionality of
zabbix. But it is disabled by default by the zabbix administrators for
security reasons. When I tried to enable it on lap-test the admin daemon
turned it off. Overall I consider this a good safeguard. If a person
gain access to the web interface he can control remotely the server
using this functionality. If we consider that it is a good functionality
to have I will explore other options.

## Diff

I have made another diff of the version of Galaxy at at.hpc and Vanila
Galaxy. The details is in email with subject "Diff of Changes in Galaxy"

## AT.HPC Reboot

On Wednesday 20/07 I have executed a reboot of at.hpc to verify the
fitness of our service scripts. The reboot went smoothly all the
services came back online without problems.

## Code Consolidation

I have looked at the task of unifying the code of the export (tsv.py)
and visualization (receipt.py) though they are essentially performing
similar task I have found that sufficient changes exists in order not to
merge them in a common code for now. The main differences are: 1)
Visualization uses CONLL-U vs export CONLL-X; 2) Handing the pos tags;
3) handing the head column (conll-x is \_ conll-u is 0). 4) Stopping
visualization after the 5th structure.The unification can happen but it
will complicate the code more at this time. This will change once the
final version of the visualization is in place.

# Week 30

Stephan and Eman in vacation. No major events this week. Milen have done
some code review and finally fixed the issue with OBT and the malicious
character 85. The USIT specific galaxy code is now under git. Note to
self I must grant Stephan access to it.

Nikolay was installing Lifeportal with Galaxy 16.01 on the new machine
and I witness a bit of his struggle with it. Some notes:

\* The 10.110.0.\* network is not required for access to Abel. What you
need is the host to see nilshenrik (nh.hpc). \* Galaxy 16.01 was a major
release with a lot of changes and a lot of problems (python path, new
drmaa implementation). I would stay away from it in the future. If we
upgrade galaxy I would go for the later releases this year.

On the monitoring side. I have made some functional tests (not only
checking if the service is on but if it responds correctly) that will
add to the others.

# Week 31

Stephan and Eman are back from vacation. Milen have done some code
review. The production version of the system was patched with the obt
changes. Some coding changes were done to the receipt visualization. The
monitoring interface had web request added to it. The week was full
about what to do of discussions:

\*) We have decided to retire the development server ps.hpc (old
production) and once the new production comes online in September
replace it with a new installation. \*) In the mean time the ps.hpc will
be used by Eman and Milen for test aimed at understanding the
performance limitation of collections. \*) Basic review of the
visualization was performed. It was decided to visualize everything with
brat except sentence (maybe). No decision was taken for what to
visualize instead of pos when token are the only annotation. When lemmas
are available and pos are not the lemmas will be visualized.

# Week 32

Emanuele has been working on language identification.

- setup a shiny new laptop for LAP development.
- langid.py wrapper, currently adds a record of class language to a
receipt. Currently has lap0 receipts on both input and outputs.
  - The tool name handle in the lapstore is 'langid' rather than
'langid.py', since (py)mongo complained about '.' in dict keys.
- added a 'get\_language' function in tool.py in the LAP library, so
that all wrappers have a unified way to determine language.
- updated xml descriptions and wrappers of most tools that have more
than one language model (currently hammering away at OBT)
- tested with LAP tests and local galaxy installation

Milen has worked on the the graphical representation:

- Worked on several implementation of the Brat integration
- We ended up updating to the latest version of Brat and Annodoc
- We decided to use per element styling of annotation nodes.

Milen has also started studying the resa aligning code following a
performance issue reported by Stephan in: [RT
Ticket](https://rt.uio.no/Ticket/Display.html?id=2233501)

# Week 33

Milen has continued his work on visualization. The new version of Brat
with per element style visualization is now integrated. The performance
issue of resa that we mentioned last week was investigated in the
beginning if this week and postpone as not a priority.

eman:

- worked on langid in the OBT stack - we learned that the statistical
disambiguator at the end of the pipeline is not trained on nynorsk
- LAP Store and Library demystification support for visualization.

# Week 34

eman:

- Got a clearer idea of how OBT stat is implemented and what possible
steps could be taken in order to enable a full nno pipeline in OBT.
For the immediate LAP future, we decided to just run nob statistical
disambiguation on nno cg3-disambiguated input.
- Thanks to Milen's visualization effort, we realized that dependency
parsing in LAP got broken during the last run of refactoring,
emitting a malformed LAP Store graph. This is now fixed.

milen:

Milen have completed the visualization (except the dependency
relations). The new visualization is based on traversing the LAF graf.
The procedure is the following:

- For each sentence segmenter in the lap receipt we extract all
sentence annotations from the graph.
- We identify the sentence border from the range nodes and extract the
sentence text.
- The sentence text is normalized by replacing newlines and tabs with
spaces
- Using the LAF Graph we extract for each tokenizer in the lap receipt
the corresponding tokens.
- Using the LAF Graph we extract for each morphpoology analyser the
annotation attached to the tokens.
- Each morphological annotation is displayed as brat annotation. For
each annotation a color is selected. If there is more than one
analysis per token the annotation receive multiple brat annotations.
This is valid case only for OBT. The OBT produces POS and LEMMA at
the same time. That is why the lemma is introduced in the comment.

A day was wasted in discovering the aforementioned by Eman bug. But I a
can safely declare that now I have a full understanding of the laf
objects.

# Week 35

Eman:

- Rework of the language identification system. All tools that can use
models/settings to deal with different language now provide a
'language' variable, with a unified way of dealing with dynamic
language selection, either picking the "mapped" language from a
detector tool or falling back to a user-selected default if the
retrieved language label is not one that the tool supports.
- Langid.py adds the following feature structure to the lapstore:
{"class": "language", "original": "eng", "mapped": "nob"}. Users can
define custom language mappings.
- Puny two-letter language codes are now translated into ISO 639-3
three-letter codes by way of the to\_three\_letter\_code() function
in lap.utils

Milen:

- The visualization reached maturity during this week. Thus with
Stephan we integrated it into the production server.
- The dependency annotation BUG of the last week was finally squashed.
The bugfix was also introduced to the production server.
- We spend small amount of time into exploring the integration of
DKPRO before the meeting with . I have create a small run project.

# Week 36

This week LAP group had a visitor: Richard Eckart de Castilho that
presented the world of DKPro to us. DKPro is a community of projects
focussing on re-usable Natural Language Processing software. We had two
days meeting during which we discussed a cooperation between LAP and
DKPro. We established the following:

- We created a format called Lap Exchange Format (LXF) that will be
used to send to and retrieve data from DKPro. The format is based on
the graph representation of LAF (LAP Annotation Format) Objects
serialized in JSON. Richard helped us in converting the LXF to JCAS
(UIMA).
- We decided to collaborate with the DKPRO community by sharing the
LXF implementation and all of the future extensions.
- We started implementation of DKPRO LAP wrapper in order to integrate
DKPro as a tool in LAP. The wrapper will export LAF object from our
mongo database in LXF json file and call DKPro. The LXF file created
by DKPRO as an output will be returned to the mongo database.
- We decided to crate as a first step CoreNLP toolkit in DKPro and
implement as tools the sentence splitter, tokenizer and dependency
parser.

# Week 37 & 38

This week our effort was focused on two major tasks:

1\) Preparation for public launch of the LAP portal. 2) Integration of
DKPro in LAP.

The work is summarized as follows:

- Added counting to the visualization interface as well as some minor
tweaks.
- Creating a DKPro tool backabone in LAP
- Standartazing LXF (Lap eXhange format)
- Integrated DKPro Sentence Splitter and Tokenizer
- Integrated DKPro POS Tagger and Parser
- Reset the Mongo and Galaxy Databases before thr launch

Eman:

- dkpc in the lap library: design and implementation of a tool
superclass to deal with input and output of LXF data
- dkpc tools: implementation of LAP wrappers for the dkpc coreNLP
segmenter/tokenizer and tagger/dependency parser
- implementation of unix linefeed normalization at text import time in
LAP
- implementation of quote, parenthesis and dash de-normalization for
models trained on PTB conventions

# Week 39

This week we worked on following activities:

- Fixed problems with visualization. We have realized that the
visualization became sluggish on big datasets. The reason for this
is the large number of nodes created for each dataset. We solved the
problem by adding an index on the node types and to ids. This
boosted the speed significantly.
- Created a Visualization of language identification tools. We have
created a prototype for the language identification visualization.
We have encountered the problem of multiple access to map files. We
solved it by using global python variables.
- Started creating the DKPro integration tests.

# Week 40

This week we worked on following activities:

- Finished the DKPro integration tests. We have modified completely
the original Richard tests as they were not adapt to the agreed LXF
but more relevant to the Milen's old exports.
- Milen have studied a bit github. We have tried to make a pull
request on Friday but it failed. Richard did not receive data. He
suggested the github project pull request. Milen will create a fork
project on GITHUB and will send it to Richard for pull request.
- While creating the integration tests we have stumbled on the
following minor bug: DKPro lap library exporter makes a double
export of the edges and ranges in a receipt as they do not contain
annotation type. This bug did not influence the system as the java
LXF reader allowed repetition by overwriting the same information. A
patch is available on LAP test (approved by Eman) and will be
committed on next integration.

# Week 41

Milen completed the integration of LXF in DKPRO codebase:

- Created a git repository
<https://github.com/kouylekov-usit/dkpro-core> which is a clone of
the dkpro.
- Commited the changes to the aforementioned repository and created
Pull Request
- Richard pulled the changes to the main dkpro repository
- Separated the DKPRO - LXF exchange part from the DKPRO call part by
request from Richard

Milen have also worked on [RT
Ticket](https://rt.uio.no/Ticket/Display.html?id=1716704). The following
language identifier was used and produced reasonable results.

de.tudarmstadt.ukp.dkpro.core.langdetect.[LangDetectLanguageIdentifier](/LangDetectLanguageIdentifier)

# Week 42

Milen have create a presentation for Gruppe for datafangst og
samlingsforvaltning (DS). Their interest was in our usage of mongo
inside LAP. Milen have also downloaded and started studying the
metawrapper provided by Richard.

# Week 43

Milen have worked on testing additional tools of DKPro and investigated
their representation. Created a test for
[StanfordLammatizer](/StanfordLammatizer) in lap DKPro script. Fixed a
bug in the DKPRO2LXF representation of LAP. Milen have started studying
Groovy a python based language used by Richard in the dkpro-meta
project.

# Week 44

Milen has worked on meta representation creating the first dump of the
Metadata for DKPro tools using the dkpro-meta project provided by
Richard.

Eman: \* Design and implementation of a word cloud-generator tool

# Week 45

Milen has worked on meta representation. Some testing of the new export
tool was done conclusions:

- We probably need more memory possibly for the DKPro Part of Speech
Tagger and Parser
- We need to think about writing the output of the DKPRO straight away
(as the nodes are generated) in order to reduce the memory imprint.

Stephan and Milen met and discussed the Meta Data representation of
DKPRO and decided we will use temporary Milen's Solution for handling
dependencies:

- Create a common sets of the jars from which the DKPro script
depends.
- For each tool the dependencies will be exported in a separate folder
using the complete classpath name.

# Week 46

Milen created a new dump of the metadata and sent report to Richard
(Richard responded on Sunday).

Mongo performance. Milen looked at Mongo performance in the current
version. The mongo default profiler was used. It work in the following
way:

1\) The profile is activated on the database. 2) It logs all the queries
that took longer than 100 milliseconds to execute.

Milen have exported the 277625 tokens corpus with the profiler on using
lap-test. The conclusions are the following:

Few queries went above this threshold. I will give their performance
problem more on garbage collection than performance problems. A new
variant of the export tool should be created that does not inquire the
database so often. Milen is preparing a new version of the export tool
that loads all the data in the memory.

Recurrent dependency analysis. Milen have investigated the recurrent
analysis and created a small patch of the receipt visualization to
abiltate it. A working version is on lap-test. The DKPRO interface
delivered correctly the analysis. And lafdb did not have problems
storing them. Test sentence:

Bills on ports and immigration were submitted by Senator Brownback,
Republican of Kansas.

A new format for export is required for such analysis as discussed the
previous week with Stephan.

Milen have started studying the metadata in DKPro but at the moment is
more confused by it. Will try to formulate decent set of questions to
Richard today.

Milen have fixed a bug in the drmaa usit script that did not handle
correctly user request for resources above the allowed limit. We should
probably have this limit visible in some way.

# Week 47

Milen have worked on the dkpro metadata. Based on the discussion with
Stephan from week 45 the tools were separated in directories with the
corresponding jars.

Milen worked also on TSV export. Milen created a graph traversal common
API. The API is used by both the visualization interface and the new tsv
headless export. Two implementations of this interface were added: 1)
Direct mongo access using queries. 2) Memory access - all the data from
the receipt is loaded in the memory and stored in hashes. Preliminary
inconclusive tests were made about performance.

# Week 48

Milen have studied in more details how models are created in DKPRO.
Milen have worked created Metadata and a model for Norwegian in UDIPipe.
The change was committed together with some bug fixes to the DKPro git
and approved by Richard. Milen started building a compile script for
dkpro tools into laptree.

# Week 47

Milen have finished the compile script for DKPro tools. Milen have
prepared and submitted a pull request to dkpro for bugfixes in the DKPro
build scripts of the tree-tagger models.

# Week 48

Milen have worked on some refactoring of the UDIPipe model and updates
to the compile script in order to accept the recent changes of the
dkpro-meta.

============================================================================================================================================================

Happy 2017

============================================================================================================================================================

# Week 3

Milen has worked not DKPRO Meta Data. An extension was made that
associated a model to more than one class. This increased the correctly
recognized tool model pairs.

With the updated meta scripts Milen have managed to make the link
between dkpro\_splitter-tokenizer and the dkpro tools. The prototype is
running on lap-test. The compile scripts runs smoothly though a download
of groovy package binary is needed as the one provided by
[RedHat](/RedHat) 6 did not behaved in the expected manner and milen did
not manage to make it behave. Milen will study the ways of Maven Groovy
interaction to discover the secret ways in order to avoid the RH6
groovy.

The new Notur project N9452k for LAP is configured on lap-test. FYI the
lap user is given access to project based on set of hack scripts that
make a exception for it. The procedure is similar for the galaxy user
(the lifeportal user) but the galaxy user is configured using a little
bit more complicated sets of scripts as the it runs some of the user
projects.

Milen have also investigated the trans object available for
visualization of receipts. The trans object as pointed out by Stephan
contains a various data inside (I assume even all of it). The names of
the tools corresponding to tool\_ids was extracted and updated in the
visualization.

# Week 4 and Week 5

Fixing issues in the DKPro Scripts as well worked on the issues
described in the previous weeks.

# Week 6

There has been a new version of the database schema in the making,
developed by eman in a private branch. we would like to merge back these
changes and put them into production during the scheduled Abel
maintenance on february 27 and 28.

\* Eman has identified necessary change in calling pyMongo and mergeed
into the trunk \* Milen has upgraded MongoDB on ‘lap-test’ to the Wired
Tiger \* Eman completeed library revisions and updates to all tool
wrappers in the branch \* Milen have made changes are required to
visualization and exporting \* All changes are put together in a version
running on lap-test. \* Consider development status on separate ticket
for receipt revisions;

# Week 7

Milen have worked on the DKPro integration. More than 30 new tools were
installed and tested on lap-test. The following issues came in view:

1\) [TreeTagger](/TreeTagger) is not working because of the kernel in
RHEL6 is too old. Maybe I can find an older version or recompile the
tree tagger binnary if i find a sorce

2\) The tools from the following languages are used:

en no sv fi da de es it bg nl el hu ru sh pl pt ro cs hr sa tr sk

3\) Tools like [UdipPipe](/UdipPipe) poss tagger provide both course
tags and simple tags. At the moment we do not use the course tags. I
assume some of it is needed for the parser although it worked without
it. I propose to add the extra annotation to the morphology annotation.

4\) [ClearNlpPraser](/ClearNlpPraser) and [UdPipe](/UdPipe) parser
require that the tagger have produced lemma as well. In the moment the
data that we pass to DKPro is the morphology node. If the lemma is in a
separate node it will not be passed. I know from the metadata that this
tools require lemma. So I can make the wrappers with special treatment
for these two parsers. We must discuss.

5\) What are we going to do with [UdPipeSegmenter](/UdPipeSegmenter). In
DKpro it is not finished as it does not contain offsets. Should I try to
implement some aligner in DKPro ? The tool is assigned to me from
Richard so we are supposed to propose a solution sooner or later.

# Week 8

A preliminary version of the new reciept was implemented by Milen. It
was a bit pointless as we decided later to change it so ... Anyway. Some
improvements were done on the tools from the previous days. Mainly
bugtesting. A new version of the export tool was officially installed on
the production server. The new version does not require head annotation
on the dependency nodes. The new version is sharing the same library
with the visualization interface. Milen Stephan and Emanuele met. It was
decided to overhaul the receipts to support multiple annotations from
the same tool. More details later.

# Week 9

Milen worked on DKPro. A new version of the of the DKPro
[UdipipeSegmenter](/UdipipeSegmenter) wrapper was created inspired by
some of the code of Richard. The code for now resides in the Milen's
repository waiting for the rest of the DKPro changes. Milen started
working on the reporting tool

# Week 10

Milen installed the Nikolay reporting tool and started the galaxy
reporting tools on lap-test. Both of them worked seamlessly. Some time
was send in trying to correctly configure it as it was particular
difficult between the version of postgrsql, python and pgsql. Milen
tired to create his own reporting server. The idea is to use the
reporting code to in order to use the Galaxy library in order to access
information about jobs and users.

# Week 11

Milen has switched his efforts from the reporting server to the real
galaxy api.
(<https://docs.galaxyproject.org/en/latest/lib/galaxy.webapps.galaxy.api.html>)
The api allows you to access basic information from Galaxy through
instantiation of objects and get requests.

# Week 12-14

Milen have worked on development of a script for reporting. The script
is installed in /home/laportal/report/generate-report.py

The script has the following options:

usage: reporting script \[-h\] \[--start START\] \[--end END\] \[--date
DATE\]

- \[--month MONTH\] \[--week WEEK\] \[--output OUTPUT\] \[--config
CONFIG\]

optional arguments:

- -h, --help show this help message and exit --start START Start Date
--end END End Date --date DATE Reference Date --month MONTH Display
current month --week WEEK Display current week --output OUTPUT
Output file --config CONFIG Configuration file

--config - Configuration file that gives the basic parameters: api\_key
and galaxy\_key. The first key corresponds to the key of the
administrator that will run the script. The second key corresponds to
the key used by galaxy to encrypt the ids of the returned by the api. We
need the second key to align the job ids returned by the api with the
job ids stored in gold. There is a default config file that is stored in
/home/laportal/report/config.ini. This file is accessible only to the
laportal user.

--output specifies the file in which the report is written. If none is
specified the system out is used.

The period for which a report is generated is determined by the --start,
--end and --date options. If --start and --end are specified the report
will be generated for the explicit period defined by them:

Example Queries:

'python generate\_report.py' - generates the report for today.

'python generate\_report.py --week=true' - generates the report for the
current week

'python generate\_report.py --month=true' - generates the report for the
current month

'python generate\_report.py --week=true --date=2017-03-1'- generates the
report for the week that contains 1st of March 2017.

'python generate\_report.py --month=true --date=2017-03-1'- generates
the report for the month that contains 1st of March 2017.

'python generate\_report.py --start=2017-03-1 --end=2017-03-5'-
generates the report for the period from 1st of March 2017 to 5th of
March 2017.

'python generate\_report.py -month= true --end=2017-03-15'- generates
the report for the period from 1st of March 2017 to 15th of March 2017.

# Week 15

Small refinements of the report script was done. As well some minor
tweaks on at.hpc to fix bugs:

1\) The newly introduced export script did not correctly function on
OBT.

2\) The visualization interface did not correctly visualize a message
when the job was in progress.

The patch for both bugs is done on at.hpc. They should be included in
the version control.

# Week 16

Milen worked on integrating the new version of UDIPipe in DKpro.

# Week 17-19

Milen continue to work on the reporting system. The new script was
separated into two scripts:

The reporting/fail script:

usage: reporting script \[-h\] \[--start START\] \[--end END\] \[--date
DATE\]

- \[--month\] \[--week\] \[--output OUTPUT\] \[--fail\]

optional arguments:

- -h, --help show this help message and exit --output OUTPUT Output
file --fail Report failed jobs

period:

- Period Selection --start START Start Date --end END End Date

reference:

- Reference date selection --date DATE Reference date/today --month
Display the month of the reference --week Display the week of the
reference

If the script is used with the fail option will give a report of the
failed jobs. The period for which the report is generated is the either
selected by a start date and end date (the default end date is the day
the script is called), or by a period related to a reference date where
the (the default reference date is the day the script is called). The
output of the report script is a json file that contains a set of all
users and their activity in the reference period. Example data for an
user is the fallowing json fragment:

"<mailto:Gunn.Lyse@nsd.no>": {

- "create\_time": "2016-10-20T10:49:00.334892", "update\_time":
"2016-10-20T10:59:40.907942"
  
  "email": "<mailto:Gunn.Lyse@nsd.no>", "id": 31, "gold": {
  
  - "jobs": {
    - "<mailto:185.Gunn.Lyse@nsd.no>": {
      
      - "amount": 9, "cpus": 1, "project": "gx\_default"
      
      <!-- -->

      
      - }
  
  <!-- -->

  
  - }
  
  }
  
  - "jobs": {
    - "local": \[
      - { "create\_time": "2016-10-20T10:56:05.683958",
"duration": 7, "job\_runner\_name": "local", "state":
"ok", "tool\_id": "langid.py", "update\_time":
"2016-10-20T10:56:12.946793" }
      
      \], "slurm": \[
      - { "create\_time": "2016-10-20T10:57:01.067035",
"duration": 81, "job\_runner\_name": "drmaa", "slurm": {
        - "amount": 9, "cpus": 1, "project": "gx\_default"
        
        }, "state": "ok", "tool\_id": "obt\_tokenizer",
"update\_time": "2016-10-20T10:58:22.336679" },
      
      \]
    
    },

}

The record contains the basic information when the user was created and
when his last activity was performed. The information of the slurm jobs
performed by the user is stored into the gold part of the fragment. N.B.
This list is the comprehensive list of all jobs submitted by the user.
This is stored only for logging purposes and can be removed in the
future. The jobs part of the fragment is separated into local and slurm
jobs. The jobs here are only relevant to the period selected by the user
of the reporting script.

If the reporting script is used with the --fail option it will output a
list of fail jobs for the selected period. The output is similar to the
default one but the jobs have additional "dump" field that contains the
output/error log of the job.

The summary script works on the output of the report script. It
generates a txt summaries about the tools and users in selected period.

usage: summary script \[-h\] \[--start START\] \[--end END\] \[--date
DATE\] \[--month\]

- \[--week\] \[--users\] \[--jobs\] \[--tools\] \[--output OUTPUT\]
file

positional arguments:

- file Portal json report file

optional arguments:

- -h, --help show this help message and exit --users Generate users
info --tools Generate tools info --output OUTPUT Output file

period:

- Period Selection --start START Start Date --end END End Date

reference:

- Reference date selection --date DATE Reference date/today --month
Display the month of the reference --week Display the week of the
reference

The script have the same period/reference specification of the period of
interest. The idea is that the reporting script will generate an
information for an extended period for example the last year and the
summary script will give summary for each month/week etc. The summary
script gives information about the users and the tools used in the
reference period. An example activity report is the following text
fragment.

id: 1 email: <mailto:oe@ifi.uio.no> last login: 2017-03-10T16:10:45.127999
created on: 2016-09-23T12:31:27.121080 This is a new user! For project
gx\_default Used time: 9:25:46(68 jobs) Remaining time: 416 days,
6:34:14 Local Jobs:

- For tool obt\_stat Used time: 0:04:19(2 jobs) For tool tokenizer
Used time: 0:00:33(8 jobs) For tool export\_tsv Used time: 0:15:49(9
jobs) For tool langid.py Used time: 0:00:31(6 jobs) For tool
langid\_py Used time: 0:00:17(2 jobs) For tool repp Used time:
0:01:33(7 jobs) For tool obt\_disambiguator Used time: 0:00:01(1
jobs) For tool wordcloud Used time: 0:01:03(2 jobs) For tool
export\_cg3 Used time: 0:05:08(3 jobs) For tool upload1 Used time:
0:00:32(7 jobs) For tool obt\_tokenizer Used time: 0:00:02(2 jobs)

Remote Jobs:

- --- gx\_default ---
  - Total slurm time: 3:56:21(29 jobs, 64 cpus). Total job time: 3
days, 21:53:25 For tool obt\_stat slurm time: 0:00:14(2 jobs, 2
cpus). Job time: 0:03:50 For tool core\_nlp\_parser slurm time:
0:02:12(1 jobs, 6 cpus). Job time: 3 days, 20:44:32 For tool bn
slurm time: 3:48:54(6 jobs, 36 cpus). Job time: 0:41:49 For tool
driver slurm time: 0:00:09(3 jobs, 3 cpus). Job time: 0:04:30
For tool obt\_disambiguator slurm time: 0:00:14(2 jobs, 2 cpus).
Job time: 0:02:27 For tool maltparser slurm time: 0:01:18(3
jobs, 3 cpus). Job time: 0:04:07 For tool obt\_tokenizer slurm
time: 0:02:14(7 jobs, 7 cpus). Job time: 0:07:40 For tool hunpos
slurm time: 0:01:06(5 jobs, 5 cpus). Job time: 0:04:30

* * *

The jobs are grouped by tool and are separated between the local and
remote jobs. Th remote jobs are organized by project. In Lap we have the
default project 'gx\_default' only. There are two reports of the
project. One from gold jobs and one from the jobs in the period
according to galaxy. This is the reason why the two number are
different. In the file attached they are also different as some of the
jobs in the gold database come from ps.hpc.

An example for a summary for tools is the following text fragment:

tool: obt\_disambiguator jobs: 119 users: 9 Local Jobs:

- jobs: 6 time: 2:03:56

Remote Jobs:

- jobs: 113 time: 14:15:44 slurm time: 0:46:35 cpus: 113

The usage of the tool is summarized from all the jobs recorded for all
the users. N.B. the two times reported for the remote jobs correspond to
the total time used. This shows that often the users will wait more time
for their job to start than the job execution itself.

# Week 20-33

Milen and Stephan met and discussed some of the objectives for the
summer. The following is the summary of the activities and results:

1\) Fixed a bug - There was a bug that cause a wrong interpretation of
the the dataset input in a tools that allowed LAP6 as input. As the
class was missing from library/python/lap/galaxy/datatypes.py it was not
correctly interpreted.

2\) Added a more complete support of LXF as input and output format.
Milen have added the LXF as a valid dataset format in LAP. A tool was
added to export dataset in LXF. An import hack was added to upload.py on
lap-test that allows to load data in LXF format as a lap-dataset. The
i/o functions for LXF are separated from other code in the file:
library/python/lap/tools/lxf.py During this I have noticed a bug in the
old version of the lap-to-dkpro export that is not impacting the results
but generates a repetition in the LXF outputs.

3\) The report script is integrated in the LAPSVN as well as some last
minute bugfixes were added.
<update date omitted for speed>{% endraw %}