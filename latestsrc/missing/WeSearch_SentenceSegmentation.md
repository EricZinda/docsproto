{% raw %}# Desiderata

Some useful features of a sentence segmentation tool (not necessarily
important for Lars Jørgen's thesis):

- Domain/genre/language independent
- Identification of non-linguistic segments
- Mark-up aware
- Mark-up normalisation
- Handling unpunctuated text
- Stand-off annotation

# Examples of Difficult Cases

- Sentence-final abbreviation:
  - *The group included Dr. J. M. Freeman and T. Boon Pickens Jr.*
- Mid-sentence abbreviations followed by proper nouns:
  - *It was due Friday by 5 p.m. Saturday would be too late* ...
compare to ... *She has an appointment at 5 p.m. Saturday to get
her car fixed.*
- Reported speech:
  - *"This issue crosses party lines and crosses philosophical
lines!" said Rep. John Rowland (R., Conn.).*
- Single sentence quotes, multi-sentences quotes, nesting of quotes
and quotes crossing sentences boundaries, straight vs curly symbols,
and period/comma inside/outside the quotation marks. Example in
Portuguese:
  - *A política de estabilização teve uma “onda de liquidações de
empresas pequenas e médias. Seus efeitos negativos sobre a
produção foram de tal monta que houve um afrouxamento do combate
à inflação.” Apesar dos efeitos depressivos da política, o
conjunto de reformas seria, segundo Fabrício, importante para o
crescimento econômico: “As mudanças ocorridas nesse período
podem ser vistas como a gênese para a retomada. E como ponto de
partida para o explosivo crescimento pós-68.” Em avaliação feita
posteriormente, Roberto considerou que o principal resultado do
PAEG não esteve “na realização de objetivos específicos, mas na
importância do esforço dedicado a reformas”.*

# Evaluation Methods

- Error rate in classifying ambiguous punctuations marks

# Existing Approaches

## Apache OpenNLP

Some details
[here](http://opennlp.apache.org/documentation/1.5.2-incubating/manual/opennlp.html#tools.sentdetect).
[MaxEnt](/MaxEnt) model - the same as [MxTerminator](/MxTerminator)?

## Gisle's Favorite Tool

[tokenizer](http://www.cis.uni-muenchen.de/~wastl/misc/) in flex(1) and
'simple C'.

## Mikheev

Mikheev, A. 2002. *[Periods, Capitalized Words,
etc.](http://www.aclweb.org/anthology/J02-3002.pdf)* Computational
Linguistics 28(3).

Treats three related aspects of text normalisation: sentence boundary
detection, disambiguation of capitalised words and identification of
abbreviations. Sentence boundary detection uses four simple rules (where
the concept of 'following' disregards brackets, quotation marks etc.):

- If a period follows a nonabbreviation it is a sentence terminal
- If a period follows an abbreviation and is the last token in a
paragraph it is a sentence terminal
- If a period follows an abbreviation and is not followed by a
capitalised word it is not a sentence terminal
- If a period follows an abbreviation and is followed by a capitalised
word which is not a proper name, it is a sentence terminal

This yields very precise results, but does not cover the case for when a
period follows an abbreviation which is followed by a proper name -
which is an ambiguous case. In these cases, Mikheev uses the majority
baseline, assuming non-sentence boundary.

## MxTerminator

Reynar, J. and Ratnaparkhi, A. 1997. [A Maximum Entropy Approach to
Identifying Sentence
Boundaries](http:/www.aclweb.org/anthology/A97-1004.pdf). In
*Proceedings of the Fifth ACL Conference on Applied Natural Language
Processing*.

Compared two maximum entropy systems - one with which benefits from
domain and genre specific intuitions (features such as honourifics,
company status designations, and another which is designed to be more
portable. The features also include membership of words in a list of
abbreviations induced from the labeled training data.

The tailored features give 0.8% points improvement in accuracy, with an
accuracy of 98.8% on when trained on sections 00-24 WSJ, and tested on
the Wall Street Journal portion of the ACL/DCI collection (Church and
Liberman 1991; formed the basis of LDC2000T43 which 'both overlaps and
supplments the million-word Penn Treebank (PTB) collection of parsed and
POS-tagged WSJ texts).

Source available [online](ftp://ftp.cis.upenn.edu/pub/adwait/jmx/).

## Punkt

Kiss, T. and Strunk, J. 2006. *[Unsupervised Multilingual Sentence
Boundary
Detection](http://aclweb.org/anthology-new/J/J06/J06-4003.pdf)*.
Computational Linguistics 32(4).

Centred on the identification of abbreviations. Uses three robust
properties of abbreviations that are valid accross languages: (1) an
abbreviation is a strong collocation of the abbreviated word and a
period, (2) abbreviations tend to be short and (3) abbreviations often
contain word-internal periods. Combined with some special heuristics for
initials and ordinal numbers, the system identifies 99.2% of
abbreviations in newspaper corpora in eleven languages.

All periods not attached to an abbreviation are sentence boundaries.

Then a number of heuristics are applied to disambiguate abbreviations as
being sentence-final or not, drawing information from: orthography of
left/right tokens, collocation of left/right tokens and frequency of
right token as sentence starter.

Tested on sections 03-05 of the WSJ portion of the Penn Treebank - error
rate of 1.65%. It is readily transferred to other languages and domains,
however with and error rate of 1.02% on Brown.

[Implemented](http://nltk.googlecode.com/svn/trunk/doc/api/nltk.tokenize.punkt-module.html)
in the NLTK.

## RASP

Briscoe, T., Carroll, J. and Watson, R. 2006. [The Second Release of the
RASP System](http://aclweb.org/anthology/P/P06/P06-4020.pdf). In
*Proceedings of the COLING/ACL 2006 Interactive Presentation Sessions*.

Uses deterministic finite-state rules based on the immediate context
(capitals, other punctuation etc.) to distinguish between periods used
to end sentences and those used to end abbreviations (including titles
and initials). The program assumes there is a sentence boundary wherever
there is a blank line, or whitespace preceded by valid sentence final
punctuation and followed by a capital letter. Jonathon has the source
code... anyone know Flex!?

## Satz

Palmer, D. and Hearst, M. 1997. *[Adaptive Multilingual Sentence
Boundary
Disambiguation](http://aclweb.org/anthology/J/J97/J97-2002.pdf)*.
Computational Linguistics 23(2).

Uses estimates of part of speech preceeding/following punctuation marks
as input to supervised machine learning. Part of speech decisions made
from a lexicon. Unable to find source/executable. Reports error rate of
1.0% on the WSJ portion of ACL/DCI.

## Splitta

Gillick, D. 2009. [Sentence Boundary Detection and the Problem with the
U.S.](http://aclweb.org/anthology/N/N09/N09-2061.pdf) In *Proceedings of
NAACL HTL 2009: Short Papers*.

A straightforward approach using support vector machines and features of
the words to the left (L) and right (R) of a period: word L; word R;
length of L; whether R is capitalised; the frequency of L without a
period; the frequency of uncapitalised R; the bigram LR; and the
capitalisation of R given the word L.

Despite the simplicity there are strong results: 0.25% error rate on
WSJ. This was achieved using 42,317 sentences for training. One concern
however - it seems that only periods are considered ambiguous, hence
cases such as in the reported speech example above will not be counted
in the evaluation. Perhaps this goes someway to explaining the seemingly
strong performance? Though perhaps not - other systems such as Satz also
seems primarily concerned with periods.

Source available [online](http://code.google.com/p/splitta/).

## Stanford CoreNLP

Only the [usage](http://nlp.stanford.edu/software/corenlp.shtml) is
documented, but seems to rely on sets of (1) acceptable sentence
boundary tokens; (2) tokens commonly following sentence boundaries; and
(3) sentence boundary tokens to ignore. A major advantage is that it
returns sentences with character offsets pointing back to the source
text.

# Related Work

Baldwin, T. and Joseph, M. P. A. K. 2009. [Restoring Punctuation and
Casing in English
Text](http://www.springerlink.com/content/v825m06653421808/fulltext.pdf).
In Lecture Notes in Computer Science, Volume 5866/2009.
<update date omitted for speed>{% endraw %}