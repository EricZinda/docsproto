{% raw %}This page contains some notes on the lexical types used in Jacy.

There is also an [on-line
database](http://compling.hss.ntu.edu.sg/ltdb/Jacy_1301/).

## Postpositions

Postpositions connect two objects in the grammar.

Case postpositions (such as が, を, に) do not add their own elementary
predicate, but serve to constrain which argument of the predicate they
modify is filled by their complement.

Other postpostions are two place predicates, where the thing they modify
(typically appearing on the right) is the external argument (ARG1) and
their complement is the ARG2: ARG2 の ARG1, ARG1 は ARG2.

Predicates with preposition type semantics are introduced by some rules:

- relative-clause-rule which introduces topic\_p\_rel with the verb as
ARG1 and the noun as ARG2.
- wh-adv-sem-type which introduces unspec\_p\_manner\_rel
- adv\_np\_rule-type which introduces unspec\_p\_rel, changing date
nouns into pps.

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}