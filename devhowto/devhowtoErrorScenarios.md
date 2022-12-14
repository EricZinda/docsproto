## Error Scenarios
We've gone through a lot to improve the error handling of the system, let's compare where we started and finished by going through some scenarios and comparing answers from the old and new code:


> World: Has files, but no large ones. 
> 
> User: "a file is large"
> 
> Old: "No, that isn't correct"
> 
> New: "a file is not large"

Pretty good. The better answer: "There are no large files" will require more complicated Natural Language Generation to get the "s" on "files". We'll do that in a future section.

What if there are no files at all?
> World: Has no files. 
> 
> User: "a file is large"
> 
> Old: "No, that isn't correct"
> 
> New: "a file doesn't exist"

The wording could be better ("There are no files"), but it is telling the user that there aren't any files *at all*, which is nice and clear. We can only improve the wording once we tackle NLG in the future section.

> World: Has files, but no large ones. 
> 
> User: "delete a large file"
> 
> Old: "Couldn't do that"
> 
> New: "a file is not large"

Same error has above. Great.

> World: Has large files. 
> 
> User: "I delete a large file"
> 
> Old: "Couldn't do that"
> 
> New: "I don't know who 'I' is"

Clearly says *why* the system couldn't do it now.

Overall, we now have error messages with the right information and semantics, but sometimes poor wording due to our simplistic Natural Language Generation functions. We'll get there.
