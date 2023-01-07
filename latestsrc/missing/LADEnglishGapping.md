{% raw %}One of the more challenging phenomena for an implementation in an HPSG
grammar is gapping, found in English, Spanish, and other languages. In a
sentence such as We gave Kim a book and Lee a laptop there is a notional
coordination of two verb phrases, but with the omission of the head of
the second VP. In a lexicalist framework, it is difficult to ensure that
each of the conjoined headless sequences of complements and modifiers
conforms to the subcategorization constraints of the overt head of the
first conjunct phrase. It is similarly challenging to provide a
compositional semantics of such sentences, where presumably one wants
multiple occurrences of the predication introduced by the overt verb,
one for each of the notional conjuncts in the gapping construction. The
developers of the DELPH-IN grammars for English and Spanish have
implemented one analysis of gapping, but at least for English, this
analysis has fallen short both in coverage and in efficiency. Hence a
better analysis is desired.

# Data

**VP-level coordination** with shared subject

- \[V NP PP\] and \_ NP PP
  - *We gave books to Kim and magazines to Chiang.*
    
    *We visited Tokyo on Monday and Kyoto on Wednesday.*
  
  \[V NP NP\] and \_ NP NP
  - *We gave Kim books and Chiang magazines.*
  
  \[V NP NP S\] and \_ NP NP S
  - *We bet Kim a dollar that he would win and Chiang a dollar that
he would lose.*
  
  More than two top-level conjuncts
  - *We gave books to Kim, magazines to Chiang, and letters to
Devito*
  
  Extraction from within gapped conjunct
  - *Which message did you send to Kim on Tuesday and to Chiang on
Friday?*
  
  One shared argument
  - *I saw Kim in the canteen on Tuesday and in the library on
Wednesday*
  
  Different numbers of modifiers
  - *I saw Kim in the canteen on Tuesday and Sam on Wednesday*
  
  Preverbal modifiers
  - *They probably hired Kim, and possibly Sandy, too*
  
  Combined with right-node raising
  - *I bet Kim one dollar and Sandy two dollars, that we'd win*
  
  Nested VP-level gapping
  - *I bet Kim one dollar we'd win and two dollars we'd lose, and
Sandy three dollars it'd be a draw*

**S-level coordination** (aka conjunction reduction)

- \[NP \[V NP\]\] and \[NP \_ NP\]
  - *He admires Paris and she Oslo.*
  
  \[NP \[V NP PP\]\] and \[NP \_ NP PP\]
  - *She gives books to kids and we magazines to parents.*
  
  Nonfinite coordination
  - *I saw Kim leave the canteen, and Sandy the library*
    
    *I want Kim to leave the canteen, and Sandy the library*

**Combined VP- and S-level coordination**

- \[NP \[V NP NP\] and \[\_ NP NP\]\] and \[NP \_ NP NP\]
  
  - *We gave books to Kim and magazines to Chiang, and Sandy letters
to Devito*
  
  \*\[NP \[V NP NP\] \[\_ NP NP\]\] and \[NP \_ NP NP\]
  
  - \**We gave books to Kim, magazines to Chiang, and Sandy letters
to Devito*
  
  \[NP V NP NP\] and \[NP \[\_ NP NP\] and \[\_ NP NP\]\]
  
  - *We gave books to Kim, and Sandy magazines to Chiang and letters
to Devito*
  
  \*\[NP V NP NP\] and \[NP \_ NP NP\] and \[\_ NP NP\]
  
  - \**We gave books to Kim and Sandy magazines to Chiang, and
letters to Devito* (intended: we gave letters to Devito)
  
  \*\[NP V NP NP\] \[NP \_ NP NP\] and \[\_ NP NP\]
  
  - \**We gave books to Kim, Sandy magazines to Chiang, and letters
to Devito*

# Corpus examples

**Brown**

*You've already sent your daughter to Miss X's select academy for girls
and your son to Mr. Y's select academy for boys, ...*

*Once again, he shook his head, kept his face expressionless and his
voice very calm, and had a strongly supported alibi ready.*

**Wall Street Journal** (18 items in 22 sections)

*When the Germans lost World War I, they lost Namibia to South Africa
and the diamonds to Ernest Oppenheimer, patriarch of Anglo American
Corp. and De Beers.*

*"I pay a lot to the farmer and five times the state salary to my
employees," he says.*

*Cast as Violetta Valery in a new production of Verdi's "La Traviata,"
Ms. Gruberova last week did many things nicely and others not so well.*

wsj02/20239030 wsj04/20465039 wsj07/20795009 wsj08/20803007
wsj11/21121014 wsj11/21146132 wsj11/21154003 wsj12/21243004
wsj13/21312027 wsj13/21315016 wsj13/21366008 wsj15/21522001
wsj16/21678003 wsj17/21778087 wsj18/21867016 wsj19/21950027
wsj19/21996006 wsj21/22162011

**Conjunction reduction**

*Whenever the place was cleaned or a meal served it was Precious who did
the work.*

*Time is a queer thing and memory a queerer; the tricks that time plays
with memory and memory with time are queerest of all.*

*Now a little flush came on her pale homely face and enchantment in her
eyes.*

WSJ (22 items in 22 sections)

*The workers can be motivated, and the company reach its full potential,
only when management embraces the employees' perspective.*

*One cell was teased out, and its DNA extracted.*

*He's not predicting a blockbuster, but he is "more optimistic than
three months ago" because employment remains strong and inflation low.*

wsj00/20013001 wsj00/20013001 wsj00/20024007 wsj02/20235003
wsj04/20445026 wsj04/20469031 wsj06/20604022 wsj07/20719041
wsj07/20773007 wsj10/21022009 wsj10/21092017 wsj11/21138003
wsj12/21218010 wsj12/21281009 wsj13/21320035 wsj13/21391019
wsj15/21528009 wsj16/21654023 wsj18/21870039 wsj19/21924004
wsj20/22033014 wsj21/22106012

# Candidate analysis 1

Record the VALENCE and the lexical predicate in each verb's HEAD, and
use a set of specific four-dtr constructions to admit these sequences:

VP and XP1 XP2

S and XP1 XP2

where the VAL of the left-most dtr constrains the form of the final two
dtrs,

and the lex-pred enriches the underspecified EP supplied by the
construction for the copied verb's semantics.

Drawbacks of the analysis:

1\. Does not extend to three or more conjuncts

2\. Uses ad hoc features that preserve lexical information in phrasal
projections

3\. Impedes efficient processing, since it blocks packing of VPs or Ss
with differing internal structure.

# Candidate analysis 2

Always propose a VP whenever you see "and XP YP (ZP) ..."

Actually propose several each time (with gaps for missing complements)

Underspecify the semantic-head predication (e.g. like VP-ellipsis)

# Notes

## Scribed by Emily

Guy: Apropos of more complicated analyses breaking beautiful analyses,
CCG analysis doesn't work for S-level coordination.

Dan: Consistent with Mark's comments that those are distinguished as two
different phenomena.

\[Thoughts: A series of non-branching rules that are all COORD + that
take a NP/PP/S daughter and behave as if there were a V head to combine
with it, and do the same effect as head-comp, head-adj, with or without
extraction. Brute force approach, too expensive. COORD + helps a bit,
but probably not enough. Nope: would require underspecified COMPS list
and all hell would break use. Would also have to have the rule introduce
a rel, with links to items on the COMPS list. So maybe you need N
versions of each rule for each type of semantic frame.\]

Dan: Parallelism --- the list of dependents has to be the same in each
conjunct in the construction.

Emily: Does the CCG analysis actually get the parallelism constraint?
How??

Francis: I believe CCG often over-generates.

Guy: give: ((S\\NP)/NP)/NP)

- Bill: NP type raised to: ((S\\NP)/NP)\\(((S\\NP)/NP)/NP) books: NP
type raised to: (S\\NP)\\((S\\NP)/NP) Bill + books:
(S\\NP)\\(((S\\NP)/NP)/NP)

Emily: Ah: Building *Bill books* and *Sandy magazines* as things looking
for a ditransitive verb to the left, then coordinating those, and then
they together find one ditransitive verb to the left.

Guy: Wouldn't allow *I gave Mary a book and magazines to Kim.*

Dan: Debate in the literature about whether to allow those. Psycholx
studies show that those asymmetrical ones are harder to process.

Emily: Can we take inspiration from that different bracketing?

Dan: Would have to change how we do extraction...

Emily: And composition. *bet* expects to pick up its
complements/adjuncts one at a time.

Guy: Following up on that, could we have two sequences of dependents,
and apply the head-comp rule twice?

Dan: Preserve the derivational history.

Guy: No ... lists of NPs.

Luis: *and* is selecting the elements on both sides, and then picking up
the verb.

Emily: Sort of like argument composition.

David: Not just arguments, also have the MODs, and have to have the same
number.

Luis/Emily: That's okay, the *and* just requires the same on both sides.

Guy: *I saw Kim leave the restaurant and Sandy the library.*

Dan: That's a nice interesting example of VP gapping and sentence-level
gapping.

Emily: Rephrases Luis's idea in terms of LCOMPS and RCOMPS, putting verb
first left with argument composition idea.

Dan: Don't want to have it pick up the verb, because I want to get the
three-conjunct version, too. In combination with a special construction
that takes a verb can probably do it.

Emily: Need to have the verb's INDEX and LTOP around though for
modification.

Dan: I think you'd need that anyway.

Francis: Yet another analysis. Let's call this the bruteler force
analysis. For some of these things, we already construct fragments. If
we make fragments for all of these long but finite number of things, and
put in an unknown verb. *Kim arrived on Tuesday and Sandy on Wednesday*.
Don't want one **arrive\_v** modified by two different things.

Luis: The *and* will put in a elided or unknown verb rel.

Dan: Points to 2nd Brown corpus example. Don't want so many fragments
floating around.

Francis: Conjoin VP and fragment with special *and*.

Dan: How do I get parallelism.

Francis: That's the magic I'm missing.

Dan: Would require the verb to expose its valence (and modifiers).

Francis: Always true?

Emily/Dan: Not true of Luis's idea.

Guy: *Who did you give what?* *Mary a book.* No magic *and* there.

Dan: But I get lots of discourse fragments that aren't constituents.
*Who's going to come tomorrow?* *Probably Kim.*

Francis: We need to build fragments anyway. In discourse we have a magic
and called discourse that does the same linking.

Dan: How do I handle the extraction cases? Not contemplating extraction
from fragments.

Francis: Well, not yet.

Guy: *I hired probably Kim and possibly Sandy(, too).* That looks like
your earlier example.

Francis: *Which message did you send to Kim on Thursday and to Chiang on
Friday?* *Ah, and to Emily on Saturday.* Shows that these things will
show up as fragments.

\[Emily: This example involves an *and* in the fragment, though.\]

Dan: The fragment analysis by itself won't get the parallelism. Luis's
proposal looks a bit more promising in that direction. Not yet sure you
have to have a different *and* --- could come from the construction.

Emily: What about extraction... record the info on the LCOMPS list that
one of them is actually extracted.

Guy: Wouldn't the verb undergo extraction?

Dan: Yes

Emily/Luis: But the and clump has to, too.

Dan/Emily: \[Realize that there are at least two proposals here.\]

Emily: \[Tries to outline the proposal, involving 4 *and*s, up to
arg1234\_rel.\]

Luis: My understanding matches Emily's.

Guy: Mine matches Dan's.

Dan: I had understood Luis's proposal to involve only one *and*. Build
up a big clump, putting things on the list but don't do any linking yet.
Then apply a rule at the top as many times as you need to pop the things
back off the list and do the linking then once you've found the verb
which will also tell you what EP you have.

Emily: Wouldn't that involve multiple lists when you have the three or
more conjunction case?

Dan: Sure, we can iterate through that.

Emily: A list of lists.

Guy: I think it can be done with recursion and the binary structure of
the coordination.

Emily: Nuh-huh.

David: If we're willing to relax the SLASH list to three items, could we
say that the *and* is picking up things to the left and the right that
have the same SLASH list? *give* with a SLASH list with two things on
it, then picks up coordinated clump that fills in that SLASH list.

Dan: So like RNR, but more elaborate. ... Seems like you have to do work
twice then onces at the *and* and once for filling. Maybe buys you some
precision.

David: You only need one *and*.

Last update: 2017-05-03 by GuyEmerson [[edit](https://github.com/delph-in/docs/wiki/LADEnglishGapping/_edit)]{% endraw %}