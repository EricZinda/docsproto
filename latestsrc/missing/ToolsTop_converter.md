{% raw %}# DELPH-IN converter to bilexical dependencies

## Background

The script converts ERG derivation tree to bi-lexical syntactic dependencies (dubbed DT), and ERG [Elementary Dependency Structures](https://blog.inductorsoftware.com/docsproto/tools/EdsTop) to bi-lexical semantic dependencies (dubbed DM).

See brief [presentation of new DELPH-IN Tools](http://www.delph-in.net/2013/tools.pdf) from the 9th DELPH-IN Summit 31 July 2013.

# Installation

The converter script is located in the [LOGON Source Tree](https://blog.inductorsoftware.com/docsproto/tools/LogonTop) (see [[LogonInstallation]] about the installation of LOGON tree on your machine):

```
${LOGONROOT}/uio/dtm/converter.py
```

A brief documentation is available at `${LOGONROOT}/uio/dtm/converter.pdf`

## Usage

`$LOGONROOT/bin/dtm` is the wrapper that invokes the converter:

```
$LOGONROOT/bin/dtm --grammar /usit/abel/u1/angelii/logon/lingo/erg --data <data> --tok erg --dtm <output> --tex <output>$LOGONROOT/bin/dtm --grammar /usit/abel/u1/angelii/logon/lingo/erg --data <data> --tok erg --dtm <output> --tex <output>
```

## Publications

* Angelina Ivanova, Stephan Oepen, Lilja Øvrelid, and Dan Flickinger. [Who Did What to Whom? A Contrastive Study of Syntacto-Semantic Dependencies](http://aclweb.org/anthology/W/W12/W12-3602.pdf). Linguistic Annotation Workshop. Jeju, South Korea, 2012
* Angelina Ivanova, Stephan Oepen, Rebecca Dridan, Dan Flickinger and Lilja Øvrelid. On Different Approaches to Syntactic Analysis Into Bi-Lexical Dependencies An Empirical Comparison of Direct, PCFG-Based, and HPSG-Based Parsers. The 13th International Conference on Parsing Technologies (IWPT). Nara, Japan, 2013
* Angelina Ivanova, Stephan Oepen and Lilja Øvrelid. [Survey on parsing three dependency representations for English](http://aclweb.org/anthology//P/P13/P13-3005.pdf). ACL Student Research Workshop. Sofia, Bulgaria, 2013
<update date omitted for speed>{% endraw %}