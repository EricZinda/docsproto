{% raw %}Jacy uses the light weight version of the lexical database ([Single
User]() mode). (2006-09-06: incomplete initial
documentation --- details may change)

Contents

1. Database Fields
   1. TDL Fields
   2. All Fields
2. Lexicon Interaction with CVS
3. Set Up
4. ToDo
5. Priveleges

# Database Fields

## TDL Fields

Defined in japanese/lex/lexdb.dfn.

    id      name            sym
    orth    orthography             str-rawlst
    unifs   orthography     (orth)  str-dlst
    unifs   type    nil     sym
    unifs   keyrel  (synsem lkeys keyrel pred)      mixed
    unifs   keytag  (synsem lkeys keyrel carg)      mixed
    unifs   altkey  (synsem lkeys altkeyrel pred)   mixed
    unifs   alt2key (synsem lkeys alt2keyrel pred)  mixed
    unifs   altkeytag       (synsem lkeys altkeyrel carg)   mixed
    unifs   compkey (synsem local cat head ptype)   mixed
    unifs   idiom   (idiom) mixed

## All Fields

Defined in japanese/lex/su-init.sql

|               |                            |                                |             |
|---------------|----------------------------|--------------------------------|-------------|
| **field**     | **SQL type**               | **Comment**                    | **Example** |
| name          | TEXT NOT NULL              | TDL lexical-id (unique)        |             |
| userid        | TEXT DEFAULT user NOT NULL | Maintainer ID                  |             |
| modstamp      | TIMESTAMP                  | Time of last change            |             |
| type          | TEXT                       | TDL lexical type               |             |
| orthography   | TEXT                       | TDL Orthography                |             |
| keyrel        | TEXT                       | TDL Key (Predicate)            |             |
| keytag        | TEXT                       | TDL CARG                       |             |
| altkey        | TEXT                       | TDL ALT Key                    |             |
| alt2key       | TEXT                       | TDL ALT2 Key                   |             |
| altkeytag     | TEXT                       | TDL ALT CARG                   |             |
| compkey       | TEXT                       | TDL ptype                      |             |
| idiom         | TEXT                       | TDL Idiom Feature              |             |
| pronunciation | TEXT                       | Pronunciation                  |             |
| comments      | TEXT                       | Any comments                   |             |
| lang          | TEXT                       | Ja                             |             |
| country       | TEXT                       | JP                             |             |
| dialect       | TEXT                       | --                             |             |
| confidence    | real DEFAULT 1             | Reduce for autoamtic additions |             |
| source        | TEXT,                      | Which lexicon it came from     |             |

# Lexicon Interaction with CVS

- Before updating the lexicon file lex/Jacy.rev
- \* do your normal checks
- \*\* (lkb::batch-check-lexicon)
- \*\* dump to tdl and flop
- \* optionally back up your existing lexicon
- \* dump the lexical database
  
       psql jacy
       jacy=# \copy lex to japanese/lex/Jacy.rev 
- Merge using normal CVS update
- \* Check things again
- \*\* load the revisions, reindex, run the grammar etc
- \*\* dump the tdl
- Update the Jacy.rev and tdl lexicon

# Set Up

Set up the database as described in the [Single
User]() page, then load the lexicon from CVS.

- Connect to the database (normally called jacy)
  
       psql jacy 
- Create the Databases
  
       jacy=# \i japanese/lex/su-init.sql 
  
  - Load the definitions
  
  <!-- -->

  
       jacy=# \copy dfn from  japanese/lex/lexdb.dfn 
  
  - Load the lexical entries
  
  <!-- -->

  
       jacy=# \\copy lex from japanese/lex/Jacy.rev 
- Load Jacy and set up the **\*lexdb-params\*** through the LKB
Options::Set Options... menu
  
       ((:DBNAME "jacy") (:TYPE :SINGLE-USER)) 
- Index for parsing and generation
  
       (lkb::new-lex-key-table lkb::*lexicon*)
       (lkb::new-semi lkb::*lexicon*)

# ToDo

- currently we can't delete entries, so we mark anything we want to
delete with the string *delete* in the comment field.

# Priveleges

How to allow multiple people to access the same DB:

    jacy=#  GRANT ALL  ON  lex_key to bond;
    GRANT
    jacy=#  GRANT ALL  ON  semi_extra to bond;
    GRANT
    jacy=#  GRANT ALL  ON  semi_frame to bond;
    GRANT
    jacy=#  GRANT ALL  ON  semi_mod to bond;
    GRANT
    jacy=#  GRANT ALL  ON  semi_obj to bond;
    GRANT
    jacy=#  GRANT ALL  ON  semi_var to bond;
    GRANT
    jacy=# \dp
                             Access privileges for database "jacy"
     Schema |    Name    | Type  |                    Access privileges                     
    --------+------------+-------+----------------------------------------------------------
     public | dfn        | table | {bond=arwdxt/bond,kuribayashi=arwdxt/bond}
     public | lex        | table | {bond=arwdxt/bond,kuribayashi=arwdxt/bond}
     public | lex_key    | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_extra | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_frame | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_mod   | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_obj   | view  | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_pred  | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
     public | semi_var   | table | {kuribayashi=arwdxt/kuribayashi,bond=arwdxt/kuribayashi}
    (9 rows)
<update date omitted for speed>{% endraw %}