{% raw %}Working out the lay of the land.

## Corpus Differences

- Maria Wolters and Mathias Kirsten. Exploring the Use of Linguistic
Features in Domain and Genre Classification. EACL'99
  
  <http://acl.ldc.upenn.edu/E/E99/E99-1019.pdf>
  
  - "When it \[genre\] is not used synonymously with the terms
"register" or "style", genre is defined on the basis of
non-linguistic criteria." (eg, the author/speaker purpose). I
think we do want synonymy with register or style? They mostly
looked at differences in tag frequency (in German texts).
- Barbara Plank, Gertjan van Noord: Effective Measures of Domain
Similarity for Parsing. ACL 2011
  
  <http://aclweb.org/anthology//P/P11/P11-1157.pdf>
  
  - Different granularity. For each test article, found 'most
similar' articles in training data and re-trained. Topic
modelling based representation (from MALLET) worked slightly
better than word based. Similarity functions tested:
  - Kullback-Leiber divergence
  - Jensen-Shannon divergence (smoothed, symmetric approximation of
KL divergence)
  - skew divergence
  - cosine
  - euclidean
  - variational (Manhattan)
  - Renyi divergence
  
  Claim to show automatic selection better than human labelling, but
only over WSJ (ie not always obvious domain diffs). In domain
adaptation set-up, in-domain data does better than automatic
selection, up to the amount of data available (but not by much -
their selection works quite well). Similar accuracies from very
different selections of articles from WSJ.
- Bonnie Webber. **Genre distinctions for discourse in the Penn
TreeBank** <http://aclweb.org/anthology//P/P09/P09-1076.pdf>
- Tom Lippincott; Diarmuid Ó Séaghdha; Lin Sun; Anna Korhonen.
**Exploring variation across biomedical subdomains**
<http://aclweb.org/anthology//C/C10/C10-1078.pdf>
- Sujith Ravi; Kevin Knight; Radu Soricut. **Automatic Prediction of
Parser Accuracy** <http://aclweb.org/anthology//D/D08/D08-1093.pdf>
- Satoshi Sekine. 1997. The Domain Dependence of Parsing
  
  <http://aclweb.org/anthology/A/A97/A97-1015.pdf>
  
  - Looked at cross-entropy between Brown genres, using
probabilities of PCFG rules. Shows fairly wide variation in
frequent subtrees for each domain.
- Proceedings of the 2010 Workshop on Domain Adaptation for Natural
Language Processing
  
  <http://aclweb.org/anthology//W/W10/W10-26.pdf>
  
  - particularly Vincent Van Asch; Walter Daelemans. **Using Domain
Similarity for Performance Estimation**
<http://aclweb.org/anthology//W/W10/W10-2605.pdf>
- Daniel Gildea. Corpus Variation and Parser Performance
  
  <http://aclweb.org/anthology//W/W01/W01-0521.pdf>
  
  - train WSJ, test WSJ: 86.35 F1, train WSJ, test Brown: 80.65 F1
(&lt;=40 words). Lexical bigrams take up largest part of model,
only add 0.5 F1 to WSJ, don't help Brown at all. Most
significant bigrams (as judged by the pruning mechansim) for WSJ
are very specific and all in NPs: New York, Stock Exchange, vice
president etc, but for Brown, very generic: It was, Of course,
had been. Pointer to earlier work (Roland & Jurafsky, 1998,
Roland et al, 2000) showing verb subcat varies much less in WSJ
than Brown. Conclusion: the standard WSJ task seems to be
simplified by its homogenous style.
- Douglas Roland and Daniel Jurafsky. 1998. How Verb Subcategorization
Frequencies are Affected by Corpus Choice.
  
  <http://aclweb.org/anthology//P/P98/P98-2184.pdf>
  
  - "The probabilistic relation between verbs and their arguments
plays an important role in modern statistical parsers and
supertaggers..." There's a difference in verb subcat frequencies
between sentences elicited for psych experiments and those in
corpora. Most are due to discourse effects - single sentences
have different characteristics to those in running text. This
doesn't apply to most of our corpora, but possibly
SemCor. And Tanaka, if we ever go that way. Other
differences were often due to verb sense frequency differences.
- Roland et. al. 2000. Verb Subcategorization Frequency Differences
between Business-News and Balanced Corpora: The Role of Verb Sense
  
  <http://aclweb.org/anthology//W/W00/W00-0905.pdf>
  
  - "...while the BNC uses include more weather uses... We are
investigating whether this is a result of the BNC discussing
weather more often, or..." Only looking at running text this
time, differences are mostly due to subtle verb sense
differences, even when controlling for majority (major) sense.
WSJ most often different in transivity (where differences exist)
to BNC and Brown, but there were some exceptions.
- Adam Kilgarriff. 2001. Comparing Corpora.
  
  <http://www.kilgarriff.co.uk/Publications/2001-K-CompCorpIJCL.pdf>
  
  - Different ways of looking at corpora:
  - which words are characteristic of a text/corpus:
    - chi-squared
    - Mann-Whitney (Wilcoxon) ranks test
    - t-test
    - MI
    - log-likelihood
    - Fisher's exact test (what log-likelyhood is approximating?)
    - TF.IDF
  - how similar are two corpora? how homogeneous is a corpus?
    - uses known-similarity corpora to evaluate similarity
measures
    - Spearman rank correlation co-efficient
    - chi-squared
    - perplexity
  
  Low-frequency and high-frequency (closed-class) words should
generally be treated separately, since they have very different
statistical properties.
- Adam Kilgarriff. 2012. Getting to know your corpus
  - <http://www.sketchengine.co.uk/documentation/raw-attachment/wiki/AK/Papers/Kilgarriff_TSD2012.pdf>
- Adam Kilgarriff. 2005. Language is never, ever, ever random.
  - <http://rex.dridan.com/protected/Kilgarriff_2005.pdf>
- Stefan Th.Gries
  - <http://www.linguistics.ucsb.edu/faculty/stgries/research/2005_STG_NullHypSignTesting_CLLT.pdf>

## UGC

- Baldwin et al. How Noisy Social Media Text, How Diffrnt Social Media
Sources?
  
  <http://aclweb.org/anthology//I/I13/I13-1041.pdf>
  
  - Use forum, blog and wiki, as in WDC, plus Twitter, comments and
BNC. All preprocessed with TweetNLP, which is probably not good
for the non-twitter data. Language mix not so relevant to us,
except as a footnote. OOV % against aspell, but not training
data. We could do both. Text normalisation (learning standard
forms and replacing) helped with OOV in twitter and comments,
but not much in the other text types. Grammaticality tested by
parsing with ERG, and looking at unparsed, root conditions and
full vs fragment. Unparsed seems much too high. Beauty and the
Beast style analysis for 100 unparseable sentences per corpus.
Says 59% of the 26% of unparsed from Wiki caused by grammar
gaps? Chi-squared and language models for intra and inter corpus
similarity.
- Jennifer Foster; Ozlem Cetinoglu; Joachim Wagner; Joseph Le Roux;
Joakim Nivre; Deirdre Hogan; Josef van Genabith. **From News to
Comment: Resources and Benchmarks for Parsing the Language of Web
2.0** <http://aclweb.org/anthology//I/I11/I11-1100.pdf>
- Jennifer Foster, Ozlem Cetinoglu, Joachim Wagner and Josef van
Genabith, 2011. **Comparing the Use of Edited and Unedited Test in
Parser Self-Training**
<http://aclweb.org/anthology//W/W11/W11-2925.pdf>

## Domain Adaptation

- Laura Rimell and Stephen Clark. 2008. **Adapting a
Lexicalized-Grammar Parser to Contrasting Domains.**
<http://aclweb.org/anthology//D/D08/D08-1050.pdf>
- Lilja ØVRELID and Arne SKJÆRHOLT. Lexical categories for improved
parsing of web data
  
  <http://aclweb.org/anthology/C/C12/C12-2088.pdf>
- David McClosky; Eugene Charniak; Mark Johnson. **Automatic Domain
Adaptation for Parsing**
<http://aclweb.org/anthology//N/N10/N10-1004.pdf>
- Barbara Plank and Khalil Sima’an. Subdomain Sensitive Statistical
Parsing using Raw Corpora
  
  <http://www.lrec-conf.org/proceedings/lrec2008/pdf/120_paper.pdf>
  
  - Build a language model on a raw sub-domain corpus. Use the
statistics to weight the training corpus sentences to train
sub-domain specific corpora. Calculate divergence of each word
in sentence with respect to each sub-domain. Use to select
parser. Else, use on trees from each sub-domain, pick best tree.
Oracle selection gets small (1 point) improvement over always
using baseline parser. Parser selection gets miniscule
improvement.
- Hal Daume III. 2007. Frustratingly Easy Domain Adaptation
  
  <http://aclweb.org/anthology//P/P07/P07-1033.pdf>
  
  - Use three variants of each feature: from target domain, source
domain and general. Allows learner to set weights separately.
Method leads to a regulariser term in the learner proportional
to the difference between source and target weights for a
feature, so we minimise this difference unless information says
otherwise.

Last update: 2014-09-04 by RebeccaDridan [[edit](https://github.com/delph-in/docs/wiki/WeSearch_Adaptation_Background/_edit)]{% endraw %}