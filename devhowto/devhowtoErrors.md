## Handling and Reporting Errors
Before we go any further, we need to step back and work through how to deal with errors and failure in the system. The way things are currently built, if the user says "there is a large file" they get the same thing back if there are no files as they do if there are files, but no large ones: "No, that isn't correct".  If the user says "I delete a file" or "Bill deletes a file" they get the response: "Couldn't do that".

We can do much better than this.

