{% raw %}# Background

In early 2014, we are preparing a minor update of DeepBank
to fix a handful of imperfections in the original release:

- missing segments: wsj09e, wsj12e, wsj20e
- synchronize final REPP treatment of ellipses and profiles
- benefit from bug fixes in EDS export
- corrections in head assignment for DT conversion
- pick up DM conversion improvements (from SDP release)
- include GML-based WDC profiles in release

Candidate fixes to apply (which would require an increment of the
grammar version):

- introduction of more idiom patterns
- automated flagged of invalid idiom fragments in gold results
- ESD-related renaming (e.g. PT and its values)
- unknown\_card and its CARG
- fix unbound ARG1 on ‘measure’ relation in ‘how quickly does he
arrive?’
- known sources of systematic annotation consistency (if any; e.g.
splitting U.S. as sandwiched period).
- rule naming (recover the one case using an underscore in the first
field)
- predicate name on not ... but
- integrate --DT percolations
- cherry-pick from the trunk: ditch gapping analysis, plug SLASH
blackholes; purge multi-word names.

n-nh\_j-cpd\_c =&gt; n-j\_j-cpd\_c n-nh\_j-t-cpd\_c =&gt;
n-j\_j-t-cpd\_c n-nh\_v-cpd\_c =&gt; n-v\_j-cpd\_c

Finally, a few aspects of ‘packaging’ that did not make it into the
first version

- update WeScience and WDC treebanks to GML versions
- export into MRG-style trees with PTB-style tokenization
- investigate high failure percentage in robust meaning construction
(and DM conversion)

Last update: 2014-03-25 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/DeepBank_OneOne/_edit)]{% endraw %}