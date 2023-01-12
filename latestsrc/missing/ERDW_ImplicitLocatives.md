{% raw %}# Implicit Locatives

English has a variety of expressions that express the location of an entity or event in time or space but don't specify any particular relationship between the entity/event and the location.  These expressions include expressions of time, such as *now*, *when*, *every day*, *the day after you met Sandy* as well as ones that indicate location including *here*, *there* and *where*.

# Examples
    Where is the stick? -> no relationship other than the stick "is" somewhere
    The stick is there. -> no relationship other than the stick "is" somewhere
    
    # From the [ESD Test Suite]()
    The dog barks every day. -> No relationship to day other than it "happens" every day
    Browne arrived the day of the garden dog. -> no relationship to day other than it "arrived" then
    The dog barks there.
    The day the dog barked arrived.
    The meeting that day was local.

# Counter Examples
    The stick is on the table. -> locates the stick in a place on the location
    He arrives before/at 10am. -> locates the arrival before/at a certain time

# MRS Expression
In the MRS, these "nonspecific" references are indicated by the predicate `loc_nonsp` and can take two forms:

> For Entities: [ loc_nonsp ARG0: e2 ARG1: x3 ARG2: x4 ]
This form is used when the item being located in a general place/time is an entity.
> - `ARG0` is an event introduced by this `loc_nonsp` predicate to allow possible modification of it by other predicates (not done below).
> - `ARG1` is the entity being located
> - `ARG2` is the general location for the entity

```
Example: where is the stick

[ TOP: h0
INDEX: e2
RELS: < 
[ which_q LBL: h6 ARG0: x4 [ x PERS: 3 NUM: sg ] RSTR: h7 BODY: h8 ]
[ place_n LBL: h5 ARG0: x4 [ x PERS: 3 NUM: sg ] ]
[ _the_q LBL: h9 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] RSTR: h10 BODY: h11 ]
[ _stick_n_1 LBL: h12 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] ]
[ loc_nonsp LBL: h1 ARG0: e2 [ e SF: ques TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ARG2: x4 ]
>
HCONS: < h0 qeq h1 h7 qeq h5 h10 qeq h12 > ]
```

> For Events: [ loc_nonsp ARG0: e8 ARG1: e2 ARG2: x9 ]
This form is used when an event "happens" in that general place/time.
> - `ARG0` is an event introduced by this `loc_nonsp` predicate to allow possible modification of it by other predicates (not done below).
> - `ARG1` is the event that is happening at the general location
> - `ARG2` is the general location where the event happens


```
Example: The dog barks there

[ TOP: h0
INDEX: e2
RELS: < 
[ def_implicit_q LBL: h11 ARG0: x9 [ x PERS: 3 NUM: sg ] RSTR: h12 BODY: h13 ]
[ place_n LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg ] ]
[ _there_a_1 LBL: h10 ARG0: e14 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: x9 ]
[ _the_q LBL: h4 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] RSTR: h5 BODY: h6 ]
[ _dog_n_1 LBL: h7 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] ]
[ loc_nonsp LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _bark_v_1 LBL: h1 ARG0: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h12 qeq h10 > ]
```

# Motivating Examples

This analysis involves a certain amount of ‘decomposition’ in the
semantics; the alternative would be to have predicate symbols such as
today\_n or here\_n which directly take events as the value of their
ARG1. The decomposition is motivated on the basis of the parallelism to
examples with prepositions contributing EPs analogous to loc\_nonsp:

- *The dog barked <span class="u">on Tuesday</span>.*/*The dog barked
<span class="u">every Tuesday</span>.*
- *The dog barks <span class="u">in the morning</span>.*/*The dog
barks <span class="u">every morning</span>.*
- *The dog barked <span class="u">in the yard</span>.*/*The dog barked
<span class="u">there</span>.*

Furthermore, while a lexical, non-decomposed analysis could in principle
be given to forms such as *today*, this analysis does not scale to
phrasal modifiers appearing the same use or to the relative clause
examples:

- *We arrived <span class="u">the week after the storm</span>.*
- *<span class="u">The day</span> the dog barked arrived.*

Examples like the following show that the modified element can also be
an entity (not just an event):

- *Exports increased 4% from the same period <span class="u">last
year</span> to $50 billion.* \[Attested example, WSJ\]

# ERS Fingerprints

    loc_nonsp[ARG1 i, ARG2 x]

# Interactions

# Reflections
- Another characteristic construction where a spatio-temporal modifier can appear without an overt mark of the type of location relation is in relative clauses whose head noun functions as a modifier within the relative clause.
- The expressions that give rise to loc\_nonsp are analyzed
syntactically as either lexical PPs (e.g. *here*) or noun phrases
(e.g. *today*, *the day of the first meeting*) which are of a class
that can be pumped to PP. In the latter case, the loc\_nonsp EP is
contributed by the phrase structure rule that builds the PP out of
the NP. Similarly, in the relative clause examples, the loc\_nonsp
is introduced by a syntactic construction.
- loc\_nonsp also appears in the decomposed meanings assigned to
expressions such as *earlier* and *overseas*.
- Some temporal nouns can only appear in this construction when they
have a modifier or a deictic determiner:
  - *Our meeting this week was interesting.*
  - *\*Our meeting the/a week was interesting.*
  - *Our meeting the week after that was interesting.*
- However, the word *every* can seemingly turn any noun into one with
this property; this likely involves a special lexical entry for
*every*:
  
  - *\*Kim phoned Sandy the last freeway exit before the state
line.*
  - *Kim phoned Sandy every freeway exit.*
- The interpretation of *every*-marked temporal locatives modifying
entities involves something subtle about the interaction of the
quantifiers. However, this is not specific to implicit locatives but
is also found with explicitly marked locatives:
  
  - *The earthquake the day after the eruption was barely noticed.*
  - *The earthquakes every ten minutes got old quickly.*
  - *The earthquake on the day after the eruption was barely
noticed.*
  - *The earthquakes on every third Tuesday got old quickly.*

# Open Questions

- Could on\_p\_temp et al be generalized to loc\_nonsp?
- ERG (1212) doesn't parse *Browne arrived the tobacco garden day.*
Are noun-noun compounds not the sort of thing that can take a word
of the *day* type and make it into a phrase that can function as a
loc\_nonsp modifier?

# Grammar Version

- 1212

# More Information

- ErgSemantics main page
- Inventory of semantic phenomena (to be)
documented
- How to cite this work

Last update: 2022-07-13 by Alexandre Rademaker [[edit](https://github.com/delph-in/docs/wiki/ERDW_ImplicitLocatives/_edit)]{% endraw %}