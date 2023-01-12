{% raw %}# Overview

This page provides a quick catalogue of ERS fingerprints for the
phenomena to be discussed at the [Comparative Computational
Semantics]() working meeting in Berlin in November 2014,
suitable for interactive exploration using the WeSearch
[Semantic Search Interface](http://wesearch.delph-in.net). The phenomena
are listed together with their fingerprints (in some cases, multiple
sets of fingerprints) and links to their ERG Semantic Documentation
pages. Copying and pasting the fingerprints into the Semantic Search
Interface will turn up all examples matching the fingerprints, which in
some cases also includes examples included to illustrate other
phenomena.

# Links

- [Semantic Search Interface to the CCS
Exemplars](http://wesearch.delph-in.net/esd/search.jsp): Find the
sentences to be discussed at the working meeting
- [Semantic Search Interface to
DeepBank](http://wesearch.delph-in.net/esd/search.jsp): Explore the
phenomena in a larger corpus of running text
- [ERS Representations as One PDF
File](http://svn.emmtee.net/trunk/uio/wesearch/ccs/erg/mrs.pdf)
- CCS Working Meeting Main Page
- ERG Semantic Documentation Main Page

# Phenomena

## 1. (Closed) Clausal Complements

Primarily illustrated by items 101–109.

    [ARG* h1]
    h2:[ARG0 e]
    { h1 =q h2 }
    
    nominalization[ARG0 x, ARG1 h]
    h:[ARG0 e]

[ERG Semantic Documentation: Propositional
Arguments]()

## 2. Coordination

Primarily illustrated by items 201–208.

Note: In this case the fingerprints we present on the ERG Semantic
Documentation page are anticipating some (technical) streamlining of the
analysis. Below are versions of the fingerprints that match the current
grammar (and the annotations we prepared for the working meeting).

    *_c[ARG0 x1, L-INDEX x2, R-INDEX x3]
    [ARG0 x2]
    [ARG0 x3]
    
    *_c[ARG0 e1, L-HNDL h2, R-HNDL h3]
    h2:[ARG0 e2]
    h3:[ARG0 e3]

ERG Semantic Documentation: Coordination

## 3. Ellipsis

Primarily illustrated by items 301–304.

    ellipsis_ref[ARG1 x]
    
    ellipsis_expl[ARG1 u]

ERG Semantic Documentation: Ellipsis

## 4. ‘Identity’ Copulae

Primarily illustrated by items 401–407.

    _be_v_id[ARG1 x1, ARG2 x2]
    h1:[ARG0 x1]
    h2:[ARG0 x2]
    { h3 =q h1, h4 =q h2 }
    
    cop_id[ARG1 x1, ARG2 x2]
    h1:[ARG0 x1]
    h2:[ARG0 x2]
    { h3 =q h1, h4 =q h2 }
    
    _be_v_nv[ARG1 x1, ARG2 h1]
    h2:[ARG0 x1]
    h1:[ARG0 e]
    { h3 =q h2 }
    
    _be_v_do[ARG1 x1, ARG2 h1]
    h3:[ARG0 x1]
    h2:[ARG0 e]
    { h1 =q h2, h4 =q h3 }
    
    _colon_nv[ARG1 x1, ARG2 h1]
    h2:[ARG0 x1]
    h1:[ARG0 e]
    { h3 =q h2 }

[ERG Semantic Documentation: Identity
Copulae]()

## 5. Nominalization

Primarily illustrated by items 501–506, but note that 503–506 are not
analyzed as nominalization in ERS (currently).

    nominalization[ARG0 x, ARG1 h]
    h:[ARG0 e]

[ERG Semantic Documentation:
Nominalization]()

## 6. Comparatives

Primarily illustrated by items 601-607.

    h:comp[ARG1 e]
    h:*_a*[ARG0 e]

ERG Semantic Documentation: Comparatives

## 7. Control Relations

Primarily illustrated by items 701–706, but note that 704–706 are not
analyzed as control in ERS (currently).

Note: In this case the fingerprints we present on the ERG Semantic
Documentation page are suggesting extensions to the fingerprint language
that are not currently supported in the search interface. Below is a
generalized version of the fingerprints that works with the present
interface.

    [ARG0 e1, ARG* x1, ARG* h1]
    h2:[ARG0 e2, ARG* x1]
    { h1 =q h2 }

[ERG Semantic Documentation: Control
Relations]()

## 8. Measure Phrases

Primarily illustrated by items 801–802; however, item 801 is not
included in our annotations and 802 is not (currently) treated as
involving a measure phrase.

    h:measure[ARG0 e1, ARG1 e2, ARG2 x]
    h:[ARG0 e2]
    [ARG0 x]

[ERG Semantic Documentation: Measure
Phrases]()

## 9. Parentheticals

Primarily illustrated by items 901–903, but note that item 901 is
analyzed as apposition instead.

    h1:parenthetical[ARG1 i1, ARG2 h2]
    h1:[ARG0 i1]

[ERG Semantic Documentation:
Parentheticals]()

## 10. Relative Clauses

Primarily illustrated by items 1001–1011, though note that 1010 and 1011
are not treated as involving relative clauses on this analysis, and
1003, as a reduced (untensed) relative, is not matched by the
fingerprints below.

    h1:[ARG0 x]
    h1:[ARG0 e{TENSE tensed}]
    
    relative_mod

[ERG Semantic Documentation: Relative
Clauses]()

    h1:with_p[ARG1 e1, ARG2 x1]
    h1:[ARG0 e1]
    h1:[ARG0 x1]

[ERG Semantic Documentation: Instrumental
Relatives]()

Last update: 2014-11-13 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/ErgSemantics_Ccs/_edit)]{% endraw %}