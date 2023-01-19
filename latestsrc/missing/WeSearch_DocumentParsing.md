{% raw %}# Document Parsing

This is a companion website to the publication:

Rebecca Dridan and Stephan Oepen. (2013). Document parsing: Towards
realistic syntactic analysis. In *Proceedings of the 13th International
Conference on Parsing Technologies (IWPT)*, Nara, Japan.

Details of software versions and options used are spelt out below.

## External pre-processors

### REPP

Rule-based tokeniser, see [ReppTop](https://blog.inductorsoftware.com/docsproto/garage/ReppTop).

### tokenizer

Rule-based sentence segmenter, downloaded from
<http://www.cis.uni-muenchen.de/~wastl/misc/>. Since the webpage has
since disappeared, and the code is GPL'd, we make available the original
sources (corresponding to the most recent release, tokenizer 1.0)
through SVN

      svn co -r 16422 http://svn.emmtee.net/trunk/cis/tokenizer

## Parsers

### Charniak & Johnson reranking parser

Charniak, E., & Johnson, M. (2005). [Coarse-to-fine n-best parsing and
MaxEnt discriminative
reranking](http://aclweb.org/anthology//P/P05/P05-1022.pdf). In
*Proceedings of the 43rd Meeting of the Association for Computational
Linguistics* (p. 173 – 180). Ann Arbor, MI, USA.

Downloaded from <https://github.com/BLLIP/bllip-parser/> on 26th March,
2012.

Document parsing (default):

    cat wsj23.txt | ./tokenizer -L en-u8 -P -S -E '' |\
     perl -ne 'next if /^$/; chomp; $sent++; print "<s $sent> $_ </s>\n";' |\
     bllip-parser/parse.sh

### Berkeley parser

Petrov, S., Barrett, L., Thibaux, R., & Klein, D. (2006). [Learning
accurate, compact, and interpretable tree
annotation](http://aclweb.org/anthology//P/P06/P06-1055.pdf). In
*Proceedings of the 21st International Conference on Computational
Linguistics and the 44th Meeting of the Association for Computational
Linguistics* (p. 433 – 440). Sydney, Australia.

Java 1.6 version of berkeleyParser.jar and eng\_sm6.gr, downloaded from
<http://code.google.com/p/berkeleyparser/> on 13th May, 2013.

Document parsing (default):

    cat wsj23.txt | ./tokenizer -L en-u8 -P -S -E '' |\
     perl -pe 's/\(/-LRB-/g; s/\)/-RRB-/g;' |\
     java -jar berkeleyParser.jar -gr eng_sm6.gr -tokenize -accurate

### Stanford CoreNLP parser

Klein, D., & Manning, C. D. (2003). [Accurate unlexicalized
parsing](http://aclweb.org/anthology//P/P03/P03-1054.pdf). In
Proceedings of the 41st Meeting of the Association for Computational
Linguistics (p. 423 – 430). Sapporo, Japan.

Version 3.20, downloaded from
<http://nlp.stanford.edu/software/lex-parser.shtml> on 12th August,
2013.

Document parsing (default):

    java -Xmx3g -cp "stanford-parser-full-2013-06-20/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat oneline edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz wsj23.txt

Last update: 2013-11-27 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/WeSearch_DocumentParsing/_edit)]{% endraw %}