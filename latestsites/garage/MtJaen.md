{% raw %}# Japanese English Machine Translation

This page describes the Jaen MT system, an MT system based on the [LOGON
architecture](), using Jacy for the source language
analysis and the ERG for the target language generation. In
order to degrade gracefully in the presence of input we cannot yet
translate, we are also working on a backup [Statistical MT
system]() based on [Moses](http://www.statmt.org/moses/).

Jaen is the elder sibling of Noja, the Norwegian-Japanese MT
system.

Most of the rules of the Jaen MT system are extracted automatically from
parallel corpora. The procedure for automatic rule extraction is
described here: MT rule extraction

Some results can be found here: MtJaenTanaka,
MtJaenFeedbackCleaning.

There are some note on how to set up an MT system with the DELPH-In
tools in the MT tutorial.

A list of things that need to be fixed in Jaen can be found here: [Todo
list for Jaen]()

## References

- Francis Bond, Stephan Oepen, Melanie Siegel, Ann Copestake, and Dan
Flickinger (2005) [Open source machine translation with
DELPH-IN](http://www2.nict.go.jp/x/x161/en/member/bond/pubs/2005-summit-osmt.pdf).
In *Open-Source Machine Translation: Workshop at MT Summit X*, pp
15--22, Phuket.
- Francis Bond, Stephan Oepen, Eric Nichols, Dan Flickinger, Erik
Velldal and Petter Haugereid (2011) [Deep Open Source Machine
Translation](http://www.springerlink.com/openurl.asp?genre=article&id=doi:10.1007/s10590-011-9099-4).
In *Machine Translation* **25**(2) 87-105

Last update: 2012-07-26 by PetterHaugereid [[edit](https://github.com/delph-in/docs/wiki/MtJaen/_edit)]{% endraw %}