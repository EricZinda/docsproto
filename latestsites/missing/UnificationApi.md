{% raw %}# Desiderata

Currently, feature unification is handled by the
PET application or the LKB.
Running these requires that the user pull in the entire HPSG framework.
It would be nice to instead have a feature unification API. This would
enable easier experimentation by providing a fast and reliable
unification framework that works independently of HPSG.

This has not been implemented, but there are parts of the cheap parser
in PET that likely get us part of the way there.

# Cheap Libraries

The cheap source tree can be used to build the following libraries:

- libcheap.a: core feature unification, type hierarchy
- libmrs.a: MRS handling

Inside libcheap.a the unification algorithm is in dag-tomabechi.h: see
in particular the "dag\_node" and "dag\_arc" structures.

"dag\_node" includes an index into a type hierarchy structure. This
structure is built by flop and loaded at grammar-load time.

# Credit

YiZhang provided the information about the Cheap libraries.
<update date omitted for speed>{% endraw %}