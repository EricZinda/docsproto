
## Implementing a Predication
With that Python background and our implementation of the `State` object, we can now implement a `_folder_n_of` function that implements the predication contract.  We will be passing an instance of the `State` object as the first argument to every predication so that it can access its own arguments *and* the world state. 

Note that the variables passed to predications will be strings like `"x1"` or `"e12"`. To get their values, the code looks them up in the `State` object:
~~~
def folder_n_of(state, x):
    x_value = state.GetVariable(x)
    if x_value is None:
        # Variable is not set yet:
        # iterate over all individuals in the world
        # using the iterator returned by state.AllIndividuals()
        iterator = state.AllIndividuals()
    else:
        # Variable is set: create an iterator that will iterate
        # over just that one by creating a list and adding it as
        # the only element
        iterator = [x_value]

    # By converting both cases to an iterator, the code that
    # checks if x is "a folder" can be shared
    for item in iterator:
        if isinstance(item, Folder):
            # state.SetX() returns a *new* state that
            # is a copy of the old one with just that one
            # variable set to a new value
            new_state = state.SetX(x, item)
            yield new_state
~~~

Now we can run our code to call our first predication:
~~~
def Example1():
    state = State([Folder(name="Desktop"),
                   Folder(name="Documents"),
                   File(name="file1.txt"),
                   File(name="file2.txt")])

    for item in folder_n_of(state, "x1"):
        print(item.variables)

# calling Example1() prints:
{'x1': Folder(name=Desktop)}
{'x1': Folder(name=Documents)}
~~~

Now we have one predication that implements the predication contract, but note that MRS is a textual format. We'll need a way to convert text into function calls in order to truly evaluate an MRS without manually converting them to Python like the above example. Let's go through that next.
