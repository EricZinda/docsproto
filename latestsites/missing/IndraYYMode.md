{% raw %}# Required Components

In order to run INDRA with the YY-mode inputs, you have to install and
set up the Indonesian POS Tagger. See
[IndraPreprocessing](https://blog.inductorsoftware.com/docsproto/garage/IndraPreprocessing).

Note that your ACE version must be at least
[0.9.19patch1](http://sweaglesw.org/linguistics/ace/download/ace-0.9.19patch1-x86-64.tar.gz)
(release 02 Jan 2015) or later, or you may get segfaults with ACE's
YY-mode.

## Setting Up

1\. Describe gle.tdl for Indonesian from Indonesian POS Tagger

For example, the tag VB is mapped to opt-tr-verb-lex in INDRA.

    generic_vv := opt-tr-verb-lex &
     [ SYNSEM.LKEYS.KEYREL.PRED #pred,
       STEM < "_generic_verb_" >,
       TOKENS.+LIST generic_token_list & 
                                < [ +POS.+TAGS < "VB" >,
                                    +PRED #pred ] > ].

2\. Edit indonesian-pet.tdl based on zhs-pet.tdl in Zhong

3\. Copy tmr folder from Zhong

4\. Edit yy.sh in \~/ind/utils

5\. Edit .bashrc

    $ gedit ~/.bashrc

add

    export INDONESIAN_TAGGER_PATH=PATH_TO_INDONESIAN_POS_TAGGER/tools/indonesian-postagger

6\. Edit NER.pl in \~/tools/indonesian-postagger

7\. Edit 1-1Tagging.pl in \~/tools/indonesian-postagger

8\. Edit tag.sh in \~/tools/indonesian-postagger

9\. Create ind2yy.py

10\. Edit Indonesian lexicon.tdl

Add TRAITS native\_token\_list to each lexical item

Before:

    makan := opt-tr-verb-lex &
      [ STEM < "makan" >,
        SYNSEM.LKEYS.KEYREL.PRED "_makan_v_rel" ].

After:

    makan := opt-tr-verb-lex &
      [ STEM < "makan" >,
        SYNSEM.LKEYS.KEYREL.PRED "_makan_v_rel",
        TRAITS native_token_list ].

# Parsing in YY mode

If you would like to parse sentences, you can use the following command.
Before that, you have to compile the data file (ind.dat). Note that you
have to add the -y option.

    $ ./utils/yy.sh PATH_OF_SENTENCES | ace -g ind.dat -y

You can input the sentence directly. For example, "David makan es krim"
is parsed as follows.

    ~/ind/utils$ echo "David makan es krim" | ./yy.sh | ace -g ../ind.dat -yTf
    SKIP: (yy mode)
    SKIP: (yy mode)
    SENT: (yy mode) 
    [ LTOP: h0 
    INDEX: e2 [ e SF: prop-or-ques TENSE: tense ASPECT: aspect MOOD: mood ] 
    RELS: < [ named_rel<0:5> LBL: h4 CARG: "David" ARG0: x3 [ x SPECI: bool COG-ST: cog-st PNG.PERNUM: pernum ] ]  
    [ "proper_q_rel"<-1:-1> LBL: h6 ARG0: x3 RSTR: h7 BODY: h8 ]  
    [ "_makan_v_rel"<5:5> LBL: h1 ARG0: e2 ARG1: x3 ARG2: x9 
    [ x SPECI: bool COG-ST: cog-st PNG.PERNUM: pernum ] ]  
    [ "_es krim_u_unknown:NN_rel"<10:7> LBL: h10 ARG0: x9 ]  
    [ exist_q_rel<-1:-1> LBL: h11 ARG0: x9 RSTR: h12 BODY: h13 ] > 
    HCONS: < h0 qeq h1 h7 qeq h4 h12 qeq h10 > 
    ICONS: < > ] 
    NOTE: 1 readings, added 99 / 52 edges to chart (14 fully instantiated, 20 actives used, 11 passives used)       RAM: 553k
    NOTE: parsed 3 / 3 sentences, avg 184k, time 0.00562s
<update date omitted for speed>{% endraw %}