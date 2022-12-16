## The Minimal Recursion Semantics Format
> This section provides an *overview* of the Minimal Recursion Semantics format that is the primary artifact used by DELPH-IN to represent the meaning of a phrase. It should be sufficient for understanding all of the rest of the material in the tutorial.  For a deeper dive into MRS, explore [Minimal Recursion Semantics: An Introduction](https://www.cl.cam.ac.uk/~aac10/papers/mrs.pdf).

The [English Resource Grammar or "ERG"](http://moin.delph-in.net/ErgTop)  ([via the ACE parser](http://sweaglesw.org/linguistics/ace/)) converts an English phrase into a text format called ["Minimal Recursion Semantics" (MRS)](https://www.cl.cam.ac.uk/~aac10/papers/mrs.pdf) that is designed to allow software to process human language. 

Because language is ambiguous, most phrases produce more than one possible MRS document, each representing a different interpretation of the phrase. Moreover, the MRS document itself has multiple interpretations. One of the challenges of building a system that uses natural language is to determine which of the many possible meanings was intended by the user. One approach to doing this will be discussed in a [later section](devhowtoWhichParseAndTree) of the tutorial.

The MRS document encodes one semantic meaning of the phrase into a set of predicate-logic-like predicates (called predications) and a set of constraints that constrain the valid ways they can be organized into a tree.  The set of valid trees define all of the alternative meanings of that MRS.

For example, the phrase: "Look under the table." produces 12 different MRS parses (interpretations). These include the interpretations: "Look at whatever is under the table" and "Look around while you are under the table" among 10 others. The MRS for the first interpretation is:
~~~
[ TOP: h0
INDEX: e2
RELS: < 
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _under_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _look_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > ]
~~~

Using the rules described in the `HCONS` section (which we will [describe later](#Constraints)), these are the two well-formed trees that can be built out of that MRS, which describe the two alternatives that *it* could mean:

~~~
            ┌────── _table_n_1(x9)
_the_q(x9,RSTR,BODY)               ┌────── pron(x3)
                 └─ pronoun_q(x3,RSTR,BODY)    ┌── _under_p_dir(e8,e2,x9)
                                        └─ and(0,1)
                                                 └ _look_v_1(e2,x3)

               ┌────── pron(x3)
pronoun_q(x3,RSTR,BODY)            ┌────── _table_n_1(x9)
                    └─ _the_q(x9,RSTR,BODY)    ┌── _under_p_dir(e8,e2,x9)
                                        └─ and(0,1)
                                                 └ _look_v_1(e2,x3)
~~~

The rest of this section will give you a base understanding of the MRS format so that we explore how to build these trees in a [later section](devhowtoWellFormedTree) and ultimately write software that pulls the users intended meaning from them.  Deriving their intended meaning is the topic of this entire tutorial.

## Underspecification
A DELPH-IN parser like ([ACE](http://sweaglesw.org/linguistics/ace/)) will usually generate more than one MRS document representing the various high-level interpretations of a phrase. Each one contains a *list* of predicate-logic-like predications and not a *tree* like you'll see in many natural language systems.  That's because it is *underspecified*.  Even though the parser has already done one level of interpretation on the phrase, there are still (usually) multiple ways to interpret *that*.  The MRS doesn't pick a primary interpretation by choosing a final tree, it provides the rules for building *all of them*. That's what "underspecified" means. `Every book is in a cave` could mean "all books are in the same cave" or "every book is in a (possibly different) cave". Given just the phrase, it isn't clear which the use intended, so it provides all the alternatives. Context (which it doesn't have) usually helps to decide which is meant.

The list of predications in provided in the `RELS` section:
~~~
...

RELS: < 
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _under_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _look_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>

...
~~~

The `HCONS` section tells you the constraints on valid ways to fit the predications together to resolve it into a "well-formed tree" which represents a single meaning:

~~~
... 

HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > ]
~~~
We'll go through each of these in detail below, but for now just know that the MRS is underspecified, and the `RELS` together with the `HCONS` provide the information to make it specific and recover one of the possible meanings.

## Predications
A phrase is converted into a set of predicate-logic like predications in the MRS which you can see in the `RELS` section of the MRS for "Look under the table":

~~~
...

RELS: < 
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _under_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _look_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>

...
~~~

Predications are "predicate-logic-like" in that they state a relation or a fact about their arguments that must be true in order for the MRS to be true. If you find values for all the variables that make all of the predications in the MRS true in a given world, then you have "solved" or "resolved" the MRS and you have (in a sense) the meaning of the sentence. So, predications are what does the work in an MRS by providing constraints or restrictions on the variables they take. 

For example: the predication `_table_n_1(x9)` in the example above is saying "restrict the set of things in the variable `x9` to be the set of things which are a 'table'" or "ensure that `x9` contains a 'table'".  If this was followed by a different predication such as `_large_a_1(x9)`, it would mean "also restrict `x9` to anything that is 'large'.  If they are both in the same MRS, then the MRS is saying "restrict `x9` to be all of the 'large tables' in the world".

We'll get into the other examples later after we've covered some more basics.

### Predication Labels
Each predication has a label in the MRS, indicated by `LBL:`, that serves as an ID or a pointer to it. Note that predications *can* share the same label name. In fact, this is how the MRS indicates they are "in conjunction" (i.e. should be interpreted together using a logical "and").

Notice the labels for the different predications in an MRS for "Look under the *large* table" and note that `_large_a_1` and `_table_n_1` share the same label, indicating they are "in conjunction":
~~~
[ TOP: h0
INDEX: e2
RELS: < [ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _large_a_1 LBL: h13 ARG0: e14 [ e SF: prop TENSE: untensed MOOD: indicative PROG: bool PERF: - ] ARG1: x9 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _under_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _look_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > ]
~~~

These labels are used to turn the flat list of predications into the set of well-formed trees that represent its various meanings. The section on [scopal arguments](#H-(Handle)-Variables,-aka-"Scopal Arguments") discusses how this works.

### Predication Names
The name of a predication, for example, `_table_n_1`, encodes important information about it:
- The "lemma" or root word (this is the first word you see): "table"
- Whether it was actually seen in the text (starts with `_`) or added abstractly (no initial `_`)
- Its part of speech. `_table_n_1` means "table" is a "noun". `_the_q` means "the" is a "quantifier" (described below)
- It may have extras at the end like `_1` to indicate which "variant" or synonym of the word it represents

There is some documentation for the predicates, especially unusual ones (found by doing a search of the [ERG site](http://moin.delph-in.net/ErgSemantics)), but their meaning mostly has to be determined by looking at the MRS and intuiting what they are trying to do (or [posting on the message boards](https://delphinqa.ling.washington.edu/)  if it isn't clear).  

### Predication Arguments
Predications have arguments, and they have names like `ARG0`, `ARG1`, `ARG2`, `RSTR`, `BODY`, etc.  Think of those exactly like the name of named arguments in some programming languages such as Python.

They also have variables assigned to the arguments like `x5`, `h1`, `e6`.  These names indicate two things: the initial letter indicates the "type" (the different types are described next) of variable it is. The number just makes it unique. The same variable may appear in more than one place and this means it is shared, just like if you used a Python variable in more than one place in a function.  So, if an MRS has two predications like this:

~~~
[ _large_a_1 LBL: h13 ARG0: e14 [ e SF: prop TENSE: untensed MOOD: indicative PROG: bool PERF: - ] ARG1: x9 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
~~~

... you can see that:
- `_large_a_1` has two arguments: `ARG0` and `ARG1`, and the variables assigned to them are: `e14` and `x9`. The first is of type `event` (`e`) and the second is of type `instance` (`x`)
- `_table_n_1` shares `x9` in its `ARG0` and so they are both restricting the same variable. This means that, ultimately, `x9` should contain only "large tables"

Thinking of MRS variables as variables in a math equation can help: The MRS is effectively defining a formula with variables. If you pick variable values such that the MRS is true for a given world, then you have understood the meaning of the MRS (in a sense).

Of all the arguments, `ARG0` is special.  It holds a variable that, in a sense, "represents" the predication.  If you read the [Minimal Recursion Semantics: An Introduction](https://www.cl.cam.ac.uk/~aac10/papers/mrs.pdf) documentation, you'll see the term "introduced" is used to describe this argument.  The predicate is described as "introducing" the `ARG0` variable. Sometimes phrases like "the variable *introduced by* predicate X..." are used.  This will become important later, mostly when we talk about [events](devhowtoEvents) or about how to [convert predications back into a phrase](devhowtoConceptualFailures). For now, it is enough to understand that `ARG0` is a special argument that represents the predication in some special ways.

#### Variable Properties

#### X (Instance) Variables
Instance variables are just like normal First Order Logic variables, or like variables in popular programming languages. The types of things they can contain are "individuals", which is another name for a "thing in the world".  They hold the things the speaker is talking about.

In the MRS for "Look under the table":

~~~
[ TOP: h0
INDEX: e2
RELS: < 
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _large_a_1 LBL: h13 ARG0: e14 [ e SF: prop TENSE: untensed MOOD: indicative PROG: bool PERF: - ] ARG1: x9 ]
[ _table_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _under_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _look_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > ]
~~~

... There are only two instance variables that represent the "things in the world being talked about":
- `x9`: "the large table"
- `x3`: "you". This is implied since it is a command. I.e. "(You) look at the table"

Note that instance variables are always *scoped* by a quantifier (a predication named with `_q` and with the argument structure: (`x`, `h`, `h`)). Meaning: a variable can only be used in the branches of the tree under the quantifier that has it as its first argument. This is important to know when creating [well-formed trees](devhowtoWellFormedTree) but also for understanding how to navigate the tree and what can be expressed where when, for example, [turning the tree back into text](devhowtoConceptualFailures).

The other variables in the MRS are there to help build up the tree (`h` variables, described next) or allow predications to refer to each other (`e` variables, described after that).  `x` variables are the most concrete type of variable that maps most obviously to what is being said in the phrase.

#### H (Handle) Variables, aka "Scopal Arguments"
The semantic meaning of an MRS is ultimately represented by a *tree* (described in the [next section](devhowtoWellFormedTree)) and handle variables represent the "holes" where branches of the tree can be placed. While instance variables are set to individuals in the world, handle (or scopal) variables are set to the `LBL:` of another predication. As [described above](#Predication-Lables), the MRS `LBL:` field serves has a way to "label" each predication with a unique identifier. This allows the MRS to specify that a predication must be put in a particular place, or to constrain (by using the label in the `HCON` section) which predications can be put where when they are moved around the tree.  

For example, if a predication like `_the_q` has a handle argument (`the_q` has two of them: `h11` and `h12`):

~~~
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
~~~
... it means it is expected to do something with the entire branch of the tree it is passed. These are called "scopal arguments". Think of it like a lambda function being passed to function in a programming language like C++ or C#.  The `the_q` predication itself will be responsible for "doing something" with the branch it is passed.  What, exactly, is specific to the predication. We'll go into this more in a [future section](devhowtoScopalArguments) of the tutorial. For now, think about scopal arguments as places to put other predications which are acting like programming language "lambda functions".

Because the MRS is [underspecified](#Underspecification), it usually doesn't directly list which predication to put in which scopal argument. You figure that out by the process of [creating a well-formed tree](devhowtoWellFormedTree).  However, if a predication has a `LBL:` that is the same handle as a scopal argument, then that part of the tree *has* actually been specified and is "locked in place" (i.e. there is no hole there for something else to be).


#### E (Event) Variables
Event variables have a rich history and lot of fascinating conceptual linguistic background to them (Davidson 1967a is a good start), but for our purposes we can think of them as holding a "bag of information" (represented in code as a dictionary, perhaps). Predications [*introduce*](#Predication-Arguments) them to provide a place for other predications to hang information that will be used by the introducer.  All event variables are scoped to the whole MRS.

For example, event variables are used by adverbs (e.g. `move slowly`) when the `move` predication needs optional information about *how* to move. `slowly` does this by adding data to the event variable that `move` introduces. You can see in the MRS below for "move slowly" that `_slow_a_1` is passed the `e2` event variable that `_move_v_1` introduces:

~~~
[ TOP: h0
INDEX: e2
RELS: < 
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _slow_a_1 LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ]
[ _move_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 > ]
~~~

The `_slow_a_1` predication is passed the `e2` argument so that it can attach data about "*how* to do something" to the event. `_move_v_1` needs `e2` passed to it so that it can inspect it and determine how to do the "moving".  

They can also be used to add information about *where* to do something. For example: `go to the store`.  `to` is one of many prepositions that can be used with "go" to say *where* to go. So, if a preposition is in the phrase, it modifies the event that `go` introduces:

~~~
[ TOP: h0
INDEX: e2
RELS: < 
[ _the_q LBL: h10 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] RSTR: h11 BODY: h12 ]
[ _store_n_1 LBL: h13 ARG0: x9 [ x PERS: 3 NUM: sg IND: + ] ]
[ pronoun_q LBL: h4 ARG0: x3 [ x PERS: 2 PT: zero ] RSTR: h5 BODY: h6 ]
[ pron LBL: h7 ARG0: x3 [ x PERS: 2 PT: zero ] ]
[ _to_p_dir LBL: h1 ARG0: e8 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: e2 ARG2: x9 ]
[ _go_v_1 LBL: h1 ARG0: e2 [ e SF: comm TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 h11 qeq h13 > ]
~~~

Event variables conceptually hold a single "event" that gets (potentially) built into a richer structure over the course of evaluating the predications. Multiple predications may "enrich" it with information before is actually used by, for example, a verb. Contrast this with an instance (`x`) variable which only holds a particular individual at a given point it time. Said another way: an instance variable is like a string and can only hold one value, where an event is like a dictionary or a list and can hold many and be added to over time.

Note that the DELPH-IN grammars are very liberal in putting event variables on predications and, depending on context, sometimes they aren't used. This is just to prevent the consumer of the MRS from having to deal with the same predication both with and without an event variable.

The predication that introduces (i.e. has it in its `ARG0` argument) an event variable will often (but not always) be the predication that consumes or "does something" with the "fully enriched" event. Predications that have it in other arguments will often (but not always) be simpling adding information to the event.


#### Other Variables Types: I, U, P
There are three other types of variables that show up in arguments sometimes.  These appear when the ERG can't decide the type of something since it falls somewhere between the types (i.e. is underspecified).

From the ERG documentation:

> "i (for individual) is a generalization over eventualities and instances; p (the half-way mark in the alphabet between h and x) is a generalization over labels and instances; and u (for unspecific or maybe unbound) generalizes over all of the above. Note that Copestake et al. (2001) use individual for what is called instance here."

`i` types come up most often in two scenarios:
- **Dropped arguments**: Sometimes the ERG just wants to ignore an argument in a predicate.  In theory, it could have defined a new predicate that was missing that argument, but to keep things consistent it just uses an `i` argument in place of what it wants to ignore.  Kind of like passing `None` in Python or `Null` in SQL.
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
