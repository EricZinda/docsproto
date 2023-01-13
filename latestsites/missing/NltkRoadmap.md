{% raw %}This page describes the plans and actions required for getting DELPH-IN
data and processing into the NLTK. For some context, please see this
[discussion](https://blog.inductorsoftware.com/docsproto/summits/StanfordNltk) from the [2016 Stanford Summit](https://blog.inductorsoftware.com/docsproto/summits/StanfordTop).

Contents

1. [Motivation](https://blog.inductorsoftware.com/docsproto/missing/NltkRoadmap)
2. [Goals](https://blog.inductorsoftware.com/docsproto/missing/NltkRoadmap)
3. [Tasks](https://blog.inductorsoftware.com/docsproto/missing/NltkRoadmap)
4. [Questions](https://blog.inductorsoftware.com/docsproto/missing/NltkRoadmap)

# Motivation

The [NLTK](http://www.nltk.org/) (Natural-Language ToolKit) is a large
and widely used (particularly in education) Python package supporting a
number of NLP tasks, but currently it only has limited support for
semantic representations, and nothing for representing/accessing
DELPH-IN data (aside from a REPP wrapper). This is a good opportunity
for us to expand our presence.

# Goals

There are three kinds of additions we can provide to the NLTK:

- Data representations (e.g. modules for representing MRS, Derivation
trees, etc.)
- Data (e.g. make Redwoods available through nltk.download() and
provide necessary CorpusReaders)
- Processors (e.g. ACE or RESTful server interfaces)

Specifically, the following:

- Data representations
  - MRS
  - DMRS
  - EDS
  - DM (bilexical dependencies)
  - Derivation (and labeled) trees
- Data
  - Package Redwoods 9th growth or later
  - Provide CorpusReader for \[incr tsdb()\] profiles
- Processors
  - ACE interface
  - RESTful client

We should see if NLTK's DependencyGraph or FeatureStructure classes can
be used for the data representations.

# Tasks

There are some non-programming tasks that need to be done, as well.

- Contact the NLTK maintainers (Ewan Klein, Liling Tan, or the
nltk-devs mailinglist)
  - if our plans are appropriate for the NLTK (or some subset of
them)
  - how to proceed with implementations
- Provide unit tests
- Write or collaborate on writing new book sections for the
functionality

# Questions

- We have several Python implementations (see
[pyDelphin](https://github.com/delph-in/pydelphin) or
[pyDMRS](https://github.com/delph-in/pydmrs)), but can we drop that
code in directly, or should we refactor based on NLTK's base
classes?

Last update: 2016-06-23 by MichaelGoodman [[edit](https://github.com/delph-in/docs/wiki/NltkRoadmap/_edit)]{% endraw %}