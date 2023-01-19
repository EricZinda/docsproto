{% raw %}# Background

This page documents a sub-task of the HPC adaptation project at UiO;
please see the [TitanTop](https://blog.inductorsoftware.com/docsproto/missing/TitanTop) page for background.

For the first few weeks of the project, participants from both groups
will establish a shared knowledge of the relevant DELPH-IN tools,
standard tasks and use patterns, and their interaction with the HPC
environment. This work package will be organized as a series of hands-on
'walk-through' sessions, most likely at a rate of about one half day per
week. The main result of this phase in the project will be a mutual,
in-depth understanding of the available resources, requirements, and
limitations in current software versions. This knowledge will be
documented through a collection of collaboratively authored wiki pags.

Based on the observations made in the initial project phase, VD and user
staff will jointly adapt and 'package' DELPH-IN tools for batch
processing, i.e. prepare a gradual shift of use patterns, away from the
currently predominant interactive style. This work package will create a
standard set of job scripts and configuration mechanisms that automate
common tasks and provide a good balance between ease of use and
flexibility, i.e. user customization of relevant parameters. The
resources developed in this work package will be contributed as new
open-source components to the DELPH-IN repository.

# TITAN-Specific Files

There is a preliminary collection of TITAN-specific files, including a
few (imperfect) SLURM job scripts in the sub-directory uio/titan/ inside
the LOGON tree. Note that, while we are experimenting, these files may
change frequently. Please remember to always make update in $LOGONROOT
often.

# Parsing

Parsing a corpus (i.e. a sequence of sentences) is an 'embarassingly
parallel' problem, in the sense that processing each sentence is
completely independent of other sentences. In parsing, memory usage is
comparatively tame: each parser client (process), typically, is limited
to a maximum process size of 1G, and the controller (process) tends to
run in less than 2G. However, parsing is quite memory-intense, in the
sense of actively writing (frequently) to and reading from large blocks
of memory. For multi-core nodes, it may be worthwhile to watch out for
possible saturation of the memory sub-system (see below).

The [\[incr tsdb()\]](http://www.delph-in.net/itsdb) controller (written
predominantly in Lisp) supports parallelization (and distribution)
across nodes at the sentence level, using PVM. The parser itself is part
of the [PET](http://www.delph-in.net/pet) package, implemented in C++
(with critical routines in pure C). A typical interactive parser
invocation could be the following:

      $LOGONROOT/parse --erg+tnt --count 7 --best 500 cb

The parse command is a shell script that will (a) launch the controller;
(b) load the grammar identified as erg+tnt (the English Resource
Grammar, [ERG](http://www.delph-in.net/erg), used in conjunction with
the TnT tagger); (c) use PVM routines to create 7 PET client processes
for parsing; (d) configure the parsing environment to return up to 500
most probable parses; and (e) work through the corpus identified as cb
([The Cathedral and the
Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/)).
The parse script and a few more existing LOGON scripts are discussed in
more detail on the [LogonProcessing](https://blog.inductorsoftware.com/docsproto/tools/LogonProcessing) pages.

By default, [\[incr tsdb()\]](http://www.delph-in.net/itsdb) will launch
a PVM daemon on the current node if necessary (i.e. if there is no
existing daemon on that node for the current user). That means that
putting seven PET clients on a single eight-core node is easy, as would
be putting 31 such clients on a 32-core node. To take advantage of
multiple nodes, however, PVM initialization will need to be informed of
the set of nodes (and number of cores per node available), i.e. inspect
$SLURM\_JOB\_NODELIST and friends. StephanOepen used to
have half-baked script support to retrieve that information from the
older SGE environment, then create a PVM initialization file
(.pvm\_hosts), and then ask [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) to use all available PVM nodes.
These steps should be adapted for SLURM, made robust (to a certain
degree), and supported in standard scripts.

Running on c-4-21 (on June 17, 14:30), here is a typical picture; tcheap
is the name of the PET parsing binary:

      top - 14:23:29 up 34 days,  1:24,  1 user,  load average: 6.57, 4.80, 2.26
      Tasks: 183 total,   9 running, 174 sleeping,   0 stopped,   0 zombie
      Cpu(s): 83.3%us,  0.8%sy,  0.0%ni, 15.8%id,  0.0%wa,  0.0%hi,  0.1%si,  0.0%st
      Mem:  16444168k total,  6499380k used,  9944788k free,   204284k buffers
      Swap: 25165812k total,    20644k used, 25145168k free,   195444k cached
    
        PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
       5423 oe        25   0  623m 603m 6120 R  100  3.8   4:55.92 tcheap
       5424 oe        25   0  593m 573m 6052 R  100  3.6   5:12.39 tcheap
       5419 oe        19   0  824m 801m 6052 R   93  5.0   5:25.01 tcheap
       5420 oe        16   0  532m 512m 6052 R   84  3.2   5:20.30 tcheap
       5422 oe        19   0  611m 592m 6052 R   80  3.7   5:01.27 tcheap
       5421 oe        21   0  433m 413m 6052 R   73  2.6   4:52.51 tcheap
       5425 oe        18   0  477m 457m 6052 R   68  2.8   5:05.77 tcheap
       5195 oe        15   0 1263m 1.0g  10m S   52  6.6   3:22.78 alisp
       6204 oe        15   0 12720 1144  820 R    0  0.0   0:00.16 top
       5038 oe        19   0 67040 1472 1168 S    0  0.0   0:00.11 slurm_script
       5188 oe        20   0 62808 1296 1056 S    0  0.0   0:00.00 parse
       5196 oe        18   0 58896  544  460 S    0  0.0   0:00.03 tee
       5418 oe        15   0  6148  752  448 S    0  0.0   0:00.00 pvmd3
       5484 oe        18   0 64820 2476  884 S    0  0.0   0:00.05 tsdb
       6158 oe        15   0 69276 1684 1212 S    0  0.0   0:00.04 bash

I believe the picture is different on the 'fat' nodes, in that all seven
parsers would manage to consume close to 100% cpu. I believe [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) is unable to keep more than 15
to 20 parsers fully loaded, but the effect observed above *may* indicate
memory congestion.

Another recurrent problem is that of synchronization across jobs:
following an update from SVN, the first job to run may need to
re-compile one or more of the [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) Lisp files (in fact, after a
make clean, all Lisp source files will be re-compiled). If another job
starts before re-compilation is complete, it will potentially also
decide to re-compile the same files, and then both processes will write
to the same object file. Presumably we could extend the defsystem() load
and compile methods, so as to first try to get a lock on the object
file, and only decide whether or not to re-compile once the lock is
available. A somewhat cruder (and potentially simpler) solution would be
to wrap a locking mechanism around the entire load-up sequence for
[\[incr tsdb()\]](http://www.delph-in.net/itsdb), i.e. block any
processes from loading and initializing [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) while another job is already in
the 'critical' block.

# (MaxEnt) Model Training and Testing

The task of learning the parameters of a statistical model, say to rank
alternate parses by probability, is substantially more cpu- and
memory-intensive than parsing. The task is typically broken down into
three sub-tasks: (a) preparing a so-called feature cache, extracting all
relevant information from the original training data (a so-called
treebank) and storing it as a Berkeley DB (depending on the size of the
training date, feature caches can vary between 10G and 100G in size);
(b) perfoming a so-called grid search for best-performing feature
choices and estimation (hyper-)parameters (typically using
cross-validation, i.e. repeatedly training on ninety percent of the
total data and testing on the remaining ten); and (c) training and
serializing an actual model, reflecting the parameters found to work
best during the grid search.

# Questions and Answers

## (1) Where do I get feedback on why my jobs fail?

- *My initial attempts at producing a 'parse' job script had
erroneously specified --mem-per-cpu=2M; the jobs were started and
terminated immediately, but even when requesting --mail-type=ALL, I
did not see any indication of why my jobs were killed (nor did I
find a log file providing that information).*

Unfortunately, SLURM does not provide feedback in situations like this,
because it is not the queue system that kills the job: --mem-per-cpu
(and similar options) cause the queue system to set ulimit(3)s for the
process(es), so in the end it is the OS that kills the job (or makes
malloc(3)s fail, and so on) \[thanks to Bjørn-Helge Mevik\].

I still wonder about two things: SGE, i believe, does provide this kind
of feedback; how is that accomplished? Furthermore, several of the
typical DELPH-IN jobs are quite memory-hungy, and seeing that part of
the software is implemented in Lisp there can be substantial variation
in process size (e.g. whenenver a gc() concludes with a need to grow the
Lisp heap) it might be worthwhile to look for a generic way of
retrieving struct rusage information (for the child process, once it
died) from the job script.

## (2) How can I set common, per-user SLURM defaults?

- *For use with the older SGE environment, I had a user configuration
file with SGE defaults (project, maximum wall-clock time, mail
notification, and so on). Is there a corresponding facility in
SLURM? If not, is there a way to include \#SBATCH statements near
the top of each job file?*

It would seem this functionality is not supported in SLURM \[thanks to
Bjørn-Helge Mevik\].

However, for some of the common options it may still be possible to set
environment variables to default values, e.g. SBATCH\_ACCOUNT and
SBATCH\_TIMELIMIT.

## (3) Can I pass command-line arguments into SLURM job scripts?

- *The sbatch documentation suggests that it should be possible to
pass command-line options to the job script, i.e. not have to
maintain separate job scripts for every single (distinct) way of
invoking the LOGON 'parse' script, say.*

Yes, sbatch stops consuming command-line options as soon as it sees the
first option that it does not recognize as its own; that option and all
following are available as parameters to the job script (e.g. accessible
as $1, $@, and so on). As of 16-jun, the following seems to work
(requesting one node and eight cores, hardwired in the job script):

      /usr/bin/sbatch $LOGONROOT/uio/titan/parse --erg+tnt --best 500 cb

However, the default sbatch in the standard PATH on TITAN is a local
wrapper script that cannot currently (as of April 2010) handle
additional command-line arguments. In general, it is advisable to use
the standard sbatch wrapper, which will provide a number of sanity
checks and sensible default settings; but if one absolutely depends on
giving additional arguments on the command line, then using
/usr/bin/sbatch is an okay work-around (at your own risk :-).

## (4) How do I monitor cpu usage for my user and project account(s)?

## (5) How to find out why my job is being held by the scheduler?

- *On June 16, I submitted a job with the following specifications:
--nodes=1, --ntasks-per-node=8, --mem-per-cpu=2G, and
--time=48:00:00 (which I think should not matter). Ganglia reports
an average load for TITAN of 225% (can this be true), but at the
same time shows dozens of compute nodes with a load of zero. The job
is still held, with job id \#279248.*

The answer is actually provided in the [TITAN User
Guide](http://hpc.uio.no/index.php/Titan_User_Guide#Large_Memory_Jobs):
the vast majority of nodes have 16G in physical RAM, but for various
reasons somewhat less than that is available for user jobs. For jobs
requesting more than about 15G of RAM, it is recommend to put them into
into the 'hugemen' queue \[thanks to Ole Widar Saastad and Bjørn-Helge
Mevik\].

I have now changed the 'parse' job script to request --mem-per-cpu=1792M
(June 17, 13:30), and after about ten minutes the job was scheduled
allright. At the same time, I am trying --partition=lowpri too, but in
the past i have somehow never succeeded in getting things to run there.
Are 'lowpri' jobs billed against my cpu quote too, I wonder? If so,
there is a risk of fruitlessly burning cpu hours: we lack a functional
checkpointing regime, hence any job that does not get to complete (on
the node where it started) will be wasted effort.

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/TitanPackaging/_edit)]{% endraw %}