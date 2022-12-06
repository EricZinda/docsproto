{% raw %}## The Predication Contract
It is important to understand [what MRS is]() and what [a scope-resolved MRS tree is]() before reading this section. Visit those links first to understand the basic concepts.

A scope-resolved MRS tree can be thought of as an *equation* that can be solved against a certain state of the world. One approach to solving an MRS is by *iteratively* finding assignments to the variables in the MRS, one by one, and collecting them. This is the "SLD" approach described in the [previous section](../devhowtoOverview). To solve an MRS tree using the SLD approach, we need to code the predications to meet a specific contract that our solver will rely on. Let's call this the "predication contract".

Recall that predications are of the form: `_table_n_1(x)` or `compound(e, x, x)`: they have a name and a set of arguments just like functions in mathematics or programming languages. We will be treating the predications we implement as classic programming language functions that can be "called" or "invoked". The two rules of our contract are"

1. The predication contract requires that, given a world state (the state of the software you want to evaluate the MRS against), a predication must iteratively its variables set to values that are true in that world state or fail. "Iteratively" means returning one answer the first time they are called, and then another the next time, until there are no more answers (in which case it fails).
2. It must also operate differently depending on whether its incoming variables are set (called "bound") or not ("unbound"):
- Calling a predication with unbound variables should return the unbound variables bound to a set of values from the world that, together, make it true. Calling it again should return a different set of bindings that make it true. Eventually, it will run out of things that can be true and should then fail.
- Calling it with bound variables should simply return the same values if true or fail if not. I.e. iterate once.

Let's use an example to illustrate: 

Imagine we want to build a natural language interface to the file system on a computer. We'll start with a simple a world with 4 things in it. We'll use Python classes (explained below) to represent them: 

```
[Folder(name="Desktop"),
 Folder(name="Documents"),
 File(name="file1.txt"),
 File(name="file2.txt")]
```
For now, we won't have files in folders, just the straight list of 4 objects in the file system.

In this world of 4 objects:

- Calling `_folder_n_of(x)` once should return `x=Folder(name="Desktop")`. Meaning: `x` was unbound, so: find an object in the world that is a "folder" and return `x` set to that object. 
- Calling it again will return `x=Folder(name="Documents")` since that is a different folder in the world state. 
- The third call will fail since there are no more folders.

Calling `_file_n_of(File(name="file1.txt"))` once will return `x=File(name="file1.txt")` because `x` was bound and thus `file_n_of` only needs to verify that it is a "file". The second call will fail.

This is the contract we need to build for each predication we want the system to understand. 

<update date omitted for speed>{% endraw %}