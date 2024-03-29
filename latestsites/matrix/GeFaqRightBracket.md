{% raw %}# Grammar Engineering Frequently Asked Questions

## The LKB says I'm missing a right bracket, but I can't figure out where. What should I do?

This error means that you have a syntax error somewhere near the
position that the LKB reports, perhaps but not necessarily a missing
right bracket. (The LKB is taking a guess there, sometimes it is right.)

Possible errors include:

- Missing right bracket.
- Missing & after a type name.
- Missing period at the end of a type definition.

To go to the position indicated by the error message, make sure your
current buffer in emacs has the right file open. Then do M-x goto-char
and type in the position number.

You can scan the area to see if something is obviously missing, but
usually its more efficient to use the tab indentation of tdl mode to
find the spot where somethings wrong. See [FAQ: How do I use tab to help
me figure out where my syntax error is?](https://blog.inductorsoftware.com/docsproto/matrix/GeFaqTabIndentation)

[Back to the Grammar Engineering FAQ](/GrammarEngineeringFaq).

Last update: 2012-08-14 by NedLetcher [[edit](https://github.com/delph-in/docs/wiki/GeFaqRightBracket/_edit)]{% endraw %}