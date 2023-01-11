{% raw %}# Background

In July 2009, at the time of the annual DELPH-IN Summit (see the
BarcelonaTop page for background), a new tagged release
of the LOGON infrastructure (see the LogonTop page for
details) becomes available. This page documents (some of) the updates
and extensions provided in this snapshot.

# New Modules

Cheetah (coli/cheetah/) is a new grammar of German, essentially adapting
the approach of Miyao et al. (in the Tokyo EnJu system) to the DELPH-IN
formalism and TiGer Treebank. Bart Cramer is the principal developer of
Cheetah.

HAG (crysmann/hag/) is a (nascent version of a) grammar of Hausa.
Berthold Crysmann is the principal developer of HAG.

KRG is now included with the LOGON tree (see the Section *SVN Specifics*
below for details, as we are starting to experiment with SVN *externals*
definition, rather than including a separate copy of KRG in the LOGON
SVN repository).

The Lexical Type Database (LTDB) is now distributed with the
LKB sources, which in turn is part of the LOGON tree.

# Updates

# Add-On Components

# SVN Specifics

# Tested (Looking Good)

# Remaining Tests

      $LOGONROOT/parse --binary --erg+tnt --count 6 --best 500 cb
    
      $LOGONROOT/parse --binary --wiki --count 6 --best 1 ws01
<update date omitted for speed>{% endraw %}