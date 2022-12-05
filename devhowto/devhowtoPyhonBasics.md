## Python Background: Basics, Classes, Functions, Iterators
This contract could be implemented in any programming language, but we'll be using Python. This section should give enough background so that even readers not familiar with Python can treat it like a "pseudo-language" and understand what it is doing. Even if you know Python, skim through this because we will be implementing a key class used elsewhere in the documentation.

The Python language has functions, classes, methods, variables, operators, statements, and other elements of many imperative programming languages such as C++, Java, Javascript, Go, etc.

It also has a notion of "iterators", which are objects that can be "iterated" or "listed" or "looped through". These can be lists (represented in square brackets like `[item1, item2]`) or special functions called "generators" which act like a list in that they return items one by one, but which allow code to dynamically generate the items that are returned.    

You iterate over an iterator of any type, whether it is a list or a generator, using the `for ... in ...` construct like this:

~~~
# '#" in Python starts a line with a comment
for item in iterator:

    # Indenting is how Python determines what code 
    # "belongs" to the thing above. Everything indented
    # here will get looped over

    # now "item" has the first value from iterator
    # and we can, for example, print it
    print(item)
~~~

If you want to write code to *dynamically* build an iterator (called a "generator"), you simply write code that calls `yield` to return each item. `yield` returns the value and then continues on the next line when the next value is asked for. If the function exits without a yield, the iteration stops:

~~~
# "def" is how you define a function in Python
# everything indented below it is in the function
def MyIterator1():
    yield 1
    yield 2
    yield 3

# Here's another function definition
# that does the same thing differently
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
~~~

We'll be doing lots of iteration and this syntactic sugar from Python makes it easy. 

Let's work through how to implement a class in Python by creating the class that will hold the state of the world: the `State` class. The current state of all MRS variables *and* the state of everything in the world will be accessed through this class. Because we want the state to be changed and passed around, we will include it as the first argument on all predications. The implementation of the `State` object can be very simple for now:

~~~
# "class" declares an object-oriented class in Python
# The parenthesis after the "State" class name surround 
# the object the class derives from (object)
class State(object):

    # All class methods are indented under the
    # class and take "self" as their first argument.
    # "self" represents the class instance.

    # "__init__" is a special method name that
    # indicates the constructor, which is called to create
    # a new instance of the class. Arguments beyond "self"
    # get passed to the function when the instance is created
    def __init__(self, objects):
        # Class member variables are created by
        # simply assigning to them
        self.variables = dict()  # an empty dictionary

        # "objects" are passed to us as an argument
        # by whoever creates and instance of the class
        self.objects = objects   

    # A standard "class method" is just a function definition,
    # indented properly, with "self" as the first argument

    # This is how predications will access the current value
    # of MRS variables like "x1" and "e1"
    def GetVariable(self, variable_name):
        # "get()" is one way to access a value in the dictionary.
        # The second argument, "None", is what to return if the
        # key doesn't exist.  "None" is a built in value in Python
        # like "null"
        return self.variables.get(variable_name, None)

    # This is how predications will set the value
    # of an "x" variable
    def SetX(self, variable_name, item):
        # You create a new instance of State by
        # calling its class name like a method.
        # We pass "self.state" as the first argument
        # so that its "__init__" constructor will copy it
        # Now we have a new "State" object with the same
        # world state
        new_state = State(self.objects)

        # Make a *copy* of all the variables and put them
        # in the new instance using the built-in Python 
        # class called "copy"
        new_state.variables = copy.deepcopy(self.variables)

        # Dictionaries hold name/value pairs.
        # This is how you assign values to keys in dictionaries
        new_state.variables[variable_name] = item

        # return returns to the caller the new state with 
        # that one variable set to a new value
        return new_state

    # This is an iterator (described above) that returns
    # all the objects in the world
    def AllIndividuals(self):
        for item in self.objects:
            yield item
~~~


Objects in the world can just be Python objects, although there are many other ways to represent them, the predication contract doesn't care. We'll create classes for each "type of thing" in our file system world:

~~~
class Folder(object):
    def __init__(self, name):
        self.name = name

class File(object):
    def __init__(self, name, size=None):
        self.name = name
        self.size = size
~~~

Creating a `State` object with a list of the objects from the example looks like this:

~~~
state = State([Folder(name="Desktop"), 
               Folder(name="Documents"), 
               File(name="file1.txt"), 
               File(name="file2.txt")])
~~~

Note that an instance of the `State` object is created by calling it like a function. This really calls the `__init__` function of `State`, and passes the supplied arguments to `__init__`. Each object in the list that we are giving to `State` is created just like `State` was: by calling it as a function. Note that arguments can be named like `name="Documents"` to clarify what is going on.
