{% raw %}# Grammar Engineering Frequently Asked Questions

## When I close the LKB Top Menu, is Lisp supposed to exit as well?

That depends on whether you're running from source or a precompiled
version of the LKB, and on how you close the LKB Top Menu. In general,
clicking the X in the upper right or left hand corner is not the
recommended fashion of closing the LKB Top Menu. Rather, choose Quit
&gt; Confirm Quit from the menu itself. In this case, if you are running
from precompiled code, the Lisp image will halt as well. If you are
running from source, your Lisp will still be alive.

## Related topics

- [When I switch between grammars (e.g., the English Resource Grammar
and a Matrix-derived grammar) the LKB sometimes behaves funny
(errors, seg faults, etc.). What's going
on?]()

[Back to the Grammar Engineering FAQ](/GrammarEngineeringFaq).
<update date omitted for speed>{% endraw %}