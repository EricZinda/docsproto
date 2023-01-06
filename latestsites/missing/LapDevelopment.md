{% raw %}# Background

These pages are intended for LAP-internal use, to aid communication
among developers. As such, they complement the LAP [email
list](https://sympa.uio.no/ifi.uio.no/info/lap-developers), [ticket
system](https://rt.uio.no), and [SVN
repository](http://svn.emmtee.net/lap). At least initially, only
registered members of the [LapGroup](https://blog.inductorsoftware.com/docsproto/missing/LapGroup) can edit this page (and
sub-pages, as long as we make sure to assign access rights correctly).
However, as these pages can be viewed by the public (including
unregistered wiki users), sensitive or private information (e.g.
passwords) should not be posted here.

# General Principles

All components beyond the basic operating system that determine LAP
functionality (and configuration) should be version-controlled in
UiO-hosted repositories, accessible to the LAP development team. In
practice, we currently have all tools, the API library, tool
descriptions, and the full Galaxy instance under SVN control (using the
LAP repository). Some additional configuration files (e.g. for the
front-end web server, authentication, and communication with the GOLD
accounting database) and scripts remain to be integrated with LAP
version control (as of May 2015).

Whereever possible, LAP services run as non-privileged users, typically
laportal.

Physical host and path names shall not be exposed to users; for example,
all references to public LAP instances should be by way of symbolic
(alias) names, e.g. lap.clarino.uio.no (production) and lap.hpc.uio.no
(development), including in URLs and such that are part of LAP-related
metadata or documentation.

Files that are only required on the LAP front-end node should be
organized on its local disks (typically below /home/laportal/), rather
than in the cluster-wide shared LAP directory (/projects/lap/).

The shared LAP directory makes a top-level directory distinction between
the development, test (currently dormant), and production instances;
please avoid putting data into the /projects/lap/ top level.

All LAP services and interfaces are fully Unicode-enabled; data is
always serialized in UTF-8 encoding.

Anonymous commits to SVN (or other activity that could not be traced to
one individual) should be avoided. For example, the laportal user
receives updates from SVN, but actual changes should only be checked in
from real developer accounts (and then pulled by laportal).

Invasive changes to third-party modules (e.g. Galaxy, GOLD, SLRUM) are
minimized and localized to the largest extent possible. Non-trivial
pieces of USIT- or LAP-specific code are kept in separate files and
versioned indepently.

All relevant steps in ‘building’ tools for the LAP Tree, configuration
of the Galaxy instance, changes to the external web server, or
non-vanilla updates to the front-end system configuration should be
recorded (either on separate wiki pages, see below, or in installation
log files).

All parts of the LAP infrastructure must be designed for concurrent (or
‘thread-safe’) execution, i.e. protect access to shared resources
through locking or other synchronization means and ensure that temporary
file names or identifiers are unique across processes and users.

References to (natural) languages always use three-letter [ISO
639.2](http://www.loc.gov/standards/iso639-2/php/code_list.php) codes,
e.g. ENG or NOB for English and Norwegian *Bokmål*, respectively.

LAP documentation standardizes on American English, avoidance of
contractions, and Oxford commas.

# See Also

Following is a list of LAP wiki pages that are more or less actively
maitained, i.e. expected to provide up-to-date information (there are
more pages in the LapDevelopment sub-hierarchy, many of which are only
of internal or historic significance):

- [LapDevelopment/Accounting](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Accounting)
- [LapDevelopment/Annotations](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Annotations)
- [LapDevelopment/Deployment](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Deployment)
- [LapDevelopment/Environment](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Environment)
- [LapDevelopment/MongoDB](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_MongoDB)
- [LapDevelopment/ToE](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_ToE)
- [LapDevelopment/Tree](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Tree)

# LAP Hardware

As of mid-2015, LAP operates two dedicated front-end servers, one for
the *development* instance (ps.hpc, aka lap.hpc.uio.no), another one for
the (forthcoming) *production* instance (at.hpc, aka
lap.clarino.uio.no). The development server is hosted on a gracefully
aging PowerEdge R710 (donated by LTG) with 2 x 6C @ 2.66 ghz, 144 gbytes
of RAM, and 500 gbytes in SSD; the production server is a project-funded
R730 with 2 x 10C @ 2.3 ghz, 192 gbytes of RAM, and 3.2 tbytes in SDD.

# LAP Ingredients

Following is an attempt at breaking down LAP into major component
pieces. More in-depth discussion of individual pieces should be
delegated to sub-pages, for example the
[LapDevelopment/Tree](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Tree),
[LapDevelopment/MongoDB](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_MongoDB),
LapDevelopment/Abel,
[LapDevelopment/Annotations](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Annotations),
[LapDevelopment/Giellatekno](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Giellatekno), or
[LapDevelopment/Tests](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Tests) pages.

## LAP Tree

LAP provides (language) processing services, e.g. segmenting a document
into sentences and tokens, tagging parts of speech, and syntactic
dependency parsing. We will refer to individual processing steps (e.g.
sentence segmentation) as *tools*, and to a (posibly singleton)
configuration of tools (e.g. the above pipeline) as a *workflow*. All
tools available through LAP are maintained in a version-controlled
repository, dubbed the *LAP Tree*. Tools in the LAP Tree are
ready-to-run binaries for a reasonably recent 64-bit (x86) Linux
environment; external dependencies beyond basic operating-system
components and a small set of standard shared libraries are wrapped with
each tool, to make it possible to run tools from the LAP Tree without
system administrator support. To allow installation of tools from the
LAP Tree into an arbitrary location, there *cannot* be any configuration
in terms of absolute path names; instead, where necessary, tools can
refer to relative locations below the root of the LAP Tree, which is
recorded in an environment variable $LAPTREE (for more background, see
[LapDevelopment/Environment](https://blog.inductorsoftware.com/docsproto/missing/LapDevelopment_Environment)).

Our design goal is to eventually allow users to request arbitrary
versions of tools (or arbitrary combinations of tool versions) from the
LAP tree, i.e. we anticipate that tool configuration in Galaxy will
comprise version information, and that a custom copy of the LAP Tree can
be created on demand (and transparently ‘behind the scenes’) for
individual Galaxy users (and, in principle, individual workflows).
Initially, however, experimentation is exclusively focused on the *head*
revision of the LAP Tree *trunk* (no pun intended), which resides in a
directory shared with the ABEL cluster nodes
(/projects/lap/development/trunk/tree/).

When creating temporary files (as can be necessary in wrapping tools
that cannot be beaten into cooperation otherwise), it is important to
consider parallelism, i.e. use adequate means to make sure that parallel
processes can never operate on the same file names; also, all temporary
files should be created relative to the environment variable $LAPTMP.

## LAP Store

Tools in LAP typically receive some input to be processed and upon
completion provide some result data, for example further analysis or
annotation of the input. All input and output data to LAP tools is
represented using the data model of the Linguistic Annotation Framework
(LAF). LAF annotation records (in LAP) are typically serialized in JSON
format and stored in a NoSQL [MongoDB
database](https://www.mongodb.org/). This LAP-internal repository of
annotation records is dubbed *LAP Store*.

The MongoDB server is installed on the LAP front-end node (ps.hpc),
using the standard RHEL6 version of MongoDB (2.4.6); the database is
configured (in /etc/mongodb.conf) to allow incoming connections on the
loopback and ABEL-internal network interfaces; authentication is
required to read or write the database. The physical database storage is
in /var/lib/mongodb/, which is a separate partition on the SSD Raid
(currently configured with only 100 gbyte space, but there is remaining
air space in the underlying logical volume).

The standard database for LAP Store is called lapstore (i.e. by default,
all tools share one database), which is writable by user lapstore.

## LAP Library

For integration with LAP, tools must be ‘wrapped’ so as to (a)
communicate (read and write annotations) with the LAP Store and (b)
register with and execute under Galaxy control. Seeing that Galaxy
proper is implemented in Python, these wrappers will often be
implemented in Python too (though a Java API, for example, might well be
considered in the future). To avoid duplication of LAP-specific wrapper
functionality, there is an emerging layer of ‘glue’ code, dubbed the
*LAP Library*. Because tool execution on ABEL utilizes library
functionality to communicate with LAP Store, the default copy of the LAP
Library is checked out from SVN into /projects/lap/library/trunk/.

The Python code is documented using docstrings, formatted along the
lines suggested at
<http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html>.

## Galaxy Instance

The LAP heart, in a sense, is an instance of the [Galaxy
Framework](http://galaxyproject.org/), a software platform for
data-intensive processing originally developed for applications in
bio-informatics. Galaxy internally can be sub-divided into various
components. The LAP Galaxy instance resides in /home/laportal/galaxy/
(on the front-end node, e.g. ps.hpc for development). Following are
brief characteristics of some noteworthy ones:

- *Galaxy System User*: Galaxy runs as a non-priviliged user laportal
(uid=226904) with Unix group laportal (gid=160632).
- *Galaxy SQL Database*: For internal storage, Galaxy uses a PostGres
database hpc\_lap hosted on dbpg-it-forskning.uio.no.
- *Galaxy Data Directory*: Besides the database (which is primarily
used for metadata), Galaxy stores actual data files in the
filesystem; LAP has a designated project area /projects/lap/, which
is NFS-mounted on the LAP front-end node (ps.hpc) and all cluster
nodes; the so-called ‘database’ directory of the Galaxy instance is
configured to /projects/lap/development/data/galaxy/.
- *Galaxy Web Server*: Galaxy operates its own internal web server on
port 8080, but for better scalability and authentication support, we
wrap it behind an [Apache HTTP Server](http://httpd.apache.org/)
proxy (see below).
- *Galaxy Tool Descriptions*: In addition to global Galaxy
configuration, each tool needs to be registered with Galaxy through
a tool description, an XML file registered with the list of
available tools; LAP tool descriptions are separated from the Galaxy
instance and reside in /projects/lap/tools/trunk/.
- *Galaxy Job Submission*:
- *Galaxy Accounting*:

## Accounting Database

## (External) Web Server
<update date omitted for speed>{% endraw %}