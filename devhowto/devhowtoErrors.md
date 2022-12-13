

## How to Return an Error
We can throw an exception or return an error code.

## When To Return an Error


Nouns and adjectives really all have the same structure and throw the same errors

There are two approaches here: 
    - We can have each piece of code test for failure and raise an error 
    OR
    - We can just record the error and only pay attention if we fail
        - which seems kind of like a hack
    - We can use a decorator to describe what error "none" means for the whole function

Problem 1:
    - A predication always records why it eventually failed
    - We only pay attention to it if it didn't return any items
        - Then why bother recording it if it returns an item??
    - Let's take "a large file":
        - large will iterate through all the large things
        - file will fail for many of them, but we don't care
        - We only care about the failures that 
        - At any given point we have our "best" error, which is the deepest error in the tree

Problem 2:
    - Again, let's take "a large file":
    - What is the error from file_n?
        - It would intuitively be "folder x is not a file"
        - The real question being asked of "file_n" is "does there exist a file x?" or "find a file"
            - we are just trying to find that file by feeding it different individuals
            - Thus the error should be "there is not a file" or "I don't know about a file"
        - Folder X is a file will fail somewhere else (in the "be" verb)

Problem 3:
    - Really, we'd like it to say "there is not a large file".  How?
        - We know where it failed, how far it got
        
Scenario: In the current engine: "There is a green rock" gets "locationNoItemsNamed" error

d_noun__x(TypeNameArg, XArg) :- arg(TypeName, _) = TypeNameArg, arg(X, _) = XArg,
	% Nouns come in the way the user said them, i.e. as a *name*
	% They need to be mapped to an ID
	tryError(
	    (   nameOf(X, _, TypeName, _),
	        known(X)
	    ),
        location(d_noun__x1, locationNoItemsNamed, TypeNameArg, XArg)).

file_n()

Design: if a predication *fails* we want an error why

It is really only if we are not going to iterate that we should throw

Is "failure" just stopping iteration or an actual exception?

Let's not call it failure, it is just "iterating as many times as is right" and there is a "reason" it stops iterating that should be captured

The caller decides if it needed zero (in the case of not()), one, two, N, etc iterations to work

If you throw when iterating, it is caught and ignore unl

Maybe: The "right" model is to jam all the individuals through at the start and have the contract only be "is this thing true"?



We can do much better than this. There are two parts to the error reporting approach we'll take: figuring out which was the right error to report and figuring what how to *say* it.

The predication contract says that any predication can be iterated until they eventually fail, and in fact this is what we do for every predication in the MRS. Every predication that runs will (eventually) fail! 

We need to start reporting errors wherever the code for a predication does fail.

This 
When an MRS fails, it obviously fails in one of its predications. 
As we walk the tree when resolving an MRS, 
### Determining the Right Error



~~~
@Predication(vocabulary, name="_file_n_of")
def file_n_of(state, x):
    x_value = state.GetVariable(x)
    if x_value is None:
        iterator = state.AllIndividuals()
    else:
        iterator = [x_value]

    for item in iterator:
        if isinstance(item, File):
            new_state = state.SetX(x, item)
            yield new_state

    DelphinContext().ReportError({"noThing": [x]})
~~~

### What to say about it


Intuitively, if we are resolving 
We record the error and its predication index
Then we can use this to know how far into the MRS it got