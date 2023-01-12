{% raw %}# Background

As in previous years, the Conference on Natural Language Learning
([CoNLL](http://www.cnts.ua.ac.be/conll/)) defines a [shared
task](http://www.inf.u-szeged.hu/rgai/conll2010st/), essentially an
invitation to research groups to compete in solving a well-defined
problem. The 2010 shared task is on finding so-called hedges (linguistic
expressions indicating various degrees on uncertainty) and determining
their scopes. This tasks is similar in some respects to Task 3 in the
2009 BioNLP [shared
task](http://www-tsujii.is.s.u-tokyo.ac.jp/GENIA/SharedTask/), and it
seems likely that structural syntactic or semantic information will be
useful in solving this problem.

The CoNLL shared task is sub-divided into two parts: Task 1, on
classifying complete utterances as to whether or not they contain
speculation, and Task 2 on determining the scope of actual hedges; the
way Task 2 is set up, it also subsumes the task of finding the actual
hedge cues. For the use of DELPH-IN technology (and other parsers), Task
2 appears most relevant. Although the CoNLL shared task description
mentions some use of Wikipedia text, it appears that most of the
training data (maybe all of it, for Task 2) is drawn from the
bio-medical domain, specifically the
[BioScope](http://www.inf.u-szeged.hu/rgai/bioscope) corpus, a resource
annotated for hedge cues and scopes.

As sub-set of DELPH-IN members plan to participate in this shared task,
possibly through one joint submission or maybe als as several
submissions, by individual groups or sub-sets of people. At present,
these include Lilja Øvrelid, Stephan Oepen, and Erik Velldal (at Oslo),
Tim Baldwin, Andrew MacKinlay, and David Martinez (at Melbourne), Yi
Zhang (at Saarbrücken), and Dan Flickinger (at Stanford). While we are
just getting going (in mid-January 2010), more collaborators would be
welcome, please contact Stephan for details.

# Relevant Resources

- [BioScope](http://www.inf.u-szeged.hu/rgai/bioscope) corpus
- [GENIA](http://www-tsujii.is.s.u-tokyo.ac.jp/GENIA) project

# Reading List

- [BioScope Annotation
Guidelines](http://www.inf.u-szeged.hu/rgai/project/nlp/bioscope/Annotation%20guidelines2.1.pdf)
(v.2.1)
- Veronika Vincze, György Szarvas, Richárd Farkas, György Mora, and
János Csirik
  
  (2008). [The BioScope Corpus: Biomedical Texts Annotated for
Uncertainty, Negation and their
Scopes.](http://www.biomedcentral.com/1471-2105/9/S11/S9)
- Andrew MacKinlay, David Martinez and Timothy Baldwin (2009). A
Parser-based Approach to Detecting Modification of Biomedical
Events.
- Roser Morante and Walter Daelemans (2009)
  
  [Learning the Scope of Hedge Cues in Biomedical
Texts.](http://www.aclweb.org/anthology/W/W09/W09-1304.pdf)
- Viola Ganter and Michael Strube (2009).
  
  [Finding Hedges by Chasing Weasels: Hedge Detection Using Wikipedia
Tags and Shallow Linguistic
Features.](http://www.aclweb.org/anthology/P/P09/P09-2044.pdf)
- Halil Kilicoglu and Sabine Bergler (2009).
  
  [Syntactic Dependency Based Heuristics for Biological Event
Extraction.](http://www.aclweb.org/anthology/W/W09/W09-1418.pdf)
- Halil Kilicoglu and Sabine Bergler (2008).
  
  [Recognizing Speculative Language in Biomedical Research Articles: A
Linguistically Motivated
Perspective.](http://www.biomedcentral.com/content/pdf/1471-2105-9-S11-S10.pdf)
- Ben Medlock and Ted Briscoe (2007).
  
  [Weakly Supervised Learning for Hedge Classification in Scientific
Literature.](http://acl.ldc.upenn.edu/P/P07/P07-1125.pdf)

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/HedgeTop/_edit)]{% endraw %}