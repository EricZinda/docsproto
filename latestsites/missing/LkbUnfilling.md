{% raw %}# Overview

Unfilling of feature structures is the removal of redundant information
from feature structures, in order to make them smaller. When only
redundant information is removed, they contain precisely the same
information as the original feature structures, but with less room.

One application for unfilling is the display of feature structures, such
as the ones associated with chart edges. When they are displayed in
full, they can be huge, but a lot of the information is redundant.
Unfilled, the feature structure becomes much clearer.

The LKB menus that display feature structures have been extended with
menu entries to display unfilled feature structures (in the "Parse Tree"
and "Chart" windows). The best way to get familiar with unfilled feature
structures is to compare a few with the unfilled variants.

As unfilling does not throw away any information from the feature
structures, they can also be used for manual unification (as used for
debugging). Note however that the results are not necessarily unfilled.

# Unfilling More Technically

Unfilling is in some sense the opposite operation of "Expand type". The
latter takes a type and make a feature structure out of it by
recursively adding all constraints that have been defined with the used
types. (Sometimes, this is called "filling".) Unfilling takes a feature
structure and recursively removes all information that "Expand type"
would have added (this is the redundant information). Unfilling an
expanded type, for instance, returns a feature structure displaying only
the type name (note though that it is not always that simple).

Last update: 2005-03-25 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LkbUnfilling/_edit)]{% endraw %}