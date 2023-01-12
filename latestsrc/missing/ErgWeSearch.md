{% raw %}# Background

Necessary steps to go from an ERG release (including treebanks) to an
instance of the WSI on-line search interface.

# WSI Software

To obtain, the WSI software, follow the instructions for "Obtaining the
application code" on WeSearch/Interface.

# Export

First, you will need an installation of the LOGON tree. See
[LogonInstallation](https://blog.inductorsoftware.com/docsproto/tools/LogonInstallation).

After you have obtained LOGON, add the parse results you wish to export:

      cd $LOGONROOT/terg
      svn switch --ignore-ancestry http://svn.emmtee.net/erg/tags/2018 .
      flop english

To run the export, return the to root of the WSI application code and
use the export script, after making a directory to receive them:

      mkdir ~/redwoods
      ./export.sh

This script assumes that you want the exported results in \~/redwoods
and that the parse profiles are located at
$LOGONROOT/lingo/lkb/src/tsdb/home/gold/terg. This will be the case if
the ERG SVN tree switched to above has a tsdb/gold directory. You may
need to edit the script if this is not the case, replacing gold with the
correct term. You will also want to edit the script if the directory you
created for the export results is not \~/redwoods. If there are a large
number of parse results to export, this may take some time to complete.

# Index Creation

Before beginning index creation, you must obtain Apache Jena. This
simply requires downloading and extracting it into the top of the WSI
application code directory:

      wget https://archive.apache.org/dist/jena/binaries/apache-jena-2.11.0.tar.gz
      tar zpSxvf apache-jena-2.11.0.tar.gz

Next, you must create a destination directory for the index. This will
become the value of DATA\_PATH mentioned in
[WeSearch/Interface](http://moin.delph-in.net/WeSearch/Interface) under
"Configuration". For example, if the indexes will live at
/ltg/ls/aserve/indices and the name of the index is to be redwoods, the
you would do the following:

      mkdir -p /ltg/ls/aserve/indices/redwoods

Then, for each representation you plan to index, create subdirectories:

      mkdir /ltg/ls/aserve/indices/redwoods/mrs
      mkdir /ltg/ls/aserve/indices/redwoods/eds

Before you can index the exports, you must unzip them:

      gunzip ~/redwoods

Finally, index the exports:

      ./create-index -f mrs -o /ltg/ls/aserve/indices/redwoods/mrs ~/redwoods
      ./create-index -f eds -o /ltg/ls/aserve/indices/redwoods/eds ~/redwoods

# Deployment

To use the new index in [WeSearch](https://blog.inductorsoftware.com/docsproto/garage/WeSearch), follow the steps for
configuration of the web application interface
([WeSearch/Interface](http://moin.delph-in.net/WeSearch/Interface)).

# Loose Ends

- quality-control export (including DM creation) for 2019
- in-line DM in export files and update index creation accordingly
- update MRS visualization to
- end-to-end ICONS support: code import from LKB-FOS, EDS and DM, RDF
and WQL extensions, visualization

Last update: 2020-08-14 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/ErgWeSearch/_edit)]{% endraw %}