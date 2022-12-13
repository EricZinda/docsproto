## Converting Variables to English
So far, the code for `large_a_1` looks like this:
~~~
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
            
    ...
    
            ReportError(f"There is not a large thing")
~~~

... and will respond to "A file is very large" with "There is not a large thing". Correct-ish, but not great. We'd *really* like to report errors at a more conceptual level. The best answer would replace "thing" in "There is not a large thing" with the "type" of thing `x` is *at the point we are reporting the error*. Remember that the `large_a_1` predication will be used for anything the user references as "large", so it will need to be flexible about how it reports its failures.

For example, here is a scope-resolved tree for "A file is large":

~~~
          ┌────── _file_n_of(x3,i8)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
~~~

Errors in that MRS from `_large_a_1` should say "There is not a large *file*" since the only things that can be in `x` by the time it gets to `_large_a_1` have already been filtered to be files. 

For "A dog is large":
~~~
          ┌────── _dog_n_1(x3)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
~~~
Errors in *that* MRS from `_large_a_1` should say "There is not a large *dog*". 

etc. 

That way, we can write one error message and have it work well no matter how the predication is used.

### Determining What to Call "x"
We can figure out what the variable `x` has been filtered to "so far" by taking advantage of some things we know:

1. We know how the tree is executed (depth-first)
2. We know what the predications in the tree are
3. We know which predication reported the error 
4. We know where that predication is in the execution order

So, if the error came from `_large_a_1`, we must have finished `_dog_n_1` but be in the middle of resolving `_a_q`.  At that point, the variable `x3` contains something that is `dog` (not even `*a* dog` yet).  In this way, we can write code which gives the English description of a variable *at a certain point in the tree's execution*. We can use that to build failure messages that have the proper "thing" for any phrase we encounter.

First, let's create the function (`EnglishForDelphinVariable()`) which takes the `variable` we want English for, the MRS, and the place in the tree for which we want the English. It walks the tree in execution order using the function we've written [in a previous section](devhowtoSimpleQuestions) called `WalkTreeUntil()` and passes each predication to a function that determines if they are "filtering" the `variable` in question. If so, it adds some data to a structure called `nlg_data` ("NLG" stands for "Natural Language Generation"). At the end, we call a function (`ConvertToEnglish`) that takes all the gathered data and turns it into English:

~~~
# Given the index where an error happened and a variable
# return what that variable "is" up to that point, in English
def EnglishForDelphinVariable(failure_index, variable, mrs):
    # Integers can't be passed by reference in Python, so we need to pass
    # the current index in a list so it can be changed as we iterate
    current_predication_index = [0]

    # This function will be called for every predication in the MRS
    # as we walk it in execution order
    def RecordPredicationsUntilFailureIndex(predication):
        # Once we have hit the index where the failure happened, stop
        if current_predication_index[0] == failure_index:
            return False
        else:
            # See if this predication can contribute anything to the
            # description of the variable we are describing. If so,
            # collect it in nlg_data
            RefineNLGWithPredication(variable, predication, nlg_data)
            current_predication_index[0] = current_predication_index[0] + 1
            return None

    nlg_data = {}
    
    # WalkTreeUntil() walks the predications in mrs["RELS"] and calls
    # the function RecordPredicationsUntilFailureIndex(), until hits the
    # failure_index position
    WalkTreeUntil(mrs["RELS"], RecordPredicationsUntilFailureIndex)
    
    # Take the data we gathered and convert to English
    return ConvertToEnglish(nlg_data)
~~~

For now, `RefineNLGWithPredication()` takes a very simple approach to seeing if a predication is "filtering" the `variable`. Predications which *introduce* a variable (as described in a [previous section](devhowtoEvents)) are, in some sense, the base "thing" that the variable is. They should clearly be part of its description. Quantifiers for that variable describe "how much" of it there are, so they should be included as well. There are lots more we could add (and we will later) but keeping it in this simple gets us a long way for now:
~~~
# See if this predication in any way contributes words to 
# the variable specified. Put whatever it contributes in nlg_data
def RefineNLGWithPredication(variable, predication, nlg_data):
    # Parse the name of the predication to find out its 
    # part of speech (POS) which could be a noun ("n"), 
    # quantifier ("q"), etc. 
    parsed_predication = ParsePredicationName(predication[0])

    # If the predication has this variable as its first argument,
    # it either *introduces* it, or is quantifying it
    if predication[1] == variable:
        if parsed_predication["Pos"] == "q":
            # It is quantifying it
            nlg_data["Quantifier"] = parsed_predication["Lemma"]
        else:
            # It is introducing it, thus it is the "main" description
            # of the variable, usually a noun predication
            nlg_data["Topic"] = parsed_predication["Lemma"]
~~~
Finally, we can take the information we gathered and convert it (in a very simple way) to English. Note that generating proper English is *much* more complicated than this, and we'll tackle doing it "right" later. For now, our naive approach will illustrate the ideas:

> Note: The code for parsing the predication is described in an [appendix](devhowtoParsePredication)

~~~
# Takes the information gathered in the nlg_data dictionary
# and convert it, in a very simplistic way, to English
def ConvertToEnglish(nlg_data):
    if "Quantifier" in nlg_data:
        quantifier = nlg_data["Quantifier"]
    else:
        quantifier = "a"

    if "Topic" in nlg_data:
        topic = nlg_data["Topic"]
    else:
        topic = "thing"

    return f"{quantifier} {topic}"
~~~
Those functions will provide the start of a system that converts a variable into English, given a spot in the MRS. 

One final piece of cleanup work remains. We will be returning a lot of the same errors from different predications, so, instead of littering the code with full sentences like "There is not a large thing", we'll use constants like `doesntExist` and allow them to take arguments like `x3`. Then, using the code above, we can build up the English for them in a shared routine that turns them into English and fills in that English with descriptions of the variables.  Like this:

~~~            
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
~~~
Most of what `GenerateMessage()` does is plug the error arguments into a string template.  The interesting work happens when one of the arguments is a Delphin variable and it calls `EnglishForDelphinVariable()`.  This is where we solve the problem we started this section with: how to describe what is in that `x` variable, as described above. 

Finally, we can change our predications to use `ReportError()` with the new error format, and change `RespondToMRS()` to respond with errors using all the ideas and code we've written in the [last](devhowtoChoosingWhichFailure) [couple](devhowtoReportingAFailure) sections:

~~~
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
~~~         
So, the predications like `large_a_1` and `file_n_of` report their failures as described in the previous sections, but now use a constant and a list of arguments as the "shape" of their errors.  If an MRS can't be solved, `RespondToMRS()` calls the `GenerateMessage()` helper function  to turn the error into English and prints it for the user.

With all that in place, we can now take some of our previous examples and make them fail to see what messages we get:

~~~
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
~~~

~~~
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
~~~

These can be refined further:
- The first example should be more like "no files are large" or "there aren't any large files"
- The last example should probably be "no files exist" or "there aren't any files"

At this point, though, you have the tools needed to fix those up as much as necessary. The tutorial won't improve them until we get to a much later section.

