{% raw %}You can run the Zhong grammar using ACE (see AceTop and
AceUse).

# Versions

You can compile three different versions of Simpplified Mandarin
Chinese, depending on your purpose of using the grammar.

The ordinary one can be compiled using the following command under
zhong/cmn/zhs. This version is the default for parsing.

    $ ace -g ace/config.tdl -G zhs.dat

The version for robust parsing can be compiled using the following. This
version includes the bridging rules. Note that this version requires a
large size of memory and much running time (see
AceOptions).

    $ ace -g ace/config-robust.tdl -G zhs-robust.dat

Recall "Parsing Robustly, Generatring Strictly!" For strict generation,
you can use the following to compile the version (see
ZhongGeneration).

    $ ace -g ace/config-strict.tdl -G zhs-strict.dat

# Modes

When parsing setencens, You can invoke YZLUI for using the graphical
user interface (see LkbLui). The LUI (Linguistic User
Interface) can be invoked by using an option -l.

    $ ace -g zhs.dat -l

You can use the YY mode for your input of parsing. See
ZhongYYMode.
<update date omitted for speed>{% endraw %}