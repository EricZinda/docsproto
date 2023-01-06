{% raw %}# Background

For all we know, LUI talks a variant of the so-called *Linguistic Server
Protocol* (LSP), which was first implemented in the LKB. This page is
intended to document enough of the protocol to make it feasible to
connect LUI to other processing engines.

In the following, we take a LUI-centric perspective, i.e. *incoming*
means commands sent to LUI.

# Basic Data Types

- *integer*
- *string*
  
  - surrounded in double quotes
- *symbol*
  
  - no quotes
- *list*
  
  - \[ zero or more space-delimited items of homogeneous type \]

# Structured Data Types

These each look like \#D\[.....\], where the letter D in this case
indicates a *dag* structure, and the contents between the brackets
depends on the structure in question.

- *dag*
- *color*
- *font*
- *xtext*
- *xtext\_menu*
- *tree*
- *failure*
- *edge*
- *genedge*
  
  - experimental...

# Incoming Commands

- quit
- parameter *symbol* value
- message *string*
- group \[ *integer* \] *integer* *string*
- tree *integer* *tree* *string*
- chart *integer* *integer* *string* *edge*\*
- chart *integer* event *symbol* *integer*
- avm *integer* *dag* *string* \[ *list* \]
- text *integer* *xtext* *string*
- update *integer*
- close *integer*

# Experimental Incoming Commands

- genchart *integer* *list* *list* *string*

# Outgoing Commands

- compare *integer*+
- parse *string* *symbol* *symbol* *symbol*
- grammar *string*
- version *string*
- quit
- tree *integer* forget
- avm *integer* forget
- chart *integer* forget
- text *integer* forget
- unify *integer* *list* *integer* *list*
  
  - requests that path list1 inside edge int1 be unified with path
list2 inside edge int2
- browse *integer* *integer* *symbol*
  
  - requests further details on edge int2 of context (tree or chart)
int1. the last argument may be: avm, avm local, edges, chart,
generate, rephrase, mrs simple, mrs indexed, mrs scoped,
mrs robust, dependencies, tree, or entity.
- type *symbol* *symbol*
  
  - requests further details on the type symbol1. symbol2 may be:
hierarchy, skeleton, expansion, or \`source.

# Experimental Outgoing Commands

- genchart *integer* explore *list*
<update date omitted for speed>{% endraw %}