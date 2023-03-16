{% raw %}# Background

This page documents a sub-task of the HPC adaptation project at UiO;
please see the [TitanTop](https://blog.inductorsoftware.com/docsproto/missing/TitanTop) page for background.

In order to eliminate the current biggest bottleneck in the DELPH-IN
toolchain, turn-around times in machine learning experiments need to be
reduced substantially. The Toolkit for Advanced Discriminative Modeling
([TADM](http://tadm.sf.net)) is the main machine learning component used
in DELPH-IN research to date. TADM estimates the parameters of so-called
discriminative, log-linear (or exponential) statistical models, where
the result of this process can subsequently serve to probabilistically
rank competing hypotheses, say directing the parser towards the most
probable analysis.

TADM is implemented in C++, built on top of the
[PETSc](http://www.mcs.anl.gov/petsc/petsc-2/) and
[TAO](http://www.mcs.anl.gov/research/projects/tao/) libraries, and was
originally developed by [Rob Malouf](http://www-rohan.sdsu.edu/~malouf/)
(then at the University of Groningen, The Netherlands). A group of
active TADM users, collaborating with Rob, hosted the project at
SourceForge around 2004 and consolidated existing patches (including
some from UiO). Otherwise, there has been no active TADM development in
recent years, and available documentation is sparse.

TADM is applied to training data (typically in the form of millions or
billions of integer-coded 'features') prepared using the [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) software (see the
[TitanItsdb](https://blog.inductorsoftware.com/docsproto/missing/TitanItsdb) page), and a single estimation run can take
several cpu hours. In searching for best-performing model parameters,
dozens or hundreds of distinct configurations need to be tested,
typically each by means of ten-fold cross validation. Hence, in current
development, TADM throughput is the primary bottleneck.

Reportedly, a parallel version of TADM was available locally at
Groningen in the late 1990s (customized for MPICH and Myrinet), and the
project will resurrect (and adapt as needed, for use on TITAN) MPI
support in TADM. Also, it will be necessary to profile some of the core
routines and experiment with different versions of low-level libraries
(notably BLAS and LAPACK) and use of the Intel compiler suite (rather
than the vanilla GNU Compiler Collection), to further improve the cpu
utilization of TADM.

This work package will be predominantly implemented by VD staff,
(re-)enabling the incomplete and currently dormant MPI support in the
TADM code base. Once the software modifications are complete, a joint
series of experiments of increasing complexity will serve to determine
the scalability of the TADM core (numeric optimization, processing huge
sparse matrices). The extended TADM software will be integrated with the
LOGON tree and contributed to the TADM project repository at
SourceForge.

# Running TADM

The LOGON tree includes pre-compiled TADM binaries, plus a
(comparatively small) sample input file. To invoke the parameter
estimation procedure, assuming a functional LOGON installation, the
following should work:

      cd $LOGONROOT/uio/titan
      tadm -monitor -events_in small.events.gz -params_out /dev/null

Running this small sample file, at present, takes on the order of ten
minutes wall clock time. Even though I do not understand TADM internals
very well (let alone PETSc or TAO), it is assumed that parameter
estimation lends itself well to parallelization.

# Practical Tasks

For adaptation at UiO, we have created a TADM branch in the local SVN
repository. Once you are set up for DELPH-IN SVN access (see the
[TitanTop](https://blog.inductorsoftware.com/docsproto/missing/TitanTop) page and email by Stephan of June 16, 2009), obtain
a TADM source tree as follows

      svn co http://logon.emmtee.net/tadm/trunk tadm

To compile, you will need (at least) copies of PETSc and TAO (in the
right versions) installed. Please see the general TADM [installation
instructions](http://tadm.sourceforge.net/install.txt) for details.

Starting in September 2009, VD staff should install TADM and inspect the
source code; according to the TADM SourceForge pages, there is at least
partial MPI support. A short-term goal should be parallelizing parameter
estimation using the small sample file. It may also be relevant to look
into performance effects of using gcc(1) vs. the Intel compiler suite,
or various implementations of auxiliary libraries, notably BLAS and
LAPACK.

Once we have an MPI-enabled version of TADM, we should jointly look at
integration with the [\[incr tsdb()\]](http://www.delph-in.net/itsdb)
experimentation environment, i.e. find out how to best make use of
parallel parameter estimation where each TADM job is part of a larger
sequence of experiments, controlled from [\[incr
tsdb()\]](http://www.delph-in.net/itsdb).

Last update: 2013-09-24 by GlennSlayden [[edit](https://github.com/delph-in/docs/wiki/TitanTadm/_edit)]{% endraw %}