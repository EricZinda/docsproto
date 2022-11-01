{% raw %}# Documentation for the Grammar Matrix Customization Import Toolbox Lexicon Library

# Introduction

This page of the Grammar Matrix customization questionnaire allows users
to upload a lexicon in SIL's
[Toolbox](http://www.sil.org/computing/toolbox/index.htm) format, and
define a mapping from Toolbox fields to Grammar Matrix lexical types.

# Sample input

### Choices:

```
section=toolbox-import
  toolboximportconfig1_idtag=\id
  toolboximportconfig1_glosstag=\ge
  toolboximportconfig1_stemtag=\lex
  toolboximportconfig1_tbpredvalues=gloss
    toolboximportconfig1_importclass1_importlextype=n1
      toolboximportconfig1_importclass1_toolboxtag1_tbtag=\psrev
      toolboximportconfig1_importclass1_toolboxtag1_tbvalue=n
    toolboximportconfig1_importclass2_importlextype=iv
      toolboximportconfig1_importclass2_toolboxtag1_tbtag=\psrev
      toolboximportconfig1_importclass2_toolboxtag1_tbvalue=v
      toolboximportconfig1_importclass2_toolboxtag2_tbtag=\val
      toolboximportconfig1_importclass2_toolboxtag2_tbvalue=S-ABS V-S
```

### Toolbox file:

```
\id 1
\lex nounlexeme1
\ge noungloss1
\psrev n
```

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}