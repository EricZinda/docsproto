## The Minimal Recursion Semantics Format

The [English Resource Grammar or "ERG"](http://moin.delph-in.net/ErgTop)  ([via the ACE parser](http://sweaglesw.org/linguistics/ace/)) converts an English phrase into a format called ["Minimal Recursion Semantics" (MRS)](https://www.cl.cam.ac.uk/~aac10/papers/mrs.pdf). MRS encodes the semantic meaning of the phrase into a set of predicate logic-like predicates (called predications) that have arguments and a set of constraints that constrain the valid ways they can be organized into a tree.  The set of trees that can be generated define the ultimate meaning of the phrase.

For example, one of the MRS parses for "Go to a cave" is:
~~~
TOP: h0
INDEX: e2
RELS: < 
[ _the_q__xhh LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _cave_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q__xhh LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron__x LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _to_p_dir__eex LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _go_v_1__ex LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > 
~~~

The rest of this section will explain what it means.

## Underspecification
The MRS is a *list* of predicate logic-like predications and not a *tree* like you'll see in many natural language systems.  That's because it is *underspecified*.  There are multiple interpretations for just about any natural language phrase and the MRS is designed to allow them all to be discovered: it doesn't pick a primary one. `Every book is in a cave` could mean "all books are in the same cave" or "every book is in a (possibly different) cave".   

So, you get a list of predicates in the "RELS" section and the "HCONS" section tells you the constraints on valid ways to fit them together.  This means we will need to [generate the possible interpretations](https://blog.inductorsoftware.com/blog/ResolvingTheMRSTree) and [decide which is right](https://blog.inductorsoftware.com/blog/ExecuteAndInterpretResults) in order to understand the phrase fully.

## Predicates
The English phrase is converted into a set of predicate logic like predicates in the MRS which you see above in the "RELS" section of the format. The names of the predicate encode important information about them including:
- The "lemma" or root word (this is the first word you see)
- Whether they were actually seen in the text (starts with `_`) or added abstractly (no initial `_`)
- Their part of speech: `_cave_n` means cave is a "noun". `_the_q` means "the" is a quantifier (described below), etc.
- They sometimes have extras at the end like `_1` to indicate which "variant" or synonym of the word they represent

There is some documentation for the predicates, especially unusual ones (found by doing a search of the [ERG site](http://moin.delph-in.net/ErgSemantics)), but I've found that their meaning mostly has to be determined by looking at the MRS and intuiting what they are trying to do (or [posting on the message boards](https://delphinqa.ling.washington.edu/)  if it isn't clear).  They take arguments, just like functions in most programming languages, or predicates in predicate logic, and these arguments behave analogously. 

For example: the predicate `_cave_n_1(x9)` in the example above is saying "filter the set of things in the variable x9 down to the set of things which are a 'cave'" or "ensure that x9 contains a 'cave'".  We'll get into the other examples later after we've covered some more basics.

## Arguments
The predicates take arguments and they have names like `ARG0`, `ARG1`, `ARG2`, `RSTR`, `BODY`, etc.  Think of those exactly like the name of named arguments in some programming languages like Python.

They also have a *value* which is a variable like `x5`, `h1`, `e6`.  These values indicate two things: the initial letter indicates the type of variable it is and the number just makes it unique (when it needs to be). Note that the same variable may appear in more than one place and this means it is shared, just like if you used a Python variable in more than one place in a function.  The different types are described below.

Of all the arguments, `Arg0` is special.  It holds a variable that is kind of like the "return value" of the predicate or "the thing that will hold the result that the predicate generates".  If you read the documentation you'll see the term "introduced" for this argument.  The predicate is described as "introducing" the ARG0 variable or phrases like "the variable *introduced by* predicate X..." are used.

### H (Handle) Variables, aka "Scopal Arguments"
The semantic meaning of the phrase is ultimately represented by a *tree* and the handle variables represent "holes" where the branches of the tree are placed.  The "LBL" indicator in MRS serves has a way to "label" each predicate so you can put them into holes them and form these branches.

If a predicate like `_the_q__xhh`  has a handle argument (`the` has two of them `h11` and `h12`):
~~~
[ _the_q__xhh LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
~~~
 it means it is expected to do something with the entire branch of the tree it is passed. These are called "scopal arguments". Think of this like a lambda function being passed to function in a programming language like C++ or C#.  The predicate itself will be responsible for "doing something" with the branch it is passed.  What, exactly, is specific to the predicate. 

Because the MRS is underspecified, it usually doesn't specify directly which branch to pass to which argument. You figure that out by the process of [fully-scoping the tree](https://blog.inductorsoftware.com/blog/ResolvingTheMRSTree).  However,  if a predicate has a label (shown as LBL in the MRS) that is the same handle as an argument, then that part of the tree has already been specified and is "locked in place" (i.e. there is no hole there for something else to be).


### X (Instance) Variables
Instance variables are just like normal First Order Logic variables. Think of them as containing a *set* of things in the world.

In the example, you can see that `_cave_n_1(x9)` has an instance variable. This predicate is filtering the set of things in x9 to be only those that are a "cave".


### E (Event) Variables
Event variables are more of a mind-bender to non-linguists. I've given some conceptual background [here](https://blog.inductorsoftware.com/blog/EnglishAsLogic) as well as a [deep dive](PrologEventStructure) on what they mean in this context. Think of an Event variable as describing a thing that happened in the world that may have many properties.

Predicates introduce an event because, for any number of reasons, the concept they represent needs to be represented abstractly so that other predicates can inspect or modify it. All event variables are scoped to the whole expression and each contains a single unique value that is conceptually set before execution begins. 

E variables hold a single event ID that gets (potentially) built into a richer structure over the course of running the predicates to represent an "event" or "situation" that is being described. Unlike X variables that are a "set of things", E variables are a single event.

Their main purpose as we'll be using them is to allow predicates to modify or pass optional information to each other. They are used in cases like adverbs (e.g. `move slowly`) where the `move` predicate needs to be passed optional information about *how* to move. `slowly` does this by adding data to the event that `move` introduces. 

Events can also be used to add optional information about where to do something. For example: `go to the cave`.  `to` is one of many prepositions that can be used with go (or none at all) to say where to go. So, if a preposition is in the phrase, it modifies the Event that `go` introduces.

Note that the ERG is very liberal in putting Event variables on things and, depending on context, sometimes they aren't used. This is just to make things easier for the programmer and to prevent having to deal with having the same predicate both with and without an event variable.

In the "go to the cave" example, the predicate `_go_v_1__ex` *introduces* (meaning has an ARG0 which is...) the event variable `e2` and `_to_p_dir__eex` *introduces* event variable `e8` and *consumes* the event `e2` that `go` introduced:
~~~
[ _to_p_dir__eex LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _go_v_1__ex LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
~~~

It is set up this way so that the `to` predicate can attach data about "where to go" to the event `e2`. `to` needs `e2` passed to it as an argument so it can do the attaching.  When the `go` predicate executes, it will look at its `e2` event and fish out where to go.  

However, the `e8` variable isn't used by anything, so it is effectively ignored in this example.  There are many phrases where the event variables used by predicates aren't used. They are there because the predicate needs it to be available sometimes, and instead of having multiple predicates, it just ignores it when it isn't used.

The predicate that introduces (i.e. has in its first (ARG0) position) an Event variable will often (but not always) be the predicate that consumes the event tree. Predicates that have it in other positions will often (but not always) be adding information to the Event.

### Other Variables Types: I, U, P
There are three other types of variables that show up in arguments sometimes.  These appear when the ERG can't decide the type of something since it falls somewhere between the types (i.e. is underspecified).

From the ERG documentation:

> "i (for individual) is a generalization over eventualities and instances; p (the half-way mark in the alphabet between h and x) is a generalization over labels and instances; and u (for unspecific or maybe unbound) generalizes over all of the above. Note that Copestake et al. (2001) use individual for what is called instance here."

`i` types come up most often in my experience in two scenarios:
- **Dropped arguments**: Sometimes the ERG just wants to ignore an argument in a predicate.  In theory, it could have defined a new predicate that was missing that argument, but to keep things consistent it just uses an `i` argument in place of what it wants to ignore.  Kind of like passing `Nothing` in Python or `Null` in SQL.
- **Other Arguments**: I have encountered very few times where an `i` argument is truly used as a variable, but when it is, so far I have ended up treating it like an `x` variable that is "existentially quantified" (globally defined).  

One example where I've seen a *used* `i` variable is when interpreting things in quotes like "yell 'I am free'":
~~~
                        ┌pron__x:x3
 pronoun_q__xhh:x3,h5,h6┤
                        │                        ┌_yell_v_1__exx:e2,x3,x8
                        └proper_q__xhh:x8,h10,h11┤
                                                 │   ┌fw_seq__xxi:x9021,x13,i14
                                                 │   ├fw_seq__xii:x13,i15,i16
                                                 │   ├quoted__ci:I,i15
                                                 └and┤
                                                     ├fw_seq_end_z__xx:x8,x9021
                                                     ├quoted__ci:free,i14
                                                     └quoted__ci:am,i16
                                                     
Logic: pronoun_q__xhh(x3, pron__x(x3), proper_q__xhh(x8, and(fw_seq__xxi(x8, x13, i14), fw_seq__xii(x13, i15, i16), quoted__ci(I, i15), quoted__ci(am, i16), quoted__ci(free, i14)), _yell_v_1__exx(e2, x3, x8)))

~~~
You can see that `i14`, `i15` and `i16` are all actually used by more than one predicate so they aren't "dropped arguments".

I've not yet encountered a `p` type, so I have no suggestions on how to think about those.


## Quantifier Predicates
Quantifiers fill a special role in the MRS (and linguistics in general).  [According to Wikipedia](https://en.wikipedia.org/wiki/Quantifier_(linguistics)) "a *quantifier* is a type of [determiner](https://en.wikipedia.org/wiki/Determiner_(class) "Determiner (class)"), such as _all_, _some_, _many_, _few_, _a lot_, and _no_ that indicates quantity".  "The" and "a" are also really common examples.  That's the kind of description you'd get in a normal "Learning English" grammar course, but the ERG uses a much more broad definition.

Without getting into a lot of theory, let's just say that quantifiers in the ERG are used to introduce and scope `X` variables and introduce a lot of the holes where branches of the tree fit.


## Constraints
The "HCONS" section of the MRS puts *CONS*traints on where the *H*andles can be validly put and still be a legal interpretation of the phrase.

All I've ever seen here are "qeq" constraints.  A qeq constraint always relates a hole to a (non-hole) handle and says that the handle must be a direct or eventual child in the tree and, if not direct, the only things between the hole and the handle can be quantifiers.  Said a different way: 

> A qeq constraint of "X qeq Y" says that the direct path from X to Y must only contain quantifiers.

As we work through [fully resolving the MRS into a tree](ResolvingTheMRSTree), we'll see more examples of how these are used.


## Index
One final part of the MRS needs to be described: `INDEX`:
~~~
TOP: h0
INDEX: e2
RELS: < 
[ _the_q__xhh LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _cave_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q__xhh LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron__x LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _to_p_dir__eex LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _go_v_1__ex LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > 
~~~
The `INDEX` part of the MRS indicates the variable introduced by the "main point of the phrase", i.e. the thing being done, which is usually the main verb.  In the example above `INDEX: e2` is referring to the variable introduced by `_go_v_1__ex`.  This indicates that the verb `go` is the main verb in the phrase.

The index is not always a verb but it does always indicate the thing that needs to get `executed` by the system in order to "do" the phrase.  This part of the MRS is used when it is finally time to [execute](ExecuteAndInterpretResults) the phrase in Prolog.
