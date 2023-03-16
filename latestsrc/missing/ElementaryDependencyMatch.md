{% raw %}# Elementary Dependency Match

Elementary Dependency Match (EDM; see [Dridan & Oepen,
2011](https://www.aclweb.org/anthology/W11-2927/)) is a granular
evaluation metric based on the so-called 'ltriples' format that can be
exported from a \[incr tsdb()\] profile. These triples are derived from
the variable-free reduction of MRSs known as *Elementary Dependency
Structures* (EDS), described by [Oepen & Lønning,
2006](http://www.emmtee.net/bib/Oep:Lon:06.pdf). EDS describes almost
all the semantics contained in an MRS (excepting scopal information),
and can be divided into three types of semantic information:

- NAMES: predicate name to char span ARGS: ARG-type relations between
char spans PROPS: features of predicates, such as TENSE and GENDER

An EDM evaluation is measured over all three types of ED, but other
combinations are possible. EDM\_NA evaluates predicate names and
arguments, and is closest to other metrics such as GR, CCG dependencies
etc. The default ouput for the evaluation script shows precision, recall
and f-score over each relation separately, as well as typical
aggregations.

To use this evaluation (following the original procedure of Dridan,
2007), you first need to set the data up as described below.
Alternatively, there is a more recent reference implementation of EDM
available as part of [mtool](https://github.com/cfmrp/mtool), the Swiss
Army Knife of Meaning Representation.

### Set up

1\. Export gold:

- $LOGONROOT/lingo/lkb/src/tsdb/home/export --binary --format ltriples
&lt;gold profile&gt;

2\. Export test:

- $LOGONROOT/lingo/lkb/src/tsdb/home/export --binary --format ltriples
--active=all &lt;test profile&gt;

This should produce directories containing one gzipped file per item
parsed. The ltriples should look like:

- \_treat\_v\_1&lt;10:17&gt; ARG2 \_user\_n\_of&lt;23:27&gt;

The links (eg. &lt;10:17&gt;) are necessary to the evaluation, and if
your output doesn't have them, ask StephanOepen why.

### Evaluate

The Perl implementation is available in SVN:

    svn co http://svn.delph-in.net/mu/evaluation/EDM/trunk

Usage: cat &lt;goldfilelist&gt;\|./edm\_eval.pl \[-i\] \[-v\] \[-p
&lt;num&gt;\] \[-s\] &lt;export directory&gt;

- -i: ignore gold where parse failed -v: verbose output
  
  -p &lt;num&gt;: parse number -s: raw figures for statistical
significance calculations

To evaluate a profile:

- ls -1 jhk.gold/\*\|edm\_eval.pl jhk.test

To evaluate a profile, only over files that received a parse:

- ls -1 jhk.gold/\*\|edm\_eval.pl -i jhk.test

To evaluate a single item:

- echo jhk.gold/3025231.gz \|edm\_eval.pl jhk.test

To evaluate a specific analysis of a single item:

- echo jhk.gold/3025231.gz \|edm\_eval.pl -p 100 jhk.test

To examine the errors in a single item:

- echo jhk.gold/3025231.gz \|edm\_eval.pl -v jhk.test

To produce the files needed for statistical significance testing:

- for file in jhk.gold/\*;
  
  - do echo $file\|edm\_eval.pl -s jhk.test;
  
  done &gt; jhk.test.stats

### Significance Testing

An implementation of the computationally-intensive randomisation test
described in:

- Alexander Yeh. 2000. More accurate tests for the statistical
significance of result differences. In Proceedings of the 18th
International Conference on Computational Linguistics (COLING 2000),
pages 947–953, Saarbruecken, Germany.

Usage:

- statsig\_shuffle.pl &lt;first stats file&gt; &lt;second stats
file&gt; \[iterations\] statsig\_shuffle.pl jhk.gold.stats
jhk.test.stats 10000

Last update: 2020-06-16 by AlexandreRademaker [[edit](https://github.com/delph-in/docs/wiki/ElementaryDependencyMatch/_edit)]{% endraw %}