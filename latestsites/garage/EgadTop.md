{% raw %}**Egad** (Erroneous Generation Analysis and Detection) is a tool that
helps a grammar developer find problematic rules in an HPSG grammar by
analyzing the grammar's generation results. The grammar developer can
also use it to obtain statistics about how the grammar performs. Such
statistics include the proportion of lexical or rule variance between
generation and parsing results, if the generated items have the same
MRS, if the top ranked generation result matches the input string, etc.

**Egad** was created by MichaelGoodman and
FrancisBond in order to improve generation results for
Jacy, but it has also been used to analyze the ERG. It relies
on both the [\[incr tsdb()]()\] and LKB packages for
parsing and generating sentences with a grammar. Please contact the
authors if **Egad** does not work with your grammar.

EgadInstallation : Installing **Egad**

[EgadAnalysis](/EgadAnalysis) : Obtaining a grammar analysis with
**Egad**

[EgadErrorMining](/EgadErrorMining) : Finding errors with **Egad**

### Publications

Michael Goodman and Francis Bond (2009) [Using Generation for Grammar
Analysis and Error
Detection](http://www.aclweb.org/anthology/P/P09/P09-2028.pdf), In
*Proceedings of the ACL-IJCNLP 2009 Conference Short Papers*, Singapore,
pp 109-112.
<update date omitted for speed>{% endraw %}