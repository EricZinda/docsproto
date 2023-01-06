{% raw %}# House Cleaning

- add Language Identification and expose NNO in OBT (and maybe other
languages in GT)
- OBT debugging
- activate custom data types \[all\]
- make ‘Help’ menu entries point to LAP documentation \[milen\]
- ‘Workflow Instructions’ give NELS error
- activate nativeSpecification and per-tool job resource defaults
(more memory and cores for B&N)
- where are the job resources when running a workflow?
- expose nynorsk in OBT
- TSV export fails when requesting non-existing annotations
- do a little more testing
- move production instance into trial mode
- update user documentation: in-galaxy bug report, emphasize valid
input formats, don't look at receipts
- standardize option names (e.g. ‘--sentence’, ‘--token’, and such;
following annotation types); provide sensible defaults in all tools
- review and harmonize ‘==process’ (and tool) naming in GT and OBT
stacks;
- review annotation structures and ‘finalize’ (for now)
- harmonize tokenization styles (Unicode) and tagging and parsing
models

# History and LAP Store Cleaning

# Authentication

- simplesaml metadata (for Feide)
- edugain: [CoCo](/CoCo)
- CLARIN SPF

milen & nikolay on the technical side; oe (with input from francesca)
driving the legal side

for the time being, standardize on mail attribute, since Galaxy requires
user ids to be valid email addresses.

once we have the production service working, look into more
sophisticated IdP discovery, e.g. discojuice or discopower.

# Certification

- enroll in Type A Service trial

# Visualization

- in-browser rendering of tagged and parsed text, using brat
- use of metadata, e.g. language, specific types of annotations (e.g.
PoS set)

# DELPH-IN Integration

# Collaboration with DSS

# Tool Integration

- constituent structure parsing
- semantic dependency parsing
- language identification
- lemmatization
- classification

# Data Import, Collections, and Parallelization

- protect against import of obviously illformed data (?)
- import archive (of document collection)
- ‘chunking’: break up processing (e.g. set of sentences) internally
and paralleize
- tool to iterate through the datasets in a collection and parallelize
- import structured data, e.g. sentence-segmented, tokenized, tagged,
or class label–bearing

# Explicit Modeling of Annotation and Tool Ontology

- data types and metadata

# Clean Re-Installation Procedure

# Interoperability with Other CLARINO Centers

# LAP Library in Java

# Get a Life after ABEL
<update date omitted for speed>{% endraw %}