{% raw %}This page documents the structure and form of annotations in LAP, i.e.
the adaptation of the Linguistic Annotation Framework (LAF) to LAP and
how it is stored in the database.

In the following, we will use the following input file toy.txt as a
running example:

    The cat chased the dog.
    Fido barked.

# MongoDB Terminology

MongoDB is a document database. This means that instead of storing
records, as a traditional SQL database, it stores free-form JSON
documents. Individual documents are grouped into *collections*,
corresponding roughly to the table of an SQL database, and collections
are grouped into databases.

LAP stores output from tools in per-user databases, and the records
created from a single run of a tool is stored in a single collection.
Thus, there is a one-to-one correspondence between collections and tool
invocations.

All documents stored in MongoDB contain an attribute \_id, a globally
unique identifier used internally by the database.

## The receipt

Metadata related to a sequence of processing steps in LAP is stored in a
file called the *receipt*. This file contains the names of the
collections created by previous processing steps and what kinds of
annotations are present in the database, and it is stored as a JSON
document. Tool scripts take the receipt as an input argument and produce
a new, updated receipt reflecting the information added by the tool.

For example, after uploading toy.txt and running it through the NLTK
punkt sentence segmenter and the REPP tokenizer, we get this receipt:

    {
        "annotators": {
            "nltk_punkt": "ff7fe1ce-1fe7-11e5-9573-8c705a6aa768",
            "repp": "ff9fe12c-1fe7-11e5-90ae-8c705a6aa768"
        },
        "media": {
            "text": "ff55d9d8-1fe7-11e5-9045-8c705a6aa768"
        },
        "annotations": {
            "token": [
                "repp"
            ],
            "sentence": [
                "nltk_punkt"
            ]
        },
        "receipt_origin": "repp"
    }

As we can see, there are four top-level fields in the document:
receipt\_origin, media, annotators, and annotations. The receipt\_origin
field is name of the tool that produced this receipt, in our case repp.
The media field is a dictionary of media types linked to the name of the
collection containing that medium. Currently, only text is supported.

The annotators field is a dictionary whose keys are the tools run on the
dataset so far and whose values are the names of the collections
containing the records created by the tool, and annotations is a
dictionary of annotation types (described in further detail later in
this document) and the names of the tools that have added annotations of
this type to the data.

The LAP API provides functionality to parse the receipt and query the
database in lap.store.

# LAF and LAP Terminology

LAF considers linguistic annotation to be annotations over a graph
comprised of *nodes* and *edges* (collectively *graph elements*), with
nodes possibly being linked to one or more *regions* in a *medium*. The
LAF model is agnostic to media types (text, audio, video, etc.), but LAP
currently only supports textual data.

LAP stores individual nodes, edges and regions as individual records in
the database.

## Regions

A *region* is a delimited subset of the media. For text, this is
obviously character offsets into the raw input string. LAP stores these
regions as (start, end) pairs, where start is the character offset of
the first character in the region and end is the offset of the first
character *not* in the region (that is, the region is the semi-open
interval \[start, end)). The offsets are zero-indexed.

For example, the region corresponding to the first sentence in our
example text is the span 0, 23 and it is stored as the following
document:

    {
            "_id" : ObjectId("5593d512b8c2543703f3cfe6"),
            "origin" : "nltk_punkt",
            "index" : 0,
            "anchors" : [
                    0,
                    23
            ],
            "type" : "region",
            "id" : "nltk_punkt-r1"
    }

## Nodes and Edges

A *node* represents anything that can be annotated with linguistic
information (tokens, sentences, PoS tags, etc.), while an *edge*
represents links between these (for example, a node representing a PoS
tag is linked by an edge to the node representing the tagged token).
Both edges and nodes can have *annotations*, feature-structures
containing the information in the node, but crucially *linguistic*
information shall only be contained in annotations on nodes; annotations
on edges can only for non-linguistic information.

All graph elements share the attributes id, a unique identifier, index,
a zero-indexed total ordering of the element relative to its sibling
elements of the same kind (or -1 if not applicable), rank, the ordering
of an element relative to other elements with the same index, and
origin, containing the name of the tool that produced it. Finally, a
graph element has an attribute annotations containing the feature
structure with the annotation actually produced by the tool (for
example, the PoS tag output by a tagger).

Nodes may additionally have a list of links, each link being a list of
ids of region objects relevant to the node (such as the region
corresponding to a token output by a tokenizer), and edges have the
additional attributes from and to, being the ids of the pair of nodes
linked by the edge.

For example, the first token created by REPP in our toy example is:

    {
            "_id" : ObjectId("5593d513b8c2543727c6fde6"),
            "origin" : "repp",
            "index" : 0,
            "links" : [
                    [
                            "repp-r1"
                    ]
            ],
            "rank" : 0,
            "annotations" : {
                    "repp" : {
                            "class" : "token",
                            "label" : "The"
                    }
            },
            "type" : "node",
            "id" : "repp-n1"
    }

This node is then linked to a sentence node (created by a different
tool, and stored in a different collection) by the following edge:

    {
            "_id" : ObjectId("5593d513b8c2543727c6fde7"),
            "origin" : "repp",
            "index" : 0,
            "from" : "repp-n1",
            "annotations" : {
                    "repp" : {
                            "class" : "token-link"
                    }
            },
            "to" : "nltk_punkt-n1",
            "type" : "edge",
            "id" : "repp-e1"
    }

The annotations field is a dictionary, currently with only a single
entry with the same name as the origin field, containing a dictionary
with the annotations produced. The exact structure of the annotation
dictionary depends on the type of annotation, described further in the
next section.

# Types of Annotations

LAP supports a number of different kinds of annotation. The type of
annotation is determined by the class entry in the annotation
dictionary.

## The \`sentence\` and \`token\` classes

The sentence and token annotation classes contains information relevant
to sentences and tokens, respectively. At present, these contain only
the single attribute label, being the label produced by the tool. This
label may or may not be the same as the raw substring in the media, as
the tool may normalize whitespace or downcase sentence-initial tokens
that are not proper names.

For example the token annotation for the first token in our example text
is:

    {
            "class" : "token",
            "label" : "The"
    }

## The \`morphology\` class

The morphology class of annotation contains information relevant to the
morphology of a node. Annotations of this type *must* contain at least
one of the attributes pos, the part-of-speech, or lemma, the lemma (the
pos field is not required in order to allow for dedicated lemmatizers
that only produce lemmata). The annotations may furthermore contain the
fields features, tool and language specific morphological features, and
derivation, containing information on derivational morphology.

For example, the PoS annotation created by [HunPos](/HunPos) on the
first token of our example is:

    {
            "class" : "morphology",
            "pos" : "DT"
    }

## The \`dependency\` class

Annotations of the dependency class represent (parts of) dependency
graphs. These are stored somewhat differently from token-level
information. Since LAF prescribes that linguistic information *must* be
attached to nodes and not edges, the intuitive approach of encoding
dependencies solely as edges between token-level nodes is not possible.
Instead, dependencies are encoded by a node and a pair of edges. The
node, annotated with data in the dependency class, contains the
linguistic information, while the edges link the head and dependent
nodes to the dependency node.

Nodes in the dependency class contain the attribute label, being the
dependency label of the arc, and the attribute head, the token index of
the head token. This latter attribute is a convenience attribute used
internally by the application to simplify conversion to CoNLL-like
formats.

## The \`linkage\` class

Nodes in the token class are linked by edges to nodes in the sentence
class, and nodes in the morphology class are linked to nodes in the
token class. However, some tools produce both tokens and morphology at
once, which will result in two sets of edges being stored in the same
collection. To easily let us extract, for example, the edges linking the
morphology nodes to token nodes, edges are annotated with the linkage
class. Annotations in this class have the attributes domain and range,
specifying what kind of node the edge is going from and what it's going
to, respectively.

For example, the edge linking the first token of our example text to the
first sentence is annotated with:

    {
            "class" : "linkage",
            "domain" : "token",
            "range" : "sentence"
    }
<update date omitted for speed>{% endraw %}