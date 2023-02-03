{% raw %}## ''Not all those who wrote opposed the changes.''

    h7:_all_q_rel(x6,h8,h9)
    h7:not_x_deg_rel(e10,u11)

- *Most but not quite all...* &lt;- can't lexicalize these as complex
predicates
- all those -&gt; partitive
- those -&gt; \_those\_q\_dem\_rel, generic\_entity\_rel

Why \_those\_q\_dem\_rel and not \_this\_q\_dem\_rel? We don't do
\_you\_n\_rel

Are there any differences between *those* and *that* as quantifiers?

- *those who*
- \**that who*
- ??*that one who*

\_lemma\_pos\_sense

Claim is that those/that are different "inflected" forms of the same
lemma

More general question:

- How do we decide what predicate names to use for quantifiers?

## ''A similar technique is almost impossible to apply to other crops, such as cotton, soybeans and rice.''

    _similar_a_to_rel(e9, x2)
    comp_rel(e10,e9,u11)

*A chair similar to Abrams arrived.*

Comparatives are a relation between a property and a reference set; the
way the reference set can be described is highly variable; dimension is
the inherent argument of the adj (or NP) being compared (ARG0 of the
adjective = ARG1 of comp\_rel) ARG2 is the reference set

- ... *taller than* : *than* should be semantically empty
- ... *similar to* : *to* should also be, but isn't currently (the
pred value for similar already has 'to' as a marker for the
generator)

Other lexical entries contributing comp\_rel: *different*

That type (comp\_rel) exists, and is clustered with some non-trivial
syntactic properties:

- That similar one to this one.

The machinery to do the long-distance thing here requires access to the
comp\_rel. Could split that to allow the lexicalized (*similar*,
*different*) ones to be single predicates while the derived ones
(*shorter*, *more beautiful*) have two predicates.

This choice is thus driven by composition, rather than by the resulting
representations, but does lead to a parallelism in the representations.

Design principles: decomposition is desirable, but not a goal in itself.
If the predicates required for decomposition exist, then it is good.

Compare relational adjectives:

- angry\_a\_at(e,x,y)

But that's a very different sense of ARG2, and since we don't have a way
of what we say they mean. So it's nicer to have comp\_rel. But if we had
\_similar\_a\_comp\_rel, that might encode the distinction too.
\_tall\_a\_comp\_rel? If we were decomposing those strings, maybe, but
not easily (if at all) for the periphrastic ones.

That solution also runs up against: \_similar\_a\_to\_rel: tells the
generator (via trigger rule) which particle to pull out.

comp\_rel introduces an ARG0. Is that comparison event something that
has temporal-spatial existence? Can be referred to? It is existentially
quantified...

Driven to it by trying to make adj & adv parallel, but it has some
precedence in the semantics literature. Ann can provide references that
back it up. In these cases, the e refers to a property.

Should we come up with a third type that is a property? verbs = event,
adj = underspecified, adverb = property. (Sometimes adv are i in current
grammar, to try to get at this, but underspecified between x and e isn't
really right.)

    e := i
    x := i
    y := i ;;; properties

Except we might want more intermediate types (placeholder names for
now):

    e-or-x := i.
    e-or-y := i.
    x := e-or-x.
    y := e-or-y.
    e := e-or-x & e-or-y.

attributive adjectives underdetermined: can be events in German *the
brown in Spring lawn* (*Der im Fruehling gruene Rasen ist jetzt braun
und ausgetrocknet.*)

- *That problem is harder than anybody expected.*

-&gt; the reference set is sometimes referred to with clause. So the
ARG2 of comp\_rel is sometimes x and sometimes h, like the ARG1 of
\_bother\_n\_rel. Thus in the LF, we'd need to resolve comp\_rel to one
of two predicates on the basis of the ARG2's type.

If comparison is between two sets along some dimension, why is comp\_rel
only two-place? The third one is there --- take the adjective rel & comp
rel together as a unit, and all three elements are there.

comp(e11,e9,u10)

Are we worried that u10 is unbound? That's fine. Is it INI or DNI? Not
represented, but this issue does connect to anaphora resolution and
whether these can be understood in context.

Does the binary approach to coordination also relate to anaphora?
(Aren't we asserting that the smaller group is something that can be
referred back to? Maybe with particular intonations that's supported?
What about testing gender on plural pronouns?)

- *John, Mary and Kate went to the park. The girls didn't bring their
coats.*
- *John went to the park. Mary went to the park. Kate went to the
park. The girls didn't bring their coats.*

Definites can introduce new groups more easily than pronouns, so if we
could construct an example where the gender on the pronoun required
Mary+Kate only (not possible in English), might find acceptability
differences.

\_and\_c\_rel: introduces an i ... should it be an x? Probably.
Shouldn't the quantifier do it? (And keep using \_and\_c\_rel for both N
and V.)

Is *electronic* in *distribute electronic and computer building
products* N or A?

Don't get A in the middle of N N compounds except if the A-N combination
is lexicalized: *\*camera blue parts*, *company annual report*, so
that's possibly a test, though it's not feasible to enter all the
lexicalized ones into the lexicon.

... discussion of whether we could block this in generation. Would
require having an underspecified representation (between A-N and N-N) so
that the generator could deal with the input.

There are lots of cases in English where it's basically impossible to
tell whether something is an A or an N.

Was there ever an underspecified A/N gen lex entry? Or some attempt at
cleverness regarding using the mass-count gen entry to handle the
unknown word's A tag. &lt;/ancient history&gt;

Los Angeles listed as a single element (MWE), but plan is to remove them
in favor of composing proper names.

Also taking out of the lexicon a lot of the single-word proper names.
Except for those in old treebanks parsed without POS-tagging unknown
words.

- *John and Mary Brown bike/\*bikes to the store.*

Right-headed analysis of compound names is wrong.

- *Abrams Browne arrived*

Two quantifiers, one for each proper name, compound\_name\_rel joining
the two.

When changing the syntactic structure, should the mapping between the
ARGs of compound\_name\_rel and the two names be the same, or opposite?

Can we get down to one entity (one quantifier) for Kim Smith?

Then should *Kim and Sandy Brown* be *Kim Brown* and *Sandy Brown* as
the entities? (Out of reach for composition.) But maybe *Kim* and *Sandy
Brown* being the entities is an okay approximation (not quite right, but
compatible.)

How many entities in *New York Stock Exchange*?

What about *University of Chicago* and *Cambridge University*?

That's a productive way to name universities. But how do we know which
ones are productive and which ones aren't? "university" is in the
lexicon. But so is "gates". (cf. Bill Gates).

ICONS relationship between the two to say they denote the same thing.
Doesn't have to be done by the grammar (*University of Washington* ...
the two entities don't refer to the same thing). Some external component
could make that call and give the ICONS constraint.

Previous meeting: could we drop quantifiers on pronouns or proper names?
Maybe pronouns, but definitely not proper names.

What are we doing with number names? The numbers are adjectives and so
have i-type ARG0s, not x-type.

*New York Stock Exchange* -- grammar provides the analysis where all
four are proper names, but the one that Dan treebanks is *New York* as a
proper name and *Stock Exchange* is an NN compound.

*John Robert Charles Smith* --- grammar gives ambiguity in the branching
structure.

- \[Emily \[Menon Bender\]\]
- \[\[Mary Ann\] Smith\]

Is the relationship between the parts of a last name different than that
between first and last name and between first and middle or two part
first names? Can we see what we're doing as an underspecification of
that?

*Pacific South West Lumber* -- can't tell what the company thought the
bracketing should have been.

Are there some cases where we can say that one bracketing is preferred
to another?

Can we say we're building up a name and make the actual entity turn up
at the end? Can we say that the entities for the name parts are
referring to the names, and then put in a unary rule at the top to put
in the person entity?

Can't do one proper\_q and two named\_rels with the same ARG0. Breaks
DMRS. Would rather that those are anaphora.

    name(x1, "Kim")
    named(x2, x1)

*The most popular names this year were Kim and Sandy.* &lt;- could model
that, but would lead to a terrible proliferation of ambiguity.

    name(x1, "Kim")
    named(x2,x1)
    proper_q(x2)
    name_q(x1)

- *Kim left.*
- *Kim of Avonlea left.*

<!-- -->


    moniker(e-or-y1, x2, "Kim")
    named(x2, e-or-y1)

Just one entity per complex name. Ambiguity for *Kim of Avonlea* or
*University of Cambridge* still but not for *John Smith Brown*, at
least, all of the different structures would still have only the
quantifier at the top.

moniker is adjective-like; in fact very similar to the card\_rel and
then we don't need to separate rels.

    named(i, x2, "Kim")

... and then only the head gets the I specialized to x.

- Kim Smith
- Smith Kim

semantically different? Yes. Which one gets the x is different.

- Kim Smith Jones
- Kim Jones Smith

will come out looking the same, modulo character positions if the names
are just modifying each other. If there is a compound\_name\_rel, then
the order of attachment is recorded.

Do we want to have access to the order of words in the semantics?

We are using it so far for: *John slipped and fell* (temporal order) and
*fish and chips* != *chips and fish*.

What about the top-most named-rel --- there is nothing for its ARG1 to
point to.

    proper_q(x1, h13, h16)
    named_n(x1,"Kim)
    named_a(w3, x1, "Smith")
    sleep(e7, x1)

Names are underspecified as named(ARG0:, CARG:) because when they join
the construction always knows which is head and which is modifier, can
specialize to named\_n and named\_a.

    named_n := named-rel
    named_a := named-rel

Abstract type not a string, so can even be done now.
<update date omitted for speed>{% endraw %}