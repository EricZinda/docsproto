{% raw %}## Notes from the LTG MRS Reading Group meeting 5-feb-2013

### Summary

We were somewhat surprised to reach the conclusion that the scoped MRSs
might be the best starting point if we want to use MRS information to
approach the \*SEM shared task data. In particular, we developed a
two-part rule which we think might cover a large number of cases.

    1. Assuming the negation cue has been identified, pick the fully resolved MRS in which that cue has the highest available scope, except:
    
    2. When the negation cue is NP negation, do not choose any scope in which the negation cue scopes higher than verbs which outscope the finite verb that the negated NP is an argument of.

Part 2 is not relevant for adverbial negation. It may possibly be more
simply stated as "Nothing but quantifiers may scope between the negation
cue and the verb which the associated NP is an argument of." Test case:
*Kim probably saw no apples.*

### More detailed notes

Looking at examples from the \*SEM shared task corpus, starting with:

    {Have} <no> {hesitation in lighting one}.

oe: Introduces the task, reminds us that if we do want to pursue an
MRS-based approach, we should review the U Groningen system in [Basile
et al 2012](http://www.aclweb.org/anthology/S/S12/S12-1040.pdf), which
was the only semantics-based participant system in the original shared
task.

MRS gives N' as in scope of quantifier (h12 qeq h13) --- actually only
hesitation and in MRS underspecified scope of no relative to have

Rule in annotation guidelines: if the object is negated, scope is over
the whole clause headed by the verb. How can we make that precise?

oe: x9 is in the scope of ... EB: for what we mean by scope in MRS, x9
isn't part of the scope tree in an interesting way

JTL: Depends on what they mean by scope; sounds like it could be h12 +
h11 EB: depending on what they resolve to

For the \*SEM guidelines, *I ate no apples* is paraphrasable as *It's
not the case that I ate apples*.

ERG analysis has 14 scope resolved forms, in which \#6 **no\_q** has
widest scope

But otherwise, there are pronouns that escape the scope

bec: How often do the MRSs resolve? Rarely tested. oe: estimates 70-90%
of the time

EB: Given the annotation rule, could we say:

- find any tensed event for which the negated x9 is an ARG2
- find scope resolutions in which the predicate associated with that
event is within the scope of the negator
- worry about pronouns ... maybe back in the syntax? (N')

JTL: *The cat ate no apple* is ambiguous between two readings:

- whole sentence is negated
- cat is outside the negation

MRS hides this by leaving that underspecified (we don't have to do that
part). The ambiguity is clearer with *Every cat ate no apple.* where
different relative scopes of *every cat* and *no apple* lead to clearly
different readings.

EB: What questions would you ask native speakers to establish that
similar things hold true in other languages?

JTL: It's predicted but the rules. Not defending it, it's just what we
see when we do the scope resolution.

\[ Discussion of all the scopes we get because we're so generous with
quantifiers, leading to the observation that the UTool developers made a
system to cook down the large set of fully resolved scopes to the
smaller set of truth-conditionally ones. See ACL papers [Koller and
Thater 2006](http://www.aclweb.org/anthology/P/P06/P06-1052.pdf) and
[Koller, Regneri and Thater
2008](http://www.aclweb.org/anthology/P/P08/P08-1026.pdf). \]

JTL: There are also syntactic restrictions that are not reflected here.
E.g., quantifiers of each part of the compound should stay together.

oe: Flickinger/Copestake repeated claim there are no scope islands in
English.

JTL: Compounds not the same as scope islands. Haven't thought about it
before, but it seems like these compounds that introduce sort of
spurious quantifiers shouldn't scope separately. Not really an island
(not about the context) but that they stick together.

(EB: Anyone know what the name of floating clumps of vegetation is?)
(JR: Wikipedia gives "floating island", "pumice raft")

Worked through *Every cat didn't run* in FOPL and then in MRS.

JTL: could have added to the MRS that h5 (body of \_every\_q) qeq h11
(label of verb), but that comes from the restriction on well formed
scope resolved MRSs that all variables must be bound.

Playing with scope resolution:

*every cat didn't chase a mouse* 6 readings

*every cat chased no mouse* 2 readings

*a cat didn't run* 2 readings

*no ghost showed up* 1 reading

*a ghost didn't show up* 2 readings

-&gt; but in the \*SEM annotation, these are probably treated the same

JTL: With simplex sentences, take the maximal scope for the negation to
match the guidelines. But with embedded sentences, what happens?

*Kim said no cats ran.* Bug report to Dan: That doesn't scope because
third argument of **say\_v\_to** is x but not expressed.

EB: Do not go above verbs which outscope the finite verb which the
negated NP is an argument of.

*John believed that the mouse didn't arrive.*

-&gt; Want negation below *believe*, but also want *mouse* below
negation

oe/EB: Works if we say, "Highest" plus that other constraint. Don't have
to worry about the subject of the higher clause because the constraint
on no unbound variables isn't putting it inside the scope of the
lower-clause negation.

oe: Any other potential counter examples?

EB: Neg raising, given how it's probably handled in the annotations:

*John didn't believe that the mouse arrived.*

bec: What about negative prefix examples?

... looking for examples where the ERG has a chance.

*The mouse is misplaced.*

oe: Challenging for our MRS based approach, because there are a lot of
morphological negation examples that are prefixes. ERG analyses a few of
these prefixes productively.

mis-a\_error\_rel is not a scopal thing in the MRS.

bec/EB: MRS probably not going to help with these

oe: decompose **\_unsolved\_a\_1\_rel** into **neg\_rel** plus
**\_solved\_a\_1\_rel** with a qeq between, via post-processing rule,
and then maybe the proposed rules will just work EB: label from
**\_unsolved\_a\_1\_rel** is now label of **neg\_rel**,
**\_solved\_a\_1\_rel** gets a new one

Bug report: *The problem was not solved.* -&gt; does not scope, again
because of unexpressed x variables, from both relational noun problem
and passive solved.

*The chair was not old.* 2 readings

JTL: problems from compounds?

*John believed the chair was not old.* 4 readings

neg\_rel doesn't have the same degrees of freedom as nominal negation
-&gt; don't need the second part of the strategy, because the neg\_rel
is more fixed than quantifiers. Can just pick the highest scope
available.

*The garden chair believed no mouse barked.* 7 readings

EB: no unbound variables rule keeps both garden and chair above believe

JTL: both qs for garden and chair have to outscope **compound\_rel**,
and chair's q has to outscope **believe**

*The chair never arrived.* 2 readings

oe: Seems like *never* is just like *not*, add to list of negation cues

*Found dead without a mark upon him.* *The chair arrived without a
garden.*

oe: Jan Tore, is that negation?

JTL: Depends on how deep you want to go into that analysis. *without a
garden* -- there doesn't have to be a garden, so it's hard to say.

JTL: If intensional verbs are scopal, shouldn't be a problem that Ps are
to.

EB: Won't be floating scope, like NP negation ... but maybe that's okay?

JR: Annotation guidelines say that scope is always the complement of the
P.

    {Some people} <without> {|possessing| genius} have a remarkable power of stimulating it.

--&gt; annotation error, all agree. Inconsistent with guidelines, JTL
says wrong semantically too.

bec: diff in meaning between

*The chair arrived without a garden.* *The chair arrived with no
garden.*

JTL: In principle without version is more ambiguous.

oe: Because negation is separate from the quantifier, and so they can
scope (somewhat) independently.

Last update: 2013-02-06 by EmilyBender [[edit](https://github.com/delph-in/docs/wiki/WeSearch_StarSem_MrsReadingGroup/_edit)]{% endraw %}