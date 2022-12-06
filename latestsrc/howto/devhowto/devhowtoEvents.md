{% raw %}## Event Variables
So far, we have been conveniently ignoring any event variables (those that start with "e"). Where instance (`x`) variables contain a single instance for any answer, event (`e`) variables are designed to build up a structure. They are how modifiers to a word get tracked. For example, we've been talking about a `_large_a_1(e2,x3) and _file_n_of(x3)` and have ignored what the event variable in `_large_a_1(e2,x3)` is for. We can't do this if we are trying to find a `_very_x_deg(e2, e1) and _large_a_1(e1,x3) and _file_n_of(x3)`.

In an MRS, any predication except a quantifier is said to "introduce" its first argument. If you look closely you'll see that every variable is only "introduced" by one predication in a given MRS.  In a sense, that variable *represents* that predication.  If a predication like `_large_a_1(e2,x3)` introduces an event variable, it does so to provide a place for other predications to hang modifiers to it.

For example, to represent something that is "very large", the word "very" needs to be able to attach its "veryness" to "large". For "very very large" you build a chain where the first "very" modifies the second which modifies "large". This is all done with events, and it happens like this because languages are recursive and allow all kinds of recursive constructions. Delphin needed a way to model this.

Here are the predications generated for: "very large" and "very very large":

```
# Very large
_very_x_deg(e2, e1), _large_a_1(e1,x3)

# Very very large
_very_x_deg(e3, e2), _very_x_deg(e2, e1), _large_a_1(e1,x3)
```

You can see that in "very large" `_very_x_deg` takes the event variable *introduced by* `_large_a_1` as an argument. The job of `_very_x_deg` is to put something in the event that `_large_a_1` can look for so that its behavior can be modified to be "very large". `_very_x_deg` also introduces *its own* event variable that other predications can modify. For example: "very very large". The first "very" modifies the event variable introduced by the second "very", etc.

This means, first, that we need a mechanism for handling event variables and, second, that our implementation of `_large_a_1` needs to be modified to pay attention in case its event is modified in some way.

Handling event variables in our solver will be easy. Since they need to be able to capture what could be a large buildup of modifications in a given sentence, we'll use a dictionary for them. We'll add a helper function to the `State` object to modify them:

```
class State(object):
    def __init__(self, objects):
        self.variables = dict() # a empty dictionary
        self.objects = objects

    def GetVariable(self, variable_name):
        return self.variables.get(variable_name, None)

    def SetX(self, variable_name, item):
        new_state = State(self.state) 
        new_state.variables = copy.deepcopy(self.variables)
        new_state[variable_name] = item        
        return new_state

    def AddToE(self, eventName, key, value):
        newState = copy.deepcopy(self)
        if newState.GetVariable(eventName) is None:
            newState.variables[eventName] = dict()

        newState.variables[eventName][key] = value
        return newState

    def AllIndividuals(self):
        for item in self.objects:
            yield item
```
`AddToE()` adds the key/value pair it is given to a (possibly new) dictionary that represents the event state and returns a new `State` object, just like `SetX()` does. 

Now let's create the `_very_x_deg` predication and modify the `_large_a_1` predication to pay attention to any modifications to its event.

```
def DegreeMultiplierFromEvent(state, e_introduced):
    # if a "very" is modifying this event, use that value
    # otherwise, return 1
    e_introduced_value = state.GetVariable(e_introduced)
    if e_introduced_value is None or "DegreeMultiplier" not in e_introduced_value:
        degree_multiplier = 1
    else:
        degree_multiplier = e_introduced_value["DegreeMultiplier"]

    return degree_multiplier


@Predication(vocabulary, "_very_x_deg")
def very_x_deg(state, e_introduced, e_target):
    initial_degree_multiplier = DegreeMultiplierFromEvent(state, e_introduced)

    # We'll interpret "very" as meaning "one order of magnitude larger"
    yield state.AddToE(e_target, "DegreeMultiplier", initial_degree_multiplier * 10)


@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
    x_target_value = state.GetVariable(x)
    if x_target_value is None:
        iterator = state.AllIndividuals()
    else:
        iterator = [x_target_value]

    degree_multiplier = DegreeMultiplierFromEvent(state, e_introduced)

    for item in iterator:
        # Arbitrarily decide that "large" means a size greater
        # than 1,000,000 and apply any multipliers that other
        # predications set in the introduced event
        if hasattr(item, 'size') and item.size > degree_multiplier * 1000000:
            new_state = state.SetX(x_target, item)
            yield new_state
```
`very_x_deg` adds a "DegreeMultiplier" to the event dictionary of its target, and also pays attention to *its own* introduced event in case someone added one there.  This allows "very very very very..." to work.

`large_a_1` now uses the same logic to determine how much to modify its default notion of "large". Obviously, what "large", "very", etc mean are very domain specific, but this illustrates the concept.

Last update: 2022-12-05 by EricZinda [[edit](https://github.com/ericzinda/docsproto/edit/main/devhowto/devhowtoEvents.md)]{% endraw %}