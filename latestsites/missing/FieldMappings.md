{% raw %}## HOW TO create initial .dfn file

Modify the example file in lkb/lexdb/example.dfn to fit your needs.

## UNDERSTANDING the DEFN table

Lexical entries in the database are stored as a collection of field
values. These field values must be mapped to AVMs before use in a
processing environment. We achieve this by providing a mapping from
fields to TDL structure, allowing the existing machinery (which works on
the TDL notation) to take over.

For example, we map the following entry from the database

               NAME: bombard_v1                                         
               TYPE: v_np_trans_le                                      
        ORTHOGRAPHY: bombard                                            
             KEYREL: "_bombard_v_rel"                                   
             KEYTAG:                                                    
             ALTKEY:                                                    
          ALTKEYTAG:                                                    
            ALT2KEY:                                                    
            COMPKEY:                                                    
           OCOMPKEY:                                                    
             SOURCE: LinGO                                              
               LANG: EN                                                 
            COUNTRY: UK                                                 
            DIALECT:                                                    
            DOMAINS:                                                    
             GENRES:                                                    
           REGISTER:                                                    
         CONFIDENCE: 1                                                  
           COMMENTS:                                                    
          EXEMPLARS:                                                    
              FLAGS: 1                                                  
            VERSION: 0
             USERID: bmw20
           MODSTAMP: 2004-06-11 00:00:00+01

to the following TDL entry

    bombard_v1 := v_np_trans_le &
     [ STEM < "bombard" >,
       SYNSEM.LKEYS.KEYREL.PRED "_bombard_v_rel" ].

by means of the following field mappings:

     mode | slot  |    field    |              path              |    type
    ------+-------+-------------+--------------------------------+-------------
     erg  | id    | name        |                                | sym
     erg  | orth  | orthography |                                | str-rawlst
     erg  | unifs | alt2key     | (synsem lkeys alt2keyrel pred) | mixed
     erg  | unifs | altkey      | (synsem lkeys altkeyrel pred)  | mixed
     erg  | unifs | altkeytag   | (synsem lkeys altkeyrel carg)  | str
     erg  | unifs | compkey     | (synsem lkeys --compkey)       | sym
     erg  | unifs | keyrel      | (synsem lkeys keyrel pred)     | mixed
     erg  | unifs | keytag      | (synsem lkeys keyrel carg)     | str
     erg  | unifs | ocompkey    | (synsem lkeys --ocompkey)      | sym
     erg  | unifs | orthography | (stem)                         | str-lst
     erg  | unifs | type        | nil                            | sym

The mode should be set to the name of the lexical database in use. slot
takes values id, orth, and unifs (these relate to internal LKB
structures). The id and orth lines above should not be changed. Each
unifs line define a mapping to a certain TDL substructure. These
mappings are determined by the remaining fields: field specifies the
database field involved in the mapping; path defines the TDL path set by
the mapping; type determines the mapping from database field value to
TDL substructure.

Possible values of type:

- sym, symbol: eg. sym 'value' -&gt; VALUE
- str, string: eg. str '"value"' -&gt; "value"
- mixed: eg. mixed '"value"' -&gt; "value"; mixed 'value' -&gt; VALUE
- str-rawlst, string-list: str-rawlst 'one two' -&gt; ("one" "two")
- str-lst, string-fs:

<!-- -->


          str-lst 'one two' ->
    
    [ FIRST "one",
      REST.FIRST "two",
      REST.REST *NULL* ]

- for which the TDL shorthand is &lt; "one", "two" &gt;

<!-- -->


- str-dlst, string-diff-fs:

<!-- -->


          str-dlst 'one two' ->
    [ LIST.FIRST "one",
      LIST.REST.FIRST "two",
      LIST.REST.REST #1,
      LAST #1 ]

- for which the TDL shorthand is &lt;! "one", "two" !&gt;

<!-- -->


- lst, mixed-fs:

<!-- -->


          (lst NODE1 NODE2) 'one * "two"' ->
    
    [ FIRST.NODE1.NODE2 ONE,
      REST.FIRST.NODE1.NODE2 *TOP*,
      REST.REST.FIRST.NODE1.NODE2 "two",
      REST.REST.REST *NULL* ]

- for which the TDL shorthand is
&lt; \[NODE1.NODE2 ONE\], \[\], \[NODE1.NODE2 "two"\] &gt;

<!-- -->


- dlst, mixed-diff-fs:

<!-- -->


          (lst NODE1 NODE2) 'one * "two"' ->
    
    [ LIST.FIRST.NODE1.NODE2 ONE,
      LIST.REST.FIRST.NODE1.NODE2 *TOP*,
      LIST.REST.REST.FIRST.NODE1.NODE2 "two",
      LIST.REST.REST.REST #1,
      LAST #1 ]

- for which the TDL shorthand is
&lt;! \[NODE1.NODE2 ONE\], \[NODE1.NODE2 TWO\] !&gt;

<!-- -->


- lst-t: as lst, but format is (lst-t TOP-MARKER PATH) where
(lst-t '\* PATH) is equivalent to (lst PATH)
- dlst-t: as dlst, but format is (dlst-t TOP-MARKER PATH) where
(dlst-t '\* PATH) is equivalent to (dlst PATH)
<update date omitted for speed>{% endraw %}