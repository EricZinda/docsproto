{% raw %}This is a page for up-to-date notes on running the [Korean Resource
Grammar](http://krg.khu.ac.kr).

The Korean Resource Grammar was originally built by
[JongBokKim](https://blog.inductorsoftware.com/docsproto/tools/JongBokKim) and [JaehyungYang](/JaehyungYang). A revised
matrix-compliant version has been rebuilt by
[SanghounSong](https://blog.inductorsoftware.com/docsproto/tools/SanghounSong) and [FrancisBond](https://blog.inductorsoftware.com/docsproto/tools/FrancisBond) --- the KRG
now both parses and generates.

### Encoding Issues

- CLIM does not currently support entering Korean directly under
linux. Instead, we recommend you enter it though emacs.
- To show Korean in the output either
  - use pangolui (see *Alternative Lui Implementations* on the
[LkbLui](https://blog.inductorsoftware.com/docsproto/tools/LkbLui) page) ([FrancisBond](https://blog.inductorsoftware.com/docsproto/tools/FrancisBond) recommends
this)
  - specify Korean fonts in the .luirc (see [LuiRc](https://blog.inductorsoftware.com/docsproto/tools/LuiRc))

### Tokenizing

- There are three script files; lkb/script, lkb/script.common,
lkb/test.
- lkb/script: If you take this, the input string should be fully
tokenized.
- lkb/script.common: If you take this, you can input just common
Korean sentences. This script will operate the pre-processor for
parsing and generation.
- lkb/test: If you want to test each grammar module with a small size
of lexicon, please take this.

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}