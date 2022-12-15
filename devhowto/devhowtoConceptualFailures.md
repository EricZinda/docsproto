## Converting Variables to English
So far, the code for `large_a_1` looks like this:
~~~
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
            
    ...
    
            ReportError("A thing is not large.")
~~~

... and will respond to "A file is large" with "A *thing* is not large" because we didn't know how to tell what kind of "thing" the variable `x` is currently filtered to be.  The best answer would replace "thing" in "A *thing* is not large" with the "type" of thing `x` is *at the point we are reporting the error*. Remember that the `large_a_1` predication will be used for anything the user references as "large", so it will need to be flexible about how it reports its failures.  `x` won't always contain files.

For example, here is a scope-resolved tree for "A file is large":

~~~
          ┌────── _file_n_of(x3,i8)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
~~~

Errors in that MRS from `_large_a_1` should say "A *file* is not large" since the only things that can be in `x` by the time it gets to `_large_a_1` have been filtered to be files. 

For "A dog is large":
~~~
          ┌────── _dog_n_1(x3)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
~~~
Errors in *that* MRS from `_large_a_1` should say "A *dog* is not large". 

etc. 

If we can get a description of what `x` is, we can write one error message and have it work well no matter how the predication is used.

### Determining What to Call "x"
We can figure out what the variable `x` has been filtered to "so far" by taking advantage of some things we know:

1. We know how the tree is executed (depth-first)
2. We know what the predications in the tree are
3. We know which predication reported the error 
4. We know where that predication is in the execution order

So, in the scope-resolved tree for "a dog is large":

~~~
          ┌────── _dog_n_1(x3)
_a_q(x3,RSTR,BODY)    
               └─ _large_a_1(e2,x3)
~~~

... if the error came from `_large_a_1`, we must have finished `_dog_n_1` but be in the middle of resolving `_a_q`.  At that point, the variable `x3` contains something that is `dog` (not even `*a* dog` yet).  In this way, we can write code which gives the English description of a variable *at a certain point in the tree's execution*. We can use that to build failure messages that have the proper "thing" for any phrase we encounter.

To do this, let's create a function (`EnglishForDelphinVariable()`) which takes 1) the `variable` we want English for, 2) the MRS, and 3) the place in the tree for which we want the English. It will walk the tree in execution order using the function we've written [in a previous section](devhowtoSimpleQuestions) called `WalkTreeUntil()`. This function will pass each predication to a different function called `RefineNLGWithPredication()` that determines if the predication is doing anything to the `variable` in question. If so, it adds some data to a structure called `nlg_data` ("NLG" stands for "Natural Language Generation"). At the end, we call a function (`ConvertToEnglish`) that takes all the gathered data and turns it into English:

~~~
# Given the index where an error happened and a variable,
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

For now, `RefineNLGWithPredication()` takes a very simple approach to seeing if a predication is "contributing to" the `variable`. Predications which *introduce* a variable (as described in a [previous section](devhowtoEvents)) are, in some sense, the base "thing" that the variable is. They should clearly be part of its description. Quantifiers for that variable describe "how much" of it there are, so they should be included as well. There are lots more we could add (and we will later) but keeping it in this simple gets us a long way for now:

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

> Note: The code for `ParsePredicationName()` is described in an [appendix](devhowtoParsePredication)

~~~
# Takes the information gathered in the nlg_data dictionary
# and converts it, in a very simplistic way, to English
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

Those functions will provide the start of a system that converts a variable into English, given a spot in the MRS. Using the MRS from "A file is large", we can test it out by calling it with different indices to see what it thinks "x1" is at that point:

~~~
def Example12():
    mrs = {"RELS": [["_a_q", "x1", ["_file_n_of", "x1"], ["_large_a_1", "e1", "x1"]]]}
    
    # Set index to failure in _a_q
    print(EnglishForDelphinVariable(1, "x1", mrs))
    
    # Set index to failure in _file_n_of
    print(EnglishForDelphinVariable(2, "x1", mrs))

    # Set index to failure in _large_a_1
    print(EnglishForDelphinVariable(3, "x1", mrs))

# Prints:
a thing
a thing
a file
~~~

You can see that, until predication #2 has succeeded (`_file_n_of`), `x1` is described as "a thing" since nothing has really filtered it yet. Once it gets to predication #3 it now holds "a file". We could easily beef up our code so that after `_large_a_1` it is described as "a large file" and we will, eventually.