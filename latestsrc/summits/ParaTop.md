{% raw %}This page describes various approaches to paraphrasing using the
DELPH-IN tools. This page was initiated by [FrancisBond](https://blog.inductorsoftware.com/docsproto/tools/FrancisBond)
and [DarrenAppling](DarrenAppling); please feel free to make additions
or corrections as you see fit.

# How to Paraphrase

- **Strict**: parse and then generate
- **Some variation**: parse and then rephrase (see
[RmrsParaphrasing](https://blog.inductorsoftware.com/docsproto/concept/RmrsParaphrasing))
- **More variation**: create a monolingual Machine Translation system
(see [MachineTranslationTop](MachineTranslationTop))

In this case, the monolingual machine translation should use the
*external* MRS exposed by the Semantic Interface ([SEM-I](https://blog.inductorsoftware.com/docsproto/concept/RmrsSemi)),
not the internal MRS, for the following reasons:

1. the SEM-I is the interface to outside resources, such as
[WordNet](/WordNet), which may also be used in generation
1. the internal MRS is subject to restructuring as the quest for ever
better linguistic analysis proceeds
1. the mtr.tdl used in MT refers to the external MRS

The SEM-I should, therefore, expose enough information for the
paraphrase engine, including some hierarchies among types, this must be
done manually at present.

# Applications

## Expanding Training Data for Statistical MT

Bond, Francis, Eric Nichols, Darren Scott Appling, Michael Paul (2008)

- [Improving Statistical Machine Translation by Paraphrasing the
Training
Data](http://www2.nict.go.jp/x/x161/en/member/bond/pubs/2008-iwslt-smt-para.pdf),
In IWSLT-2008.
{% endraw %}