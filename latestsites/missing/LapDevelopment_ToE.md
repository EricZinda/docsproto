{% raw %}# Background

# Processing Notes

Download the [English ToE Graph](http://purl.org/linkedpolitics/English)
in Turtle format (June 3, 2015), a file of 421 megabytes, which we
version as
[english.ttl](http://svn.emmtee.net/lap/trunk/public/toe/english.ttl) in
the public section of the LAP SVN repository.

To simplify parallelization, we extract the transcribed text of each
speach into a separate file, also expanding escaped newlines (‘\\n’),
replacing non-breaking spaces with regular spaces, and stripping initial
and trailing whitespace
(‘[split.py](http://svn.emmtee.net/lap/trunk/public/toe/split.py)’):

      python split.py english.ttl /work/users/oe/toe/txt

The June 2015 version of the data comprises 292,379 speeches (for some
63 million whitespace-separated tokens). We create groups of 300
speeches (files) each:

      for i in txt/*.txt; do basename ${i%%.txt}; done \
      | split -l 300 -a 3 -d - batch.0;

Each of the groups can be processed sequentially (one speech at a time)
using the ToE-specific
‘[parse](http://svn.emmtee.net/lap/trunk/public/toe/parse)’ workflow,
which comprises the following analysis steps:

- *CIS Tokenizer* for sentence segmentation;
- *REPP* for PTB-style tokenization;
- the *B&N* parser for PoS tagging and dependency parsing;
- export to RDF, using the LAP ontology (see below).

Assuming the LOGON
‘[trickle](http://logon.emmtee.net/trunk/uio/titan/trickle)’ script,
parsing jobs can be submitted for processing on ABEL as follows:

      for i in /work/users/oe/toe/batch.0???; do \
        echo sbatch ~/src/lap/public/toe/parse "${i}"; 
      done > ~/src/lap/public/toe/toe.0.job
    
      cd log;
      $LOGONROOT/uio/titan/trickle --start --limit 400 ../toe.0.job
    
      while true; do $LOGONROOT/uio/titan/trickle --limit 400 ../toe.0.job; sleep 60; done

After watching the first several hours of parsing, it appears that
processing the complete corpus will take about 170,000 cpu hours (which
seems unreasonably high—even for the relatively costly B&N parser and
our wasteful strategy of re-initializing the parser for each speech) and
will give rise to approximately 2.7 billion triples.

# Linguistic Annotations

Linguistic annotations of the text data available at
<http://linkedpolitics.ops.few.vu.nl/> are offered in the form of rdf
named graphs. Such graphs are linked to the text content for each speech
in a given day in the ToE data; an example file containing the full
graph presented in this article is available at
<http://svn.emmtee.net/lap/snug/toe14/rdf/ns1:Speech_6.trig>.
Annotations from the tools in LAP are related to each other using the
LAF data model. The information is encoded in rdf triples defined by a
LAP ontology that can be viewed in full at
<http://svn.emmtee.net/lap/snug/toe14/rdf/lap.ttl>.

The example contains sentence, token, part-of-speech and dependency
annotations for **ns1:Speech\_6** (the 6th plenary speech held on
20-07-1999). The named graph **ns1:Graph\_Speech\_6** is linked to
**ns1:Speech\_6** via the predicate **lap:hasLapAnnotations**:

    ns1:Speech_6 lap:hasLapAnnotations ns1:Graph_Speech_6.

The graph itself with the pertaining annotations exists in [TriG
syntax](http://www.w3.org/TR/trig/):

    ns1:Graph_Speech_6 {
    
    lap:bn_N29 a lap:Dependency;
      dependency:type "SBJ".
    
    lap:bn_N30 a lap:Dependency;
      dependency:type "ROOT".
    
    lap:bn_N31 a lap:Dependency;
      dependency:type "OBJ".
    ...
    }

With a sparql database aware of the ToE data, the LAP ontology and the
described named graph, obtaining all the tokens for **ns1:Speech\_6**
can be achieved with the following query:

    BASE <http://purl.org/linkedpolitics/English>
    PREFIX lpv: <vocabulary/>
    PREFIX ns1: <eu/plenary/1999-07-20/>
    
    PREFIX lap: <http://lap.uio.no/rdf/lap/> 
    PREFIX token: <http://lap.uio.no/rdf/lap/token_> 
    
    select ?lapid ?token  
    WHERE {
        ns1:Speech_6 lap:hasAnnotation ?b.
        GRAPH ?b {
            ?token a lap:Token.
            ?token token:surface ?v
        }
    }

Output from the sparql engine:

    -------------------------------
    | lapid        | token        |
    ===============================
    | lap:repp_N1  | "–"          |
    | lap:repp_N2  | "Thank"      |
    | lap:repp_N3  | "you"        |
    | lap:repp_N4  | "for"        |
    | lap:repp_N5  | "clarifying" |
    | lap:repp_N6  | "that"       |
    | lap:repp_N7  | "point"      |
    | lap:repp_N8  | "."          |
    | lap:repp_N9  | "However"    |
    | lap:repp_N10 | ","          |
    | lap:repp_N11 | "you"        |
    | lap:repp_N12 | "don”t"      |
    | lap:repp_N13 | "know"       |
    | lap:repp_N14 | "how"        |
    | lap:repp_N15 | "long"       |
    | lap:repp_N16 | "this"       |
    | lap:repp_N17 | "would"      |
    | lap:repp_N18 | "have"       |
    | lap:repp_N19 | "lasted"     |
    | lap:repp_N20 | "had"        |
    | lap:repp_N21 | "it"         |
    | lap:repp_N22 | "been"       |
    | lap:repp_N23 | "an"         |
    | lap:repp_N24 | "address"    |
    | lap:repp_N25 | "!"          |
    | lap:repp_N26 | "("          |
    | lap:repp_N27 | "Applause"   |
    | lap:repp_N28 | ")"          |
    -------------------------------

Last update: 2015-06-06 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_ToE/_edit)]{% endraw %}