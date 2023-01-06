{% raw %}Over tapas on 17 April 2018, the discussion of arguments v. adjuncts
turned up an interesting avenue to explore: How do the degrees of
freedom in ERG lexical entries relate to the various tests for the
argument/adjunct distinction. This page is meant as a place to collect
(a) those degrees of freedom/dimensions of variation, (b) work towards
understanding how they do and don't cross-classify (surely some of the
cells in that multidimensional matrix are empty) and (c) how they relate
to the various tests in the literature.

## ERG Dimensions of variation

- Syntactically selected or not (aka "argument" v. "adjunct", in ERG
terms)
- Semantic role: none (e.g. in raising constructions), semantic
argument, semantic functor
  - Subdimension for semantic functor: scopal or non-scopal
- Control relation or not
- Obligatory or not

## Persistent tests in the literature

- Iterability: But maybe not with manner?
- Obligatoriness: Syntactically required
- Dialogue test: Semantically required
- Ontological obligatoriness: every event described by this verb
requires a certain role
- Specificity: Appears with only a few verbs, then it's probably an
argument of those verbs. (Converse of universality or flexibility)
Ex: selected PPs *wait for somebody*
- *Do so* test: *Dan ate sushi with Stephan's wife and I did so with
somebody else's wife. \#And I did so pizza.* Not just about do so
not being able to combine with an NP. \**Kim relied on Chris on
Tuesday and Sandy did so on Pat on Wednesday.*

## Less stable/more debunked tests

- Extraction only from arguments, not adjuncts

### Rough notes from 24 April WG meeting

==== Illustrating ERG dimensions ====

    Kim ate sushi in Oslo
     sushi: selected, assigned a role
     in Oslo: not selected, takes verb as an argument
    
    Kim stumbled into the room:
     into the room: selected, takes verb as an argument
    
    Kim jumped into the water:
     selected, but takes verb as an argument
     jump(kim)
     into(jump,water)
    
    Kim slipped into the room.
    Kim slipped (different sense only).
    
    Kim put the books in the box
     put(Kim,books,in the box)
     in(book,the box)

#### Tests

- Iterability -- assigned by different theories: HPSG, LFG, FGD (FGD
uses it to decide whether to put it in the valence lexicon)
- Obligatoriness
- Specificity

Misalignment between dialogue test & ontological obligatoriness --- time
& place mostly ontologically required, but won't pass the dialogue the
test.

Arrive -- where you arrive is obligatory, but not from where:

    A: Charles arrived yesterday.
    B: Where did he arrive?
    A: #I don't know.
    
    A: Charles arrived yesterday.
    B: Where did he arrive from?
    A: I don't know.
    
    A: Charles arrived.
    B: When did he arrive?
    A: I don't know.

But:

    The marchers came from all corners of the city and numbered over 100,000 when they arrived at city hall.
    
    She put the books in the box in the basement.
     -- only ''in the box'' fills the ARG3 of ''put''
    
    They arrived in the train station in Oslo.
    In Oslo, they arrived in the train station.
    ?In the train station, they arrived in Oslo.
    
    He arrived in Europe yesterday in France in a small town called Pons.
    He lived in France for a long time in a small town called Pons.

Prague folks have a hard time picking which one is the argument and
which is the adjunct.

# Notes from ERG Walk-Through

More fine-grained bar-levels than ‘classic’ HPSG: MODIFIED feature (with
internal structure) allows adjuncts to leave a mark on their head. Used
for grammaticality contrasts in \**We arrived the day* vs. *We arrived
the first day.* Also used to control spurious ambiguity with pre- and
post-head modification. Maybe also used to block iteration, e.g. with
multiple cardinal adjectives.
<update date omitted for speed>{% endraw %}