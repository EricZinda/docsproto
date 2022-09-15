{% raw %}## Matrix Feedback

### Scribe: EmilyBender

Antske: Original Matrix comes from the ERG, edited with reference to
Japanese and German and a few things people knew. Not much has been
changed since (though some additions). When people create grammars based
on Matrix, often find things that aren't useful/that you want to
change/that are bugs. In building gCLIMB I came across obvious bugs that
surely others would have noticed before but no one told us. Also there
was a misconception that Matrix developers don't want changes to
matrix.tdl --- we do, we just want to know about them! When I was doing
gCLIMB, I kept notes on what I changed in matrix.tdl and also did the
spring cleaning algorithm (see paper with Yi Zhang and Emily). Can tell
you what types people don't use---either from the matrix or from
abandoned analyses in their own grammar. I have this vision that it
would be nice if you could use it in the process of CLIMBification. We
also measured how much was stripped of different grammars. It was
helpful for Francis, who took over a grammar---can't tell what's part of
unused analyses. He was quite happy with the list of all the things.

Antske: I looked at the types not used from the grammar matrix and tried
to classify them for why they weren't used --- phenomenon not used in
the grammar, alternative analysis (or bug fix) via new types or
overwriting types. That led to an overview, but it's a very preliminary
study. I think it makes a lot of sense to do this as a collaborative
study. In some cases, I had to guess. The only grammar we really know
this of is the Wambaya grammar -- Emily did an analysis in the current
paper.

Antske: Points to notes from [Tomar meeting](../TomarMatrix). Nothing much
happened, but I hope that if I make plans to work with people, since
that'll get me doing it. Ways of doing this: [ParGram](/ParGram) model
(probably not reasonable for us). Shared core grammar that everyone
actually constantly updates a la [CoreGram](/CoreGram), also probably
not reasonable.

Berthold: Comparison to [ParGram](/ParGram), isn't the point of
coordination for us the semantics, not the syntactic features? And
aren't the semantic aspects of the matrix pretty stable?

Emily: Yes, but there have been some changes: messages gone,
L-INDEX/L-HANDLE merge coming up. But we're also interested in hearing
about places where the syntax from matrix.core is actively unhelpful ---
not saying everyone has to do it the same way, but we want to know when
it's not working for you.

Antske: Some examples that have come up, e.g. branching of coordination
for Turkish, Korean.

Antske: And some things aren't very thoroughly tested (e.g. wh
questions?).

Emily: We're doing wh questions in class now, and definitely benefited
from your work as you fixed things for gCLIMB.

Antske: I still think there's interest in the pull request idea, getting
people to constantly stay up to date with the Matrix.

Emily: Maybe more interesting to plan a joint analysis project.

Antske: And reviving the matrix mailing list.

Berthold: Training a grammar engineer for French. Matrix has been a nice
starting point. For HaG, didn't take advantage of too many of the
choices, want a small core, all the rest done myself. Trying to train
someone else, I find a bit daunting There's a version with all the
choices stuff taken out again, and a version generated by the choices
file, so she can compare and try to understand. I fear if I throw all
the types that come from the Matrix at her, it's too passive. Hard to
gain confidence in changing things. Question: Who keeps this backwards
compatibility with the Matrix.

Emily: Best practice is CLIMB.

Antske: There is a bit of a learning curve, but it pays off. You put
analyses in choices files. Can play with analyses as long as you want.
Helps for backtracking. Better than just keeping grammar in version
control. Because you are constantly combining things -- get
self-documentation of what contributes to what, can test which analyses
work together.

Emily: I think you want to teach tdl in a small sandbox, and then go for
CLIMB. It's a bit more overhead, but much better for long-term
maintenance of the grammar.

Berthold: Any good references?

Emily: Antske's thesis!

Berthold: Anything shorter?

Antske: Ch 3, also ACL 2011 paper, workshop paper with Emily, LREC
paper.

Dan: Is there a minimal example somewhere?

Antske: The grammars I used in my thesis are all available, but
relatively big. The Dutch ones are smaller…

Joshua: Not so different from pulling the customization system source
code.

Antske: Was also interested in looking at the relation to the analyses
in the customization system, but to make it workable… That's also in the
SlaviCLIMB thing I made, and I cleaned out a lot of stuff from the
customization system that I knew we wouldn't be working with. Can take
stuff out of the customization system. If your goal is long-term grammar
development, but throw stuff away.

Emily: So SlaviCLIMB might be the right place to look for a small
example.

Antske: Will add to my todo list to make a very small CLIMB for some
language. And I'm happy to help anyone get set up with CLIMB. Email me!

Luis: [ClimbTop](https://blog.inductorsoftware.com/docsproto/tools/ClimbTop) talks about SHORTCLIMB and gCLIMB but not
obvious how to get the latter.

Antske: The link for gCLIMB is in my thesis, but I should add it to that
page.

Dan: And the SlaviCLIMB?

Antske: At DFKI -- need guest account.

Emily: This should be on the [ClimbTop](https://blog.inductorsoftware.com/docsproto/tools/ClimbTop) page too.

Glenn: Is the abbreviated path code you mention in your thesis required
for CLIMB or orthogonal?

Antske: Orthogonal … not required.

Glenn: So what's the motivation for the short paths? Are long paths
really that inconvenient?

Antske: It helps with alternative analyses that change the feature
geometry, like in the change to SYNSEM in the 1980s. But also because a
lot people are always asking for it. Also it checks for certain kinds of
errors.

Emily: Back to Matrix feedback, if people are using CLIMB (and stripping
down what they don't need from customization system), that would be
interesting too.

Antske: Can look at the changes that are made in existing grammars ---
analytical process of classifying changes. Also really like Emily's idea
of jointly working on particular phenomena.

Antske: Also interested in comparing to Stefan Müller's work and he
contacted us about writing, but we wanted to clean the Matrix first… The
question of what should be static and what should be dynamic/customized
is really interesting. A lot of stuff just not used because they're not
relevant to the language. There's a whole scale of how you could do
this. For example, the Portuguese grammar took a different stance on
certain principles, and that changed almost everything in the Matrix.
Then we have Petter Haugereid's way of dealing with subcategorization;
very interesting, but fundamental changes in how the grammar works high
up in the hierarchy. In the long run, do we want to have a customizable
matrix where we allow Haugereid sub cat.

Emily: Like Joshua's rmrs version of matrix.tdl, too.

Antske: Dan was interested in that for the ERG as well, but maybe more
of a CLIMB thing than a Matrix thing.

Emily: Laurie going to be working on coordination, and as part of that
will move coordination stuff out of matrix.tdl to the libraries.

Antske: We have things where there are all the options like
head-types.tdl, but when grammar engineers have a theory in their mind,
they start redefining it. For example Yi Zhang & Rui Wang's work on
Mandarin, wanted functional v. lexical head types. Keep giving all the
disjunctive heads? Those were the bulk of types cleaned out from the
grammars. Would be interesting to see which combinations people use. So
maybe even offering everything and seeing what they use.

Emily: But it's not a very friendly hierarchy. I think it predates
customization. Maybe better to just generate the disjunctive types
required on the fly and let people make their own disjunctive types.

Emily: Target of spring cleaning was matrix core and not customization
system, right?

Antske: If you did everything right and used the CLIMB method, it should
remove anything except what's in Matrix core…

Berthold: If you have to radically change the way some feature passing
is done e.g. to get multiple slashes going. I tried to have a matrix.tdl
that I left intact, plus fundamentals.tdl where I started overwriting
those types. If it's trivial changes. Had to redefine
basic-binary-phrase; didn't want alternative versions flying around and
my editor/lkb coupling showing me the wrong one. So I gave up trying to
do this layers. The next step I foresee is when I want to do edge
features.

Emily: Edge features are easier because they can be done with type
addenda. Also, we have L-PERIPH and R-PERIPH (from ERG), used in
Antske's word order stuff, also treatment of 2nd position phenomena in
567 grammars.

Antske: Some languages you might not want separate SUBJ/COMPS lists.

Berthold: Or more than just SUBJ/COMPS. GG has more than just those.

Antske: But things you can put on the SLASH come from just one place.

Berthold: You might be thinking of my underspecified COMPS list for
partial VP fronting. Don't try to integrate those with the arguments of
the verb I haven't seen yet. If there weren't the cases two accusative
arguments, I might have gone the LFG way.

\[Technical discussion of German word order and GG\]

Antske: So what if someone wants to do just one list?

Emily: I think we're not expecting people to pull updates of matrix.tdl
that often, as the main value is in the MRS and that doesn't change that
often. So maybe in that case just encourage people to go edit, so they
can keep the benefits of what else is there. And wouldn't it be fun to
visit the alternate future where we get deep into CLIMB-ifying deep
things in the matrix, like MRS/RMRS/DMRS and SUBJ/COMPS v. SUBCAT v.
Haugereid-style.

Luis: Sanghoun, on arriving at NTU, updated all of our grammars by going
back to the customization system, and being able to do that was night.

Emily: Ah right --- probably especially getting the information stuff,
which was in the customization system & core.

TJ: And can also take stuff out. When I did adjectives, I took some
things out of the core.

Antske: If some people update only the core and we've moved e.g. the
coordination rules out, that will be problematic. Are we changing
versions numbers?

Emily: Relying on svn revisions. We'd noted one in a footnote in a paper
that Olga was trying to reproduce, and she was excited to find it.

Olga: But even with that I couldn't reproduce.

Antske: Sometimes that not enough for reproducibility. In my case
couldn't quite reproduce.

Emily: Why?

Antske: Choices files had changed…

Emily: So missing part of the data.

Emily: Back to the point of changes to matrix.tdl, we should get in the
habit of announcing all major additions/changes to the customization
system on the matrix mailing list. And on major bug fixes, like the
cockroach Laurie is working on.

Antske: **To summarize,**

1. changes to the matrix should be announced on matrix mailing list.
1. remind people that we always want to hear back when they're making
changes
1. I (Antske) should go back through the changes I report from my
thesis and see which still need to be ported.
1. paper on how people have used the matrix over time?

Emily: Someone has to be pushing that forward---but I anti-volunteer,
because I'm that person for too many other projects right now.

Antske: I can, after mid-July. Look at new changes to the matrix and
contact authors of spring cleaned grammars for their input.

Emily: And maybe invite others to be spring cleaned?

Antske: That code is still brittle --- have never managed to run it on
GG for instance. GG uses older tdl standards that we're not using in
matrix.tdl.

Emily/Berthold: Probably fixed now, if GG is running with ace.

Antske: The big grammars are perhaps too big for my algorithm.

Emily: \[looks at Glenn\]

Glenn: Well positioned to do that, and the key missing piece is detailed
in your dissertation. Would provide it as a command line that could be
run in linux or windows.

Antske: What helped with bigger grammars was to first run Yi's
compression code, which made it work for Jacy. Sometimes that leads to
types that aren't removed but could be (as explained in my thesis). The
code is open, but I'm not an expert programmer.

Luis: Where is it?

Antske: I have to look. If it's not on github already, I'll put it
there.

Berthold: I think it's the size of the type hierarchy in GG. The grammar
is pre quick-check. Moved all the distinctions done on HEAD & CONT up to
the synsem level --- makes a big grammar. Was done for efficiency
purposes back in the day.

Emily: github -- use the delphin space.

Emily: Target venue: Journal of Language Modeling

Antske: Will make a plan in mid-late July and email … who?

Emily: Suggest developers list to ask who wants to be involved and then
take it off-list.

TJ: Would it be reasonable to have people make changes in matrix.tdl &
try with regression tests and send a message to matrix-dev.

Emily: Would encourage people to send us suggestions without running the
regression tests themselves!

Antske: The spring cleaning algorithm can also clearly show us what we
could add in matrix.tdl. Underspecified head-spec type, that many people
seem to make.

Glenn: basic-head-spec-phrase COMPS on mother was identified with
non-head-dtr.
{% endraw %}