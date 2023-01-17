{% raw %}# Overview

Since the publication of Copestake (2002), the general documentation of
the LKB system (and its approach to using typed feature structures in
grammar writing), the software has been continuously extended. Although
we have in general attempted to preserve the documented functionality
and interfaces, there is an array of additional facilities that users
may find useful. The following is an overview of some of the major new
components. All of them are optional, in the sense that basic grammar
writing and processing can be achieved without using extra facilities;
in fact, some of the new components target \`power' users (building very
large-scale grammars) and specific applications (e.g. machine
translation). A more detailed summary of code changes to the LKB is
available from the CVS source repository logs and the
[LkbEvolution](https://blog.inductorsoftware.com/docsproto/missing/LkbEvolution) page.

# Lexical Database Integration

Versions of the LKB since about 2004 come with an optional interface to
an external database storing the lexicon. See the [LkbLexDb](/LkbLexDb)
page for more information and instructions on how to set up the database
and maintaining it.

# Semantic Interface (SEM-I) Support

# Interfacing the LKB to an OWL Ontology

# Preprocessor Support

See [LkbPreprocessing](https://blog.inductorsoftware.com/docsproto/missing/LkbPreprocessing). Topics covered include:
XML-Based Interface to External Preprocessors, (Internal) Finite State
Preprocessing, Characterization.

# MRS Rewrite System (Transfer Component)

# Feature Structure Unfilling

Unfilling of feature structures is the removal of redundant information
from feature structures, in order to make them smaller. When only
redundant information is removed, they contain precisely the same
information as the original feature structures, but with less room.
Unfilling support in the LKB was added by
FrederikFouvry and is documented further on the
[LkbUnfilling](https://blog.inductorsoftware.com/docsproto/missing/LkbUnfilling) page.

# Linguistic User Interface (LUI)

The Linguistic User Interface (LUI) is an on-going project to build a
visualization tool for the most common object types in constraint-based
grammars, i.e. trees, feature structures, MRSs, charts, et al. While the
LKB comes with built-in browsers for all of these, the current use of
the CLIM (Common-Lisp Interface Manager) toolkit in the LKB severely
limits portability, ease of use, and programmatic extension. The
[LkbLui](https://blog.inductorsoftware.com/docsproto/tools/LkbLui) pages describe the current state of play for
integration of LUI with the LKB.

# Linguistic Server Protocol (LSP)

# Robust Minimal Recursion Semantics
<update date omitted for speed>{% endraw %}