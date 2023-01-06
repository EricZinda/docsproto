{% raw %}# Robust Evaluation of Syntactic Analysis

resa is a syntactic evaluation tool that does not require processing to
have been carried out over fixed sentence segmentation and tokenisation.
Evaluation is carried out over triples of (start\_char, end\_char,
label) which identify a span within a document by inter-character
positions, and the assigned label (which differs according to the level
of annotation). When there are no segmentation differences, phrase
structure evaluation produces the same scores as evalb, for the same
parameter files.

The canonical citation for resa is:

Rebecca Dridan and Stephan Oepen. 2013. Document parsing: Towards
realistic syntactic analysis. In *Proceedings of the 13th International
Conference on Parsing Technologies*, Nara, Japan.

Details of the software and data used in that paper are available
[here](https://blog.inductorsoftware.com/docsproto/missing/WeSearch_DocumentParsing).

The code is distributed through a Subversion (SVN) repository. For
read-only access, please use a command like the following:

    svn co http://svn.delph-in.net/resa/trunk resa

resa has many options (see below), but a normal invocation to evaluate
an .mrg file requires only the raw text, the gold .mrg file and the
system .mrg file (and an evalb-style parameter file, if you want to
ignore traces), and will evaluate all triple types present:

    resa -r wsj23.txt -g gold/wsj23.mrg -t goldtok/wsj23.mrg -p none.prm
    
    SENT: R: (2416/2416) = 1, P: (2416/2416) = 1, F: 1, EX: (2416/2416) 1
     TOK: R: (56684/56684) = 1, P: (56684/56684) = 1, F: 1, EX: (2416/2416) 1
     POS: R: (55146/56684) = 0.972867, P: (55146/56684) = 0.972867, F: 0.972867, EX: (1386/2416) 0.573675
      PS: R: (40070/44276) = 0.905005, P: (40070/43916) = 0.912424, F: 0.908699, EX: (1108/2416) 0.458609
     ALL: R: (154316/160060) = 0.964113, P: (154316/159700) = 0.966287, F: 0.965199, EX: (761/2416) 0.314983
    
    resa -r wsj23.txt -g gold/wsj23.mrg -t repptok/wsj23.mrg -p none.prm
    
    SENT: R: (2416/2416) = 1, P: (2416/2416) = 1, F: 1, EX: (2416/2416) 1
     TOK: R: (56622/56684) = 0.998906, P: (56622/56649) = 0.999523, F: 0.999215, EX: (2389/2416) 0.988825
     POS: R: (55078/56684) = 0.971667, P: (55078/56649) = 0.972268, F: 0.971968, EX: (1372/2416) 0.567881
      PS: R: (40041/44276) = 0.90435, P: (40041/43908) = 0.911929, F: 0.908124, EX: (1106/2416) 0.457781
     ALL: R: (154157/160060) = 0.96312, P: (154157/159622) = 0.965763, F: 0.96444, EX: (751/2416) 0.310844
    
    resa -r wsj23.txt -g gold/wsj23.mrg -t tokenizer-repptok/wsj23.mrg -p none.prm
    
    SENT: R: (2245/2416) = 0.929222, P: (2245/2339) = 0.959812, F: 0.944269, EX: (2245/2416) 0.929222
     TOK: R: (56579/56684) = 0.998148, P: (56579/56626) = 0.99917, F: 0.998659, EX: (2367/2416) 0.979719
     POS: R: (55046/56684) = 0.971103, P: (55046/56626) = 0.972098, F: 0.9716, EX: (1364/2416) 0.56457
      PS: R: (39654/44276) = 0.895609, P: (39654/43940) = 0.902458, F: 0.899021, EX: (1009/2416) 0.417632
     ALL: R: (153524/160060) = 0.959165, P: (153524/159531) = 0.962346, F: 0.960753, EX: (685/2416) 0.283526

Alternative file formats are valid: both line (LINE) and column (TAB)
oriented files can be used to evaluate segmentation and tagging.
Additionally, it is possible to output the characterised tuples that are
actually evaluated (using the --interim option) and these files can also
be directly used as input (CHAR format).

    Usage: ./resa <options>
    
    Options:
      -h [ --help ]               This usage information.
      -r [ --raw ] arg            Raw text file, required unless gformat and tformat are CHAR.
      -g [ --gold ] arg           Gold annotation file.
      -t [ --test ] arg           Test annotation file.
      -v [ --verbose ]            Unmatched tuples printed to STDERR.
      -s [ --stats ]              Print output in tab-delimited form.
      -f [ --fuzzy ]              Allow fuzziness in spans around punctuation
      -u [ --unlabelled ]         Unlabelled evaluation for phrase structure labels or dependencies
      -m [ --multi ]              Allow multiple tags (only valid for POS tags in LINE format).
      -b [ --boundary ]           Use sentence boundary end point, rather than span.
      -i [ --interim ]            Output interim characterised files.
                                  Files will be of form <file basename>.{gold,test}.tuples
      -p [ --param ] arg          evalb-style parameter file.
      -G [ --gformat ] arg (=MRG) Annotation format of gold file:
                                    LINE: 1 sentence per line
                                    TAB: 1 token per line, second+ column(s) (if present) considered to 
                                         be POS. Empty lines considered sentence breaks.
                                    MRG: .mrg format as in Penn Treebank.
                                    CONLLX: CONLL-X format.
                                    CHAR: Characterised tuples as from option --interim
      -T [ --tformat ] arg (=MRG) Annotation format of test file, options as for gold format.
<update date omitted for speed>{% endraw %}