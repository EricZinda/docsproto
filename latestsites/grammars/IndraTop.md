{% raw %}# INDRA

This page is for a broad-coverage Indonesian Resource Grammar (INDRA)
within the framework of Head Driven Phrase Structure Grammar (HPSG)
(Pollard and Sag, 1994) and Minimal Recursion Semantics (MRS) (Copestake
et al., 2005).

## Online Demo

Using [Demophin](http://compling.hss.ntu.edu.sg/demophin/indra/)
(temporary server:
[Demophin](http://chimpanzee.ling.washington.edu/demophin/indra/)) or
[delphin-viz Demo](http://delph-in.github.io/delphin-viz/demo/). You can
parse simple sentences such as *Adi tidur di sini* "Adi sleeps here" and
*Adi mengejar Budi* "Adi chases Budi".

Compare INDRA with other DELPH-IN HPSG grammars using
[TypediffTop](https://blog.inductorsoftware.com/docsproto/tools/TypediffTop) ([online
version](http://hum.csse.unimelb.edu.au/typediff/)).

## Repository

You can download the current grammar from the
[Github](https://github.com/davidmoeljadi/INDRA). You can get the
grammar using the following command.

    $ git clone https://github.com/davidmoeljadi/INDRA

## Specifications

- [Grammar
Catalogue](http://moin.delph-in.net/GrammarCatalogue/#Indonesian_Resource_Grammar_.28INDRA.29)
(check INDRA/METADATA, ./create-catalogue-entry.sh \~/grammar/INDRA/
-w for html or -l for latex)
- Processing: [IndraAce](IndraAce),
[IndraPreprocessing](IndraPreprocessing),
[IndraYYMode](http://moin.delph-in.net/IndraYYMode)
- Machine Translation: [IndraTranslation](IndraTranslation)
- Testing: [IndraRegressionTest](IndraRegressionTest)
- Treebanking: [IndraTreebanking](https://blog.inductorsoftware.com/docsproto/tools/IndraTreebanking)

## Testsuites

- MRS Testsuite:
[MatrixMrsTestSuiteIndonesian](https://blog.inductorsoftware.com/docsproto/matrix/MatrixMrsTestSuiteIndonesian)
- Phenomena-based Testsuites:
<https://github.com/davidmoeljadi/INDRA/tree/master/testsuites>

## Phenomena in Indonesian

- [Intransitive and transitive verbs, Applicative -i constructions,
Verb reduplication](../LADIndonesianMorphology)
- [Passive voice](CapitolHillPassives)
([Discussion](../CapitalHillPassivesDiscussion))

## Contributors

- [DavidMoeljadi](https://blog.inductorsoftware.com/docsproto/tools/DavidMoeljadi)
- [FrancisBond](https://blog.inductorsoftware.com/docsproto/tools/FrancisBond)
- [SanghounSong](https://blog.inductorsoftware.com/docsproto/tools/SanghounSong)
- [DanFlickinger](https://blog.inductorsoftware.com/docsproto/tools/DanFlickinger)
- [MichaelGoodman](https://blog.inductorsoftware.com/docsproto/tools/MichaelGoodman)
- [LuisMorgadoCosta](https://blog.inductorsoftware.com/docsproto/tools/LuisMorgadoCosta)

## References

Moeljadi, David, Francis Bond, and Sanghoun Song (2015) [Building an
HPSG-based Indonesian Resource Grammar
(INDRA)](http://aclweb.org/anthology/W/W15/W15-3302.pdf). In Proceedings
of the Grammar Engineering Across Frameworks (GEAF) Workshop, 53rd
Annual Meeting of the ACL and 7th IJCNLP, pages 9–16, Beijing, China,
July 26-31, 2015.

Moeljadi, David, Francis Bond, and Luís Morgado da Costa (2016) [Basic
copula clauses in
Indonesian](http://web.stanford.edu/group/cslipublications/cslipublications/HPSG/2016/headlex2016-mbm.pdf).
In [Proceedings of the Joint 2016 Conference on Head-driven Phrase
Structure Grammar and Lexical Functional
Grammar](https://web.stanford.edu/group/cslipublications/cslipublications/HPSG/2016/),
pages 442–456, Warsaw, Poland.

## Acknowledgments

This grammar was supported in part by

- MOE Tier 2 grant *That's what you meant: a Rich Representation for
Manipulation of Meaning* (MOE ARC41/13)
- MOE Tier 2 grant *Grammar Matrix Reloaded: Syntax and Semantics of
Affectedness* (MOE ARC21/13)

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}