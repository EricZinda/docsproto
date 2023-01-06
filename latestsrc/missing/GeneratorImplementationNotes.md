{% raw %}This page contains a core dump of [WoodleyPackard](/WoodleyPackard)'s
brain after working on a DELPH-IN compatible generator.

Generation is the process of constructing a surface realization of the
meaning contained in an input MRS structure.

The basic algorithm for generation is quite similar to chart parsing. A
number of semantically contentful lexemes and rules are "activated"
(inserted into the chart) by virtue of a match between the MRS
predicate\[s\] supplied in that particular sign and one or more MRS
predicates in the input semantics. Additionally, a number of
semantically vacuous signs are inserted into the chart according to the
*trigger rules*. After chart initialization, lexical and syntactic rules
are allowed to run to exhaustion. Finally, all generated edges are
checked for compatibility with the input semantics, and the compatible
ones are output as the result.

Some notes for would-be generator developers. These notes are written
from the viewpoint of generating with the ERG.

- There is in effect only one cell in the chart. The adjacency
criterion for combinability of two edges is that the sets of input
EPs that they dominate are disjoint.
- To rule out the construction of edges in which the "wrong" MRS
variable combines with a predicate, we use a technique dubbed
*skolemization*. This means setting the INSTLOC property of the TFS
representation of each MRS variable to a unique string, such as the
variable's name. The effect of this is to block many combinations of
input edges that should not combine (e.g. paraphrasing *The black
cat ate a small mouse.* to *The black mouse ate a small cat.*) These
combinations would be rejected in the post generation MRS
compatibility test anyway, but generating them takes up a lot of
time.
- Along the same line, applying a "cheap scope" to the input MRS also
blocks many unwanted edges (e.g. paraphrasing *I think the cat
thinks the dog is asleep.* to *The cat thinks I think the dog is
asleep.*) An easy way to do this is to use the same skolem constant
(INSTLOC property) on the handles on the high and low side of the
QEQs.
- **Index accessibility filtering** is a technique to block the
generation of edges that *seal off* MRS variables that still need to
be combined with more EPs. For example, we would like to avoid
spending time generating *I see a cat chasing a mouse.* when the
correct result is *I see a cat chasing a frightened mouse.*, because
there is no way to form an edge that spans all of the input EPs from
*I see a cat chasing a mouse.* (in particular, the EP corresponding
to *frightened* will be unrealized). We would like to avoid
generating anything containing with "a mouse". In practice, we can
avoid going beyond *chasing a mouse* with this technique, which is a
large step in the right direction.
- At least for the ERG, a significant portion of the lexicon and rule
inventory are considered informal, i.e. suitable for parsing but not
for generation. Unfortunately, this distinction is not made explicit
in the grammar proper. The canonical list of signs unsuitable for
generation resides in the file "lkb/globals.lsp", in the parameters
\*duplicate-lex-ids\* and \*gen-ignore-rules\*
- Generating from non-native predications (e.g. the year 1973, or my
name) is a bit tricky. The ERG pulls this trick off with the
parameter \*generic-lexical-entries\*, which is a list of generic
lexemes to try when an EP in the input MRS does not match anything
in the semantic index (i.e. regular lexemes and rules).
- The LKB generator uses a head-driven rule instantiation ordering,
which is different from the key-driven ordering used for parsing.
This may make some difference in efficiency. **Update** I tried this
out. According to my experiments, key-driven generation is nearly a
factor of 2 *faster* than head-driven generation, so the LKB may
stand to gain a considerable speed-up from this trivial change.
([JohnCarroll](https://github.com/delph-in/docs/wiki/JohnCarroll)
adds: there were some misleading comments and variable names in the
LKB source - now corrected; the LKB generator has always been
key-driven, like the parser)

(Following notes added by GlennSlayden)

- When generating from parser outputs, lookup of lexical entries by
predicate name requires some care because, by design, VPM
round-trips are lossy with regard to a grammar's type *vs.* string
distinction. For **predicate names**, reverse VPM should prefer the
string when both type and string are available (e.g.
*\_week\_n\_1\_rel* in the ERG), whereas for **substructure
values**, reverse VPM should prefer type values (e.g. *3* in the
ERG). Of course, values for any features listed in the
\*value-feats\* (LKB) configuration setting (e.g. CARG) must always
be instantiated as strings. Note that there may be additional edge
cases depending on how strings are added to the grammar. For
example, if parsing the sentence "I have a pronoun\_q\_rel." causes
*pronoun\_q\_rel* to be added to the grammar as a string, then
following the heuristic above means that the string version will
incorrectly be set as the PRED of the quantifier rel. Finally, this
also points to a general problem with adding new strings to the
grammar in the course of parsing or generating: if runtime strings
are persisted in a global grammar singleton, then they may introduce
side-effects to subsequent operations.
- There is also an interaction between reverse VPM and the
\*sem-relation-suffix\* configuration setting. Consider for example
generating from the parse of "Cats eat dog food," where the input
MRS contains *compound\_rel*. Although "compound" will be found the
lexicon as a word, interpreting this discovery as sanctioning
"compound\_rel" as a string PRED is not the correct result; in this
case, (contrary to the above heuristic) the *compound\_rel* type
should have precedence.
- With the ERG, PRED values can be further specialized by grammar
rules. For example: In the city, I slept. Here, lexical entry "in"
contributes *\_in\_p\_rel* which is later specialized to
*\_in\_p\_state\_rel*. This means that PRED lookup for generation
must include supertypes, or equivalently, that LEs be indexed not
just by their PREDs, but further by all of their subtypes.
<update date omitted for speed>{% endraw %}