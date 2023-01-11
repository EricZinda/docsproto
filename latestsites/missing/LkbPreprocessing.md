{% raw %}# XML-Based Interface to (External) Preprocessors

As part of the EU-funded
[Deep-Thought](http://www.project-deepthought.net) project, the LKB was
interfaced to an external finite-state preprocessor, morphological
analyzer, and tagger using an XML-based interface. This interface could
serve to harmonize existing connections to external preprocessors (e.g.
to [ChaSen](http://chasen.aist-nara.ac.jp) in the Japanese grammar) over
time, and probably should be used as the role model for future
integrations.

The *Simple PreProcessor Protocol* is documented on the
LkbSppp page.

The MAF-based XML annotation scheme is documented on the
LkbMaf page.

# (Internal) Finite-State Preprocessing

To use the built-in finite-state preprocessor please a line such as the
following in your grammar's script file:

      (read-preprocessor (lkb-pathname (parent-directory) "preprocessor.fsr"))

Once a preprocessor has been loaded, preprocess-sentence-string will
automatically send input to the correct finite-state preprocessor. If no
preprocessor has been loaded, you get the LKB's default built-in
preprocessor (this throws away punctuation, modulo \*bracketing-p\*. and
creates a sequence of tokens by splitting on space characters).

# Characterization

Characterization support allows the deep processor to relate components
of the linguistic analysis to the input text. To enable simple
(character-point based) characterization support, set the following in
your grammar's globals.lsp:

(setf \*characterize-p\* t)

You must also ensure that CFROM/CTO features (of type lkb::\*toptype\*)
are provided in the (R)MRS semantics component of your grammar. Eg.
\[from the ERG\]

      relation := relation_min &
      [ PRED predsort,
        LBL handle,
        WLINK *list*,
        CFROM *top*,
        CTO *top* ].

These features are used to store and propogate pointers during
linguistic processing. You can see these features in the semantic
analysis:

    The dog barks. 
    <rmrs cfrom='-1' cto='-1'>
    <label vid='1'/>
    <ep cfrom='0' cto='14'><gpred>prpstn_m_rel</gpred><label vid='1'/><var sort='e' vid='2' tense='present'/></ep>
    <ep cfrom='0' cto='3'><realpred lemma='the' pos='q'/><label vid='6'/><var sort='x' vid='9' pers='3' num='sg'/></ep>
    <ep cfrom='4' cto='7'><realpred lemma='dog' pos='n' sense='1'/><label vid='10'/><var sort='x' vid='9' pers='3' num='sg'/></ep>
    <ep cfrom='8' cto='14'><realpred lemma='bark' pos='v' sense='1'/><label vid='11'/><var sort='e' vid='2' tense='present'/></ep>
    <rarg><rargname>MARG</rargname><label vid='1'/><var sort='h' vid='4'/></rarg>
    <rarg><rargname>RSTR</rargname><label vid='6'/><var sort='h' vid='8'/></rarg>
    <rarg><rargname>BODY</rargname><label vid='6'/><var sort='h' vid='7'/></rarg>
    <rarg><rargname>ARG1</rargname><label vid='11'/><var sort='x' vid='9' pers='3' num='sg'/></rarg>
    <hcons hreln='qeq'><hi><var sort='h' vid='4'/></hi><lo><label vid='11'/></lo></hcons>
    <hcons hreln='qeq'><hi><var sort='h' vid='8'/></hi><lo><label vid='10'/></lo></hcons>
    </rmrs>

For more sophisticated characterization support see LkbMaf.
<update date omitted for speed>{% endraw %}