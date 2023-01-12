{% raw %}# Background

In [WeSearch](https://blog.inductorsoftware.com/docsproto/garage/WeSearch), we are exploring the use of semantic
technologies, in particular RDF triple stores, to search potentially
very lage collections of semantic annotations.

In the DELPH-IN context, there are three relevant types of semantic
representations: (a) Minimal Recursion Semantics (MRS); (b) Elementary
Dependency Structures (EDS); and (c) DELPH-IN MRS-Derived Bi-Lexical
Dependencies (DM). Of these, MRS is arguably the most interesting, both
in terms of completeness (EDS and DM are derived, simplified
representations) and design choices in mapping MRS elements to RDF.

Unlike the full MRS, its reduction to the EDS level of representation
(described in more detail on the [EdsTop](https://blog.inductorsoftware.com/docsproto/tools/EdsTop) page) maps trivially
onto RDF graphs. The same holds for the DM format, which is part of the
SemEval 2014 Task 8 on [Broad-Coverage Semantic Dependency
Parsing](http://alt.qcri.org/semeval2014/task8/), where there already is
an exploratory [search interface](http://wesearch.delph-in.net/sdp/) for
DM graphs.

# MRS Terminology

Following is an MRS example for the sentence *Kim promised his manager
to sing.* There are multiple exchange formats for MRS, and here we use
what is called the *simple* serialization (the format deployed by, among
others, [WikiWoods](https://blog.inductorsoftware.com/docsproto/garage/WikiWoods) and [DeepBank](https://blog.inductorsoftware.com/docsproto/garage/DeepBank) distributions,
owing to its premiere balance of human and computer readability):

      [ LTOP: h1
        INDEX: e3 [ e SF: PROP TENSE: PAST MOOD: INDICATIVE PROG: - PERF: - ]
        RELS: < [ proper_q_rel<0:3>
                  LBL: h4 ARG0: x6 [ x PERS: 3 NUM: SG IND: + ] RSTR: h5 BODY: h7 ]
                [ named_rel<0:3>
                  LBL: h8 ARG0: x6 CARG: "Kim" ]
                [ "_promise_v_1_rel"<4:12>
                  LBL: h2 ARG0: e3 ARG1: x6 ARG2: x10 [ x PERS: 3 NUM: SG IND: + ] ARG3: h9 ]
                [ def_explicit_q_rel<13:16>
                  LBL: h11 ARG0: x10 RSTR: h13 BODY: h12 ]
                [ pronoun_q_rel<13:16>
                  LBL: h17
                  ARG0: x15 [ x PERS: 3 NUM: SG GEND: M PRONTYPE: STD_PRON ]
                  RSTR: h18
                  BODY: h19 ]
                [ pron_rel<13:16>
                  LBL: h20
                  ARG0: x15 ]
                [ poss_rel<13:16>
                  LBL: h14 ARG0: e16 [ e SF: PROP TENSE: UNTENSED MOOD: INDICATIVE PROG: - PERF: - ] ARG1: x10 ARG2: x15 ]
                [ "_manager_n_1_rel"<17:25>
                  LBL: h14 ARG0: x10 ]
                [ "_sing_v_1_rel"<29:34>
                  LBL: h21 ARG0: e22 [ e SF: PROP-OR-QUES TENSE: UNTENSED MOOD: INDICATIVE PROG: - PERF: - ] ARG1: x6 ARG2: p23 ] >
        HCONS: < h1 qeq h2 h5 qeq h8 h9 qeq h21 h13 qeq h14 h18 qeq h20 > ]

To establish some terminology, an MRS is a four-tuple comprised of a
*top* handle, an *index*, a bag (i.e. multi-set) of *elementary
predications* (EPs), and a bag of *handle constraints*; each elementary
predication has a *label*, *predicate*, set of *role–argument* pairs,
and a set of (constant) *parameters*; although this is not exemplified
in the above, multiple predications can share the same label, i.e. these
do not function as unique identifiers. Predicates and role labels are
case-insensitive strings; parameters are case-sensitive strings. Labels
and role arguments are *variables*, which come in three basic types:
labels are of type ‘h’ (for handle or hole), events (prototypically
associated with verbal semantics) are of type ‘e’, and instances
(prototypically the semantics associated with nominals) are of type ‘x’.
In addition to these most specific variable types, there are
underspecifications as follows: ‘i’ (for individual) is a supertype of
‘e’ and ‘x’; ‘p’ (the half-way mark in the alphabet between ‘h’ and ‘x’)
is a supertype of labels and instances; and ‘u’ (for unspecific or maybe
unbound) is a supertype of all of the above. Variables can have
*variable properties*, which have the form of property–value pairs;
property labels are case-insensitive strings, and values are strings
that draw on a small but language-specific pre-defined hierarchy.
Finally, elementary predications can carry *link* information, relating
pieces of semantics to pieces of the underlying utterance; in our
example above, links are coded as so-called characterization ranges,
i.e. sub-string indices.

Consider the EP associated with the proper name *Kim*:

      [ named_rel<0:3>
        LBL: h8 ARG0: x6 CARG: "Kim" ]

This elementary predication has label ‘h8’ and predicate ‘named’ (by
convention, MRS-internally predicate symbols always have the suffix
‘\_rel’, but this is most commonly stripped in downstream processing);
its surface link is the character range ‘&lt;0:3&gt;’, i.e. the
sub-string starting at character position zero, and ending before
character position three. The EP has one argument, labeled ‘ARG0’, whose
value is the variable ‘x6’, and one parameter, labeled ‘CARG’, with
value ‘Kim’. As shown here, ‘x6’ appears to not carry variable
properties, but looking at the first occurence of the variable in the
full example MRS above, it actually has three properties, labeled ‘NUM’,
‘PERS’, and ‘IND’.

Returning to the full MRS above, and completing our terminological
walk-through ‘h1’ is designated as the top handle, and ‘e3’ as the
index. Finally, there are five *handle constraints*, each a binary
relation holding between two labels. The only type of constraint used in
the ERG is ‘=q’ (equal modulo quantifier insertion), and handle
constraints can only be expressed in terms of label-type variables that
actually occur in the MRS.

With several different types of components comprising the complete MRS,
there are a number of design decisions to be made in mapping these
structures onto an RDF ontology. Before turning to these choices,
consider the following example query, which is taken from the on-going
ERG Semantic Documentation project (see the pages
[ErgSemantics](https://blog.inductorsoftware.com/docsproto/erg/ErgSemantics) and
[ErgSemantics/RelativeClauses](https://blog.inductorsoftware.com/docsproto/missing/ErgSemantics_RelativeClauses)):

      h:*[ARG0 x]
      h:*[ARG0 e {TENSE tensed}]

This query (also called the ‘fingerprint’ of the semantics associated
with relative clauses in the ERG) is meant to match MRSs where there are
(at least) two EPs that have the same label (variable ‘h’), and where
the first EP has (at least) a role ‘ARG0’, with a value of type ‘x’, and
the second EP also has (at least) a role ‘ARG0’, but with its value
constrained to be of type ‘e’ and containing (at least) the variable
property ‘TENSE’ with a value compatible with ‘tensed’ (which in the ERG
inventory of variable properties is a supertype of, among others,
‘past’, ‘pres’(ent), ‘fut’(ure).

# MRSs in RDF

Given different types of components in an MRS, an embedding into RDF
will require different types of resources (classes), minimally (it would
seem) *predication*, *variable*, and *property*. The MRS hierarchy of
variable types we should be able to model as sub-classes, e.g.

      @prefix mrs: <http://www.delph-in.net/rdf/mrs#>.
    
      mrs:predication a rdfs:Class.
      mrs:variable a rdfs:Class.
      mrs:property a rdfs:Class.
    
      mrs:i a rdfs:Class; rdfs:subClassOf mrs:variable.
      mrs:p a rdfs:Class; rdfs:subClassOf mrs:variable.
      mrs:h a rdfs:Class; rdfs:subClassOf mrs:p.
      mrs:x a rdfs:Class; rdfs:subClassOf mrs:i, mrs:p.
      mrs:e a rdfs:Class; rdfs:subClassOf mrs:i.

Similar to the EDS and DM worlds, roles and parameters can be
represented as properties of predications (seeing as there is a small
and fixed inventory of role labels), and the same approach should hold
for MRS variable properties.

      mrs:role a rdf:Property.
      mrs:LABEL a mrs:role.
      mrs:ARG0 a mrs:role.
      ...
    
      mrs:role rdfs:domain mrs:predication; rdfs:range mrs:variable.
      mrs:LABEL rdfs:range mrs:h.
    
      mrs:parameter a rdf:Property.
      mrs:parameter rdfs:domain mrs:predication; rdfs:range rdfs:Literal.
      mrs:CARG a mrs:parameter.

Finally, handle constraints may just map to properties (where there
could in principle be room for other types of constraints than just
‘=q’):

      mrs:constraint a rdf:Property.
      mrs:qeq a rdf:Property; rdfs:subPropertyOf mrs:constraint;
    
      mrs:qeq rdfs:domain mrs:h; rdfs:range mrs:h.

Last update: 2015-11-19 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/WeSearch_Rdf/_edit)]{% endraw %}