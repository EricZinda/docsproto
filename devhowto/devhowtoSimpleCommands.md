## Simple Commands
It is finally time to implement a "command" so that users can actually *do* something with the system we are building. We're going to implement the "delete" command.

We'll start with the MRS for "delete the file", which has a couple of predications beyond "delete" we'll need to deal with:
~~~
[ TOP: h0
INDEX: e2
RELS: < [ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _the_q LBL: h9 ARG0: x8 [ x PERS: 3 NUM: sg IND: + ] RSTR: h10 BODY: h11 ]
[ _large_a_1 LBL: h12 ARG0: e13 [ e SF: prop TENSE: untensed MOOD: indicative PROG: bool PERF: - ] ARG1: x8 ]
[ _file_n_of LBL: h12 ARG0: x8 [ x PERS: 3 NUM: sg IND: + ] ARG1: i14 ]
[ _delete_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ARG2: x8 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h10 qeq h12 > ]

***** chosen solution next *****

                                               ┌── _large_a_1(e13,x8)
                                   ┌────── and(0,1)
               ┌────── pron(x3)    │             │
               │                   │             └ _file_n_of(x8,i14)
pronoun_q(x3,RSTR,BODY)            │
                    └─ _the_q(x8,RSTR,BODY)
                                        └─ _delete_v_1(e2,x3,x8)
~~~

"delete the file" is straightforward except for pron
"delete every file": what to do if one of the files cannot be deleted?
    Best: do it transacted?
    Next: do it until we fail?
"delete the folder": maybe needs a planner to delete files first and then folder?
"describe the file" ditto except for how to print?

We will simply print out when something happens instead of doing it to avoid bugs ruining things.

Not sure if this is really necessary: Need to motivate why to implement special index variants of verbs
