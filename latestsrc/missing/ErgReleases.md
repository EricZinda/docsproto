{% raw %}# Background

This page (a work in progress, like so many others on this wiki)
collects some practical and historic information around official
snapshots of the ERG, e.g. officially released versions of the grammar.

# (Pre-)Release MRS Quality Control

Once new treebanked and thinned profiles are available, run a set of
automated wellformedness tests on the MRSs, for example:

      $LOGONROOT/redwoods --terg --default \
        --filter syntax,lnk,fragmentation erg/trunk/mrs/12-02-06/pet.1

# Optimize the Set of Quick-Check Paths

     cheap -limit=100000 -repp -cm -packing \
       -qc-unif=0 -compute-qc-unif=pet/qc.tdl english.grm < lkb/checkpaths.items 

# Re-Generate the Core SEM-I

The bulk of the semantic interface (SEM-I) is auto-generated from the
lexicon (recorded as ‘core.smi’):

      (in-package :mt)
      (setf semi
        (construct-semi       
         :ids t :rules t :descendp t :embedp t
         :semi (read-semi
                "~/src/logon/lingo/erg/etc/erg.smi"
                :includep nil :finalizep nil :recordp nil)
         :patches "~/src/logon/lingo/erg/etc/patches.lisp"
         :finalizep t))
      (print-semi
       semi :stream "~/src/logon/lingo/erg/etc/hierarchy.smi"
       :format :hierarchy)
      (print-semi
       semi :stream "~/src/logon/lingo/erg/etc/abstract.smi"
       :format :compact :filter "^[^_]")
      (print-semi
       semi :stream "~/src/logon/lingo/erg/etc/surface.smi"
       :format :compact :filter "^_")

The master file ‘erg.smi’ is manually maintained and includes the
auto-generated entries; the separate ‘patches.lisp’ will hopefully
become unnecessary after the 1214 release.

# Validate the Predicates Used in Transfer Rules

Transfer rules operate on MRSs, hence should be compatible with the
specifications of the Semantic Interface (SEM-I):

    (loop
          for mtrs in *transfer-rule-sets*
          do
            (format t "~%~a:~%" (mtrs-id mtrs))
            (loop
                for mtr in (mtrs-mtrs mtrs)
                for eps
                = (append
                   (test-semi-compliance (mtr-filter mtr))
                   (test-semi-compliance (mtr-context mtr))
                   (test-semi-compliance (mtr-input mtr))
                   (test-semi-compliance (mtr-output mtr)))
                for preds
                = (loop
                      for ep in eps
                      for pred = (mrs:rel-pred ep)
                      when (and pred
                                (or (stringp pred) (symbolp pred))
                                (not (equal pred "never_unify")))
                      collect pred)
                when preds
                do
                  (format t "  ~a: ~{~s~^ ~}~%" (mtr-id mtr) preds)))

# Validate and Update the (DT) Head Table

To identify new rules (or ones deleted from the grammar), the following
will compare the head table on file (by default ‘etc/rules.hds’) to the
grammar inventory of constructions:

      (in-package :tsdb)
      (read-heads "~/src/logon/lingo/terg/etc/rules.hds" :test (list #'lkb::dt-test))

# Validate the Mapping from Generic to Native Lexical Entries

The definitions of lexical types for generic lexical entries should be
annotated with ‘equivalences’ in terms of native lexical entries and
(optionally) lexical rules, e.g.

      ;; <type val="v_np*_pr-3s-unk_le">
      ...
      ;; <native> v_3s-fin_olr v_np*_le
      ;; </type>

These pseudo-XML comments (as originally introduced for the lexical type
database) are interpreted at grammar load time and can be serialized
into summary form (say for comparison to lexical entries defined in
‘gle.tdl’) as follows:

      (loop
          for context in *tdl-all-contexts*
          for type = (rest (assoc :type context))
          for native = (rest (assoc :native context))
          when (and type native)
          collect (cons type native) into result
          finally
            (loop
                for (type . native) in (sort result #'string< :key #'first)
                do (format t "~a: ~a~%" type native)))

In addition to the above, we should also confirm that there are ‘native’
correspondences declared for all types instantiated by generic lexical
entries (with possible exceptions, e.g. the generic type for ‘year of
century’ named entities, for which there is no native equivalent):

      (with-open-file (stream "~/src/logon/lingo/terg/gle.tdl")
        (loop
            for line = (read-line stream nil nil)
            for i from 1
            while line do
              (multiple-value-bind (start end starts ends)
                  (ppcre:scan ".+:=[ \\t]*([^ \\t]+)" line)
                (when (and starts ends)
                  (let* ((type (subseq line (aref starts 0) (aref ends 0)))
                         (match
                          (find type *tdl-all-contexts*
                           :key #'(lambda (foo) (rest (assoc :type foo)))
                           :test #'string=))
                         (native (rest (assoc :native match))))
                    (when (or (null native) (string= native ""))
                      (format
                       t "missing native declaration for `~(~a~)' (line ~d)~%"
                       type i)))))))

# Re-Generate CTYPE Hierarchy and Abstractions

For the various distinct configurations, maintaining the inventory of
construction types requires some manual resoluton; to generate a point
of reference (for the current grammar, e.g. including the speech
extensions):

      (generate-ctypes :file "/tmp/ctype.tdl")

# Generate Maximum Entropy (and Optionally PCFG) Models

Parse ranking models included with the grammar are trained on the
standard training *plus* development splits, for example Sections 01 to
12 for WeScience. By default, the Maximum Entropy training
scripts (re-)generate a fresh feature cache, hence the following two
jobs must *not* run in parallel

      sbatch ${LOGONROOT}/uio/titan/redwoods \
        --redwoods --run train.wescience.lisp
    
      sbatch ${LOGONROOT}/uio/titan/redwoods \
        --redwoods --run train.redwoods.lisp

Unlike in the 1111 release, no PCFG model (for chart pruning in PET) is
included with the 1212 release and onwards.

# Update Summary Statistics of Redwoods Treebanks

Since its October 2010 release, the ERG includes a spreadsheet that
summarizes key statistics of the gold-standard profiles that comprise
the Redwoods Treebank. The raw data for addition to the file
‘etc/redwoods.xls’ can be generated automagically:

      (in-package :tsdb)
      (loop
          with *phenomena* = nil
          with *statistics-aggregate-dimension* = :phenomena
          with *statistics-all-rejections-p* = t
          with *tsdb-home* = (logon-directory "lingo/terg/tsdb/gold" :string)
          initially (purge-profile-cache :all)
          for db in (find-tsdb-directories)
          for name = (get-field :database db)
          do (analyze-trees name :append "/tmp/redwoods.csv" :format :csv))

# Populate the Linguistic Type Database

Instructions on invoking the relevant script to populate the type
database can be found at LkbLtdb.

# Create tar(1) Ball for Download

In addition to being able to directly obtain tagged releases from the
DELPH-IN SVN repository, there is a collection of compressed archives,
one for each release, for direct download available at
<http://www.delph-in.net/ftp/erg/> (hosted on the main DELPH-IN server
in Oslo, though one could easily re-direct this to the LinGO server). A
soft link current.tgz in the download directory is what selects which
version will be accessed by the *Download* button on the [main ERG
page](http://www.delph-in.net/erg).
<update date omitted for speed>{% endraw %}