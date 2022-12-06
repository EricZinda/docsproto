{% raw %}## Converting MRS as text to a Python Function call
So far, we have been calling our predications directly as functions. To be able to translate MRS into executable code we're going to need a way to convert from the MRS textual representation to actual Python function calls. This section describes the approach and code we'll use to do that.

We'll represent each predication in our MRS as a Python `list` with the predication name as the first element and the arguments as the rest. Like this for the `folder_n_of(x1)` and `compound(e1, x1, x2)` predications:
```
["folder_n_of", "x1"]
["compound", "e1", "x1", "x2"]
```
This will be a simple Python representation that is easy to convert to when given a raw MRS document.

To convert them into a Python function (like the one we wrote [above](../devhowtoImplementPredication.md)) and call them, we need a mapping from the predication name as a text string (e.g. `"_folder_n_of"`) to the function and module where the function lives. We'll do this using a Python feature called "decorators". It isn't important to understand *how* it works (but if you want to: [read this section](../devhowtoPythonDecorators)). For our purposes, just understand that by writing two small Python classes we can now write code like this:
```
vocabulary = Vocabulary()

@Predication(vocabulary, name="_folder_n_of")
def folder_n_of(state, x_target):
    # ... implementation of folder_n_of goes here ...
```

The `@Predication(...)` "decoration" above the function runs code that sticks the Python function (i.e. `def folder_n_of(...)`) and the predication name (i.e. `_folder_n_of`) into the instance of the `Vocabulary` class it is given. 

Note that the function name can be arbitrarily different than the predication name. In this case we've removed the leading "_", but we could have also done something like this:

```
vocabulary = Vocabulary()

@Predication(vocabulary, name="_folder_n_of")
def my_folder_predication(state, x_target):
    # ... implementation of folder_n_of goes here ...
```

Either way, the `vocabulary` instance will record the mapping between all of the functions decorated with `@Predication(vocabulary, name=...)` and the predication they are implementing.

Marking all of the predications with the `@Predication(vocabulary)` decorator gives us a `vocabulary` object which knows how to map names of predications to the actual function that implements them. With that, we can now build a `CallPredication()` function that uses this object to map the string name of the predicate, plus the list of arguments, to an actual Python function and execute the contract on it:

```
# The format we're using is:
# ["folder_n_of", "x1"] 
#   The first item is the predication name
#   The rest of the items are the arguments
def CallPredication(vocabulary, state, predication):
    predication_name = predication[0]

    # the [1:] syntax returns a new list that starts from
    # the first item and goes until the end of the list.
    predication_args = predication[1:]

    # This is where we look up the actual Python module and 
    # function name given a string like "folder_n_of"
    # It returns a two-item list, where item[0] is the module
    # and item[1] is the function
    module_function = vocabulary.Predication(predication_name)

    # sys.modules[] is a built in Python list that allows you
    # to access actual Python Modules given a string name
    module = sys.modules[module_function[0]]

    # functions are modeled as properties of modules in Python
    # and getattr() allows you to retrieve a property
    # so: this is how we get the "function pointer" to the
    # predication implementation
    function = getattr(module, module_function[1])

    # [list] + [list] will return a new, combined list
    # in python. This is how we add the state object
    # onto the front of the argument list
    function_args = [state] + predication_args

    # You call a function "pointer" and pass it arguments
    # that are a list by using "function(*function_args)"
    # So: this is actually calling our function (which 
    # returns an iterator and thus we can iterate over it)
    for next_state in function(*function_args):
        yield next_state

def Example2():
    state = State([Folder(name="Desktop"),
                   Folder(name="Documents"),
                   File(name="file1.txt"),
                   File(name="file2.txt")])

    for item in CallPredication(vocabulary,
                                state,
                                ["_folder_n_of", "x1"]):
        print(item.variables)

# Calling Example2() outputs:
{'x1': Folder(name=Desktop)}
{'x1': Folder(name=Documents)}
```

The `Example2()` function shows how we can use all of this to call a predication using our new text-based format. With this in place, we can tackle more complicated groups of predications such as conjunctions in the [next section](../devhowtoConjunctions).

Last update: 2022-12-05 by EricZinda [[edit](https://github.com/ericzinda/docsproto/edit/main/devhowto/devhowtoMRSToPython.md)]{% endraw %}