{% raw %}# Some issues raised in analysing Chinese Relative Clauses

[ZhenzhenFan](/ZhenzhenFan) (FrancisBond)

We sketch an outline of how we handle relative clauses in Chinese, show
that the simplest analysis calls for fewer quantifiers and suggest some
strategies for dealing with this.

This is the third [Virtual Linguistic Analysis Design
Session](https://blog.inductorsoftware.com/docsproto/missing/VirtualLinguisticAnalysisDesign). It will be held on Wednesday,
March 1, 2016 at 00:00:00 UTC/GMT (Seattle 4pm (Tue), Singapore 8am,
Berlin 1am)

Details on [Overleaf](https://www.overleaf.com/4475340bfjkny).

**Notes from the Session** \[ Thanks to our transcriber, Wang Wenjie! \]

**LEGEND:**

Dan: Dan Flickinger; EMB: Emily Bender; FCB: Francis Bond; Guy: Guy
Emerson Joanna: Joanna Sio; LL: Liling Tan; Luis: Luis Morgado Costa;
Ping: Ping Xue; Woodley: Woodley Packard; ZZ: Zhenzhen Fan

### Question 1: Is there a neater way to allow the head noun (modified by the relative clause) to be non-specified? Our existing implementation requires changes in many places with "SPR olist" constraint on the noun.

EMB: Regarding question you are posing. I would expect that the easier
example is where the Rel. Cl. is closer to the head noun. So I'm
surprised your (framework?) comes next in terms of making \#5 possible
instead of in terms of making \#4 possible.

ZZ: Yes, looking at the original general order, we have the CL phrase
before the noun, and the assoc(iative) phrase is preceding that. The DE
phrase is, in a way, similar to the assoc. phrase. So our previous
grammar can easily allow that. Because it is expecting the specifier of
the noun to be saturated first before combing with the associative
phrase.

In order to allow \#5, we have to take away that constraint that the
noun has to have the SPR satuated first. And we started doing lots of
changes all over the place.

FCB: And that chain that leads to is the complements... In the original
grammar, complements must have a saturated specifier, extracted
complement... so the thing it extracts must have a saturated specifier,
and therefore we get \#4 but not \#5.

EMB: That's probably the part of that chain that I would have done
differently at the beginning. <span class="u">Instead of matching the
whole SLASH value from the relative clause to the MOD value of DE, I'll
just match the HOOK</span>. All you really need to match there is the
semantic information.

If you look at analysis of relative clauses in other large grammars,
you'll find that when you have something whose whole LOCAL value is
matched with the SLASH, it's a relative pronoun. But there are no
relative pronouns in Chinese, right? DE is not a pronoun. So, it is
mediating the relative clause, but it is not actually using head noun as
the full syntactic filler of the SLASH.

Joanna: There is a minor difference between \#4 and \#5. In \#4, when
you have rel cl. appearing before the DEM CL Noun sequence, you get a
restrictive reading. In \#5, when you have relative clause between the
classifier, you can also have a non-restrictive reading as well.

EMB: It will be so nice to have that go the other way!

Joanna: When you have different types of relative clauses, when you have
a stage-level and individual-level, you prefer to have a individual
level between the CL and the Noun, and the stage-level to the left-hand
side of the demonstrative. So there is some of preference for the kind
of relative clause we like to have.

Guy: Can clarify what is stage level?

Joanna: Suppose you have two relative clauses, one stage level (talking
about temporary properties), and the other individual level (permanent
properties), the preference is to have the individual-level one to be in
between CL and Noun, and more temporary properties to the left-hand
side. So, in general, there is some kind of preference, in terms of the
meaning of the relative clause.

EMB: I've heard of this for adjectives, but not for relative clauses.
So, a stage-level thing is "happy", as a state, versus "optimistic"
which is more on an individual level.

Joanna: Supposed we have something like "The tall boy I saw yesterday",
you would like to have "I saw yesterday" to the left of the
demonstrative, and "tall" between the classifer and the noun.

EMB: Ok, so it's not the relative clause that's being individual or
stage. It's if you have an individual-level adjective, it wants to go
closer to the noun?

Joanna: Yeah, that's what I meant. So when you have something that is
more temporary, then you want to have it, because adjective and relative
clauses, in both cases, you will use DE. So, the order depends on stage-
or individual-level.

Guy: Will this apply to something you do regularly?

"The person who eats rice", something which they do regularly.Does that
count as an individual-level property?

Joanna: When you have 1, then people say you can have it in either
position. Except when you have 2, then people prefer the more temporary
one.

Guy: So, "The person who eat rice whom I saw yesterday." As in, he eats
rice generally, but you saw that person yesterday/

Joanna: Ok, then I would prefer to say "I saw yesterday that eat rice
man"

Dan: I can provide more motivation for decoupling the value of the MOD
LOCAL, and the value of SLASH. I think it is an illusion that they are
the same, just because they are both nominal and they have the same
referential index, that is, the same HOOK, as Emily as saying.

It should at least be clear that in languages where case is marked, we
can expect that case is the same in upper noun and the place where there
will be a gap. Like when you say "The book that I saw impressed Mary",
"the book" in the main clause must be in the nominative case, but the
gap must be accusative.

I know that Chinese doesn't have case marking, so we don't have that
immediate evidence. But in the general design of how relative clauses
work, we don't want to have that kind of structural identity between the
noun being modified and the gap inside the relative clause. They are
different syntactic structures. One is covered in the referential index
that has to be identified.

I think you will find it most troublesome to handle these constructions
as described in \#4 and \#5.

\[...\] and then the value inside of SLASH should be a saturated noun
phrase. Something with an empty specifier.

FCB: In the document, I just added DE-COMP-LEX-2. de-comp-lex-2 :=
de-super-lex & raise-sem-lex-item & no-icons-lex-item &

- \[ SYNSEM \[ PAREN -,
  - LOCAL \[ CAT \[ HEAD.MOD &lt; \[ LOCAL.CONT.INDEX \#slash
\] &gt;,
    
    - VAL \[ COMPS &lt; \[ LOCAL \[ CAT \[ HEAD +vj,
      
      - VAL \[ SUBJ &lt; &gt; \] \] \],
      
      <!-- -->

      
      - NON-LOCAL.SLASH 1-dlist & &lt;!
        
        - \[ LOCAL \[ CAT \[ HEAD noun,
          - VAL.SPR &lt; &gt; \],
          
          <!-- -->

          
          - CONT.INDEX \#slash \] \] !&gt; \] &gt;,
      
      <!-- -->

      
      - SUBJ &lt; &gt; \] \] \],
    
    NON-LOCAL non-local \] \].

Dan: You will have to say something about syntactic structure of the
value of SLASH, not just about that semantic (...), right? You want to
say that the value of SLASH is a feature struture whose local value
describes a noun phrase. That is, its category is head noun, its valence
is specifier empty. Crucially specifier empty. The value of the
complement of DE with the gap must be a fully saturated noun phrase.

In the embedded clause, you have a completely normal looking, actual
noun phrase gap. What we don't have is a noun phrase in the value of the
MOD feature, because it's either an N-bar or an NP. It is underspecified
for the value of that specifier. Inside the SLASH, you said that the CAT
should have a HEAD value of noun.

I expect there will be other general properties of this de-comp-lex,
that says that the MOD value is something like a nominal phrase.

FCB: In sentence 5, "the book" isn't specified.

EMB: The gap is though.

Dan: "The book" will be the value of MOD. If you look at that MOD value,
it says only there some constraint. In Super-type, the head value must
be NOUN.

My suggestion is, you don't say anything about the specifier value of
that value in MOD. It should have no opinion about its specifier...

EMB: How will we get the QEQs or the label sharing with the relative
clause in Eg. 4. You and I agree \#5 should not be the difficult one,
now that we've untangled this thing about the SLASH value. \#4 is
trickier, because we want to gloss this piece as the determiner, as the
specifier of the noun phrase, and the relative clause is attaching
outside of that.

SSH: If \#4 and \#5 have the same meaning in terms of semantics, which
one is more natural?

ZZ: Personally I feel both are OK. I do not expect one to be more
popular than the other.

Joanna: When there is only one modifier, then both are fine, I think.

EMB: If you consider Mei yi ben shu 每 一 本 书 (every book).

ZZ: In that case, I would prefer the first one (\#4)

Dan: So I guess we can say they are both acceptable.

Emily, how to get label of book to be shared with label of rel. cl. I
think it's a little fancier for this discussion

EMB: I can see how an analysis that just says MOD value of DE doesn't
care about the specifier value of the noun it is combining with the SPEC
it combines with. And the Long-distance dependency will get the index of
"book" as the ARG2, right?

In terms of getting a well-formed MRS, how do you attach label of
relative clause to anything?

Dan: Probably have to suspend that worry. Have to worry in adposition,
and other places. Not quite trivial. Might become distracted in that
question, in this discussion about relative clauses.

EMB: Ok. Fair enough. Just to say it is the same question we haven't
solved elsewhere.

Guy: If we look at DMRS and MRS term, it's the same thing we have to get
hold of. Will this be easier to construct the right semantics?

EMB: More tractable in DMRS than MRS?

Guy: SHU is ARG 1 of XIE. In DMRS, only difference is whether it is
ARG2/RQ or ARG2/NEQ. It's just having a link there.

EMB: And the ARG2 link is there, in DMRS, we can just add EQ information
alongside?

Guy: Yeah.

EMB: That is messing with my intuition about MRS and DMRS equivalents.

FCB: In "this piece book", label of that is not the label of "book".

EMB: The LTOP points to nothing.

Dan: \[distorted and muffled\]

FCB: Right. Happy though I am to move this problem to later, I think
these are relatively common. If they are all going to be ill-formed,
that's a little bit of a worry.

EMB: It's not a problem that is unknown or not being worked on.

Dan is right, whatever solution works for adpos. or extrapos. that might
be good. The extraposed relatives might be tractable through the DMRS
thing. That solution should also work here. Going down this path will
set up ZHONG to benefit from work done elsewhere.

Dan: Having it as a central property in ZHONG might push us to getting a
solution faster, as it is part of a relatively common solution, so we
should come up with a better solution.

Woodley: Can we be assured that solution we use today is not
incompatible with deferring that?

Dan: I'm not sure we get a choice with this particular question. Have to
do real contortions in syntax to have that quantifier, bind the handle
of book, and still leave it exposed just long enough for it to combine,
and then seal itself off.

I don't think we are doing ourselves harm by making this division so
that the semantics of \#4 is not quite completely fully connected.

FCB: I think it's even worse in Chinese, because constructions in
"John's this book", "John's one book", "The book John" are completely
possible. Have to happen before the DET. So we'll have a lot of these.

EMB: Other possible degree of freedom is to decide that you don't want a
determiner to be actually introducing a quantifier, but treat it
effectively as a modifier. But given that "every" shows up there, it
seems pretty robust to call it a quantifier.

DAN: One strategy I've been thinking about for a similar phenomenon in
English, which is to delay the point at which you break the label of
that quantified expression into a nonbranching rule that says this is
now a finished noun phrase.

Essentially a unary rule that says, after you've done everything you're
going to do to this nominal constituent (picked up modifier,
quantifer)... during all of that time, the label of BOOK is still
exposed, it is still the LTOP of that phrase, until you have released
the NP out into the wild, through further composition with other
phrases, you say now that it is a fully quantified noun phrase, and I'm
going to throw away that label so nobody else can get to it.
Essentiually an LTOP zeroing rule.

I have a couple of those in the grammar. Seems to work alright, not sure
if it offends people's aesthetics. But it mechanical way of
accomplishing what you are asking, especially if it is going to be a
frequent phenomena.

So the quantifier comes in, it does its things with that book, but it
does not erase the LTOP of that phrase. Then, eventually it becomes a
saturated noun phrase, and nobody else gets to touch it.

EmB: You need the LTOP zeroing rule because you've got some other rules
that identifies the LTOP of the complement?

Dan: That...(supposed to happen...)? \[unclear; audio distortion\]

Either have identity or embedding. Head-comp rule should identify the
complement, or embedding it some place. We want neither of those effects
for quantifier phrases. So we have to throw away that LTOP.

Does that make sense in terms of potential strategy, Francis?

FCB: Yes! I think so.

Dan: Not that hard to write such a rule. Give me a noun phrase that has
its (??) rule, and \[...\] semantic \[...\], and the DTR can still get
through the modification. It's allowed to be \[audio distortion\]

\[...\] and having the semantic effect of erasing the LTOP. And then the
rest of the composition proceeds just it's supposed to.

Ping: Flattens that portion of the compositionality, I guess.

Dan: It does not have to be beautiful. Everytime you build a noun
phrase, you have this extra pumping rule that pushes it into its
rightful shape for further composition.

FCB: So it can't be pushed to the thing that compose it? Say, I'm the
last thing that happen to you, and I will \[distortion\] your
quantifier, effectively.

Dan: you have that option, but I think there is a generalisation there
that any time you build a complete noun phrase, whether it combines a
coordination or head-complement structures, or extraction, or as a
subject... whatever happens to it, it never get to expose its label. If
you don't insist on that happening at that moment you build that NP, you
run the risk of somebody forgetting.

FCB: Ok. So that's a possible solution. It sort of saddens me, because
the next thing is that we were trying to get rid of is the pumping rule,
so...

### Question 2: can we remove bare-np-phrase rule and leave the referential indices unspecified? We might use ACE cleanup transfer rules to add quantifiers to nouns that did not have them.

EMB: Seems to be pushing something in the core compositional semantics
out into another process that has very powerful machinery.

Dan: Play devil's advocate. Oepen has been playing a little bit with
this strategy, to look for parts where this isn't true. I think it's at
least worth exploring, Francis. You are making a very strong prediction
that syntax will not tell you anything about what that bare quantifier
should be. But I think for the most part that is going to be true.

What you're saying is, I'm going to hand you an MRS structure that isn't
yet a real MRS, because it's still missing a number of quantifiers. And
then you would say you know exactly what to do about those. Grab
outermost handle, and then attach the quantifier.

Risky if you allow yourself to have scopal modifiers as adjectives.
Something like "the alleged cat", or "the fake senator". If those build
a nominal phrase, whose labels are not predictably the same as the noun
that introduces the ARG0, I think you might be in some trouble. That is,
you'd have to start going back and computing through the chain of
syntactic adjunct rules, in order to figure out what was going to go
into the quantifier restriction in the QEQ.

FCB: OK.

Dan: As long as it is always an intersective modification of nouns, and
as soon as you have an ARG0 for the noun, you absolutely know what to
with its quantifier. You take the label of that noun and put it into the
QEQ into the restricter for its quantifier.

That will work in the current grammar, where I don't allow scopal
modifer over nominal phrases. But I really don't know if that's going to
be defensible in the long run.

Guy: What's the difficulty with saying "the alleged" or "the fake"?

Dan: In "the fake cat", then in my post-processing cleanup, go to every
ARG0 inside of a nominal phrase; everything that is a referential index.
If you don't already have a quantifier for that, put in the quantifier
relation of this bare NP (kind?), the underspecified quantifier and then
sew things up (perfectly), making them the restrictor of that quant rel,
the QEQ \[... overlapping voices\]

If you only can do that if you know exactly how to get from the ARG0 to
the handle. It's fine as long as it is inside single predication of the
noun. But as soon as you allow other guys to intervene, how would you
know what is your local information, say, I'm going to find out how far
up that chain I have to go before I find the thing that's going to be in
the restrictor of the quantifier?

I feel like I may be making it harder for people who...

Guy: But can't you go from the ARG0 to find the predicate, and that has
a label? Is it not enough?

Dan: That's not the one that's going to be in the restrictor of a
quantifier for something like "alleged cat", because it's "alledged"
that outscopes the label of "cat", and \[audio distortion\]

Guy: Is this an analysis which is currently not in the ERG?

Dan: That's correct. \[audio distortion\]

Woodley: ERG will not handle "there was some alledged cat?"

Dan: I don't yet believe that that "alledged" is demonstrably a scopal
modifier. I think there is a more interesting semantic effect going on
for things like "alledged" and "former" and "fake" and "probable", and
it's not just the same as what happens with the adverbs which have
morphological similarity.

EMB: I think a more compelling example of scopal nominal modifiers is
things like "likely". The example I try to convince people sometimes
with is "The most likely winner of every medal was disqualified". And I
think I can construct scope ambiguity that have "every" from "every
medal" going between "likely" and "winner"

Dan: If you can do that, then that will start to be evidence that there
should be a scopal modifier, and as I say, I'm not excluding that, but
allowing that possibility makes them more difficult to do this kind of
post-processing cleanup that Francis suggested. Not impossible; there is
still scopal element. One could build a handle chansing an operative,
and then zooming along until it fell off a cliff. Ok, you are the last
guy to touch, you go into the restrictor of the quantifier.

EMB: But it might not be that easy to do just with current transfer
machinery.

Dan: I think not.

So, what you might do for Chinese, for the time being, is to say that we
are not going to do quantification in phrases, and then we can do a
\[audio distortion\] to get rid of that (...) and writing a
post-processing parsing rule that does the cleanup. It should be ok.

FCB: One question we wanted to ask about this: it's still not clear what
we gain from doing this, apart from a sense that our trees look slightly
nicer. Or perhaps capturing intuition about Chinese that in fact,
specifiers are optional. Which I must admit, is also how I feel about
Japanese. Where putting these rules in to get the semantics right, but
it's not really a syntactic phenomenon, almost.

That's why doing it as a rule, where we are saying we have, as Dan said,
a not quite complete MRS. We need quantifiers everywhere, and so I'm
stepping into the interesting issue of scopal modification.

Emily, you think it should be done by the core grammar.

EMB: I can see the appeal of doing (...) it is completely predictable,
so we'll put it in afterwards, but I think it weakens out claim
monotonic composition.

Guy: Why is it not monotonic if it is completely predictable?

EMB: It's a sort of general HPSG thing where we do this in one
processing step, from the string to the semantic representation, so
maybe "monotonic" is the wrong modifier there.

Guy: In a sense, this is what happens for events as well, because event
variables are not quantified. And even if we want to map this onto
first-order logic, we have to put in those quantifiers.

EMB: That's true. So we are already sort of occupying a half-way
position here, so we could be filling them for the X-type (?) indices
when they don't have a quantifier.

Woodley: Is there any claim that MRSes for this langugae, in fact, have
no need or right for it to have quantification in there, in the final
MRS?

FCB: It depends on what you consider the MRS to be. If we think of MRS
as an underspecified representation of the semantics, then we could say,
maybe for Chinese, we would want to be able to specify the semantics
even more. And if I was purely parsing Chinese and then generating
Chinese again, I could probably go without filling in those quantifiers
at all.

On the other hand, if you think of the MRS as something that should form
a net, we have an idea of a well-formed MRS having these properties,
then what we'd be creating are not well-formed MRS, so maybe we then
need to distinguish between the super-underspecified MRS and the
underspecified-to-this-level MRS. I don't know if we have names for
those already.

EMB: We have been in this phase before, talking about
underspecification, and trying to come up with a name for it.

So, if it's just aesthetics, it seems to come down to whether you have a
greater negative reaction to spindly trees or post-processing MRSes.
Since I have no particular attachment to the shape of trees, I am not
troubled by seeing the non-branching NP over N productions.

FCB: I think we have colleagues who don't like them, I must admit. I
don't like them\* \_very\_ much. (\*spindly trees, not the colleagues)

But what I would like to have is a broader coverage, and then try one
versus the other, and if one takes 30% less time, I might take that,
although that's very implementation-dependent. And currently, the
cleanup rules are very experimental. So we'll need a little more input
from Woodley to get this, and give us exactly what we want.

On the other hand, it's often the case that in Japanese, there are
people who argued that the specifier is optional, and the grammar should
reflect that. And I think we are not really reflecting that. We are
saying, lots and lots of times, putting in the specifier is completely
predictable and not very interesting, it's the second-most common rule
in JACY. It doesn't seem to do anything interesing. But all of these are
aesthetic judgements, in a sense.

Woodley: Have you had the feeling that long sentences cannot be parsed
because of its presence?

FCB: No, it's not a very expensive rule. I feel we are doing something
which is not very useful from the POV of representing Japanese. I guess
a representation without these quantifiers is actually a better one in
some sense.

EMB: I think the discussion gets more interesting when we are talking
about the more interesting quantifier predications. "Every", "some" and
"most" in the ESD(?) discussion, where we were trying to look into the
inventory of what's the ERG, and there was quite a few, some of which I
think are not actually species of quantifier, but some of them are.

But if the expression of that kind of stuff does not end up in the
position that we call the SPEC of NP for Japanese or Chinese, then I
think your argument becomes stronger.

So, I don't mind saying that every noun in Chinese and Japanese has the
possibility of combining with an overt specifier that's doing the
quantifier thing, if that's where the quantifiers are actually expressed
when they are expressed overtly.

But if usually we get the quantifier as (loading) numeral classifier
phrases, then it becomes much less (?) because it feels like we're
saying something wrong with these languages.

FCB: Right. OK, then we'll go back and think.

Partly, we'll need to do this before when we were co-indexing all the
slash to get the right analysis. If we don't do that anymore, and there
is less urgency, we may still play with it. One of these places where it
would be nice to have cleaned... lots of small changes in lots of
places.

Do people still have enough energy to discuss One More Thing?

Ping: Missed much of discussion due to connection.

One thing which occurs to me about Chinese NP structure: keep in mind
that NP structure allows classifiers. So, when we think about NP
structures and also quantifiers, we have always to keep that in mind,
and reserve some syntactic position for classifers, overt or not.

FCB: Ok, thanks.

Guy: Is that already currently happening in the numeral classifier
phrase?

Ping: Yeah.

FCB: Yeah. Currently, we treat the classifier, at least for sortal
classifier, as that specifier positon in the noun phrase.

Ping: Classifier will be filling that specifier position? Yes, I'll need
to take a closer look and see.

FCB: Yes. I'm sorry, this fragment we prepared today does not discuss
that in a lot of detail. Maybe in the paper in HPSG, we put a bit more
detail in that.

### Question 3: can we use feature "LIGHT +" and "LIGHT -" to differentiate words and phrases?

EMB: About feature LIGHT: the use of LIGHT is meant to distinguish those
that can function as if they were just words, in the context of
constructions that wants to accept only lexical DTRs instead of pharsal
DTRs. However, it is not very well abstracted in matrix.tdl. One of the
places where there is a lot of English-specified stuff still hanging
around.

So if you want to use that LIGHT +/- distinction to make that kind of
extension in the grammar, and you need to take some stuff out of
matrix.tdl to make it happen, please feel free.

ZZ: Ok, that's great.

FCB: How is LIGHT, then, different between Phrase and Lex?

EMB: For one thing, you don't want to rely on the synsem type in that
way, because there are a lot of other noise that can come in there. But
also, there are things that are technically phrasal constructions, but
still behave as if they weren't in various places.

In the English grammar, pre-head modifiers of nouns are supposed to be
lexical only. So, if you get an adjective phrase, it tends to go to the
right. But you get what Dan calls the n-ed construction, something like
"the three-legged dog". That is a prasal construction, but can still fit
into pre-noun position.

There are also other places where, depending on the head, the head-comp
phrase still counts as \[LIGHT +\], and so in the matrix, borrowing from
the ERG (version of 2001), we say the LIGHT value of the head-complement
phrase's mother comes from this other feature called HC-LIGHT of the
head daughter, where the head DTR gets to basically say what it is
doing.

Generally, whenever we want to use LIGHT in other grammars, I find
myself tweaking things. So far, I haven't had to make modifications to
matrix.tdl, but that's just because we haven't got as big as what you
are doing with ZHONG

ZZ: What is the difference between HC-LIGHT and LIGHT?

EMB: HC stands for head-complement. It's a feature that allows lexical
heads to say what the LIGHT value of the phrase should be when they
combine with their complement via the head-complement phrase. Somewhere
in the ERG, there are head-complement structures that count as \[LIGHT
+\]. We'll need Dan to come back online to find what they are. But I
suppose you could search the ERG for \[HC-LIGHT +\] and then find
examples.

Ping: Any example where this LIGHT feature is used in Chinese sentences?

ZZ: We have some places where we want to say that this rule shouldn't
apply to the phrases. It should only apply to the lexeme. And then, we
use \[LIGHT +\] to indicate that. For example, for resultative verbs in
Chinese. We want to say the two verbs we're combining must not be
phrases already. So, we use \[LIGHT +\] to say that this node must be a
word, and that it hasn't formed any phrase yet.

For example: Chi-bao 吃饱 "eat full". This is the resultative structure
combining two verbs "eat" and "full". When we do this, we shouldn't
allow the first or second verbs to be some phrase already formed by some
other rules.

So in the rule I have put as an example, rslt-compound-phrase, we want
to make use of this feature to say that its head daughter is \[LIGHT +\]
— it's a word — and its non-head daughter is also \[LIGHT +\] — another
word. And then, in other rules, after we have done the combining, we
want to put in a \[LIGHT -\] there so that they will not go through the
same rule, recursively, again.

LL: Is this problem caused by tokenizer, where the tokenizer did not
understand whether it is a phrase or not?

ZZ: No, it shouldn't be tokenized together, because you can have
something in between. You can have 吃不饱 ("eat not full").

LL: Ok. Does the same feature occur in Japanese then?

FCB: Off top of my head, I can't remember. I think we do something else
when we do the VVs

Woodley(?): I think it will occur in Thai, and I'll have to look into
using the LIGHT feature in the same way, if that's what it's meant for,
because we can also insert a negation in there, but we definitely want
it to be lexical only. And I was thinking of the resultative; same
example that you mentioned.

EMB: ZZ, another thing I want to say: I was surprised you said there is
no relative clause in example \#8.

ZZ: In a strict sense, not the same example as 1, 2, 3, because the noun
there is not one of the subject, object or indirect object. In this, we
are saying "room" is the place where this event happen. In some other
examples, we can even have a head noun which is referring to an abstract
concept, like "the problem of assigning this feature to grammar", where
"the problem" is not an argument in the sentence, but actually refers to
the whole thing.

So, strictly, this should not be treated the same as the other examples,
as we don't do any SLASHing here, and we shouldn't link them together.
So that's why we need a separate rule or lexical type.

EMB: So I think there might be three different things that might be
going on. This one, to me, looks like it is actually an extracted
adjunct. Maybe what's a little surprising about that is that, if it were
not extracted, it would need some sort of adposition like ZAI 在. But
you get this in other languages, so I won't be surprised if there were
some languages that don't like or want you to relativise on adjuncts.
But English does, and I won't be surprised that Chinese does.

So, if you look in matrix.tdl, it probably has an extracted adjunct
rule; I probably saved that from the ERG. And then, the interesting
question becomes how you will link the SLASH value of DE with "room", in
this case, because if the extracted adjunct — this is the place where
you might want to look ahead to topic-comment structure, and see what
happens there and if you can do adjunct extraction. And what shape is of
the filler, as opposed to the gap.

Second possibility for the problem case is actually not a modifier but a
complement. In English, we get examples with the head-noun "fact". So,
"the fact that everybody knows" is ambiguous, between fact being the
filler of the missing argument of "know", or "fact" being a complement
taking noun and so "the fact that everybody knows that thing", where
"that thing" and "fact" are not co-referent.

And the third possibility is the examples you get in Japanese too, where
there really is absolutely no role for the head noun in a relative
clause, adjunct or otherwise, and it's actually just a topic-comment
structure. But I don't think that's what's going on in \#8. It looks
more like an extracted adjunct.

ZZ: So we should have an extracted adjunct rule to allow that, and then
do it similar to the extracted argument?

EMB: That's what I would suggest with this one, yes.

FCB: Currently, we give it the semantics that looks very much like
topic-comment, or an adjunct. We basically say there is some relation
between "Zhangsan" and "(...)", and we don't very much about what that
relation is. That's why we call it associative; that there is some
association between "room" and "write". I don't know how to extract an
adjunct. Can you say a little more about that?

EMB: If we look at matrix.tdl, there is a type called
extracted-adj-phrase, and it basically is a non-branching rule again, it
says the Mother has a non-empty SLASH value, and that non-empty SLASH
value has its MOD value hooked up with the various bits of the Mother,
so we're basically saying we can put onto the SLASH list of this element
something that semantically is supposed to be a modifier.

Now in English, the example \[\], since we have a special kind of
relative pronoun that says the noun that it is modifying here is going
to function as a place or time modifier of this syntactic clause. But
Chinese doesn't have relative pronouns, right? So the question is, could
we have either DE or the extracted adjunct phrase put into the
relationships? I'm not saying that the associative thing is wrong,
especially if you also get the topic-comment ones that are akin to the
ones in Japanese.

"トイレ に 行けない CM" (toile ni ikenai CM) \["Commercials that you
can't go to the bathroom." It means the commercials that are so
compelling that you have to stay and watch. No role for "commericals" in
that embedded clause/relative clause. So if you have those, it becomes
less appealing to create separate analyses for the abstracted adjunct
one and because you'll probably always going to get that ambiguity.

### Question 4: when using bare-nominal-phrase to implement nominalising DE, (where we can have a relative clause referring to an non-existing noun in the structure, or we can also have an associative DE being nominalised in that way) we found adding in "p" to head causes prepositional phrases to be pushed up to be NPs. What's a better approach?

EMB: A goodmodel would be... Dan has a non-branching rule that takes a
certain kind of noun and turns them into adverbial modifiers, and so
this is for nouns like "today", and a few others. And here, I think he
just uses a feature that pick out the class of nouns that are allowed to
do that, and that restricts the rule, really, and so the exact (?) of
the rules are not quite the same, but the way he picks out certain class
of heads down inside those phrases is maybe akin to what you need here.

FCB: We can have this feature possibly for multiple POS classes. We want
to do it with classifier phrases, with DE, we maybe want to do it with
demonstratives. They all have this feature "bare noun".

EMB: Yes, provided they fit in semantically the same way with the
generic\_n\_rel that you are adding, that shouldn't be a problem.

FCB: Dan, do you know what that feature is called?

Dan: No, but I'm thinking more that it's like the partitive construction
that are used for turning various things into noun phrases. So,
something like "the unexpected", which is an adjective that turns into a
noun phrase, or a determiner like "some' or many", turning into a full
NP.

FCB: Yes.

Dan: I think in those cases, I probably have two rules, not one — I
couldn't combine them into a single rule — and then I enumerate the...
with a slightly more fine-grained set of head types; I used multiple
inheritance in the values of the feature HEAD, to say that this guy is
not a preposition, and is something that should undergo this rule.

So I call it a partitive, or some kind of pre-nominal, or something
(pick a name that is mnemonic for you), and then those lexical entries
or phrases that you want to undergo that conversion rule, those head
values could be of this particular subtype, and nobody else could be.

So by introducing multiple inheritance into the head type hierarchy, you
can group a collection of head values, of whatever you like \[muffled\].
And then a new rule can say that my daughter is something of that head
type, whatever unifies with that guy can come into this rule. And I do
that rather than adding another feature into the feature structure,
which I think (...)

ZZ: Similar to what Francis has suggested.

Dan: Yes. Same philosophy. I'm trying to sketch a bit more of what the
mechanism might be. There's the temptation always to add more features,
because one can kind of see those, but I think there is a little more
elegance and clarity in putting a little more work into the type
hierarchy for the head values.

FCB: So specialising the part-of-speech \[muffled\]

Dan: So, specialising... but maybe even going in the other direction,
generalising. So, if right now, noun and verb and preposition are all
subtypes of just part-of-speech, and that's the only parent, you could
say there is another sub-type of POS called "promotable". And then,
let's say prepositions and verbs will also be sub-types of "promotable"
(but nouns will not be), then we can promote anything that is a
preposition or verb via that rule, because the rule would say that its
daughter has type promotable.

EMB: I'm not sure it's going to work in this case, though, because we
are re-suing the head-type "prep" for the actual prepositions and DE,
which shows up as a post-position in this. So if they want to do that
kind of cross-classification (?), they might have to distinguish between
prepositions and post-positions, which might have a shared mother "AdP"
or something.

ZZ: Actually they are there. There is a PrepP and PostP. So maybe we
should use PostP instead of PrepP for DE.

EMB: Yah.

Dan: You might be right.

FCB: So we need to complicate our type hierarchy a little bit.

**\[ Thanks to everyone who participated in this VLAD! :smiley:**

Last update: 2016-03-17 by ZhenzhenFan [[edit](https://github.com/delph-in/docs/wiki/LADChineseRelatives/_edit)]{% endraw %}