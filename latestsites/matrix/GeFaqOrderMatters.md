{% raw %}# Grammar Engineering Frequently Asked Questions

## In which files does order matter?

Order in fact matters in all of the .tdl files, but in different ways:

- In labels.tdl, order matters because the LKB will use the first
label whose constraints match the node to be labeled, even if there
is a more specific label further down the file that also matches.
Therefore, if you have two labels which are consistent with each
other, unless you put the more specific one first, it will never get
used.
- In all of the .tdl files (including labels.tdl), order matters in
that if you define two types or entries with the same identifier
(string before the :=), the second will overwrite the first. The LKB
will print a warning when this happens.
- [Type addendum](https://blog.inductorsoftware.com/docsproto/matrix/GeFaqTypeAddendum) statements (:+) are valid only if
they follow the initial type definition statement (:=) for the type
in question.
- For the same reasons, order matters across files. If you define a
type with the identifier foo in two or more different files, only
the definition from the file loaded last (per lkb/script) will be
retained.

## Related topics

- [How do I see what definition the LKB has read in for a
type?](https://blog.inductorsoftware.com/docsproto/matrix/GeFaqViewType)
- [How do I look at fully specified lexical entries or
rules?](https://blog.inductorsoftware.com/docsproto/matrix/GeFaqViewEntry)

[Back to the Grammar Engineering FAQ](/GrammarEngineeringFaq).

Last update: 2012-09-17 by NedLetcher [[edit](https://github.com/delph-in/docs/wiki/GeFaqOrderMatters/_edit)]{% endraw %}