{% raw %}# Distinguishing Scopal from Non-Scopal Semantic Arguments

## Background

We take it as given (for now) that certain predicates have scopal
argument positions, i.e. contribute to the articulation of the scope
tree. Examples are the sole arguments of *seem* and *not* and the second
argument of *deny* in the examples below:

- *It seems that Kim left.*
- *The dog did not bark.*
- *Kim denies that the dog barked.*

In calling these argument positions scopal, we believe we are making at
least the following claims:

1. Quantifiers may scope in between the predicate and its scopal
argument.
   - *The dog did not chase every cat.*
   - *Kim denied that every dog barked.*
2. A proposition embedded as a scopal argument is not necessarily (for
the purposes of e.g. presupposition calculation) in the same context
as the embedding predicate.
   - *Kim believes that every dog barked.*

Currently, in the English Resource Grammar (and DELPH-IN grammars more
generally), we distinguish two types of elements which are adverbial
modifiers syntactically and predicates (operators/scopal predicates or
non-scopal predicates) semantically, which we call *scopal* and
*non-scopal* modifiers. The former take the (semantics of the) syntactic
head they combine with as a scopal argument:

- *Kim never left.*

While the latter instead are predicated of the event variable of the
head they combine with:

- *Kim left quickly.*

While what we construct in the ERG are *meaning representations* (and
not *logical forms*), for the subset of expressions which can be handled
in some suitable object language, there is meant to be a mapping from
each meaning representation produced by the ERG to one or more
expressions in that object language. Assuming something like (a suitable
variant of) higher-order predicate logic, we imagine that our non-scopal
modifiers correspond to ordinary predicates while our scopal modifiers
would likely have operator status.

## Problem Statement

While we feel that some items are fairly clearly in one category (scopal
modifiers) or the other, we find it difficult to categorize many other
times. Accordingly, we have the following questions:

1. Is this distinction in fact well-defined?
2. If so, what tests can we use to classify particular predicates?
3. If not, what representation should we use? (Underspecification;
assimilating all modifiers to one type; others?)

## Key Examples

The modifiers *for a long time* and *deliberately* seem like good
candidates for non-scopal modifiers, but then it is not clear to us what
it means for them to modify negated clauses:

- *Kim didn't speak for a long time.*
- *Kim deliberately didn't speak.*

Note also close semantic similarity between negation and *fail*, where
we are more comfortable having non-scopal modification of failing
events:

- *Kim failed to speak for a long time.*
- *Kim deliberately failed to speak.*

We can also pair likely non-scopal modifiers with verbs that seem to be
close paraphrases, and which (as verbs) we expect to take verbal
projections as clausal arguments:

- *Kim successfully barked.* / *Kim succeeded in barking.*
\[Nominalization might make this one moot.\]
- *We were happy to discuss scope.* / *We happily discussed scope.*

What about when a (putative) scopal modifier appears to modify only a
(putative) non-scopal modifier but not the head?

- *Kim probably baked a cake for Sandy.* / *Kim baked a cake probably
for Sandy.*

## Possible Semantic Tests

- Entailment: This is a one-directional test, where the lack of
entailment shows that the modifier must be scopal, but availability
of entailment doesn't tell us anything.
  - *It's raining heavily* ⇒ *It's raining*
  - *It's probably raining* !⇒ *It's raining*
  - *It's not raining* !⇒ *It's raining*
- Scope ambiguities: This test is difficult to apply!
  - *Every dog barked* (one reading)
  - *Every dog barked loudly* (one reading)
  - *Every dog didn't bark* (two readings)

## Possible Syntactic Correlates

- Hypothesis regarding syntactic position: Non-scopal modifiers (but
not scopal ones) can appear in sentence final position without an
intonation break before them.
  - \**The dog will bark probably/almost/allegedly*
  - *The dog will bark loudly/quickly/here/now/in Paris/for a long
time*
- Hypothesis regarding extraction: Non-scopal modifiers (but not
scopal ones) can appear at the left edge of a matrix clause while
being interpreted as a modifier of an embedded verb.
  - *In Paris, my guidebook suggests that we try the escargot, but
in Berlin, it suggests that we try the pastries.*
    
    - Note: *in Paris* and *in Berlin* are interpreted as
modifying *try*, not *suggests* in both clauses.
  - *Emily proposed that ACL be in Paris. Berthold wanted ACL to be
in Madrid. In Paris, Berthold suggested we have DELPH-IN.*
    
    - Note: *In Paris* is interpreted as modifying *have*, not
*suggest*, in this (somewhat forced) context.
  - *Emily thought that the dog probably yowled. But Berthold
thought the dog certainly yowled and probably Berthold thought
the cat yowled.*
    
    - Note: Even with the forced context, *probably* isn't
interpreted as modifying *yowled*.

## Notes from Discussion (2017/08/18)

Mary: Are these all of the places where quantifiers can scope? There are
others.

Dan/Emily: Like what?

Mary: Restriction of a quantifier.

oe/Dan: That is another scopal argument in our framework.

Mary: If you have a relational noun.

Dan: Like *belief*?

Mary: Or *friend of*.

Dan: What about *friend of*?

Mary: You can scope a quantifier *every friend of a student* ... *a
student* can scope around *friend of*. What's the predicate here?

Dan: *friend of* is a predicate, but not one that doesn't let things
scope under it.

Mary: So you have other places where quantifiers can go and you're happy
about that.

Dan: Correct.

Mary: We're just looking at things that are arguments of things for now.

Emily: You look skeptical of the claim that *quickly* is not scopal.

Mary: There are exmaples like *he made the cakes slowly*. You have to
introduce event variables for these to make sense. Could mean: Each cake
was made slowly, or he made each cake quickly but took a big rest in
between. Scope ambiguity?

Dan: Collective/distributive is another dimension. Also need to worry
about it in coordination. Maybe we're setting it aside too quickly.
Maybe the availability of it will tell us something we didn't know
before, but for the moment we're pretending we don't know about it.

oe: And yes, we are assuming a variant of a neo-Davidsonian event
semantics, where we are relatively generous with our use of
eventualities. I think Krifka has argued for at least some of them. For
*he baked the cakes slowly*, we'd have one meaning representation, with
bake(e,x,y) and essentially slow(e)

Emily: Actually slow(e',e), which is part of what Stephan meant by
'generous'...

oe: We don't want to ambiguate those two distinct readings or spell out
subevents or ... we don't explicitly quantify our events, just assume
appropriately scoped existential quantification.

Dag: So *usually* doesn't quantify over events?

Dan: We don't have any event quantifiers --- haven't tried to unpack
*always*, *never* etc. We have left those event quantifying adverbs as
opaque. And someone downstream could say I know how to interpret that,
if they wanted to unpack. We're not particularly proud of that
laziness...

oe: *Frequently* would be a candidate where we would have to ask. We
picked *not* and *quickly* as scopal vs. non-scopal, respectively.

* * *

Dan: The distinction is difficult because we have a forced choice.
Scopal or not, not possible to underspecify. Doesn't lend itself well to
blurriness.

* * *

Dan: And even worse there, that *for* might be semantically empty ---
cf. *Kim baked Sandy a cake.* --- so then there's really nothing for
*probably* to predicate itself off.

oe: But can you use the NP NP construction and then insert *probably* to
mean it was only about the recipient?

Dan: No, but that could be a syntactic fact.

* * *

Dan: Maybe a little bit more about the background of the discussion: The
really vexing thing is that as we run through the next 2000 adverbs, I
have to for every one of them decide if they're scopal or not. When I
run into *frequently*, *usually*, *rarely*, *nearly*... I have to
decide. *Kim nearly left* doesn't entail *Kim left*. Does that mean it's
scopal? Or is it something else about the rest of the meaning of
*nearly*? And if *rarely* is non-scopal but *never* is scopal, what
about *rarely* v. *almost never*? Shouldn't they mean the same thing?

* * *

oe: Non-scopal ones correspond to the vanilla, motivating cases in
Davidson's presentation of events. Things you can predicate of the
eventuality, that don't modulate veridicality, and don't require that we
open a position for a quantifier to scope there. Then we're left with
... the other type.

Dan: We keep coming back to quantifiers, because at least for English we
don't know of any other scopal operators that can float up and down the
scope tree. But German is interestingly different in two respects. Some
scopal operators can appear at the end of the VP (different from
English) and we thought that maybe correlated with the observation that
you can have partial scope constraints: I at least outscope these, but
there might be things that happen in between. So one scopal operator to
the left and one to the right fight it out (within just one syntactic
structure). We don't have clear cases of that so far in English, though
if we could find a post-VP convincingly scopal modifier, we could make
construct similar motivation for the partial scope. That would make it
easier to do some of these rescoping tests.

Dan: We hope to focus this discussion on adverbial guys --- the whole
space of adjectives seems even more vexed. In the adnominal case, we've
taken the not likely to be correct simplifying view that they're all
non-scopal, including *former*, *fake*, *probable*.

oe: But you just said we're not having that discussion today...

Dan: But if someone had a brilliant idea? Though we hope to keep the
discussion focused by just looking at the adverbial guys.

oe: One thing that pretty clearly drives us to making an argument
position scopal is when the type of the argument corresponds to the
semantics of a clause, as with *We were happy to discuss scope*. We
assume that *happy* takes that thing that we sometimes call a
proposition as its complement. Our main test there is that you can
insert negation: *We were happy not to discuss adnominal modifiers.*
Then the argument of *happy* would have to be not discussing.

Dag: *Kim didn't speak for a long time.* Do you have a distinction
between the event and something like topic time that you could also
modify?

Dan: Like Reichenbach? No---tried that once, but didn't keep it in the
grammar. But if you think that more articulated representation of these
elements in tense and aspect would give us an affordance for a sharper
distinction, that could be fun.

Dag: Then you have two things it could modify: the event time, or the
topic time (which under normal assumptions would be higher than the
negation).

oe: Here's the meaning representation we currently provide.

    neg[speak(e,Kim) ∧ for-a-long-time(e)]

Emily: Just the one?

Dan: Yeah, I don't know how to do the other.

Dag: If you put in an eventuality for the negation.

oe: We so far shy away from that...

Emily: It's there, we just don't expose it.

Dag: Having an eventuality for the negation would be like getting the
topic time.

Dan: If I could explain it in terms of the tense semantics, maybe it
would be less embarassing. We'd have to think about what we mean by that
exposing of the negation event.

Dan: How much longer do you think we can get away without having
quantification for events, if we were going to do things like *rarely*
and *frequently*? Our observation so far is that we don't know of
syntactic behavior that corresponds to/impinges on that. Assuming the
mapping can be done after the fact from frequently(e) to many(e,body).
Maybe worse if I have it as a non-scopal modifier. If I have it as
scopal, then at least the scope tree would be the right shape.

Dag: You can get ambiguities there: *Typhoons usually arise in the
Pacific*. Usually, if you're in the Pacific, there will be typhoons or
if you're in the Pacific there will usually be typhoons.

Emily: But how does that relate to different scope trees?

Dan: Is there a puzzle for how I get that lowering of the effect of
*usually* that is there whether or not it's scopal or non-scopal.

oe: If usually were scopal, doesn't that turn into parallel to *Kim
didn't speak for a long time*, assuming that *in the Pacific* is
ambiguous.

Emily: And we are maybe less embarassed about giving *usually* its own
eventuality?

Dan: Still a little embarassed; we still want *arise* to give the main
eventuality for

oe: Did you just make up that example?

Dag: No, it's from \_The Generic Book\_ (Krifka, ed).

Dag: But there are similar examples when there's no overt genericity
operator: *Ties must be worn* (in a restaurant) v. *Dogs must be
carried* (next to an elevator). Genericity is this weird operator that
sometimes isn't overt but sometimes is.

Dan: It can be overt too: *Dogs must always be carried* (with implicit
"if there is a dog")

Emily: Isn't it about the ambiguity between *always* and the generic
operator?

Dag: The assumption is that the generic operators, there's a restrictor,
so the ambiguity has to do with whether or not the subject (dogs, ties)
is in the restrictor.

Dan: Would that work for *usually*, *rarely*, *frequently*?

Dag: Yes.

Dan: Would that give me a way to pull together *rarely* and *never*?
*Rarely* seems to be the limiting case of *never*: *very very rarely*
seems to go to *never* in the limit. But maybe there's something not
quite linguistic coing on there.

Dan: What if we took the strong Occam's Razor view and said there isn't
a disticntion at the level of composition. Adverbials are slippery and
to pretend that loudly is different in kind from *never* is maybe a
mistake. What would I lose if I made them all scopal, but lots of the
scopes just never amounted to much.

Mary: Does that mean you'd get two representations for every sentence
with an adverb in it?

Dan: No, for *every dog happily chased a cat*, I'd get *happily* as the
outermost quantification, taking *chase* as its argument. But that seems
to predict more possible scopings for the quantifiers.

oe: If *happily* were scopal, on our current standard assumptions about
where quantifiers go, you'd get some more.

Dan: I get more than two already with *Every dog didn't chase a cat*.

Emily: Yes, six.

Dan: So the question is do I want six with *happily*? How about with
*frequently*?

Mary: *happily* has to be relative to some individual that's happy. So
happy has to take not just the situation that the individual is happy
about, but also the individual who is happy about it: every(happy(some
or every(some(happy both okay --- these seem different, is there some
particular cat that the dog is happy about chasing. For *frequently*
it's even clearer.

Dan: With *every* always.

Emily: That's forced (for *happy*) because of variable binding, like
Mary said.

Mary: But not for *frequently* --- and the six seem okay.

Dan: So you're saying that the fact that happy takes that variable would
rule out some.

Emily: Did you convince yourself of all six of those?s

Mary: There's a poor cat that gets chased every hour by all of the dogs
all at once or there's a poor cat that each of the dogs likes to chase,
but not necessarily all at once.

Emily: But then here's where I fail as a semanticist: we have to next
hold those scenes in our minds and see if the sentence can be used to
describe them.

Dag: But we only need one quantifier: *Every dog frequently barks.*

Mary: Seems different from *Frequently, every dog barks.*

\[ group lays out readings \]

Dan: Can I get both of those as readings for *every dog frequently
barks*

Mary: There are strong preferences for scoping from word order; have to
do things with the intonation.

Dag: So just one of each is enough, right?

Emily: But we'd have other problems if the order pins it down.

Mary: Really just tendencies ... if someone says you can't get that
reading

Dan: ... they probably aren't trying hard enough.

Dag: German is supposed to be scope rigid.

Mary: Yeah, because of free word order.

Dag: When it's fronted, can you still get the low scope reading?
*Frequently, every dog barks.*

Dan: I get both of them, I think. I can picture both of those scenes,
and I think the sentence works for both of them.

Emily: I'm having a hard time getting the low reading, but I'm bad at
these.

Mary: I think they're both there.

oe: So we've made a good case for *frequently*, but what about
*happily*?

Mary: Happy about different things?

oe: I wanted to get back to that, because we haven't explicitly
discussed that property of *happily*. You seem to be assuming that if
it's attaching as a modifier, it's also predicated of the subject or
maybe agent.

Mary: *The horrible man happily beats his dog.* --- it's the subject.

oe: Is it also the subject, or always the subject?

Mary: Would be easier if it's the subject, but probably not necessarily.

Dan: *The cookie was happily eaten by the kid.*

Emily: *There's happily lots of cookies.*

Dan/Mary: That's the discourse *happily*.

oe: We can't pin it down in the syntax.

Dag: A bit like depictives, oriented towards one of the participants.

Emily: I think we can handle this by marking that argument as an anaphor
that needs an antecedent in the same clause, and once we pin that down
it reduces the possible scope readings.

Mary: nods

oe: So *happily* is two-place?

Dan: It already is ... it's the same predicate as for the adjective
*happy*.

Mary: What about *deliberately*?

Dan: You can get *The cookie was deliberately eaten by the kid*?

Mary: Yes.

Emily/Dag: *Deliberately* is agent-oriented, not subject oriented. (This
has been widely studied.)

Emily: Back to *happy*/*happily* --- same predicate, but different
argument type for ARG2?

Dan: \[Tests and finds that in adverbial use \_happy\_a\_with only takes
ARG1 which takes the event as ARG1.\] Can fix that.

Dan: But now you're asking me to make another distinction, because you
don't want *slow* to take two arguments do you?

oe: What about *The child slowly ate the apple*/*The child was slow to
eat the apple*/*My daughter is slow to eat dinner*

Dan: Not clearly the same sense --- VP\[to\] complement taking *slow*
seems to mean something like "hesitant".

oe: But you were getting around to improving the grammar by making
*happily* like *happy*.

Dan: I'm not yet sure I want the ARG2 to be the proposition rather than
the eventuality.

Dag: There's literature on this type of participant-oriented adverbials.

Emily/Dan: That's a good search term?

Dag: Yes.

Dan: Would that literature help me see that *slowly* or maybe others
that aren't.

Emily: My guess is that scopal v. non-scopal and participant-oriented v.
not might be different dimensions.

Dan: That makes the problem of adding adverbs harder. Slows the pace of
lexical acquisition, especially without adequate tests.

Dan: What's a crystal clear case of non-participant-oriented, aside from
*not*, *never*, or *probably*?

Dag: Degree adverbials, like *deeply*: *He loves her deeply*.

oe: Manner adverbials, like *heavily*.

Dan: *He heavily dropped the box on the floor.* Yeah, the guy's not
heavy.

oe: So far we aren't seeing any reason to make *heavily* scopal. If we
try to apply what we did for *frequently*, *Every athelete breathed
heavily*: Is that ambiguous?

Dan: If I make them all scopal, can I find another way to differentiate
*heavily* from *happily*? Mary's observation about the
participant-oriented ones taking another argument reducing the readings
is quite tempting.

Emily: But that's not going to help you with *heavily*.

Dan: I want to know if I can play that game one more time.

oe: And furthermore, you'll be able to take advantage of similarity to
*happy* the adjective.

Dan: Yes.

oe: So what I thought was a challenging example... the challenge
dissipates.

Dan: Tell me about *merely*. *Every dog merely barked.* How many
readings?

Emily: The two readings would have to be each dog only barked, or all
that happened was that all the dogs barked. But I don't think that
sentence can have the second reading.

oe: So would that second reading also be the meaning of *Merely, every
dog barked.*?

Dan/Emily: Star.

oe: And what would it mean if grammatical?

Emily: I'm a scientist!

oe: So making *merely* scopal would overpredict scope ambiguities. Also,
making everything scopal would undermine our reason for having
Davidsonian events.

Dan: But we also need to be able to count them (quantification over
events).

oe: What about *Every dog barked on Tuesday.*?

Emily: Yes! I can at least come up with the two situations, and I think
the sentence works for both of them, but maybe that doesn't require two
different readigs. *What was the day that the all the dogs barked? Every
dog barked on Tuesday.*

Mary: Cumulative event v. separate ones.

Dag: With *The dog barked on Tuesday*, there's a containment relation
between event and topic time. You see it much more clearly with
negation.

Dan: *Every dog didn't bark on Tuesday*

Emily: All were quiet, vs. Fido was quiet. Oh, but that's just
every/neg. Do we really need the *every*?

Mary: *The dog didn't bark on Tuesday.*

Dag: I think *on Tuesday* has to take wide scope.

Emily/Dag: But then we have the problem of focus of negation coming in,
which muddles these ones.

Emily: What about *The dog always barks on Tuesdays*?

Mary: That's kind of the habitual thing, which is a whole can of worms
in itself.

Dan: So it may again not be about a scope difference, but rather about
generics.

oe: Can we try *probably*? Steering clear of negation, but picking
something we're pretty confident is scopal.

Dan: *The dog probably barked on Tuesday.* There was a barking event and
I think it was on Tuesday, or there was probably a barking event, and if
so, it was on Tuesday.

Mary: It's probably the case that my dog barked on Tuesday. What's the
other one?

Dan: It was actually Wednesdasy.

Mary: Oh, yeah -- these things sometimes act like focus operators.

Emily: There's too many moving parts.

oe: So that focus of negation problem isn't limited to negation.

Dan: *My dishwasher probably died last week.* Last week, something
terrible happened. It seems probable that what my renters were
complaining at me about was the dishwasher dying. Seems convenient to
hang that on what probably is predicated of.

Dan: What do normal people do with this? Do they make a two-ways
distinction or not?

Mary: I think adverbs are hard.

Dan: But what would someone like Krifka say --- two kinds, maybe not
these two kinds?

Mary: So you're starting from the assumption that all of these are
one-place?

Dan: No -- things like if-then can be two place.

Emily: And we were happy to be convinced that *happily* is two-place.
(Pun not intended.)

oe: So were we about to decide that *on Tuesday* is scopal?

Dan: No.

Dan: We've used up the hour and a half we asked you for, and I can't do
semantics for more than 90 minutes. Any last words? Any references we
should look into?

Dag: There's lots of stuff on adverbials...

oe: We don't want to read lots of stuff. We want to read the thing.
We're lazy.

Dan: Did Davidson have anything to say about this? He knew about scope.
Did he say how his events fit into the scopal universe?

Dag: No, he was a philosopher.

oe: Parsons-style would be that *on Tuesday* is an event modifier.

Dag: Because he doesn't have topic times?

oe: He would kind of have to eventually, but he doesn't initially. It's
a very clean story initially.

Emily: He's not broad coverage.
<update date omitted for speed>{% endraw %}