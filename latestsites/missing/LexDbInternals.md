{% raw %}# WARNING: THIS PAGE MAY BE OUT-OF-DATE

The LexDB uses a PostgreSQL database to provide a source of lexical
items for client applications such as the LKB. This page provides some
minimal documentation on the structure of the database.

# The ''fld'' table

The *fld* table stores user-defined the field definitions used in
constructing the *rev* table below. The contents are set by the script
install-lexdb. Field definitions cannot be altered once the LexDB has
been created.

# The ''rev'' table

The *rev* table stores revisions of lexical items. It has the following
structure. The first 4 fields, which hard-coded, have the following
definitions:

        Column | Type | Modifiers
    ---------------+--------------------------+-----------
     name | text |
     userid | text |
     modstamp | timestamp with time zone |
     dead | boolean |

Following these are the user-defined fields specific to a particular
LexDB. These are obtained from the .fld file provided to the script
install-lexdb (and stored in the *public.fld* table of the LexDB for
later reference). The following are the user-defined fields used by the
ERG LexDB:

     type | text |
     orthography | text |
     keyrel | text |
     altkey | text |
     alt2key | text |
     keytag | text |
     altkeytag | text |
     compkey | text |
     ocompkey | text |
     pronunciation | text |
     complete | text |
     semclasses | text |
     preferences | text |
     classifier | text |
     selectrest | text |
     jlink | text |
     comments | text |
     exemplars | text |
     usages | text |
     lang | text |
     country | text |
     dialect | text |
     domains | text |
     genres | text |
     register | text |
     confidence | real |
     source | text |

The fields (name,userid,modstamp) provide the primary key. The field
dead marks dead revisions.

# The ''dfn'' table

The *dfn* table stores the mapping used to construct FS lexical entries
from fields of a revision entry. See
[LexDbFieldMappings](https://blog.inductorsoftware.com/docsproto/tools/LexDbFieldMappings).

     Column | Type | Modifiers
    --------+------+-----------
     mode | text | not null
     slot | text | not null
     field | text | not null
     path | text |
     type | text |

# The ''meta'' table

This table stored miscellaneos configuration settings and other data.

A sample *public.meta* is shown below:

              var | val
    -----------------------+-------------------------------
     lexdb-version | 4.80
     supported-psql-server | 7.4
     supported-psql-server | 8.0
     supported-psql-server | 8.1
     user | foo
     user | bar
     mod_time | 2005-11-16 19:12:16.798424+00

A sample private *meta* is shown below:

        var | val
    ------------+-------------------------------
     filter | true
     build_time | 2005-11-16 19:12:32.446169+00
     mod_time | 2005-11-16 19:11:18.955607+00

- user is set for each user for whom a private schema has been
initialized;
- filter is an SQL WHERE-clause which determines which revision
entries are accessible to a user (*lex* view);
- mod-time stores the time at which data in the schema was last
modified;
- build\_time stores the time at which the (private schema) *lex* view
was last "rebuilt".

# Public and private schemas

The PostgreSQL database is created and owner by the database user lexdb.
This user is the owner of the schema public. In order to make use of the
LexDB a client must connect as a separate user. The first time a user
connects their private database schema will be initialized.

A private schema contains a private versions of the *rev* and *meta*
tables. When lexical items are modified by the user (or new items
created) changes are stored in the private schema and, when ready, these
new revision entries are then transferred to the public schema (this
requires a lexdb login authorization).

A private schema also contains *lex\_cache* and *lex\_key* tables, and a
*lex* view with the same structure as the *rev* table. The *lex* view
contains full details of all entries directly accessible for lexical
lookup (that is, for each named entry, the most recent revision to pass
the filter). The *lex\_cache* and *lex\_key* tables contain cached
details of these entries in order to allow efficient lookup.

# The ''lex\_cache'' table

       Column | Type | Modifiers
    -------------+--------------------------+-----------
     name | text |
     userid | text |
     modstamp | timestamp with time zone |
     orthography | text |

# The ''lex\_key'' table

This table provides keys for the lookup of lexical items by component
words. Eg. a revision with orthography 'a few' will be keyed on both 'a'
and 'few'. Keys are in normalized (lower case) form as provided by the
client application. (We do not use the PostgreSQL lower() function as it
may differ to the equivalent function used in the client application.)

      Column | Type | Modifiers
    ----------+--------------------------+-------------------------------------------------------------
     name | text | not null
     userid | text | not null default "current_user"()
     modstamp | timestamp with time zone | not null default ('now'::text)::timestamp(6) with time zone
     key | text | not null

# The ''lex'' view

Eg.

        Column | Type | Modifiers
    ---------------+--------------------------+-----------
     name | text |
     userid | text |
     modstamp | timestamp with time zone |
     dead | boolean |
     type | text |
     orthography | text |
     keyrel | text |
     altkey | text |
     alt2key | text |
     keytag | text |
     altkeytag | text |
     compkey | text |
     ocompkey | text |
     pronunciation | text |
     complete | text |
     semclasses | text |
     preferences | text |
     classifier | text |
     selectrest | text |
     jlink | text |
     comments | text |
     exemplars | text |
     usages | text |
     lang | text |
     country | text |
     dialect | text |
     domains | text |
     genres | text |
     register | text |
     confidence | real |
     source | text |
    View definition:
     SELECT rev_all.*
       FROM lex_cache
       JOIN rev_all USING (name, userid, modstamp);
<update date omitted for speed>{% endraw %}