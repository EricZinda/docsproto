{% raw %}To ensure the compatibility of separately developed systems for working
with DELPH-IN-produced resources, we should formalize the formats of
files and structures used by multiple systems.

# Goals

- Provide a BNF representation of the syntax for each structure
- Provide an interpretation of fields, values, etc.
- Small Test set for implementers to test against
- "Official" implementations follow the specifications rather than the
other way around
- Documentation for future delphinistas

# Structures and Representations

## \[incr tsdb()\]

- profiles (relations, results, etc; see
[ItsdbReference](../ItsdbReference))
- [ItsdbDerivations](../ItsdbDerivations)

## MRS

- Simple MRS
- Indexed MRS
- XML Later...
- RMRS
- DMRS

## PET

- [PetInput](https://blog.inductorsoftware.com/docsproto/garage/PetInput)

# Discussion

## SEM-I

- A wellformed mrs normally has information about types, information
from the grammar
- It is desirable that the hierarchy among mrsitems and predicates get
to stand in hierarchical relation - different from in the grammar
- Semantic hierarchy and grammar hierarchy are separate. For example:
person-number is conflated as single property in the grammar, MRSs
dont
- How many grammars have a semi? ERG and [NorSource](/NorSource). Jacy
has an input to the transfer machinery.
- Can a type hierarchy be shared between the grammar and the SEM-I?
May be incompatible in principle.
- One shouldn't need a grammar loaded to do MRS manipulation.
- Building two hierarchies in parallel is a little duplication of
effort

## Documentation

The best action is to set up a page let people add info, mark it as
proposal/draft, and request for comments

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}