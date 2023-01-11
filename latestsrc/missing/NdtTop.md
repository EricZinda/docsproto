{% raw %}# Background

Internal (for the time being at least) notes on working with the
Norwegian Dependency Treebank at LTG.

# Initial Set-Up

      svn co http://svn.emmtee.net/ltg/ndt

The source code of the Regular Expression–Based Pre-Processor (REPP) and
the toolkit for Robust Evaluation of Syntactic Analysis (RESA) is
included as an external SVN dependency. As a first-time, preparatory
step, both tools needs to be compiled. In tokenization/src/repp/ and
tokenization/src/resa/, run:

      autoreconf -i
      ./configure
      make

# Segmentation and Tokenization

      cat ../data/txt/nob/ap001.txt \
      | ./src/sentence-split_no.perl \
      | while read line; do \
          echo "$line" | ./src/repp/src/repp -c repp/nob.set --format line; \
        done \
      > ap001.t

RESA compares two views on syntactic analysis—gold and test, in our
case–and and aligns sentence end points and tokens to the original raw
text (thus recovering character start and end points); ‘-b’ requests the
use of sentence end boundaries (rather than spans); ‘-v’ means to output
any mismatched triples; and ‘--interim’ will create additional files (in
the current directory, but named after the gold and test inputs)
containing all triples. Finally, the file descriptor magic serves to
swap standard output and standard output, such that we can filter for
sentence and token errors and record mismatches in yet another file.

      ./src/resa/src/resa \
        -r ../data/txt/nob/ap001.txt \
        -g ../data/conll/nob/ap001.conll -G CONLLX \
        -t ap001.t -T TAB \
        -b -v --interim 3>&1 1>&2 2>&3 3>&- | egrep 'SENT|TOK' > ap001.e

# Random Notes

For comparison to the CIS tokenizer:

      cat ../data/txt/nob/ap001.txt \
      | ~/src/logon/cis/bin/linux.x86.32/tokenizer -L german-utf8 -S -p -P -E '' \
      | while read line; do \
          echo "$line" | ./src/repp/src/repp -c repp/nob.set --format line; \
        done \
      > ap001.t

Last update: 2015-06-26 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/NdtTop/_edit)]{% endraw %}