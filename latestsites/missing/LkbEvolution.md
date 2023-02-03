{% raw %}# Detailed Development Log of Code Changes

This page is intended as a relatively technical log of changes to the
LKB source code, in a sense a condensed summary of the CVS revision
history. LKB developers will likely find this information most
interesting, but it may also help some users to stay up-to-date on
latest LKB development. For a more high-level summary of changes to LKB
functionality and additions of new facilities, see
[LkbUpdates](https://blog.inductorsoftware.com/docsproto/missing/LkbUpdates) instead.

Please note that some of the LKB variables and functions mentioned in
these development logs refer to LKB internals and might change in future
versions; documentation of new or experimental facilities here is
primarily targetting LKB developers (or system integrators), thus it
seems important to maintain a conceptual distinction between the
\`official' LKB interface (e.g. what is documented in Copestake, 2002,
plus updates on, say, the [LkbUpdates](https://blog.inductorsoftware.com/docsproto/missing/LkbUpdates) page) and system
internals.

## Wed Feb 9 12:35:40 PST 2005

Portability::

- to allow compilation on SBCL (a variant of CMUCL that apears to be
very actively developed currently and is available for many
platforms, including
  
  Linux on PPC and MacOS X) i had to rename the LKB structure type to
ltype. this change is trivial in nature but affects a large number
of source files; it is possible that i introduced errors as i worked
through the renaming. furthermore, i moved to the latest versions of
PPCRE (the regular expression library) and the defsystem() facility;
i can now compile and run on SBCL on Linux (x86.32).

## Fri Dec 31 13:28:52 PST 2004

Selective Unpacking::

- the unpacking code has moved into a new file main/unpack.lsp, the
(unused) *id* argument to unpack-edge!() et al. has been deleted,
and a new selective unpacking mode added: selectively-unpack-edges()
searches for the *n* best consistent results (as determined by a
Redwoods-style ME model) without exploring the complete forest;
generate-from-mrs() takes a new *nanalyses* keyword argument to
enable selective unpacking.

64-Bit Support::

- to add support for 64-bit Linux (on AMD64 and EM64T), all binary
directories
  
  formerly called linux have been broken up into linux.x86.32 and
linux.x86.64; a small number of code changes was required to add
support for the (new) Allegro CL 7.0 and allow the LKB to run in
true 64-bit mode; the PVM et al. binaries and .so files bundled with
\[incr tsdb()\] have been recompiled against PVM 3.4.5 and are
included in the distribution in both a 32-bit and 64-bit version
each.

## Fri Nov 26 15:16:31 GMT 2004

Redwoods-Style MRS Banking::

- discriminant extraction, storage in \[incr tsdb()\], and the CLIM
and HTML UIs now support comparison and annotation of sets of MRSs;
discriminants in this mode are triples extraced from the
(handle-free) elementary dependency view
  
  on MRSs, either of the form (*predicate*, *role*, *predicate*) or
(*predicate*, *property*, *value*), where the latter form implicitly
assumes that the specific property occurs in the ARG0 of the first
*predicate*. to make multiple occurences of the same predicate
unique, it is necessary to have a way of \`anchoring' each EP to a
part of the original input: for the time being, MRS banking depends
on the availability of a new LNK property in EPs (see below).

Generation from Fragmented MRSs::

- in LOGON, there is a notion of \`fragmented' MRSs, i.e. a single MRS
that corresponds to a sequence of MRSs associated to a sequence of
chunks found by the (XLE) parser in robust mode; while each fragment
is expected to be semantically well-formed, the individual pieces
are connected by virtue of a
  
  *fragment\_rel* that can be viewed as a highly underspecified
conjunction, i.e. uses roles L-HNDL, L-INDEX, R-HNDL, and R-INDEX to
encode a binary tree. generation from fragmented MRSs is triggered
by fragmentp() of the input MRS to generation, then aims to extract
*connected* fragments, generate from each individually, and
cross-multiply the resulting strings. new variables:
\*semi-fragment-relations\* and \*fragment-start-symbols\*.

Discovery of Orthographic Variants::

- there is new code to compile a file in the format of variants.tab as
it is part of recent versions of the ERG. essentially, the code
looks for sets of lexical entries that are equivalent modulo STEM
and ONSET and outputs an ordered list of (identifiers of) such
lexical entries, with the additional information of whether or not
they occur in \*duplicate-lex-ids\* (the ones following the colon in
variants.tab), i.e. are disabled for generation. new variable:
\*orthographic-variants\* (a hash table relating such sets); new
functions: find-orthographic-variants() and
orthographic-variants-p().

MRS Internals::

- the scratch slot has been removed from the psoa structure (it was
unused, and the transfer component which had originally introduced
it no longer has a need for it). a new link slot was added to the
rel structure, jointly with support in the MRS reader and printer(s)
to support a LNK property on EPs, viz. a list of (token) identifiers
corresponding to this bit of MRS. the idea is the same as with
characterization' (i.e. the CFROM and CTO\` properties on EPs), but
in some set-ups (i.e. the XLE, [VerbMobil](/VerbMobil), YY) there is
no way of obtaining (or defining) character positions; new variable:
\*rel-link-feature\*. other minor changes to MRS internals include a
new variable \*mrs-equalp-ignored-roles\* to further parameterize
mrs-equalp() (i.e. allow an application to specify a set of roles to
be ignored for the test) and a means of color-coding individual EPs
in MRS HTML output, see changes in basemrs.lisp and interface.lisp.

Minor LKB-Internal Changes::

- the edge structure now has an additional slot string to allow
recording the surface form associated to an edge explicitly, i.e. on
generator outputs. the cache in unpack-edge()! has been simplified
to no longer incur each unpacking failure (which was done
exclusively for accounting purposes) for each context that embeds an
edge; the effect is that some of the problematic items in generation
from the new Rondane corpus no longer cause apparent non-termination
in upacking (viz. where there are huge numbers of globally
inconsistent hypothesis in the forest as a result of the latest ERG
move to restrict the syntactic information associated to
punctuation).

\[incr tsdb()\] Functionality::

- for PVM communication, a new variable \*pvm-encoding\* or additional
slot encoding on cpu definitions can be used to force a certain
encoding for \[incr tsdb()\] to client communication; for backwards
compatibility, the default is nil, in which case the encoding
continues to be determined by arbitrary environment factors, e.g.
value of LANG and -locale option on Lisp start-up. furthermore,
there is emerging support for an alternative Redwoods update mode,
looking for an exact match to the \`gold' target rather than using
discriminants; also, the stochastic experimentation tools have been
significantly extended to support scripting of series of experiments
and the type of set-up documented in the TLT04 paper (see
redwoods.lisp and maxent.lisp).

Extension of Transfer Engine::

- the MRS rewrite engine has seen a couple of bug fixes and extensions
that are
  
  all backwards-compatible (e.g. the addition of EQUAL and SUBSUME
flags) since its last release from the LOGON source code repository.
while this add-on component is still exclusively used within LOGON,
hope that there will be separate documentation at some point.
<update date omitted for speed>{% endraw %}