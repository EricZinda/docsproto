{% raw %}# Overview

This page has some, probably out-of-date discussions about how to make parsing in DELPH-IN more robust.  

Here are some other discussions:
* Discussion at Tomar
* Discussion at Squamish

# PCFG Parsing

the two-stage parser starts with conventional HPSG parsing, until a
fixed point where no more edges are created (ie. empty task agenda).

the PCFG parsing stage then starts. first it sets the score of all full
edges to 1. since all log probabilities should be &lt;= 0, this marks
the edges to be rescored later with PCFG model. then an iteration is
done on all passive inflrs\_complete\_p() non-input full items, trying
to initialize new parsing tasks on the agenda. the parsing tasks are
sorted in the agenda according to the PCFG score for the constructed
local tree. this guarantees that best subtrees for a given span is
always constructed first (also thanks to the fact that, unlike the MEM
scores, generative PCFG model score monotonically decrees when ascending
in the constructed tree).

now let's consider the packing of PCFG edges. since for the given span
and category, the highest score passive edge is always created first, i
simply packed the latter ones into the existing one (that is to say,
always pack proactively). also, packing never happens between PCFG and
HPSG edges. because only the representative edges (with maximal local
score) remain in the chart, they will guarantee that the higher edge
built with the representative daughter edges will also receive the
maximal score, among all of its possible decompositions. this is a nice
trick which makes Viterbi decoding (1-best unpacking) trivial: no need
to call hypothesize\_edge at all, just take the representative edge on
the top (or the best representative if there are more than one). ah,
writing this down just reminds me that i do need to call
hypothesize\_edge(E,0) on each full edge taken from the HPSG stage (if
packing is enabled there too). this is to assign the max local PCFG
score to each of the HPSG full edges. i forgot to do this, and might be
receiving sub-optimal hypothesis under packed full HPSG edges.

when PCFG rules tries to build new edges, different checking options are
available for the routine passive\_item\_exists():

- -robust=1: does not care whether a HPSG full edge already
  - exists. this basically assumes that PCFG rules and HPSG rules,
although share same names, are not interfering with each other.
this mode guarantees that the optimal PCFG tree will be found.
the drawback is that edges built in the first stage might be
duplicated in the PCFG universe.
- -robust=2: if an HPSG full edge exists for a span with a specific
  - rule, the same edge will not be rebuilt in the PCFG parsing
stage (as long as the triggering rule's LHS matches that HPSG
rule name). this mode does not guarantee to find the tree with
maximal PCFG score. it is basically assuming there is no need to
find alternative PCFG analyses for phrases analysed by the HPSG.
i was also worried about whether this will affect the 1-best
unpacking (e.g. whether this will distorted the order of edges
to be created in the forest), but it seems that i was
overcautious.
- -robust=3: elaborated duplication checking. if the PCFG edge to be
  - built has the same category of an existing HPSG edge, and all
its daughters matches the HPSG edge's daughters' rules (i assume
packed nodes does not need to be checked, and they should be
built with the same rule, or am i wrong here?). this mode will
not duplicate edges, and still find all necessary alternative
PCFG analyses.

the three settings put increasing extra burden on the checking routine.
optimization needed at certain stage. for instance, i need to to keep an
immutable copy of the first stage chart, so that iteration only on
non-PCFG edges can be achieved. indexing and caching will also help.

one might argue that one don't even need to do the stage one HPSG
parsing to construct the passive edges. if the PCFG large enough, it be
able to build these passive edges by itself. But keeping the HPSG
passive edges help to improve robustness of the PCFG, in case a HPSG
rule triggers a valid but rare branching that has not been observed in
the treebank. Also, when using -robust=2,3, one might save some memory
and processing, if passive\_item\_exists() is done efficiently.

Last update: 2022-11-14 by Francis Bond [[edit](https://github.com/delph-in/docs/wiki/RobustTop/_edit)]{% endraw %}