{% raw %}# Notes in Progress on the WeSearch Query Language (WQL)

operator characters

- : (colon), separates optional node identifier from node content;
- \[ (left square bracket), separates node properties from outgoing
arcs;
- \] (right square bracket), terminates a list of outgoing arcs;
- (whitespace), separates role labels and values in list of arcs;
- , (comma), separates role–value pairs within list of outgoing arcs;
- \+ (plus sign), indicates (optional) lemma object property;
- / (slash), indicates (optional) pos property;
- ? (question mark), Lucene-style single-character wildcard;
- \* (asterisk), Lucene-style arbitrary sub-string wildcard;
- \| (vertical bar), logical disjunction (see below);
- ( and ) (left and right parentheses), grouping of sub-expressions
(see below);
- ! (exclamation mark), reserved for negation (to be defined);
- \\ (backslash), escape character, suppressing operator status for
all of the above.

It is conventional to separate descriptions of different nodes by
whitespace, in fact typically even linebreaks; furthermore, the node
identifier prefix (indicated by :) is conventionally not separated by
white space from the node description. However, unless we find a
technical reason to enforce these conventions, we will try to be robust
and even allow something like

      x : + terrible[ ARG1 y ]y:crisis[]

# Logical Operators

There is support for logical disjunction and grouping of
sub-expressions, to control the scope of disjunction; by default,
disjunction scopes at the highest possible level.

      (
       _light_a_1[ARG1 x]
      |
       _light_n_1[ARG0 y]
       x:compound[ARG1 y]
      )
      x:_bulb_n_1

The logical operators can only be used *between* nodes, i.e. not
*inside* the description of one node.

# Open Questions

What to do about parameterized predicates, e.g. named(Abrams); possibly
we can re-purpose the parentheses within the node description.

What to do about case distinctions? Ideally, we would like matching of
node and role labels to not be case-sensitive (but parameters like
"Abrams" in the above can make case distinctions). Maybe use the
first-line Lucene index to normalize case distinctions in labels?

Last update: 2016-04-21 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/WeSearch_QueryLanguage/_edit)]{% endraw %}