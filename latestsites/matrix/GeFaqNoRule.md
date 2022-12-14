{% raw %}# Grammar Engineering Frequently Asked Questions

## I've added a rule to my grammar but the LKB doesn't seem to have found it. What's happening?

There are a few possibilities here. If the rule is not available through
the View &gt; Grammar Rule or View &gt; Lexical Rule menus, then
perhaps:

1. You added a new rule type but did not instantiate the rule in
rules.tdl, irules.tdl, or lrules.tdl. Without a specific entry, the
type won't do anything.
2. You added a new rule type, and through a cut-and-paste error, gave
it the same name as an existing rule. If multiple entries have the
same name, only the last one will be incorporated into the grammar.
3. There is an error in your rule instance definition (e.g., the
constraints on the rule instance are incompatible with those of a
supertype) that the LKB flags only as a warning. In this case, a
warning will appear in the LKB Top window, but the grammar will
still load. You may have to scroll up to see the warning.

If the rule is available through View &gt; Grammar Rule or View &gt;
Lexical Rule, but not firing when you expect it to in parsing (not
visible in the parse chart), then most likely there is a bug in the
rule. To try to locate the bug, try interactive unification.

## Related topics

- [I don't think I'm getting any error messages. Does that mean I
don't have any errors?]()
- How do I get the LKB to show me the parse chart?
- [How do I look at fully specified lexical entries or
rules?]()
- How do I do interactive unification?
- [The LKB seems to be "forgetting" a constraint/definition I've
coded. Why?]()
- [I have a type/lexical entry/rule which doesn't seem to be
inheriting a constraint from its supertype. What might be going
on?]()

[Back to the Grammar Engineering FAQ](/GrammarEngineeringFaq).
<update date omitted for speed>{% endraw %}