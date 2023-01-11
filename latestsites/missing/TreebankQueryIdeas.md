{% raw %}A list of kinds of queries that have come up that do not seem to be
directly supported by existing treebank search facilities:

- Constituents with a disjoint EP graph in terms of ARG composition.
For example, the constituent *made Sandy* in *Kim made Sandy laugh.*
(Inspired by conversation with Ann about DMRS composition.)
Initially, it looked like this might require a search mechanism that
reinflated the gold trees edge by edge and exported the sement for
each edge along the way. However, on further discussion, we
suspected that only head-complement constructions would likely be
relevant, and with existing software (i.e. the FFTB set up) it
should be relatively straightforward to (1) find edges licensed by
head-complement rules, (2) label EPs with their edge of origin
(rather than characterization), (3) search for instances of the HCR
where the INDEX of the non-head daughter does not appear as an ARGn
of any EP from the head daughter (and also isn't a scopal argument).

Last update: 2015-12-08 by EmilyBender [[edit](https://github.com/delph-in/docs/wiki/TreebankQueryIdeas/_edit)]{% endraw %}