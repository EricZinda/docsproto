{% raw %}# Cross-Domain Experimentation and Parser Adaptation

Main topics of this discussion:

- characterize domain/genre
- error analysis
- grammar adaptation
- model adaptation

Domain and genre adaptation of PET parser is required.

First of all, the clear definition of the terms domain and genre should
be formulated. One of the articles where authors operate with these
terms is (Wolters and Kirsten, 1999).

The next question is which part of the parser to adapt: statistical
elements or the grammar?

There is a related work about supertagging. However in the current
implementation the supertagger is not used for disambiguation.
Disambiguation or possibly pre-processing can help in adaptation. Can
supertagger contribute to accuracy? Currently we only produce pruning of
the lexical types and lexical rules (for tractability). Gold-standard
übertags could massively reduce ambiguity.

It is necessary to look at the errors on the in- and out-of-domain data
separately and find out whether we have problems related to the lexical
level or to the constructions.

ØVRELID and SKJÆRHOLT (2012) looked at clustering (Brown clusters) for
Web Data.

It would be beneficial to quantify the distinction between genre and
domain. Some relevant research is reported in ["Large-Scale Syntactic
Processing: Parsing the Web" 2009 JHU CLSP
Workshop](http://www.cl.cam.ac.uk/~ah433/jhu09.pdf). How to define how
different the domains are and the styles are? Plank and van Noord (2011)
talk about typical words for particular domains.

Supertagger and ubertagger could probably be elaborated to achieve
higher accuracy. E.g. improvements could be introduced for unknown words
handling (now unknown words are assigned a generic label). We could use
some more elaborate model for unknown words. Domain and genre may
require different types of adaptations.

Candidate types of adaptation:

- Grammar adaptation (e.g. Foster et al. (2011); Baldwin et al.
(2013))
- pre-processing (we must keep the raw text)

In some cases grammar adaptation and preprocessing are close to each
other and it does not matter where to make the change. For example,
"because" = "coz" - first to change it in the text or to add "coz" to
the lexicon. Current ERG version already contains "coz" lexical item. If
the "Coz" is capitalized, the grammar thinks it is either unknown word
or a generic entity (unknown word), so we get more possible analyses and
then the statistical ranker decides which tree to choose.

Candidate statistical modules for adaptation:

- PoS-tagger
- ubertagger
- dependency parser (for pruning the search space of HPSG parser)
- parse ranker

# Aims and Questions

**Aim:** to use the WDC to explore differences and similarities between
domains and genres, to find ways of automatically detecting domain or
genre similarity, and to use this information to adapt the PET parser
for better performance over a detected domain or genre.

## Questions

- What is 'domain'? What is 'genre'? Can we quantify these concepts in
a way useful for parsing?
- What are useful ways of comparing corpora, for the purposes of
parsing?
- What are the common challenges for accurate parsing, and are these
distributed uniformly across text types?
- How do we measure parser accuracy?

# References

(see [WeSearch/Adaptation/Background](https://blog.inductorsoftware.com/docsproto/missing/WeSearch_Adaptation_Background))

- Maria Wolters and Mathias Kirsten. Exploring the Use of Linguistic
Features in Domain and Genre Classification. EACL'99

<http://acl.ldc.upenn.edu/E/E99/E99-1019.pdf>

- Baldwin et al. How Noisy Social Media Text, How Diffrnt Social Media
Sources?

<http://aclweb.org/anthology//I/I13/I13-1041.pdf>

- Barbara Plank, Gertjan van Noord: Effective Measures of Domain
Similarity for Parsing. ACL 2011

<http://aclweb.org/anthology//P/P11/P11-1157.pdf>

- Lilja ØVRELID and Arne SKJÆRHOLT. Lexical categories for improved
parsing of web data

<http://aclweb.org/anthology/C/C12/C12-2088.pdf>

Last update: 2014-03-06 by RebeccaDridan [[edit](https://github.com/delph-in/docs/wiki/WeSearch_Adaptation/_edit)]{% endraw %}