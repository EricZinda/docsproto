{% raw %}### Choosing the Right Failure
Before we go any further, we need to step back and work through how to deal with and report on failures in the system. The way things are currently built, if the user says, "There is a large file" they will get the response: "No, that isn't correct".  If the user says "I delete a file" or "Bill deletes a file" they will get the response: "Couldn't do that".  We can do better, but we'll need to work through a few challenges first.

The first challenge is to figure out *which* of the failures encountered to return. Usually there is more than one. To see why, recall that we are solving MRS by effectively pushing all the items in the world "through" the MRS until we find the ones that make it true. For "A file is large", the MRS and resolved tree are:

```
[ TOP: h0
INDEX: e2
RELS: < 
[ _a_q LBL: h4 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] RSTR: h5 BODY: h6 ]
[ _file_n_of LBL: h7 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] ARG1: i8 ]
[ _large_a_1 LBL: h1 ARG0: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: x3 ]
>
HCONS: < h0 qeq h1 h5 qeq h7 > ]

          ┌────── _file_n_of(x3,i8)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
```

Our conceptual approach to solving it is:
1. `_a_q` iteratively sets `x3` to each object in the world and calls `_file_n_of` with that value
2. If `_file_n_of` succeeds, `_a_q` then calls `_large_a_1` with the values returned
3. If `large_a_1` succeeds, then `a_q` succeeds and stops iterating. 

(In reality, we optimize step #1 to have `_a_q` call `file_n_of` with free variables instead of iterating through every object. This allows `file_n_of` to more efficiently return the files in the system without testing every object. Conceptually, though, it is the same.)

So, let's take a world that has the following items in it, run it through the MRS for "A file is large" and see where things fail:

```
a folder
a small file
a large file
a dog
```

`a folder`:
1. `_a_q` sets `x3` to `a folder` and calls `_file_n_of` with that value
2. `_file_n_of` fails

`a small file`:
1. `_a_q` sets `x3` to `a small file` and calls `_file_n_of` with that value
2. `_file_n_of` succeeds, `_a_q` then calls `_large_a_1` with the values returned
3. `large_a_1` fails. 

`a large file`:
1. `_a_q` sets `x3` to `a large file` and calls `_file_n_of` with that value
2. `_file_n_of` succeeds, `_a_q` then calls `_large_a_1` with the values returned
3. `large_a_1` succeeds, therefore `a_q` succeeds and stops iterating. 

So, when solving the MRS with this world definition, we hit (in this order):
- a `_file_n_of` failure
- a `large_a_1` failure
- a solution (i.e. no failure)

Even though the system hit two failures in solving the MRS, the user that said "a file is large" for this world wouldn't expect *any* failures to be reported. They would expect something like "correct!" to be said.

Another example, what if the user said, "A file is *very* large"? In solving the MRS with the same world you'd get (in this order):  
- a `_file_n_of` failure
- a `large_a_1` failure (since none are "*very* large")
- a `large_a_1` failure (since none are "*very* large")
- a `_file_n_of` failure

There were 4 failures encountered when solving the MRS for this case. The user would ideally like the error to be, "No, there isn't a very large file", which presumably corresponds to the middle two. Which heuristic helps us choose those?

One heuristic that works well in practice is this: If there is a solution for an MRS, don't report any errors. If there is no solution for an MRS, report the error from the "deepest/farthest" failure possible.

The intuition for why this works is this:

If there was a solution: it means that there was a way to make the phrase work logically in the world. Presumably, it will make sense to the user too, even if it isn't what they meant (though likely it is), so no failure should be reported. 

If there wasn't a solution, the user will want to know why not. The "real" reason why not is "because the MRS did not have a solution", but that is unsatisfying. Also: no human would respond with that. A human would respond with where they got blocked attempting to do what the user asked. Furthermore, even if the human tried, or thought about, 10 different approaches to performing the request, they usually won't describe the 10 ways they tried that quickly didn't work out. They'll list the failure that is "the closest they got to succeeding".  For example:

> (In a world where there 10 things on the counter, including milk, and Bob is holding things he can't put down)
Alice: "Could you give me the milk?"
Bob: (good answer) "My hands are full"
Bob: (bad answer) "I thought about handing you ketchup, but then realized it wasn't milk"


The second one is bad for many reasons, but here we'll focus on the fact that Alice probably wanted the one "closest to the solution" one as a starting point. Bob tried to solve the request by looking at each thing on the counter until he found the milk (that was 10 different "failures" until one succeeded). Then, he tried to "give it to Alice" which failed because his hands were unavailable. She could ask for more detail or alternative solutions if she really wanted them. The failures that got the farthest in the tree are usually closest to a solution and thus will usually "make the most sense" to report.

Here's a more explicit algorithm:
- Track the "depth" of each predication in the tree, where "depth" means "call order"
- Every time a predication fails, if it is the "deepest" failure so far, remember that error
- If the MRS has no solutions, report the remembered error to the user

So, we will need to remember the "current deepest" error as we go. To organize the methods and variables dealing with executing predications and tracking errors, we'll move our existing `Call()`, `CallPredication()` and `RespondToMRS()` functions into a class called `ExecutionContext`. Then, we can track our "current deepest" error there, along with a variable that tracks how deep the currently executing predication is.

The following methods aren't changed at all from what we wrote in previous sections except for `Call()`.  It now assigns an "index" to each predication as they are executed so we know how deep we are.
```
class ExecutionContext(object):
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self._error = None
        self._error_predication_index = -1
        self._predication_index = -1

    def Call(self, vocabulary, state, term):
        last_predication_index = self._predication_index
        self._predication_index += 1

        # If "term" is an empty list, we have solved all
        # predications in the conjunction, return the final answer.
        # "len()" is a built-in Python function that returns the
        # length of a list
        if len(term) == 0:
            yield state
        else:
            # See if the first thing in the list is actually a list
            # like [["_large_a_1", "e1", "x1"], ["_file_n_of", "x1"]]
            # If so, we have a conjunction
            if isinstance(term[0], list):
                # This is a list of predications, so they should
                # treated as a conjunction.
                # Call each one and pass the state it returns
                # to the next one, recursively
                for nextState in self.Call(vocabulary, state, term[0]):
                    # Note the [1:] syntax which means "return a list
                    # of everything but the first item"
                    yield from self.Call(vocabulary, nextState, term[1:])

            else:
                # The first thing in the list was not a list
                # so we assume it is just a term like
                # ["_large_a_1", "e1", "x1"]
                # evaluate it using CallPredication
                yield from self._CallPredication(vocabulary, state, term)

        self._predication_index = last_predication_index

    # Do not use directly.
    # Use Call() instead so that the predication index is set properly
    # The format we're using is:
    # ["folder_n_of", "x1"]
    #   The first item is the predication name
    #   The rest of the items are the arguments
    def _CallPredication(self, vocabulary, state, predication):
        # The [0] syntax returns the first item in a list
        predication_name = predication[0]

        # The [1:] syntax returns a new list that starts from
        # the first item and goes until the end of the list
        predication_args = predication[1:]

        # Look up the actual Python module and
        # function name given a string like "folder_n_of".
        # "vocabulary.Predication" returns a two-item list,
        # where item[0] is the module and item[1] is the function
        module_function = vocabulary.Predication(predication_name)

        # sys.modules[] is a built-in Python list that allows you
        # to access actual Python Modules given a string name
        module = sys.modules[module_function[0]]

        # Functions are modeled as properties of modules in Python
        # and getattr() allows you to retrieve a property.
        # So: this is how we get the "function pointer" to the
        # predication function we wrote in Python
        function = getattr(module, module_function[1])

        # [list] + [list] will return a new, combined list
        # in Python. This is how we add the state object
        # onto the front of the argument list
        function_args = [state] + predication_args

        # You call a function "pointer" and pass it arguments
        # that are a list by using "function(*function_args)"
        # So: this is actually calling our function (which
        # returns an iterator and thus we can iterate over it)
        for next_state in function(*function_args):
            yield next_state

    def RespondToMRS(self, state, mrs):
        # Add the MRS as a variable in the state so that it can
        # be accessed by predicates
        state = state.SetX("mrs", mrs)

        # Collect all the solutions to the MRS against the
        # current world state
        solutions = []
        for item in self.Call(vocabulary, state, mrs["RELS"]):
            solutions.append(item)

        index_variable = mrs["Index"]
        sentence_force = mrs["Variables"][index_variable]["SF"]
        if sentence_force == "prop":
            # This was a proposition, so the user only expects
            # a confirmation or denial of what they said.
            # The phrase was "true" if there was at least one answer
            if len(solutions) > 0:
                print("Yes, that is true.")
            else:
                print("No, that isn't correct.")

        elif sentence_force == "ques":
            # See if this is a "WH" type question
            wh_predication = FindPredicate(mrs["RELS"], "_which_q")
            if wh_predication is None:
                # This was a simple question, so the user only expects
                # a yes or no.
                # The phrase was "true" if there was at least one answer
                if len(solutions) > 0:
                    print("Yes.")
                else:
                    print("No.")
            else:
                # This was a "WH" question
                # return the values of the variable asked about
                # from the solution
                wh_variable = wh_predication[1]
                for solution in solutions:
                    print(solution.GetVariable(wh_variable))

        elif sentence_force == "comm":
            # This was a command so, if it works, just say so
            # We'll get better errors and messages in upcoming sections
            if len(solutions) > 0:
                # Collect all of the operations that were done
                all_operations = []
                for solution in solutions:
                    all_operations += solution.GetOperations()

                # Now apply all the operations to the original state object and
                # print it to prove it happened
                final_state = state.ApplyOperations(all_operations)

                print("Done!")
                print(final_state.objects)
            else:
                print(f"Couldn't do that: {self._error}")
                          
            
# Create a global execution context to use when running the MRS
execution_context = ExecutionContext(vocabulary)


# Helper to access the global context so code is isolated from
# how we manage it
def DelphinContext():
    return execution_context


# Helper used by predications just to make the code easier to read
def Call(*args, **kwargs):
    yield from DelphinContext().Call(*args, **kwargs)~~~
```

At this point, we've just restructured things and started giving an "index" to every predication, but not using it. Next, we can create a `ReportError()` method and a helper to make it easy to call.

```
class ExecutionContext(object):
    
    ...
    
    def ReportError(self, error):
        if self._error_predication_index < self._predication_index:
            self._error = error
            self._error_predication_index = self._predication_index

def ReportError(error):
    DelphinContext().ReportError(error)
```

With all that in place, we will now remember which is the right error to report. The [next section](../devhowtoReportingAFailure) will describe what they should say. This is not as obvious as it might seem. 
<update date omitted for speed>{% endraw %}