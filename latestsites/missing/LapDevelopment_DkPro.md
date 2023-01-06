{% raw %}# Local Build Instructions

Recipe for Stephan to obtain a collection of JAR files in the right
directory structure to populate the LAP Tree.

# Conventions Assumed

- no discontinuous regions
- no annotations on edges

# Observations and Open Questions

- ? uniqueness of identifiers
- currently unable to run the same tool twice
- record provenance:
- why is ‘annotations’ field a dictionary? by convention never more
than one annotation; the key seems redundant
- similarly, ‘links’ is list of lists for LAF compliance
- ‘index’ encodes sequence information but not absolute positions

# Action Items

- make LXF output proper JSON: hide \_id and produce double-quoted
JSON strings
- hide ‘head’ on dependency nodes
- hide ‘annotations’ on edges
- include --threads and --identifier as command line options
- pass tool identifier as parameter into adaptor

# Hypothetical (For Now)

- what should be the graph structure when a dependency parser
annotates two separate layers of token-level analysis, e.g. PoS tags
and stems (as features)
<update date omitted for speed>{% endraw %}