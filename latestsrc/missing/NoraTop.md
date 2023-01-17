{% raw %}# Background

The so-called WeScience<sub>0</sub> project is a preparatory joint
initiative with the [Norwegian Open Research
Archives](http://www.ub.uit.no/wiki/openaccess/index.php/NORA) (NORA)
and the UiO [Center for Information
Technology](http://www.usit.uio.no/suf/ds/) (USIT); the project is
partially funded by NORA in 2009 and forms part of the larger
[WeScience](http://www.delph-in.net/wescience) initiative coordinated by
the UiO [Language Technology
Group](http://www.ifi.uio.no/research/groups/lns/lt.html). Some general
motivation for the project and a preliminary project plan are available
through the original [project
proposal](http://www.emmtee.net/nora/nora.20-apr-09.pdf). Related
initiatives include the [ACL Anthology Reference
Corpus](http://acl-arc.comp.nus.edu.sg/), the
[HyLaP](http://hylap.dfki.de/) project at DFKI Saarbrücken, and the UK
[Intute Repository Search](http://www.intute.ac.uk/irs).

This page (and other NORA sub-pages), at least as of August 2009,
primarily serve for project-internal communication. Access to these
pages is limited to registered wiki users, using the exact user name
registered on the [NoraGroup](https://blog.inductorsoftware.com/docsproto/missing/NoraGroup) page. Please contact
StephanOepen or [GisleYtrestol](/GisleYtrestol), in case
you want additional NORA pages to be created, experience difficulties
with reading or editing these pages, or need assistance related to wiki
usage more generally.

# Project Objectives

The WeScience<sub>0</sub> effort can be sub-divided by basic processing
tasks. These include (a) PDF Inspection
([NoraInspection](https://blog.inductorsoftware.com/docsproto/missing/NoraInspection)), (b) text extraction
([NoraExtraction](https://blog.inductorsoftware.com/docsproto/missing/NoraExtraction)), (c) language identification
([NoraIdentification](https://blog.inductorsoftware.com/docsproto/missing/NoraIdentification)), (d) text correction
([NoraCorrection](https://blog.inductorsoftware.com/docsproto/missing/NoraCorrection)), (e) sentence boundara detection
([NoraSegmentation](https://blog.inductorsoftware.com/docsproto/missing/NoraSegmentation)), and (f) interfacing to the
[Lucene](http://lucene.apache.org/java/docs/) search engine
([NoraLucene](https://blog.inductorsoftware.com/docsproto/missing/NoraLucene)). Please view the individual pages for details
and the current state of play.

The main deliverables from the project comprise (i) a flexible
pre-processing pipeline, implementing tasks (a) through (e) above; (ii)
documented knowledge on the strong and weak points of various existing
tools (for text extraction and segmentation, for example) and parameter
settings, correlated to common PDF production methods; and (iii) a
revised on-line search interface for NORA, based on Lucene and
supporting full text search. The IFI Language Technology group has the
primary responsibility for tasks (a) through (e) (and, correspondingly,
deliverables (i) and (ii)), whereas USIT focuses on task (f) (and
deliverable (iii)).

# TextGrabber

The software application \[[TextGrabber](/TextGrabber)\] is now
finished, and the technical report can be downloaded
[here](http://folk.uio.no/gisley/wescience0/techreport.pdf).
\[[TextGrabber](/TextGrabber)\] is the software that has been developed
to meet the demands of this project.

# People Involved
<update date omitted for speed>{% endraw %}