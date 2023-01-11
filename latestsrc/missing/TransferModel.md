{% raw %}# Objective

This page shows how a trigram model for transfer ranking can be built.
The first part shows how profiles with MRSs can be built and how MRS
triples can be exported. It overlaps with [DelphinTools](https://blog.inductorsoftware.com/docsproto/garage/DelphinTools)
and [RedwoodsTop](https://blog.inductorsoftware.com/docsproto/garage/RedwoodsTop). The second part shows
ErikVelldal's procedure for creating an MRS trigram
model.

Contents

1. [Objective](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
2. [Preliminaries](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
3. [Exporting MRS triples from
Logon](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   1. [Creating the profiles](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   2. [Exporting triples from the
profiles](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
4. [Creating the transfer model](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   1. [Remove formatting](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   2. [Produce context cues](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   3. [Extract the vocabulary](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
   4. [Train the model](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)
5. [Loading the transfer model](https://blog.inductorsoftware.com/docsproto/missing/TransferModel)

# Preliminaries

The procedure requires three tools:

- The CMU Toolkit (<http://mi.eng.cam.ac.uk/~prc14/toolkit.html>),
- SMT [QuickRun](/QuickRun)
(<http://ufal.ms.mff.cuni.cz/~curin/SMT_QuickRun/>), and
- [DelphinTools](https://blog.inductorsoftware.com/docsproto/garage/DelphinTools).

The installation of the CMU Toolkit may conflict with Logon, so you may
need to comment out the Logon settings in the .bashrc file temporarily
while the installation is going on.

# Exporting MRS triples from Logon

First, set a variable and a path:

    TSDBHOME=$LOGONROOT/lingo/lkb/src/tsdb/home
    export PATH=$LOGONROOT/lingo/lkb/src/tsdb/home:$PATH

## Creating the profiles

This step is needed if you do not have a profile. It shows how you can
get a profile from the object sentences of a bilingual corpus file. (See
also [DelphinTools](https://blog.inductorsoftware.com/docsproto/garage/DelphinTools).) Note that there are various other
ways to do this. The first command below creates a new version of the
bilingual corpus, where the object language comes first. The second
command parses the sentences in the object language and stores the MRSs
(of the five top ranked parses) in 'bitxt.'

    logon_do --bitext PATH/TO/BILINGUAL/CORPUS/FILE $TSDBHOME/bitxt
    logon_do --count 5 --limit 5 --grammar jaen --task omrs $TSDBHOME/bitxt

## Exporting triples from the profiles

This command extracts triples from the top ranked MRSs of the profile
created above. (See [RedwoodsTop](https://blog.inductorsoftware.com/docsproto/garage/RedwoodsTop).)

    $TSDBHOME/export --binary  --condition "result-id=0" --format triples bitxt/omrs

# Creating the transfer model

This is ErikVelldal's procedure for creating a transfer
model, and his comments are given below. (I
(PetterHaugereid) have added a couple of paths.)

## Remove formatting

First we remove all formatting inserted by the export code (to get only
the tuples) and cat everything to a single file. Note that, in the pipe
below, the script from the SMT\_[QuickRun](/QuickRun) package only
inserts the "context cues" used by the CMU SLM toolkit, ie. the sentence
boundaries &lt;s&gt; and &lt;/s&gt;. (Note also that the path to the
extracted triples '$LOGONROOT/tmp/bitxt.omrs/' may differ if you did not
follow the procedure above.)

    export PATH=/PATH/TO/SMT_QUICKRUN/bin:$PATH
    find $LOGONROOT/tmp/bitxt.omrs/ -name *.gz | xargs zcat | awk '!/(^[\;\{\}\[]|^[[:space:]]*$)/' | add_sent_marks.prl | gzip > /tmp/mrstuples.gz

## Produce context cues

Produce a file holding the context cues, to be referenced by the CMU
toolkit.

    export PATH=/PATH/TO/CMU_TOOLKIT/bin:$PATH
    echo "<s>" > ccs; echo "</s>" >> ccs

## Extract the vocabulary

    zcat /tmp/mrstuples.gz | text2wfreq > mrs.wfreq; cat mrs.wfreq | wfreq2vocab -top 65535 > mrs.vocab

## Train the model

    zcat /tmp/mrstuples.gz | text2idngram -temp /tmp/ -n 3 -vocab mrs.vocab > mrs.idngram; idngram2lm -idngram mrs.idngram -n 3 -vocab mrs.vocab -binary mrs.binlm -calc_mem -context ccs -witten_bell

The MRS trigram model is written into the file 'mrs.binlm.'

# Loading the transfer model

The transfer model is loaded in an MT system's lkb/mt.lsp.

For example, if the transfer model is in the same directory:

    (setf *transfer-tm*
     (namestring (make-pathname
                  :directory (this-directory)
                  :name "mrs.binlm")))
<update date omitted for speed>{% endraw %}