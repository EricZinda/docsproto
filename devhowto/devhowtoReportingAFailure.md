## Reporting a Failure
With all that in place, we can now start reporting errors from predications. As outlined in the [predication contract](devhowtoPredicationContract), "failure" is when the predication is not true for its arguments, so let's add a little code at the end of `large_a_1` to record an error when there is a failure. We'll call the new `ReportError()` method and pass it what (naively) seems like the right error given the code:

~~~
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
    x_target_value = state.GetVariable(x_target)
    if x_target_value is None:
        iterator = state.AllIndividuals()
    else:
        iterator = [x_target_value]
    
    degree_multiplier = DegreeMultiplierFromEvent(state, e_introduced)
    for item in iterator:
        if hasattr(item, 'size') and item.size > degree_multiplier * 1000000:
            new_state = state.SetX(x_target, item)
            yield new_state
        else:
            # starting a string with: f" allows you to put local Python
            # variables into it using {}, in a kind of template approach
            ReportError(f"'{item}' is not large")
~~~
`large_a_1` looks at an object, check if it has a size at all, and if so, if it is "large" and succeeds if it is. If not, a logical error to report would be "this thing is not large".

If we run "A file is very large" using our same example world:

~~~
a folder
a small file
a large file
a dog
~~~

... and using our new error heuristic, we'll get these failures (#2 will be remembered as the error using our new heuristic):

1. a `_file_n_of` failure
2. a `large_a_1` failure (since none are "very large")
3. a `large_a_1` failure (since none are "very large")
4. a `_file_n_of` failure

The actual error reported will be: "'a small file' is not large". Even though this error looked like it made sense in the code, it is pretty far from the one we wanted: "There isn't a very large file".  If the world was simpler, we might have gotten an even worse result.  For example in this world:
~~~
a dog
a folder
~~~
`file_n_of` would give us the error: "'a dog' is not a file" instead of "There isn't a very large file". Clearly a bad response.

Something is wrong with the approach. We can correct it if we remember what is going on at the abstract level: We are finding values for the variables that make the MRS true.  The *mechanics* are to feed every object in the world through the system, but the overall *objective* is to, for example, find an `x` that makes `_large_a_1` true. So, if we quit describing the *mechanics* and describe the failure of the *objective*, we'll get a better error.

Said another way: evaluating `_large_a_1(x)` means "Give me the large things in the world".  If it fails, that means: "There is not a large thing in the world". So, changing our code to be this:

~~~
@Predication(vocabulary, name="_large_a_1")
def large_a_1(state, e_introduced, x_target):
            
    ...
    
            ReportError(f"There is not a large thing")
~~~

Will respond to "A file is very large" with "There is not a large thing" which is ... better. One improvement is to make the error include "very" when "very" is modifying it, which is easy. But, even with "very" included, most users would still view it as a logical, if somewhat opaque, answer.  The [next section](devhowtoConceptualFailures) will improve it even more.