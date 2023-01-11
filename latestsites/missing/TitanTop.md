{% raw %}# Background

The [Language Technology
Group](http://www.mn.uio.no/ifi/english/research/groups/ltg/) (LTG) at
the University of Oslo (UiO) is about to start a joint preparatory
project with the UiO [Research Computing Services
group](http://hpc.uio.no) (VD), aiming to scale up
[DELPH-IN](http://www.delph-in.net) technology for efficient use on
high-performance computing (HPC) resources. Please see the full [grant
application](http://www.delph-in.net/titan/notur.mar-09.pdf), if you
require more detailed background information. A more high-level overview
of DELPH-IN-related language technology research at UiO is available as
[slides copies](http://www.emmtee.net/oe/talks/notur.5-jun-08.pdf) from
a presentation held at the 2008 [annual NOTUR
meeting](http://www.notur.no/notur2008/). In 2008 and 2009, the project
is funded by the Norwegian Metacenter for Computational Science
([NOTUR](http://www.notur.no/)).

This page, at least initially (June 2009), mostly serves
project-internal purposes. It is intended to provide the necessary
background information on DELPH-IN software and typical use patterns for
VD staff, on the one hand, and to document emerging recipes for using
DELPH-IN tools on the UiO [TITAN](http://hpc.uio.no/index.php/Titan)
facilities, on the other hand.

The page was created and is maintained by StephanOepen.
Please be conservative in making (non-trivial) changes, i.e. please make
sure you are reasonably sure of the information you post here.

# Communication

There is an archived [mailing
list](http://lists.delph-in.net/mailman/listinfo/titan) for this
project: titan@delph-in.net. All project members should be subscribed
already, but please feel free to contact StephanOepen in
case you feel you should be added to the list. Ideally, all email
relevant to the project should be sent to the mailing list.

# Resource Allocations

The project was granted a resource alloation of 10,000 cpu hours on
TITAN for the allocation period 2009.1 (April 1 through September 30,
2009). This allocation is available as account number nn9106k, which
should be used in all [SLURM](https://computing.llnl.gov/linux/slurm/)
(the queueing system on TITAN) commands. To gain access to these cpu
allocations, user accounts need to be registered with the project;
please contact StephanOepen for details.

# Basic Software Installation

The project will use the so-called LOGON tree for its experimentation,
essentially an integrated, ready-to-run distribution of core DELPH-IN
components. Please see the LogonTop and
LogonInstallation pages for basic instructions on
obtaining a complete installation, but please read the following
paragraphs first.

Because the project will depend on a few add-on components in the LOGON
tree, notably the full [Allegro Common
Lisp](http://franz.com/support/documentation/8.1/doc/contents.htm)
environment, all project members will require a personal DELPH-IN SVN
user account, and always use the authenticated SVN access method
(through http://logon.emmtee.net/ rather than through the
world-readable, unauthenticated http://svn.emmtee.net/); please see the
LogonExtras page for details.

To get started, run the following command (on a suitably modern Un\*x
system):

      htpasswd -n $USER

Please choose a low-security (i.e. web-quality) password and email the
output of the command to StephanOepen. This information
will determine your DELPH-IN SVN user account.

Once your SVN account is active, as a quick-start guide, try the
following:

      svn co http://logon.emmtee.net/trunk logon
      cd logon/franz
      svn switch http://logon.emmtee.net/extras/trunk/franz
      cp ~oe/src/logon/franz/linux.x86.32/devel.lic linux.x86.32
      cp ~oe/src/logon/franz/linux.x86.64/devel.lic linux.x86.64

Next follow the instructions on the
LogonInstallation page, completing at least the
remaining parts of step (1) (i.e. the first-time account setup, adding a
few LOGON-specific settings to your personal shell configuration file
.bashrc). Once these steps are complete (including logging out and back
in, for the changes to take effect), confirm basic functionality by
running a lightweight and short job:

      $LOGONROOT/parse --erg mrs

In some cases, the LOGON tree only includes pre-compiled binaries for
software that the project is likely to modify, specifically
[PET](http://www.delph-in.net/pet) and [TADM](http://tadm.sf.net).
Source code for PET and TADM is hosted in separate SVN repositories, and
we will likely create private branches for use in this project.

# Project Tasks

At present, the DELPH-IN tools are not immediately applicable to
large-scale HPC environments. This is in part owed to missing
'packaging' and interfaces (for effective batch operation), and in part
owed to a lack of support for distributed and parallel processing. The
main objectives of the project are to (a) adapt the core DELPH-IN tools
for effective use on the UiO TITAN cluster and (b) to train the UiO
members of DELPH-IN in the daily routines of HPC usage. The project is
organized as four sub-tasks, each with its own wiki page for specific
information: (1) Packaging, Scripting, and Training
(TitanPackaging); (2) MPI Support in TADM
(TitanTadm); (3) Profiling and Optimizing PET
(TitanPet); and (4) MPI Support in [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) (TitanItsdb).
<update date omitted for speed>{% endraw %}