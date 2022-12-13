{% raw %}## Reporting a Failure More Robustly
One final piece of cleanup work remains in our effort to report decent failures from an MRS that can't be solved. We will be returning a lot of the same errors from different predications, so, instead of littering the code with full sentences like "There is not a large thing", we'll use constants like `doesntExist` and allow them to take arguments like `x3`. Then, using the code [from the previous section](../devhowtoConceptualFailures), we can create a shared routine that turns them into English and fills them in with descriptions of the variables at the point of failure.  Like this:

```
# error_term is of the form: [index, error] where "error" is another 
# list like: ["name", arg1, arg2, ...]. The first item is the error 
# constant (i.e. its name). What the args mean depends on the error
def GenerateMessage(mrs, error_term):
    error_predicate_index = error_term[0]
    error_arguments = error_term[1]
    error_constant = error_arguments[0]

    if error_constant == "doesntExist":
        arg1 = EnglishForDelphinVariable(error_constant, error_arguments[1], mrs)
        return f"{arg1} doesn't exist"

    elif error_constant == "adjectiveDoesntApply":
        arg1 = error_arguments[1]
        arg2 = EnglishForDelphinVariable(error_constant, error_arguments[2], mrs)
        return f"{arg2} is not {arg1}"
```
Most of what `GenerateMessage()` does is plug the error arguments into a string template.  The interesting work happens when one of the arguments is a Delphin variable and it calls `EnglishForDelphinVariable()`.  This is where we solve the problem we started the [previous section](../devhowtoConceptualFailures) with: how to describe what is in that `x` variable. 

Finally, we can change our predications to use `ReportError()` with the new error format, and change `RespondToMRS()` to respond with decent errors using all the ideas and code we've written in the [last](../devhowtoChoosingWhichFailure) [few](../devhowtoReportingAFailure) [sections](../devhowtoConceptualFailures):

```
@Predication(vocabulary, name="_file_n_of")
def file_n_of(state, x):
    
    ...

            ReportError(["doesntExist", x])
            
            
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
            
    ...
    
        ReportError(["adjectiveDoesntApply", "large", x_target])
        

def RespondToMRS(self, state, mrs):

    ...
    
    if sentence_force == "prop":
        if len(solutions) > 0:
            print("Yes, that is true.")
        else:
            message = GenerateMessage(mrs, self.Error())
            print(f"No, that isn't correct: {message}")
```
So, the predications like `large_a_1` and `file_n_of` report their failures as described in the previous sections, but now use a constant and a list of arguments as the "shape" of their errors.  If an MRS can't be solved, `RespondToMRS()` calls the `GenerateMessage()` helper function to turn the error into English and prints it for the user.

With all that in place, we can now take some of our previous examples and make them fail to see what messages we get:

```
# Evaluate the proposition: "a file is large" when there are no *large* files
def Example10():
    state = State([Folder(name="Desktop"),
                   Folder(name="Documents"),
                   File(name="file1.txt", size=1000000),
                   File(name="file2.txt", size=1000000)])

    mrs = {}
    mrs["Index"] = "e1"
    mrs["Variables"] = {"x1": {"NUM": "pl"},
                        "e1": {"SF": "prop"}}
    mrs["RELS"] = [["_a_q", "x1", ["_file_n_of", "x1"], ["_large_a_1", "e1", "x1"]]]

    state = state.SetX("mrs", mrs)
    DelphinContext().RespondToMRS(state, mrs)
    
# Prints:
No, that isn't correct: a file is not large
```

```
# Evaluate the proposition: "a file is large" when there are no files, period
def Example11():
    state = State([Folder(name="Desktop"),
                   Folder(name="Documents")])

    mrs = {}
    mrs["Index"] = "e1"
    mrs["Variables"] = {"x1": {"NUM": "pl"},
                        "e1": {"SF": "prop"}}
    mrs["RELS"] = [["_a_q", "x1", ["_file_n_of", "x1"], ["_large_a_1", "e1", "x1"]]]

    state = state.SetX("mrs", mrs)
    DelphinContext().RespondToMRS(state, mrs)

# Prints:
No, that isn't correct: a file doesn't exist
```

These can be refined further:
- The first example should be more like "no files are large" or "there aren't any large files"
- The last example should probably be "no files exist" or "there aren't any files"

At this point, though, you have the tools needed to fix those up as much as necessary. The tutorial won't improve them until we get to a much later section.

<update date omitted for speed>{% endraw %}