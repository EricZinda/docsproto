{% raw %}## Scopal Arguments
Scopal arguments are predication arguments that are actually *other predications* and not variables. They indicate that the predication should do its job using the results of the whole "branch" it is given. Exactly *what* job depends on the predication. The most common scopal arguments are seen in quantifiers like "a, the, every, some" etc. Their job is limit the number of answers in some way. They do that by taking a `RSTR` argument that indicates what the quantifier is about (e.g. "a folder"), and a `BODY` argument that says what we are restricting the quantification to (e.g. "something *large*"). 

For example take "a file is large". One of the scope resolved trees for it is:

```
       ┌───── _file_n_of(x3,i8)
_a_q(RSTR,BODY)
            └ _large_a_1(e2,x3)
```
If we convert this into text it would be:
```
 _a_q__xhh(x3, _file_n_of__xi(x3, i8), _large_a_1__ex(e2, x3))
```
And finally, using our text format you get:
```
["_a_q__xhh", "x3", ["_file_n_of__xi", "x3", "i8"], ["_large_a_1__ex", "e2", "x3"]]
```
(Ignore for the moment the `i8` argument, in this case it just means "ignored". The `e2` event argument can also be ignored for now, we'll get to that soon.)

This MRS says "from all the files in the world model, return a single (arbitrary) one that is large". It is indicating that we want the answer to be "a" (i.e. an arbitrary single) large file, whereas `_large_a_1(e,x) and _file_n_of(x)` would give us *all* large files.

If you look at the resolved tree, it really is just one predication with the other two as arguments. So, the `Call()` solver we built is only going to call the function that implements `_a_q__xhh`. The work of implementing the rest of the tree goes to that predication itself. It works this way because the job of predications with scopal arguments is to handle *how* those trees get resolved. That is their whole point. Thus, they need control over the resolution behavior for those arguments.

To implement `_a_q__xhh` using our predication contract, we conceptually:

1. Find the first set of variable assignments returned from the first argument (called `RSTR`) `_file_n_of(x3,i8)` using `Call()` from within `_a_q`
2. Use *those* variables to find a solution to the second argument (called `BODY`)`_large_a_1(e2,x3)`, again using `Call()` from within `_a_q`
3. If there was at least one answer, this is true: return each of the the body solutions that worked from `a_q`, one by one.  Don't "backtrack" to find another "file" since `a_q` should only return "one, arbitrary thing"
4. If there was not an answer from the first "file", go back to #1 and try again (remember that our contract says these predications will keep returning values until there are no more)

If there were no large files, `a_q` fails instead of returning any assignments, as per the predication contract. Here's the Python code that does all this:

```
@Predication(vocabulary, name="_a_q")
def a_q(state, x_variable, h_rstr, h_body):
    # Run the RSTR which should fill in the variable with an item
    for solution in Call(state, h_rstr):
        # Now see if that solution works in the BODY
        success = False
        for body_solution in Call(solution, h_body):
            # If it works, stop looking. This one is the single arbitrary item we are looking for
            yield body_solution
            success = True
            break
        if success:
            break
```

At this point we have a fully functional evaluator, but there are a few things still to work out:
- We have been ignoring all the variable types except "x" variables.
- How to deal with questions vs. commands vs. propositions
- How to report errors

Last update: 2022-12-05 by EricZinda [[edit](https://github.com/ericzinda/docsproto/edit/main/devhowto/devhowtoScopalArguments.md)]{% endraw %}