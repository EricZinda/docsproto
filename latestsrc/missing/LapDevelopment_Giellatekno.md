{% raw %}# Background

In wrapping the UiT Giellatekno (GT) pipeline for Sami segmentation,
tokenization, morphological analysis, and dependency parsing, we need to
(a) decide how many individual steps of processing to distinguish (from
the LAP point of view) and (b) how to map the input and output data from
the GT pipeline to LAF-compatible annotations.

Following is a sample invocation (against the LAP Tree), which was
originally suggested by Trond Trosterud of UiT:

      cat $LAPTREE/gt/etc/test.txt \
      | $LAPTREE/perl/lap/perl $LAPTREE/gt/script/preprocess --abbr=$LAPTREE/gt/sme/abbr.txt \
      | $LAPTREE/hfst/lap/hfst-lookup $LAPTREE/gt/sme/analyser-gt-norm.hfstol \
      | $LAPTREE/perl/lap/perl $LAPTREE/gt/script/lookup2cg | sed 's/0.000000//g' \
      | $LAPTREE/vislcg3/lap/vislcg3 -g $LAPTREE/gt/sme/disambiguation.cg3 \
      | $LAPTREE/vislcg3/lap/vislcg3 -g $LAPTREE/gt/sme/functions.cg3 \
      | $LAPTREE/vislcg3/lap/vislcg3 -g $LAPTREE/gt/sme/dependency.cg3

It probably makese sense to conceptually distinguish the following
layers:

- \(a\) (maybe normalization and) tokenization (preprocess)
  
  \(b\) morphological analysis (hfst-lookup)
  
  \(c\) segmentation and morpho-syntactic tagging (disambiguation.cg3)
  
  \(d\) grammatical function analysis (functions.cg3)
  
  \(e\) dependency parsing (dependency.cg3)

# Sample Input

    Dán skábma čuojaha Mari Boine ovttas Kai Sombyn ja Ája joavkkuin. Go beakkán artistta guovttos čuojaheaba oktasaš konsearttaid vuosttaš gearddi, de šaddaba garvit sámi báikkiid gos girkuin lea juoigangielddus. Dattetge illudeaba sakka ovttasbargui.

# Sample Intermediate Output (After Morphological Analysis)

    "<Dán>"
             "dát" Pron Dem Sg Loc Attr
             "dát" Pron Dem Sg Ill Attr
             "dát" Pron Dem Sg Acc
             "dát" Pron Dem Sg Gen
    "<skábma>"
             "skábma" N Sg Nom
    "<čuojaha>"
             "čuodjat" V* IV* Der/h V TV Ind Prs Sg3
             "čuojahit" V TV Ind Prs Sg3
    "<Mari>"
             "Mari" N Prop Sem/Fem Sg Acc
             "Mari" N Prop Sem/Fem Sg Nom
             "Mari" N Prop Sem/Fem Attr
             "Mari" N Prop Sem/Fem Sg Gen
    "<Boine>"
             "Boine" N Prop Sem/Sur Sg Gen
             "Boine" N Prop Sem/Sur Sg Nom
             "Boine" N Prop Sem/Sur Sg Acc
    "<ovttas>"
             "ovttas" N Coll Sg Nom
             "ovttastit" V TV Imprt ConNeg
             "ovttastit" V TV Ind Prs ConNeg
             "ovttastit" V TV Imprt Sg2
             "ovttas" Adv
             "okta" Num Sg Loc
             "ovttastit" V TV VGen
    "<Kai>"
             "Kai" N Prop Sem/Mal Sg Nom
             "Kai" N Prop Sem/Mal Sg Gen
             "Kai" N Prop Sem/Mal Attr
             "Kai" N Prop Sem/Mal Sg Acc
    "<Sombyn>"
             "Somby" N Prop Sem/Sur Ess
    "<ja>"
             "ja" CC
    "<Ája>"
             "Ája" N Prop Sem/Org Sg Gen
             "ája" N Sg Nom
             "Ája" N Prop Sem/Org Sg Nom
             "Ája" N Prop Sem/Org Sg Acc
    "<joavkkuin>"
             "joavku" N Pl Loc
             "joavku" N Sg Com
    "<.>"
             "." CLB
    "<Go>"
             "go" Pcle Qst
             "go" CS
    "<beakkán>"
             "beakkán" A Sg Gen
             "beakkán" A Sg Nom
             "beakkán" A Sg Acc
             "beaggit" V IV Ind Prs Sg1
             "beakkán" A Attr
    "<artistta>"
             "artista" N Sg Gen
             "artista" N Sg Acc
    "<guovttos>"
             "guovttos" N Coll Sg Loc
             "guovttos" N Coll Sg Gen PxSg3
             "guovttos" N Coll Sg Nom
             "guovttos" N Coll Sg Acc PxSg3
    "<čuojaheaba>"
             "čuojahit" V TV Ind Prs Du3
             "čuodjat" V* IV* Der/h V TV Ind Prs Du3
    "<oktasaš>"
             "oktasaš" A Attr
             "oktasaš" A Sg Nom
    "<konsearttaid>"
             "konsearta" N Pl Acc
             "konsearta" N Pl Gen
    "<vuosttaš>"
             "vuosttaš" A Ord Sg Nom
             "vuosttaš" A Ord Attr
    "<gearddi>"
             "gearddi" Adv
             "geardi" N Sg Gen
             "geardi" N Sg Acc
    "<,>"
             "," CLB
    "<de>"
             "de" Adv
    "<šaddaba>"
             "šaddat" V IV Ind Prs Du3
    "<garvit>"
             "garvit" V TV Inf
             "garvit" V TV Ind Prs Pl1
             "garvit" V* TV* Der/NomAg N Pl Nom
             "garvit" V TV Imprt Pl2
    "<sámi>"
             "sápmi" N Sg Acc
             "sápmi" N Sg Gen
    "<báikkiid>"
             "báiki" N Pl Gen
             "báiki" N Pl Acc
    "<gos>"
             "gos" Adv
    "<girkuin>"
             "girku" N Sg Com
             "girku" N Pl Loc
    "<lea>"
             "leat" V IV Ind Prs Sg3
    "<juoigangielddus>"
             "juoigan#gieldu" N Sg Acc PxSg3
             "juoigan#gieldu" N Sg Loc
             "juoigan#gieldu" N Sg Gen PxSg3
             "juoigan#gielddus" N Sg Nom
    "<.>"
             "." CLB
    "<Dattetge>"
             "dattetge" Adv
    "<illudeaba>"
             "illudit" V IV Ind Prs Du3
    "<sakka>"
             "sakka" Adv
    "<ovttasbargui>"
             "ovttasbargu" N Sg Ill
             "ovttasbargat" V* IV* Der/PassS V IV Ind Prt Sg3
    "<.>"
             "." CLB

# Sample Output

    "<Dán>"
            "dát" Pron Dem Sg Acc @OBJ> #1->3
    "<skábma>"
            "skábma" N Sg Nom @SUBJ> #2->3
    "<čuojaha>"
            "čuojahit" V TV Ind Prs Sg3 @FMV #3->0
    "<Mari>"
            "Mari" N Prop Sem/Fem Attr @>N #4->5
    "<Boine>"
            "Boine" N Prop Sem/Sur Sg Nom @<SUBJ #5->3
    "<ovttas>"
            "ovttas" Adv @<ADVL #6->3
    "<Kai>"
            "Kai" N Prop Sem/Mal Attr @>N #7->8
    "<Sombyn>"
            "Somby" N Prop Sem/Sur Ess @<OPRED #8->1
    "<ja>"
            "ja" CC @CNP #9->8
    "<Ája>"
            "Ája" N Prop Sem/Org Sg Gen @>N #10->11
    "<joavkkuin>"
            "joavku" N Sg Com @<ADVL #11->3
    "<.>"
            "." CLB #12->3
    
    "<Go>"
            "go" CS @CVP #1->5
    "<beakkán>"
            "beakkán" A Attr @>N #2->3
    "<artistta>"
            "artista" N Sg Acc @OBJ> #3->5
    "<guovttos>"
            "guovttos" N Coll Sg Nom @SUBJ> #4->5
    "<čuojaheaba>"
            "čuojahit" V TV Ind Prs Du3 @FS-ADVL> #5->13
    "<oktasaš>"
            "oktasaš" A Attr @>N #6->7
    "<konsearttaid>"
            "konsearta" N Pl Gen @>N #7->9
    "<vuosttaš>"
            "vuosttaš" A Ord Attr @>N #8->9
    "<gearddi>"
            "geardi" N Sg Gen @<ADVL #9->5
            "gearddi" Adv @<ADVL #9->5
    "<,>"
            "," CLB #10->1
    "<de>"
            "de" Adv @ADVL> #11->13
    "<šaddaba>"
            "šaddat" V IV Ind Prs Du3 @FAUX #12->0
    "<garvit>"
            "garvit" V TV Inf @IMV #13->12
    "<sámi>"
            "sápmi" N Sg Gen @>N #14->15
    "<báikkiid>"
            "báiki" N Pl Acc @<OBJ #15->13
    "<gos>"
            "gos" Adv @ADVL> #16->18
    "<girkuin>"
            "girku" N Pl Loc @ADVL> #17->18
    "<lea>"
            "leat" V IV Ind Prs Sg3 @FS-<ADVL #18->13
    "<juoigangielddus>"
            "juoigan#gielddus" N Sg Nom <ext> @<SUBJ #19->18
    "<.>"
            "." CLB #20->12
    
    "<Dattetge>"
            "dattetge" Adv @ADVL> #1->2
    "<illudeaba>"
            "illudit" V IV Ind Prs Du3 @FMV #2->0
    "<sakka>"
            "sakka" Adv @>N #3->4
    "<ovttasbargui>"
            "ovttasbargu" N Sg Ill @<ADVL #4->2
    "<.>"

# Design Decisions

*Granularity*: Should steps (a) to (e) above be wrapped as a single
(complex) component, or each individually. We opt for the latter, to
enable users to only run parts of the pipeline and have access to the
corresponding intermediate analyses layers.

*Sequencing*: Unlike in analysis pipelines we have constructed earlier
(e.g. English dependency parsing), sentence segmentation in Giellatekno
only happens as a bi-product of step (c), i.e. morpho-syntactic
disambiguation. This should not cause problems in the LAP context,
however; step (a) only creates token regions and corresponding nodes;
steps (b) and (c) receive as their inputs the token sequences for a full
document (i.e. cannot expect to iterate over sentence regions); and step
(c) inserts multiple layers of annotation into LAP Store: in addition to
annotation nodes for morpho-syntactic analysis, it also creates regions
and corresponding nodes for sentence segments.

*Ambiguity*: Morphological analysis in Giellatekno (step (b), also often
called multi-tagging) creates ambiguous outputs, i.e. multiple possible
morpho-syntactic analyses per token. Because downstream processing may
need to refer back to one specific analysis (i.e. the part of speech and
morphological features used as the leaves of a parse tree), ambiguity
must be represented as a set of nodes, i.e. each individual
morpho-syntactic analysis establishes its own annotation node. This begs
the question of how to represent the relations among alternatives, i.e.
minimally an ordering relation (assuming an n-best list).

A related open question is how to represent the result of
disambiguation: Should the disambiguated layer of morpho-syntactic
analysis be represented as a sequence of (a) nodes that copy the lemma,
part of speech, and features from lower-level nodes; of (b) ‘meta’-nodes
that refer to those lower-level nodes that remain after disambiguation;
or (c), similarly, ‘meta’-nodes that mark lower-level nodes discarded in
disambiguation as invalid (at this layer)?

*Interpretation*: The CG3 output format appears designed for compactness
more than for explicitness. In wrapping Giellatekno (and similar tools),
we cannot avoid making explicit different types of annotation in LAP
Store. To do so, we have to work out the right level of interpretation
of the CG3 outputs, while not making explicit distinctions or additional
interpretation that is not required in the LAP context. For example, the
first two elements in each analysis represent the *lemma* and *part of
speech*; also, it seems fairly clear that tags like Sg or Nom are to be
interpreted as values for Number and Case, respectively; finally,
@&lt;SUBJ and \#19-&gt;18 represent a *function tag* and *dependency
head* assignment. Given parallelism to explicit distinctions in other
components, it is tempting to make explicit those properties marked in
italics (lemma, part of speech, function tag, dependency head), even
more so as the latter two only originate from later layers of analysis
(steps (d) and (e), respectively).

How much interpretation to apply to the remaining tags is more of an
open question, and possibly a ‘lazy’ approach is sufficient in LAP, viz.
merely recording a list of additional tags on the annotation nodes
created by step (b). This representation would seem somewhat parallel to
CoNLL-style, token-oriented formats common in dependency parsing, where
there is one column reserved for a list of feature–value pairs, where
valid feature and value names need not be pre-defined. However, in the
CG3 context, feature names are not spelled out, but presumably there is
an unambiguous association from unique values to corresponding features;
it seems undesirable to spell out such a component-specific mapping in
the wrapper—instead, it should ideally be declared as part of the
component metadata. Hence we will leave feature names implicit for now,
unless we encounter a more specific need in the LAP context.

Also, dependency analysis is technically different from the syntactic
dependency parsers integrated before: Step (d) above (function tagging)
leads to a dependency node in the LAP data model (bearing the function
tag), as well as to *one* edge linking the node to the argument node (of
type morphology). The second edge of the bi-lexical dependency relation,
however, is first generated by step (f) above, i.e. it amounts to
actually connecting the dependency node to its head.

Finally, we note what appears like morphological derivation in a single
analysis, e.g. from the above:

    "<čuojaheaba>"
             "čuodjat" V* IV* Der/h V TV Ind Prs Du3

We will thus treat the sequence of tags suffixed with an asterisk as a
separate component in the (newly generalized) morphology node type (and
treat the Der/h tag as its right boundary).

# Workflow Simulation

    $LAPTREE/etc/driver ==tool import ==process text $LAPTREE/gt/etc/test.txt /tmp/media.oe.sme.rpt
    $LAPTREE/etc/driver ==tool gt ==process tokenize /tmp/media.oe.sme.rpt /tmp/gt.tokenize.oe.sme.rpt
    $LAPTREE/etc/driver ==tool gt ==process disambiguate /tmp/gt.tokenize.oe.sme.rpt /tmp/gt.disambiguate.oe.sme.rpt
    $LAPTREE/etc/driver ==tool export ==process cg3 --style gt /tmp/gt.disambiguate.oe.sme.rpt
<update date omitted for speed>{% endraw %}