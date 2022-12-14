{% raw %}Some thoughts on mapping MRSs to Wordnet sense (mainly illustrated with
the ERG and PWN). Examples use a variant of the indexed MRS to save
space (part of the work on Lexical Semantics).

Contents

1. Single Words
   1. Proper Nouns
   2. Decomposed nouns
   3. Superlatives
   4. Different POS
2. Multiple Words
   1. Compositional Compound Nouns
   2. [Non Compositional Compound
Nouns]()
   3. Idioms
3. Phrases
   1. Coordination
   2. Light Verbs

## Single Words

In straight forward cases like this, each open class predicate maps to a
wordnet sense.

    The cat_{cat_n1} ate_{eat_v1} a dog_{dog_n1}.
    e3:
     _1:_the_q⟨0:3⟩[BV x6]
     x6:_cat_n_1⟨4:7⟩[]
     e3:_eat_v_1⟨8:11⟩[ARG1 x6, ARG2 x9]
     _2:_a_q⟨12:13⟩[BV x9]
     x9:_dog_n_1⟨14:18⟩[]

Mapping the predicates to lemmas gives us directly:

    x6:_cat_n_1 = cat_n1
    e3:_eat_v_1 = eat_v1
    x9:_dog_n_1 = dog_n1

Note that quantifiers are sometimes in wordnet, sometimes not:

    Each_{each_a1} cat_{cat_n1} ate_{eat_v1} a dog_{dog_n1}.
    e3:
     _1:_each_q⟨0:4⟩[BV x5]
     x5:_cat_n_1⟨5:8⟩[]
     e3:_eat_v_1⟨9:12⟩[ARG1 x5, ARG2 x9]
     _2:_a_q⟨13:14⟩[BV x9]
     x9:_dog_n_1⟨15:19⟩[]

Here we also have:

    _1:_each_q = each_a1

(with a non matching pos a &lt;&gt; q)

### Proper Nouns

For proper nouns (and numbers and a few others), the predicate is an
abstraction like named\_rel, and the value is in the CARG:

    Bast_{Bast_n1} ate_{eat_v1} a dog_{dog_n1}.
    e3:
     _1:proper_q⟨0:4⟩[BV x6]
     x6:named⟨0:4⟩("Bast")[]
     e3:_eat_v_1⟨5:8⟩[ARG1 x6, ARG2 x9]
     _2:_a_q⟨9:10⟩[BV x9]
     x9:_dog_n_1⟨11:15⟩[]

We want:

    x6:named = Bast_1

### Decomposed nouns

Some words are given complex semantics:

    A cat_{cat_n1} ate_{eat_v1} here_{here_a1}
    e3:
     _1:_a_q⟨0:1⟩[BV x6]
     x6:_cat_n_1⟨2:5⟩[]
     e3:_eat_v_1⟨6:9⟩[ARG1 x6]
     e10:loc_nonsp⟨10:15⟩[ARG1 e3, ARG2 x11]
     x11:place_n⟨10:15⟩[]
     _2:def_implicit_q⟨10:15⟩[BV x11]
     e16:_here_a_1⟨10:15⟩[ARG1 x11]

*here* is given semantics equivalent to "in this place". Ideally, we
would like a mapping such as:

    e10:loc_nonsp = here_a1
    x11:place_n = here_n1

with "e16:\_here\_a\_1" unmapped. "in this place" = here\_a1 and "this
place" = hear\_n1

There are not so many of these, it should be possible to do them with
exception handling

### Superlatives

Wordnet has some superlatives (linked through domain usage to
superlative\_n\_1): *best, worst, least, ...*

As far as I can tell, they are not actually linked to the relevant
adjectives!

I think we should tag these with the relvant adjective (*good, bad,
less; , ...*) and distinguish if need be by the presence of the
superlative predicate.

### Different POS

ERG collapses many adjective/adverb distinctions: they are all 'a'.
Wordnet often has them as different entries, linked with derivation
links. I lean towards collapsing them :-).

## Multiple Words

Sometimes both the ERG and PWN treat a MWE as a single concept, and then
it is easy.

    The cat_{cat_n1} gobbled_{gobble up_v1} a dog_{dog_n1} up_{gobble up_v1}.
    e3:
     _1:_the_q⟨0:3⟩[BV x6]
     x6:_cat_n_1⟨4:7⟩[]
     e3:_gobble_v_up⟨8:15⟩[ARG1 x6, ARG2 x9]
     _2:_a_q⟨16:17⟩[BV x9]
     x9:_dog_n_1⟨18:21⟩[]

The character mapping is a bit less direct, but the final mapping should
be just:

    x6:_cat_n_1 = cat_n1
    e3:_gobble_v_up = gobble_up_v1
    x9:_dog_n_1 = dog_n1

**PROBLEM** sometimes they will disagree. Postpone mapping for now.

### Compositional Compound Nouns

    The cat_{cat_n1} ate_{eat_v1} a guard_{guard_n1&guard_dog_n1} dog_{dog_n1&guard_dog_n1}.
    e3:
     _1:_the_q⟨0:3⟩[BV x6]
     x6:_cat_n_1⟨4:7⟩[]
     e3:_eat_v_1⟨8:11⟩[ARG1 x6, ARG2 x9]
     _2:_a_q⟨12:13⟩[BV x9]
     e15:compound⟨14:23⟩[ARG1 x9, ARG2 x14]
     _3:udef_q⟨14:19⟩[BV x14]
     x14:_guard_n_1⟨14:19⟩[]
     x9:_dog_n_1⟨20:23⟩[]

NTU WN tags both the single and MWE in this case, SemCor maps
only the MWE I think we want:

    x6:_cat_n_1 = cat_n1
    e3:_eat_v_1 = eat_v1
    x9:_dog_n_1 = guard_dog_n1
    x14:_guard_n_1 = guard_n1

A guard dog is a dog, which has something to do with a guard, so we
imply x9:\_dog\_n\_1 = dog\_n1 through the magic of hypernymy.

One could think of something like:

    x6:_cat_n_1 = cat_n1
    e3:_eat_v_1 = eat_v1
    x9:_dog_n_1 = dog_n1
    x14:_guard_n_1 = guard_n1
    e15:compound = guard_dog_n1

But this isn't quite right (works better for A&B}.

### Non Compositional Compound Nouns

    The cat_{cat_n1} ate_{eat_v1} a guard_{hot_dog_n1} dog_{hot_dog_n1}.
    e3:
     _1:_the_q⟨0:3⟩[BV x6]
     x6:_cat_n_1⟨4:7⟩[]
     e3:_eat_v_1⟨8:11⟩[ARG1 x6, ARG2 x9]
     _2:_a_q⟨12:13⟩[BV x9]
     e14:_hot_a_1⟨14:17⟩[ARG1 x9]
     x9:_dog_n_1⟨18:21⟩[]

Here, we don't want the semantics "a dog that is hot", so:

    x6:_cat_n_1 = cat_n1
    e3:_eat_v_1 = eat_v1
    x9:_dog_n_1 = hot_dog_n1

Ideally, the ERG should contain "hot dog" as a single entry, so that
things map even better.

### Idioms

*X keeps tabs on Y*

We don't really know how to mark the whole idiom (although the ERG
recognizes it)

*X doesn't know X's arse from X's elbow* "X is an idiot." ?Postprocess

How should we show this?

## Phrases

### Coordination

*grass and brown snakes* grass\_snakes and brown\_snakes ?Postprocess

### Light Verbs

*give a start* give\_start? Do we just make entries for all light verbs?

Many more corner cases to come :-): "Sleeping Beauty: is sleep v or n",
more complex MWEs, ... .
<update date omitted for speed>{% endraw %}