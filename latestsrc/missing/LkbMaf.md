{% raw %}A (modification of) the Morpho-syntactic Annotation Framework (MAF) has
been integrated into the LKB. MAF is currently an ISO Working Draft
(<http://www.tc37sc4.org/new_doc/ISO_TC_37-4_N225_CD_MAF.pdf>), and
provides a framework in which an (XML) standoff annotation document is
used to describe annotations with regard to a processed document. Our
modification of the MAF XML format is conceptually compatible with the
MAF draft, and syntactically our MAF/LKB XML format is largely
compatible with the MAF XML format. Using MAF/LKB we are able to ease
the integration of preprocessing components into the LKB setup (work on
other DELPH-IN components, such as PET, is ongoing).

The MAF/LKB XML serialization format consists of a &lt;maf/&gt; header
followed by &lt;token/&gt; and &lt;wordForm/&gt; annotation definitions.
The annotation elements live in a lattice (directed acyclic graph). (MAF
XML allows the annotation elements to be listed sequentially, but we
insist on the catch-all lattice representation for ease of machine
processing.)

The global &lt;maf/&gt; element carries global metadata relative to the
annotated document as a whole. Mandatory document and addressing
elements reference the document to which the standoff annotations refer,
and the pointer addressing scheme used (eg. character offsets,
xpoint-based addressing, ... ). Non-mandatory metadata are handled
following the recommendations of the OLAC Metadata Standard
(<http://www.language-archives.org/OLAC/metadata.html>).

Sample MAF header:

     <maf document='text.xml' addressing='xchar'>
      <olac:olac xmlns:olac="http://www.language-archives.org/OLAC/1.0/"
       xmlns="http://purl.org/dc/elements/1.1/"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.language-archives.org/OLAC/1.0/ 
          http://www.language-archives.org/OLAC/1.0/olac.xsd">
       <creator>LKB</creator>
       <created>12:11:43 12/12/2005 (UTC)</created>
      ...

The standoff annotations are grounded via &lt;token/&gt; elements. A
&lt;token/&gt; element anchors annotations to a contiguous span of text,
defined via pointers in from/to attributes. The addressing scheme for
these pointers must be specified in the &lt;maf/&gt; header. Each
&lt;token/&gt; element possesses an id attribute for reference by
&lt;wordForm/&gt; elements. Additionally, a value attribute may be used
to record the contents of the span (eg. that between the from and to
pointers).

Sample &lt;token/&gt; element (incomplete -- see below):

      <token id='t2' from='4' to='7' value='dog'/>

The annotation content is provided by &lt;wordForm/&gt; elements. This
content is represented as a typed feature structure following the
TEI/ISO XML format. This structure should contain a meta component
describing the component which produced the annotation content.

Each word form is built on top of one or more &lt;token/&gt; or other
&lt;wordForm/&gt; elements -- eg. they define a hierarchical structure
with &lt;token/&gt; elements forming the leaves. The tokens associated
in this manner with a &lt;wordForm/&gt; must form a contiguous sequence.
(The MAF draft allows a &lt;wordForm/&gt; to reference zero tokens; our
approach is to instead introduce pointlike &lt;token/&gt;'s in such
cases.) The annotation hierarchy is defined via a daughter attribute on
&lt;wordForm&gt; elements (NOTE: this is our generalisation of the MAF
draft's tokens attribute -- the MAF draft allows only for explicit XML
nesting of &lt;wordForm/&gt;'s, but we find this inadequate in the
general case). The daughters attribute is a space-separated list of
token and/or wordForm ids; each &lt;wordForm/&gt; element possesses an
id attribute for this purpose (NOTE: the MAF draft does not define such
an attribute).

Additional &lt;wordForm/&gt; attributes are provided by the MAF draft,
primarily for the purposes of convenience (eg. form, tag). We find these
additional attributes unnecessary for our purposes.

Sample &lt;wordForm/&gt; element (incomplete -- see below):

     <wordForm id='w2' daughters='t1'>
      <fs>
       <f name='stem'>dog</f>
      <fs>
     <wordForm/>

The &lt;token/&gt; / &lt;wordForm/&gt; elements live as edges on a
global lattice for the full document. This provides an elegant
representation of structural ambiguity, able to scale to the complexity
which may be produced by, say, a speech recoginiser. (NOTE: The MAF
draft allows a simple sequential listing of &lt;token/&gt;'s /
&lt;wordForm/&gt;'s -- for the purposes of machine processing we find it
simpler to work solely with the normative global lattice.) The lattice
is defined via a set of &lt;state/&gt; elements, and via source/target
attributes on edges referencing ids of &lt;state/&gt; elements. (NOTE:
The MAF draft defines a separate &lt;transition/&gt; element, having a
source and a target attribute, for the purpose of defining edges.)

Sample edge elements:

      <token id='t2' from='4' to='7' value='dog' source='s1' target='s2'/>
    
     <wordForm id='w2' daughters='t1' source='s1' target='s2'>
      <fs>
       <f name='stem'>dog</f>
      <fs>
     <wordForm/>

The full lattice is encapsulated in an &lt;fsm/&gt; element. E.g.

      <fsm init='v0' final='v3'>
       <state id='v0'/>
       <state id='v1'/>
       <state id='v2'/>
       <state id='v3'/>
    ...

... PAGE UNDER CONSTRUCTION ...
<update date omitted for speed>{% endraw %}