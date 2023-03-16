{% raw %}How can the HPSG and Universal Dependencies communities benefit each
other for some integration? Alexandre Rademaker

FrancisBond: There was some work some time ago using
CoNLL dependencies to constrain the output of parses in delphin to build
a partially annotated treebank from there (or as a first step in
annotation). It was reasonably successful. There were small issues due
to tokanization differences. One dependency produced by Stephan Oepen's
group in Norway filled a "lexicalized thing" from this so that was more
similar to UD, so there is code to do that.

AlexandreRademaker: Good to know!

BertholdCrysmann: Treebanking is one of the big
bottlenecks in grammar engineering. Can the scribe provide a pointer to
this success? Pointers (thanks, Francis):
<http://www.aclweb.org/anthology/W09-1204>
<https://folk.uio.no/rdridan/papers/iwpt13-dt.pdf>

DanFlickinger: As far as converting to/from UD, you can
restrict yourself to the big stuff and leave fine points are
under-determined, as Stephan did.

BertholdCrysmann: Even with partial disambiguation,
you should be able to train models on that. You have to throw a lot of
data at it for the domain.

JohnCarroll: So it's domain specific (the dependency
parsers)?

BertholdCrysmann: Yes

AlexandreRademaker: Depending on the parser, in
the case of Portuguese, some parsers fair badly with morphology.

AlexandreRademaker: We started with a rule based
grammar and refined based on a corpus- surely we're not the only group
to do that. This is good for checking annotation consistency.

EmilyBender: DMRS to UD doesn't make sense because that
would be mapping semantics to syntax. But there is a dependency that
comes off of our syntax trees, so we could do that mapping. But why?
That's a lossy mapping. We have more info than UD. Is it just to give UD
more data?

AlexandreRademaker: It could help to advocate in
favor of HPSG-- we (DELPHIN) could help improve UD trees. This sounds
like a political question, so it's difficult to answer. One point I'd
like to raise: from my position in the industry, most people don't care
about precision. So we (industry) want to benefit from more parses, but
we don't want to be the sole owner of a grammar that never gets used
again. We want to get grammars on top in industry, but our priority
isn't precision, it's maintaining and increasing. Being connected with
huge data communities benefits both groups.

BerndKiefer: Coming back to the old idea of hybrid robust
processing could be interesting. If we combined UD and HPSG in cases
where we can't get a good parse, that could indicate where we need to
relax constraints. This can hint at ways to improve both grammars. There
is a lot in there for the "medium level expert".

GuyEmerson: One benefit of delphin to UD is a plug for
delphin tools. This is a selling point for us.

EmilyBender: Maybe our UD annotations would be even more
consistent than theres.

GuyEmerson: We could go from our parse tree to UD in a
similar style to DMRS.

EmilyBender: Antske did something like this. Maybe it
wasn't UD standard.

GuyEmerson: So we could coerse that into the UD framework.

DanFlickinger: There was an attempt to map the Alpino
treebank to UD. So there's code. There are 50 lines that do almost
everything and 1000 lines handling small cases. We could do something
analogous to get the big stuff with small effort. I think that's the
most tempting reason-- to package this and make it usable, make it
visible and get feedback so that we can refine. Some other groups are
tying to do this (LFG). It's expensive so give it to a grad student.

AlexandreRademaker: I've suggested to my people
that they can mine trees in treebanks for information. They acknowledge
that this is a good idea. So I think what Dan suggests is something that
i could interest my clients in. We start with small course tree and
build to something richer/more fine-grained. Real projects could
benefit.

BertholdCrysmann: follow up on Dan's comment about
Alpino- do I remember correctly that the semantic output is already kind
of a dependency structure?

DanFlickinger: Yes. It's still syntax. We shouldn't try
to map our semantics but our syntax surely.

EmilyBender: I overheard at Olso that they want to
convert UD to DMRS. Is that happening?

DanFlickinger: I don't know. There was uncertainty how
useful that would be. The mismatches in fundamental things (ambiguity
etc.) is more annoying than interesting. A lot of information can be
lost. Ultimately it was ruled uninteresting, not unuseful. But the
question is what's the motivation?

EmilyBender: I thought it was to learn more about
composition.

JanBuys: One advantage to leverage UD representations is to
improve coverage. For example the lexicon in our grammar might be
restricted-

EmilyBender: Bootstrap that coverage to improve lexical
disambiguation?

JanBuys: Exactly. It wouldn't be perfect but it could help

JohnCarroll: There have been discussions going back a
ways- years ago we produced a set of 500 sentences that were annotated
and someone else produced 500 and we compared them and in fact got very
different outputs with different dependency annotations.

DanFlickinger: But one goal of UD is a standardized
system. The idea was: don't do pairwise mappings- do one time mappings
to ud and compare those.

JohnCarroll: In those days it was just about comparison,
now its about training purposes.

JanBuys: In the other direction- would it be possible to use
the grammar to make the UD annotation process more efficient or
consistent? Only for dependencies (not MRS), they can leverage our
infrastructure.

AlexandreRademaker: Yes, that's the first thing I
thought of. Our Portuguese UD bank is small and we'd like to grow it
quickly. Any tool to help with consistency would be a huge help.

FrancisBond: Oslo has been working on this-- Dan, is
there a DM to UD converter?

DanFlickinger: A script form MRS to DM exists.

EmilyBender: That's just for semantics. There is a script
for syntax as well.

DanFlickinger: But i don't know if there is one to get
to UD. Stephan would be a good person to talk to about this.

WeiweiSun: You could just use a statistical model for this.
There are many treebannks for Mandarin and many papers discuss this kind
of conversion to create heterogeneous treebanks, so we don't need to
reinvent this from scratch. Another thing- why UD?

AlexandreRademaker: Because Google, Stanford an
Prague were the first three big groups.

DanFlickinger: An attempt at a positive spin on why
these are so popular is that they take on a very interesting problem-
there is an intersection of interests among research groups- not a total
overlap but there is non-empty intersection. Most groups can make use of
something in those treebanks. Language independence is one of those
interests. There are levels of representation that are of some use to a
variety of groups (even typologists).

AlexandreRademaker: What Dan just said is
summarized by Manning.

DanFlickinger: Manning's Law does hit on this.

EmilyBender: And it's a good name.

JohnCarroll: And they've learned from CoNNL.

Last update: 2018-06-20 by KristenHowell [[edit](https://github.com/delph-in/docs/wiki/DiderotHPSGandUG/_edit)]{% endraw %}