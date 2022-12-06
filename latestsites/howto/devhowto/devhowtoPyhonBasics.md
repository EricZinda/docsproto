{% raw %}## Python Background and the State object
The [predication contract](../devhowtoPredicationContract) could be implemented in any programming language, but we'll be using Python. This section should give enough background so that even readers not familiar with Python can understand what it is doing and treat it like a "pseudo-language". Even if you know Python, skim through the section since we will be implementing a key class (`State`) used elsewhere in the documentation.

The Python language has functions, classes, methods, variables, operators, statements, and other elements shared by many imperative programming languages such as C++, Java, Javascript, Go, etc. How these work will be described as we go along and should be relatively straightforward to understand if you are proficient in an existing imperative programming language. 

Python also has a notion of "iterators" which needs a bit more attention. Iterators are objects that can be "iterated" or "listed" or "looped through". These can be lists represented in square brackets like `[item1, item2]` or special functions called "generators" which act like a list but which allow code to dynamically generate the items that are returned.    

You iterate over an iterator of any type using the `for ... in ...` construct like this:

```
# '#" in Python starts a line with a comment
for item in iterator:

    # Indenting is how Python determines what code 
    # "belongs" to the thing above. Everything indented
    # here will get looped over

    # now "item" has the first value from iterator
    # and we can, for example, print it
    print(item)
```

If you want to write code to *dynamically* build an iterator (called a "generator"), you simply write a fuction that calls `yield` to return each item. `yield` returns the value and then continues on the next line when the next value is asked for. If the function exits without a yield, the iteration stops (this is what we've been calling "fail" in the predication contract):

```
# "def" is how you define a function in Python
# everything indented below it is in the function
def MyIterator1():
    yield 1
    yield 2
    yield 3

# Here's another function that does
# the same thing differently
def MyIterator2():
    # A list in Python is surrounded by []
    my_list = [1, 2, 3]
    for index in my_list:
        yield index


def OutputResults():
    for item in MyIterator1():
        print(item)
    for item in MyIterator2():
        print(item)

# Calling OutputResults() prints:
# 1
# 2
# 3
# 1
# 2
# 3
```

We'll be doing lots of iteration and this syntactic sugar from Python makes it easier. 

Let's work through how to implement a class in Python by creating the class that will hold the state of the world: the `State` class. The current state of all MRS variables *and* the state of everything in the world will be accessed through this class. Because we want the state to be changed and passed around, we will include an instance of it as the first argument on all predications. The implementation of the `State` object can be very simple for now:

```
# "class" declares an object-oriented class in Python
# The parenthesis after the "State" class name surround 
# the object the class derives from (object)
class State(object):

    # All class methods are indented under the
    # class and take "self" as their first argument.
    # "self" represents the class instance.

    # "__init__" is a special method name that
    # indicates the constructor, which is called to create
    # a new instance of the class. 
    def __init__(self, objects):
        # Class member variables are created by
        # simply assigning to them
        self.variables = dict()  # an empty dictionary

        # "objects" are passed to us as an argument of the
        # constructor by whoever creates an instance of the class
        self.objects = objects   

    # This is how predications will access the current value
    # of MRS variables like "x1" and "e1"
    def GetVariable(self, variable_name):
        # "get()" is one way to access a value in a dictionary.
        # Its second argument, "None", is what gets returned if the
        # key doesn't exist.  "None" is a built in value in Python
        # like "null"
        return self.variables.get(variable_name, None)

    # This is how predications will set the value
    # of an "x" variable. It has to return a *different*
    # state object with that variable set
    def SetX(self, variable_name, item):
        # You create a new "State" instance by
        # calling its class name like a method.
        # We pass "self.objects" as its first argument
        # so that State's "__init__" constructor will 
        # use the same world state we have here.
        # Now we have a new "State" object with the same
        # world state
        new_state = State(self.objects)

        # Make a *copy* of all the variables and put them
        # in the new instance using the built-in Python 
        # class called "copy"
        new_state.variables = copy.deepcopy(self.variables)

        # Dictionaries hold key/value pairs.
        # This is how you assign values to keys in dictionaries
        new_state.variables[variable_name] = item

        # "return" returns to the caller the new state with 
        # that one variable set to a new value
        return new_state

    # This is an iterator (described above) that returns
    # all the objects in the world
    def AllIndividuals(self):
        for item in self.objects:
            yield item
```
The variables store in our `State` object are treated as "immutable", meaning the system can treat each `State` instance as representing the state of the world, including MRS variables, at one "snapshot" in time. The system knows that the snapshot cannot be changed. This will be important because it allows us to do *backtracking* as we search our tree of solutions.

> Note: The *entire* State object is not immutable, just the assignment of values to variables.  We'll address this later, but it won't be a problem in the simple examples we're working with now.


Objects in the world can just be Python objects, although there are many other ways to represent them (the predication contract doesn't care). We'll create classes for each "type of thing" in our file system world:

```
class Folder(object):
    def __init__(self, name):
        self.name = name

class File(object):
    def __init__(self, name, size=None):
        self.name = name
        self.size = size
```

Creating a `State` object with a list of the objects from the example looks like this:

```
state = State([Folder(name="Desktop"), 
               Folder(name="Documents"), 
               File(name="file1.txt"), 
               File(name="file2.txt")])
```

Note that an instance of the `State` object is created by calling it like a function. This really calls the `__init__` function of `State`, and passes the supplied argument (a list) to `__init__`. Each object in the list that we are giving to `State` is created just like `State` was: by calling it as a function. Note that arguments can be named like `name="Documents"` to clarify what is going on.

Now you've seen some of the basic Python you'll see throughout the tutorial and we've defined the core `State` class we'll use in our predications.  Next, we'll [implement a predication](../devhowtoImplementPredication).
<update date omitted for speed>{% endraw %}