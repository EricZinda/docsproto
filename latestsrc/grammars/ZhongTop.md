{% raw %}Zhong \[\|\] is an HPSG/MRS-based DELPH-IN grammar for the Chinese
languages, including Mandarin Chinese (simplified and traditional),
Cantonese, Min, etc. Currently Simplified Mandarin is the best supported
language. This grammar is based off ManGO
(<http://moin.delph-in.net/MandarinGrammarOnline>) created by Justin
Yang ([JustinChunleiYang](https://blog.inductorsoftware.com/docsproto/tools/JustinChunleiYang)) and Dan Flickinger
(<http://lingo.stanford.edu/dan/>).

#### Note on naming

The grammar's name is the first character of 中文 *Zhōngwén* “Chinese
Language”. The grammar's name is frequently written "Zhong \[∣\]", where
the final three characters are an ASCII approximation of the Chinese
character 中. In some fonts this looks better, with the middle pipe
character extending above and below the brackets. You can approximate
this in LaTeX with something like Zhong \\texttt{\[{\\large$\|$}\]}. The
final three characters are not pronounced, and it is also acceptable to
call the grammar merely "Zhong".

# Repository

You can download the current grammar from the
[Github](https://github.com/delph-in/zhong). You can get the grammar
using the following command.

    $ git clone https://github.com/delph-in/zhong.git

# Demo

You can try Zhong (for Simplified Mandarin Chinese) here: [Delphin-Viz
Demo](http://delph-in.github.io/delphin-viz/demo/). Select "Zhong (UW)"
as the grammar. Currently you have to segment the sentences yourself.

# Specifications

## Processing

- [ZhongAce](../ZhongAce)
- [ZhongPreprocessing](../ZhongPreprocessing)
- [ZhongYYMode](../ZhongYYMode)

## Translating

- [ZhongGeneration](../ZhongGeneration)
- [ZhongTranslation](../ZhongTranslation)

## Testing

- [ZhongRegressionTest](../ZhongRegressionTest)
- [ZhongCoverage](../ZhongCoverage)
- [ZhongHistory](../ZhongHistory)

## MRS Testsuites

- [MatrixMrsTestSuiteMandarin](https://blog.inductorsoftware.com/docsproto/matrix/MatrixMrsTestSuiteMandarin)
- [MatrixMrsTestSuiteZhTw](https://blog.inductorsoftware.com/docsproto/matrix/MatrixMrsTestSuiteZhTw)
- [MatrixMrsTestSuiteCantonese](https://blog.inductorsoftware.com/docsproto/matrix/MatrixMrsTestSuiteCantonese)
- [MatrixMrsTestSuiteIndonesian](https://blog.inductorsoftware.com/docsproto/matrix/MatrixMrsTestSuiteIndonesian)

## Phenomena-based Testsuites

<https://github.com/delph-in/zhong/tree/master/cmn/zhs/testsuites>

## Publications

##### Canonical Citation

- Fan, Zhenzhen, Sanghoun Song, and Francis Bond (2015) [An HPSG-based
Shared-Grammar for the Chinese Languages: Zhong
\[∣\]](http://www.aclweb.org/anthology/W15-3303), Grammar
Engineering Across Frameworks 2015 (in conjunction with ACL 2015).
Beijing, China.

##### Other Publications

- Fan, Zhenzhen (2019) [Building an HPSG Chinese grammar (Zhong)](https://dr.ntu.edu.sg/handle/10356/87331)
Doctoral thesis, Nanyang Technological University, Singapore.
- Fan, Zhenzhen, Sanghoun Song, and Francis Bond. (2015) [Building Zhong
\[∣\], a Chinese HPSG
Meta-Grammar](http://web.stanford.edu/group/cslipublications/cslipublications/HPSG/2015/fsb.pdf),
The 22nd International Conference on Head-Driven Phrase Structure
Grammar.
- Wang, Wenjie, Sanghoun Song, and Francis Bond. (2015) A Constraint-based
Analysis of A-NOT-A Questions in Mandarin Chinese, The 22nd
International Conference on Head-Driven Phrase Structure
Grammar.

## Contributors

- [FrancisBond](https://blog.inductorsoftware.com/docsproto/tools/FrancisBond)
- [SanghounSong](https://blog.inductorsoftware.com/docsproto/tools/SanghounSong)
- [ZhenzhenFan](/ZhenzhenFan)
- [JustinChunleiYang](https://blog.inductorsoftware.com/docsproto/tools/JustinChunleiYang)
- [DanFlickinger](https://blog.inductorsoftware.com/docsproto/tools/DanFlickinger)
- [MichaelGoodman](https://blog.inductorsoftware.com/docsproto/tools/MichaelGoodman)
- [BoChen](/BoChen)
- [HuiZhenWang](https://blog.inductorsoftware.com/docsproto/tools/HuiZhenWang)
- [JoannaSio](/JoannaSio)
- [LuisMorgadoCosta](https://blog.inductorsoftware.com/docsproto/tools/LuisMorgadoCosta)
- [ShanWang](https://blog.inductorsoftware.com/docsproto/tools/ShanWang)
- [WenjieWang](https://blog.inductorsoftware.com/docsproto/tools/WenjieWang)

This grammar was supported in part by:

- MOE Tier 2 grant *That's what you meant: a Rich Representation for
Manipulation of Meaning* (MOE ARC41/13)
- MOE Tier 2 grant *Grammar Matrix Reloaded: Syntax and Semantics of
Affectedness* (MOE ARC21/13)

Last update: 2022-04-26 by Francis Bond [[edit](https://github.com/delph-in/docs/wiki/ZhongTop/_edit)]{% endraw %}