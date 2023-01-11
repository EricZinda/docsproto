{% raw %}# Instructions

Supertagging in this manner requires chartmapping.

## Extracting supertags for training (and train TnT)

I have code that will extract lexical types (and optionally inflectional
rules) from a derivation tree in a profile, and align these tags with
the external tokens (ie post-REPP). This depends on having a
grammar/profile with the p-input relation containing the input tokens,
and the token feature structures in the derivation tree. This code
requires a grammar file and a profile, and produces output that can be
used to train TnT (although other output formats are possible).

Download the extraction code:

    svn co http://svn.delph-in.net/mu/preprocess/STAG/branches/input/ 

Compile it:

    autoreconf -i 
    ./configure 
    make 

Run:

    ./tagextract [-i] $LOGONROOT/lingo/erg/english.tdl $LOGONROOT/lingo/erg/tsdb/gold/wescience > wescience.tags

Train:

    $LOGONROOT/coli/bin/linux.x86.32/tnt-para -o ws_model wescience.tags

## Changing the grammar

There are three types of changes need to be made to the grammar to use
supertags for restriction:

### Settings

To use the inbuilt tagging capabilities of PET (which will be rolled
into trunk once there has been wider testing, and agreement from
grammarians to release the grammars with the appropriate settings file),
certain settings need to be set in the pet dir of the grammar:

*taggers*: most important, lists the taggers in order they are to be
run. The actual string used to indicate individual taggers is not
important, as long as the relevant settings (below) are prefixed with
the same string.

- &lt;prefix&gt;*-command*: REQ, command line for tagger
- &lt;prefix&gt;*-tok\_sep*: REQ, string that separates tokens
- &lt;prefix&gt;*-utt\_sep*: REQ, string that separates items
- &lt;prefix&gt;*-tag\_format*: REQ, specifies the output of the
tagger, one of:
  
  - "single" - one tag per token, format: word tag
  - "multi" - multiple tags per token, format: word (tag prob)+
  - "genia" - genia output, format: word lemma POS chunk NE
- &lt;prefix&gt;*-arguments*: OPT, command line arguments for tagger
- &lt;prefix&gt;*-mapping*: OPT, words that should be mapped before
input to tagger
- &lt;prefix&gt;*-utterance-start*: OPT, token that should be given to
tagger before each item (for taggers that assume continuous input)
- &lt;prefix&gt;*-utterance-end*: OPT, token that should be given to
tagger after each item (for taggers that assume continuous input)
- &lt;prefix&gt;*-pos\_sep*: OPT, string to separate token and POS in
tagger input. Non-empty pos\_sep indicates that the tagger expects
token and POS as input.
- &lt;prefix&gt;*-namedentities*: OPT, controls whether named entities
are added as extra tokens. Ignored if tag\_format != "genia".

### TDL type changes

An STAG feature and stag type needs to be added to the grammar. If the
supertags are to include inflectional rules, there also needs to to be a
feature to pass around a lexical rule list to be discharged. The
supertagger-types.tdl file available at:
<http://svn.delph-in.net/mu/preprocess/STAG/branches/input/stag_utils/supertagger-types.tdl>
makes the edits to the current ERG (via type addendum where
appropriate).

In order to have the supertags restrict the parser, the types and/or
rules that could be filtered need to be altered. The mechanism for
lexical type and lexical rule filtering are quite different and require
different editing:

#### lexical types

Filtering happens when the token feature structure is unified with the
lexical entry. This happens by adding a constraint to the lexical type
(via type addendum), eg:

    aj_-_i-an-nmd_le :+ [ TOKENS.+LIST < [ +STAG.+STAGS < "aj_-_i-an-nmd_le", ... > ],... > ].

The constraint could be the full lexical type or, for example, a
substring of such. These addenda can be automatically generated from the
lexicon. (A script is available at
<http://svn.delph-in.net/mu/preprocess/STAG/branches/input/stag_utils/lexicon2supertags.pl>.)
For lexical types that should never be removed from the parse chart, the
constraint can simply not be added.

#### lexical rules

Filtering happens here by the discharging of a list of rules created
during token mapping from the supertag. Since the lexical rules
(currently) are only distinguished to the necessary level at the
instance level, not in separate types, the type addendum concept cannot
be used. Hence, the lexical rules need to be directly extended.

A example of a rule that is restricted by requiring that the first
element of the DTR's LRS equal to the rule name is shown:

    n_pl_olr :=
    %suffix (!s !ss) (!ss !ssses) (es eses) (ss sses) (!ty !ties) (ch ches) (sh shes) (x xes) (z zes)
    lex_rule_infl_affixed &
    [ ND-AFF +,
      DTR.LRS < "n_pl_olr" . #lrs >,
      LRS #lrs,
      SYNSEM mass_or_count_synsem &
             [ LOCAL plur_noun ],
      RNAME "LNPL" ].

Unlike for the lexical types, if a specific rule is not to be
restricted, but other rules are, the unrestricted rule must still be
extended to pass the DTR's LRS up:

    n_pl_olr :=
    %suffix (!s !ss) (!ss !ssses) (es eses) (ss sses) (!ty !ties) (ch ches) (sh shes) (x xes) (z zes)
    lex_rule_infl_affixed &
    [ ND-AFF +,
      DTR.LRS #lrs,
      LRS #lrs,
      SYNSEM mass_or_count_synsem &
             [ LOCAL plur_noun ],
      RNAME "LNPL" ].

### Token mapping rules

The current method of getting the supertags into the (pre-)parsing
process is to use the same mechanism as is currently used for POS tags,
and to process the tag lists in token mapping. This requires extra rules
in tmr/pos.tdl to separate the tags into POS or supertag depending on a
prefix which was added as the tags were received from the tagger. If the
supertag contains lexical rules, they need to be separated from the
lexical type at this point. A sample pos.tdl that has the extra (and
altered) rules for the current ERG trunk can be found at
<http://svn.delph-in.net/mu/preprocess/STAG/branches/input/stag_utils/pos.tdl>

## Running the parser

Currently, a branch of PET has the ability to tag with both POS tags and
supertags built in. To use, check out and compile the code:

    svn co https://pet.opendfki.de/repos/pet/branches/tagger
    
    autoreconf -i
    ./configure --with-tsdb=$LOGONROOT/lingo/lkb
    make

Run cheap with a -tagger option that selects the settings file (above)
with the right set of taggers.

Last update: 2012-07-04 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/WeSearch_SuperTagging_Setup/_edit)]{% endraw %}