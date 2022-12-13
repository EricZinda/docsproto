{% raw %}## Converting Variables to English
So far, the code for `large_a_1` looks like this:
```
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
            
    ...
    
            ReportError(f"There is not a large thing")
```

... and will respond to "A file is very large" with "There is not a large thing". Correct-ish, but not great. We'd *really* like to report errors at a more conceptual level. The best answer would replace "thing" in "There is not a large thing" with the "type" of thing `x` is *at the point we are reporting the error*. For example, here is a scope-resolved tree for "A file is large":

```
          ┌────── _file_n_of(x3,i8)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
```

Errors in that MRS from `_large_a_1` should say "There is not a large *file*" since the only things that can be in `x` by the time it gets to `_large_a_1` have already been filtered to be files. 

For "A dog is large":
```
          ┌────── _dog_n_1(x3)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
```
Errors in *that* MRS from `_large_a_1` should say "There is not a large *dog*". 

etc. 

That way, we can write one error message and have it work well no matter how the predication is used.

### Determining What to Call "x"
We can figure out what the variable `x` has been filtered to "so far" because:

1. We know how the tree is executed (depth-first)
2. We know what the predications are
3. We know which predication reported the error 
4. We know where that predication is in the execution order

So, if the error came from `_large_a_1`, we must have finished `_dog_n_1` but be in the middle of resolving `_a_q`.  At that point, the variable `x3` contains something that is `dog` (not even `*a* dog` yet).  We'll build our error system assuming we have a way to construct the English for a variable in that manner. 

Furthermore, we will be returning a lot of the same errors from different predications, so, instead of littering the code with full sentences like "There is not a large thing", we'll use constants like `doesntExist` and allow them to take arguments like `x3`. Then, we can build up the English for them in a shared routine.  Like this:

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
            
            
# error_term is of the form: [index, error] where error can be anything
# but we are assuming it is another list like: ["name", arg1, arg2, ...]
# What the args mean depend on the error
def GenerateMessage(mrs, error_term):
    if error_term[1][0] == "doesntExist":
        arg1 = EnglishForDelphinVariable(error_term[0], error_term[1][1], mrs)
        return f"{arg1} doesn't exist"

    elif error_term[1][0] == "adjectiveDoesntApply":
        arg1 = error_term[1][1]
        arg2 = EnglishForDelphinVariable(error_term[0], error_term[1][2], mrs)
        return f"{arg2} is not {arg1}"
```

So, the predications like `large_a_1` and `file_n_of` report their failures as described in the previous sections, but use a constant and a list of arguments as the "shape" of their errors.  If an MRS can't be solved, `RespondToMRS()` calls a helper function called `GenerateMessage()` to turn the error into English and prints that for the user. 

Most of what `GenerateMessage()` does is plug the error arguments into a string template.  The interesting work happens when one of the arguments is a Delphin variable and it calls `EnglishForDelphinVariable()`.  This is where we solve the problem we started this section with: how to describe what is in that `x` variable. For now, we will keep it *very* simplistic. Later we can make this much better.  Natural language generation (i.e. creating English as opposed to understanding it) is a whole different world to explore.

```
# Given the index where an error happened and a variable
# return what that variable "is" up to that point, in English
def EnglishForDelphinVariable(failure_index, variable, mrs):
    # Integers can't be passed by reference in Python, so we need to pass
    # the index in a list so it can be changed as we iterate
    predication_index = [0]

    # This function will be called for every predication in the MRS
    def RecordPredicationsUntilFailureIndex(predication):
        # Once we have hit the index where the failure happened, stop
        if predication_index == failure_index:
            return False
        else:
            # See if this predication can contribute anything to the
            # description of the variable we are describing
            RefineNLGWithPredication(variable, predication, nlg_data)
            predication_index[0] = predication_index[0] + 1
            return None

    nlg_data = {}
    
    # WalkTreeUntil() walks the predications in mrs["RELS"] and calls
    # the function RecordPredicationsUntilFailureIndex, until it returns
    # something besides None
    WalkTreeUntil(mrs["RELS"], RecordPredicationsUntilFailureIndex)
    
    # Take the data we gathered and convert to English
    return ConvertToEnglish(nlg_data)


# See if this predication in any way contributes words to 
# the variable specified. Put whatever it contributes in nlg_data
def RefineNLGWithPredication(variable, predication, nlg_data):
    # Parse the name of the predication to find out its 
    # part of speech (POS) which could be a noun ("n") or
    # quantifier ("q"), etc. 
    parsed_predication = ParsePredicationName(predication[0])

    # If the predication *introduces* this variable and
    # is not a quantifier, then it is the "main" description
    # of the variable, usually a noun predication
    if predication[1] == variable:
        if parsed_predication["Pos"] == "q":
            nlg_data["Quantifier"] = parsed_predication["Lemma"]
        else:
            nlg_data["Topic"] = parsed_predication["Lemma"]


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
```

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

> Note: The code for parsing the predication (which we will use often) is below:


```

# Returns a dict:
# {
#     "Surface" : True | False
#     "Lemma" : "go"...
#     "Pos" : "v"...
#     "PredicateRaw":
#     "Sense": "dir"...
# }
def ParsePredicationName(name):
    result = {}
    result["PredicateRaw"] = name
    if name[0] == "_":
        params = name[1:].split("_")
        result["Surface"] = True
    else:
        params = name.split("_")
        result["Surface"] = False

    # From this point forward, everything up to the POS is the lemma
    # and everything after the POS is the sense
    gotPOS = False
    for item in params:
        if not gotPOS:
            # some words like "a" look like a POS so don't get tricked
            # if we don't have a lemma yet
            if "Lemma" in result and item in ["q", "p", "n", "v", "j", "a", "r"]:
                result["Pos"] = item
                gotPOS = True
            else:
                # Keep adding to the lemma until we find POS (if it exists)
                # e.g. d_fw_seq_end_z__xx
                result["Lemma"] = item if "Lemma" not in result else f"{result['Lemma']}_{item}"
        else:
            result["Sense"] = item if "Sense" not in result else f"{result['Sense']}_{item}"

    if "Lemma" not in result:
        result["Lemma"] = "#unknown#"

    if "Pos" not in result:
        # u for unknown
        result["Pos"] = "u"

    return result
```

Last update: 2022-12-12 by EricZinda [[edit](https://github.com/ericzinda/docsproto/edit/main/devhowto/devhowtoConceptualFailures.md)]{% endraw %}