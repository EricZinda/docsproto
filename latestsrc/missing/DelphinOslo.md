{% raw %}# DELPH-IN at the University of Oslo

The Oslo Machine Translation Research Group is part of the [Department
of Nordic Studies and Linguistics](http://www.hf.uio.no/inl) at the
[University of Oslo](http://www.uio.no) (UiO). The group is the
co-ordinator of the national [LOGON initiative](http://www.emmtee.net),
a five-year basic research project working towards high-quality
Norwegian -- English machine translation. The LOGON architecture
incorporates both *deep* LFG and HPSG grammars, more *shallow* NLP
components (including a PoS tagger, chunker, and NE recognizer), as well
as stochastic processes for disambiguation and robustness at all
processing levels. The group currently has seven members, of which four
are graduate students, and participates in an array of national and
international training and research initiatives.

One of the central research questions in LOGON is on the utility of
current language technology for machine translation, as the project is
essentially assembling its translation pipeline from general-purpose NLP
resources, many of them from the DELPH-IN repository. While Norwegian
analysis is accomplished using the (proprietary) LFG resource NorGram,
the transfer and English realization components are both open-source.
LOGON adopts a semantic transfer approach and uses MRS as its meaning
representation and interface language. The transfer module was realized
as a general-purpose MRS rewriting engine (in most respects a
generalization of the older \`munging' machinery available in the LKB)
and is publicly available. Target language realization uses the [LinGO
English Resource Grammar](http://www.delph-in.net/erg/) (ERG) and the
generation component in the LKB. In close collaboration with partners at
Sussex, Stanford, and Cambridge Universities, the LKB generator was
significantly improved in its efficiency and robustness for use in
LOGON. On-going research at UiO revolves around aspects of
(cross-linguistic) meaning representation in MRS, the acquisition of
transfer knowledge, and further refinements of the English realization
module (including work on the LinGO ERG and the underlying software). A
particular focus in this second phase of the LOGON project (as of early
in 2005) is on stochastic disambiguation in all three phases of the MT
pipeline.
<update date omitted for speed>{% endraw %}