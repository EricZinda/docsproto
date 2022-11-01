{% raw %}# Heart of Gold

<http://heartofgold.dfki.de> is the current 'official' website where you
can find [documentation](http://heartofgold.dfki.de/Documentation.html),
[downloads](http://heartofgold.dfki.de/Download.html) and
[papers](http://heartofgold.dfki.de/Publications.html). There is some
additional documentation about installation and troubleshooting at
[HogInstallation](HogInstallation).

The [Heart of Gold](http://heartofgold.dfki.de) is a middleware
architecture for the integration of deep and shallow natural language
processing components. It provides a uniform and flexible infrastructure
for building applications that use Robust Minimal Recursion Semantics
([RMRS](../RmrsTop)) and/or general XML standoff annotation produced by
natural language processing components. The framework uses
[XSLT](http://www.w3.org/TR/xslt) as integration language for querying
and combining XML standoff markup.

The main purpose Heart of Gold was developed for is integration of
various shallow natural language processors with the highly efficient
[HPSG](http://hpsg.stanford.edu) parser [PET](https://blog.inductorsoftware.com/docsproto/garage/PetTop) in order to
increase robustness of HPSG grammars for various languages such as
[English](http://www.delph-in.net/erg),
[German](http://www.dfki.de/~crysmann/gg/),
[Japanese](http://www.delph-in.net/jacy),
[Greek](http://www.delph-in.net/mgrg) and
[Norwegian](https://blog.inductorsoftware.com/docsproto/grammars/NorsourceSummary). HPSG
grammars can be developed with the [LKB](../LkbTop), compiled to a binary
grammar image, and at runtime executed by PET within the Heart of Gold.

Although the focus of Heart of Gold is deep-shallow integration, the
framework itself is generic and hence could also be used to, e.g.,
combine multiple purely shallow systems on XML basis, or to integrate
other deep parsers.

The Heart of Gold has been developed under the wings of the EU-funded
project [DeepThought](http://www.project-deepthought.net/) and the
BMBF-funded project [QUETAL](http://quetal.dfki.de) and in the context
of the DELPH-IN collaboration. The main developer of Heart of Gold is
[UlrichSchaefer](../UlrichSchaefer).

The core middleware (and also the PET system) is available under an LGPL
open source license. However, some of the components for which we
provide adapters are only available for research purposes or have their
own licenses different from LGPL.

There is also a [mailing
list](http://lists.delph-in.net/mailman/listinfo/hog) for discussions
and announcements concerning Heart of Gold.

Last updated: EricZinda - Tue Oct 25 13:59:11 2022 -0700
{% endraw %}