{% raw %}# Background

This page documents a sub-task of the HPC adaptation project at UiO;
please see the TitanTop page for background.

[PET](http://www.delph-in.net/pet) (Platform for Efficient HPSG
Processing Techniques) is the egine used commonly for batch parsing with
DELPH-IN grammars: given a sequence of natural language utterances
(typically sentences), it performs an n-best search for syntactic and
semantic analyses according to the constraints provided by the grammar.
PET is implemented in C<sup>++</sup> (with core routines in pure C) and
was originally developed in the mid-1990s.

At the time, PET was relatively carefully optimized, down to levels of
memory locality, register utilization, alignment, and instruction
pipelining (all targeting \`large-memory' [UltraSparc](/UltraSparc)
hardware of those days). The software has seen substantial enhancements
in functionality in recent years, but for almost ten years it has not
been carefully profiled and optimized for maximum effiency on modern
hardware. At the same time, DELPH-IN grammars have grown substantially
in recent years, and the technology is now more standardly applied to
relatively large amounts of unrestricted, running text.

This sub-project will apply various application-level and in-kernel
profiling tools to analyze and improve resource utilization in PET, both
at per-process level and at a per-node level. From cursory,
non-systematic observations made so far, for example, it appears that
saturation of the memory sub-system can be a limiting factor to
utilizing all cores of a standard TITAN node jointly.

# Running PET

The LOGON tree includes pre-compiled PET binaries and a pre-processed
input file to PET: uio/titan/cb.yy. This is a short text, comprising
rather difficult language, an [open source advocacy
essay](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/).
To parse this input, by-passing [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) and everything else, run the
following:

      cheap -t -yy -packing -cm -default-les=all -nsolutions=500 \
        -memlimit=1024 -timeout=60 $LOGONROOT/lingo/erg/english.grm \
        < $LOGONROOT/uio/titan/cb.yy

Note that there are multiple PET binaries packaged with the LOGON tree,
corresponding to the SVN *trunk* vs. the *cm* (chart mapping) branch.
$LOGONROOT/bin/cheap is a wrapper script that sets up the process
environment and invokes the appropriate binary. The command-line option
-t in the example above selects the *cm* version of PET; when running
the actual binary directly (e.g. using a binary compiled locally; see
below), this extra option must be omitted.

Besides profiling a single parsing process, it may also be worthwhile
simultaenously putting eight of these jobs on a standard TITAN node, to
see whether there are scalability issues.

# Practical Tasks

VD staff should obtain a PET installation from source. For use at UiO,
we depend on the so-called *chart mapping* branch of PET, which is
available via SVN:

      svn co https://pet.opendfki.de/repos/pet/branches/cm pet

Some instructions on compilation are available in the README file that
comes with the source tree, as well as on the DELPH-IN
PetDependencies page. To get started, it should be
sufficient to use Boost and ICU but ignore the various XML input modes
(and XML-RPC support), [\[incr tsdb()\]](http://www.delph-in.net/itsdb),
and ECL.
<update date omitted for speed>{% endraw %}