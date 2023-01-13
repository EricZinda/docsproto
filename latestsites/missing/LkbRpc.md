{% raw %}# Background

As of late 2010, the LKB sports an XML-RPC interface to select
system-internal functionality (an API of sorts). Initially, this add-on
module is only available in the so-called LOGON tree (see the
[LogonTop](https://blog.inductorsoftware.com/docsproto/tools/LogonTop) page for background) and limited to quite a small
number of functions, viz. those needed to enable an on-going PhD project
on incremental parsing.

# Server Initialization

Before going into server mode, the LKB and [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) code needs to be loaded, as
well as the grammar to be used (e.g. the ERG). Assuming a functional and
complete LOGON system, the following will start the XML-RPC server on
port 4013:

      (lkb::rpc-initialize :port 4013)

A convenient short-hand to do all of the above from the command line is
available in the LOGON tree, e.g.

      $LOGONROOT/lingo/lkb/server --tty --erg --rpc 4013

Note that this script will also initialize a generation server, which
requires compiling a set of indices for the grammar the first time it is
invoked; this process can take several minutes to complete.

The LKB XML-RPC server will bind to the custom port specified when
initializing the server (4013 in the above examples) and does not use a
server-specific prefix in request URLs. Hence, assuming the above
example, XML-RPC requests should be directed to http://localhost:4013/
(or maybe the actual machine name, rather than using localhost).

# Interface Functions

Following is a semi-formal summary of the available interface. In terms
of XML-RPC data types, *integer* in the following corresponds to
&lt;I4&gt; and *string* to &lt;STRING&gt;.

Many of the interface functions either create or operate on so-called
*chart edges*, essentially a representation of a tree fragment, where
the daughters (if any), in turn, are represented as edges.

- **chart.create** → integer This function creates a new chart object,
which can subsequently serve as the (per-client) storage for chart
edges. Return values greater than zero indicate success (and
constitute valid chart handles for subsequent calls).
- **grammar.instantiate-lexical-entry** ( integer *chart*, string
*surface*, string *entity* ) → integer
  
  Instantiates the lexical entry named *entity*, specializing its
orthography to *surface*, and stores a new edge in *chart*. An edge
handle (greater than zero) is returned on success; the function will
fail in case *entity* does not name valid lexical entry in the
grammar, which case a negative value is returned.
- **grammar.instantiate-rule** ( integer *chart*, string *entity* ) →
integer
  
  Instantiates the grammar rule named *entity* and stores a new edge
in *chart*. An edge handle (greater than zero) is returned on
success; the function will fail in case *entity* does not name a
valid grammar rule, in which case a negative value is returned.
- **chart.combine** ( integer *chart*, integer *mother*, integer
*child*, integer *index* ) → integer
  
  Combines chart edges *mother* and *child*, by unifying the feature
structure of *child* into the argument position of *mother*
indicated by *index* (where argument positions are zero-based); when
successful, stores a new edge in *chart*. A zero return value
indicates unification failure.
- **chart.root** ( integer *chart*, integer *edge*, string *entity* )
→ integer
  
  Tests the feature structure of *edge* against the start symbol
*entity*, i.e. attempts to unify the two structures; a zero return
value indicates failure, negative return values an invalid call, and
a non-zero positive value success.
- **chart.release** ( integer *chart* ) → integer
  
  Release the storage associated to *chart*, including all edges
recorded there. Upon successful completion (indicated by a zero
return value), *chart* is no longer a valid handle, nor are any edge
handles contained in chart.

In addition to the above methods, which are appropriate to (re-)build
HPSG derivations, the following is a convenience method that can be used
for custom setups:

- **grammar.instantiate-type** ( integer *chart*, string *entity* ) →
integer
  
  Instantiates the type named *entity* and stores a new edge in
*chart*. An edge handle (greater than zero) is returned on success;
the function will fail in case *entity* does not name a valid type,
in which case a negative value is returned.

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/LkbRpc/_edit)]{% endraw %}