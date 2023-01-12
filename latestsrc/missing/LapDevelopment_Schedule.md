{% raw %}# LAP-Related Work Packages

- |                            |            |
|----------------------------|------------|
| WP1 (Centres Setup)        | 1 PM       |
| WP2 (National Registry)    | 1 PM       |
| WP8 (LAP)                  | 30.5+23 PM |
| WP9 (Tool Adaptation)      | 0 PM       |
| WP10 (Metadata Adaptation) | 2 PM       |
| WP11 (Management)          | 2.5 PM     |

# Initial Schedule

Compared to the proposed milestones from the project proposal, the
project effectively started 18 months later than originally expected.
The CLARINO grant was finally approved in the spring of 2012; the job
search for the main LAP position completed in August that year, and
LAP work effectively started in October 2012.

- |     |                                             |      |     |      |     |
|-----|---------------------------------------------|------|-----|------|-----|
| 8.1 | LAP requirement and interface specification | 2012 | 4   | 2013 | 3   |
| 8.2 | LAP first testable prototype                | 2013 | 1   | 2014 | 1   |
| 8.3 | LAP inclusion of analysis tools             | 2014 | 1   | 2014 | 3   |
| 8.4 | LAP first production version                | 2014 | 3   | 2015 | 1   |
| 8.5 | LAP documentation, workshop, evaluation     | 2015 | 2   | 2016 | 3   |
| 8.6 | LAP Tuning and complete version             | 2016 | 4   | 2017 | 3   |
  
  |     |                                    |      |     |      |     |
|-----|------------------------------------|------|-----|------|-----|
| 9.1 | Tool adaptation, testable versions | 2013 | 1   | 2014 | 3   |
| 9.2 | Tool testing and final versions    | 2014 | 2   | 2015 | 2   |

# Revised Schedule

Due to repeated leaves of absence of core staff, LAP personnell
allocation has lagged behind projections by close to nine person months
at the end of 2014. Accordingly, the implementation of LAP milestones
8.2 and onwards have fallen behind schedule by a little more than half a
year. With its progress report for the second tertial of 2014, the
LAP team proposed the following schedule revisions:

- |     |                                         |      |     |      |     |
|-----|-----------------------------------------|------|-----|------|-----|
| 8.2 | LAP first testable prototype            | 2013 | 1   | 2014 | 3   |
| 8.3 | LAP inclusion of analysis tools         | 2014 | 3   | 2015 | 1   |
| 8.4 | LAP first production version            | 2015 | 1   | 2015 | 3   |
| 8.5 | LAP documentation, workshop, evaluation | 2015 | 4   | 2017 | 1   |
| 8.6 | LAP Tuning and complete version         | 2017 | 2   | 2018 | 1   |

It remains to be determined where things stand regarding WP9, and
whether and how the schedule should be adjusted there.

# Description of Work (WP8)

*This work package comprises the following sub-tasks: (a) user
requirements and technology survey (including the wider CLARIN and
META-NET contexts); (b) architecture specification; (c) middleware
design and implementation; (d) user interface design and implementation;
(e) integration of language analysis components; (f) support and
training to component providers and users (including documentation); (g)
portal maintenance and operations; and (h) liaising with other CLARIN(O)
participants.*

The analysis portal presupposes authentication and authorization
services in WP3, access to the data in the repositories at the content
providers, and access to compatible tools (WP9).

\[...\]

*LAP will assist in license clarification, interface definitions for
conversion from and to inter- change formats, ‘wrapping’ of tools for
HPC use, general ‘hardening’ to improve scalability and
interoperability, and on-line documentation. Technology developed (or
currently used) in Norway will be complemented with standard language
analysis tools available from inter- national players, with a bias
towards general-purpose, open-source systems.* \[...\]

# Main Work Package Dependency: WP9

*Existing grammars and taggers will be adapted so as to produce a CLARIN
compatible format and become more easily integrated in pipelines within
the LAP, as well as in other conformant platforms. This work will be
carried out by tool providers in cooperation with IFI (UiO). Rule-based
taggers for Norwegian Bokmål and Nynorsk (comprising a tokenizer,
morphological analyser, guesser, and rule-based disambiguator), as well
as statistical taggers for orthographically transcribed spoken
Norwegian, Swedish, Danish, Icelandic, and Faroese will be adapted. The
tagger adaptation will be carried out by the Text Laboratory (UiO),
while some work on the Oslo–Bergen Tagger will be done in cooperation
with Uni Research. Furthermore, the constraint grammars for Sami will be
adapted and optimized by UiT. For the three Sami languages, there are
efficient morphological transducers and, for one of them, grammatical
and dependency parsers available.*
<update date omitted for speed>{% endraw %}