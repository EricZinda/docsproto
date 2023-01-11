{% raw %}# Overview

The LOGON Benchmarking Suite is a collection of scripts to execute and
time various tasks that are representative of the LOGON MT system (and
the larger collection of [DELPH-IN](http://www.delph-in.net/) NLP
tools). The suite is intended as a cross-platform performance meter.

# Benchmarking Tasks

The benchmark suite comprises the following tasks:

- **tadm** Maximum Entropy Estimation using the
[TADM](http://tadm.sourceforge.net) learner. Given a training sample
of 98109 events in 1317 contexts (using 323665 features), estimate
parameters of a discriminative model. Without a prior and
convergence thresholds of 1e-12 (relative) and 1e-24 (absolute), we
expect to run 493 and 446 iterations, respectively, in 32- and
64-bit mode. This task is heavy on floating point arithmetic,
manipulating large, sparse matrices. TADM is implemented in C++ and
centrally builds on the [PETSc](http://www-unix.mcs.anl.gov/petsc/)
and [TAO](http://www-unix.mcs.anl.gov/tao/) numerical optimization
libraries.
- **cheap** Unification-Based Parsing using the
[PET](http://www.delph-in.net/pet) parser and [LinGO English
Resource Grammar](http://www.delph-in.net/erg) (ERG). Using 1154
inputs from the first section of the [LOGON](http://www.emmtee.net)
Jotunheimen corpus, the parser is run in exhaustive mode with pro-
and retro-active packing (imposing a maximum chart size of 100,000
edges). Results are enumerated from the parse forest and scored,
though not recorded. The specific *cheap* binary used for this
benchmark (i.e. the one in the LOGON tree) is compiled off the PET
*main* branch with mmap() disabled. This task has virtually no
floating point activity but is almost exclusively occupied with
unifying and copying relatively large feature structures: blocks of
memory are allocated, initialized, traversed, compared to other
feature structures (where values are exclusively ints), and
eventually either copied or released. PET is implemented in C++ with
the feature structure core in pure C.
- **ape**
- **generate** Again using the ERG, exhaustively generate from the 326
stored semantic forms in the ERG *hike* treebank. This task is
calling into the standard
LogonProcessing/BatchGeneration
script, i.e. is using a chart size limit of 50,000 edges and
selective unpacking (and storage) of the top-50 results. Although
computing the inverse relation, this task is similar in nature to
the *cheap* and *ape* tasks but using the
[LKB](http://www.delph-in.net/lkb/) generator implemented in
Common-Lisp (and executing in Allegro CL 8.0).
  
  Oddly, the *generate* task appears to benefit from having to
re-compile its sources (typically upon the first execution following
a make update): timings varied between 557s vs. 974s (on *mt*,
comparing the first and second runs, respectively). Possibly there
is an effect on the garbage collector when the compiler is loaded,
and somehow we may ended up avoiding an extra full gc(); weird. To
make measurements comparable, we now make sure the generator code is
compiled prior to execution of the task.

To date, there are no tasks that are heavy on (disk) i/o, nor are we
executing any large-core processes. The above were designed so as to run
on relatively dated equipment with small-ish amounts of physical memory.
However, we should probably add a large-core SVM run (for select nodes)
and possibly also something reading and writing a disk-based
(AllegroCache) BTree of at least several gigabytes. Finally, it would
seem tempting to include end-to-end processing through the LOGON
pipeline, say on the *base* test suite, because that will exercise
context switching heavily (and is likely to benefit from hyperthreading
and multi-core cpus).

# Running the Suite

Execution of individual tasks, parallelization, and general control are
all implemented in a simple shell script. To run the complete benchmark
suite (see below), use:

      $LOGONROOT/uio/test/run

Alternatively, the script accepts a command-line option --count to
enable parallelization and an option --32 to run 32-bit binaries on
64-bit kernels; furthermore, a task identifier can be provided as the
final command-line argument. To execute a four-way run of the 32-bit
*tadm* task, for example, use:

      $LOGONROOT/uio/test/run --32 --count 2 tadm

By default, each task is executed four times, using a round-robin
strategy: thus, execution of other tasks is interleaved with the
repetition of a token task. Upon completion of each task, its output is
validated against the expected result, and the log file is marked
invalid in case validation fails.

The default parallelization tests will execute all tasks (though
skipping the 32-bit runs on 64-bit installations) again, running two,
four, eight, et al. processes (executing the same task) concurrently.
The maximum parallelization factor is determined from /proc/cpuinfo as
the number of cpus reported by the kernel. Thus, for a dual-cpu
(single-core) node with hyperthreading enabled, parallel tests will
execute both two-way and four-way runs.

# Benchmarking Results

All timing results are in wall-clock seconds, i.e. reflecting real time
for the completion of each task. Execution times reported are averaged
over four runs for each task. Typically, the benchmarking suite should
be run on otherwise unloaded nodes, so as to make sure that real time
for task execution is not affected by other, simultaenous demands on the
node.

- |                                                         |          |               |              |                   |         |              |                |
|:-------------------------------------------------------:|:--------:|:-------------:|:------------:|:-----------------:|:-------:|:------------:|:--------------:|
|                         *node*                          | **tadm** | **tadm (32)** | **generate** | **generate (32)** | **ape** | **ape (32)** | **cheap (32)** |
|    *mv* (1 single Pentium M, 1.7ghz, 2gbyte, 32-bit)    |          |               |              |                   |         |              |                |
|      *mt* (2 single Xeon, 2.8ghz, 3gbyte, 32-bit)       |          |      463      |              |        980        |         |              |      1083      |
|      *cc* (2 single Xeon, 3.4ghz, 6gbyte, 32-bit)       |          |               |              |                   |         |              |                |
|      *nm* (2 single Xeon, 3.4ghz, 6gbyte, 64-bit)       |   292    |      406      |     455      |        881        |         |              |      895       |
| *tiger* (4 single Opteron 850, 2.4ghz, 32gbyte, 64-bit) |   355    |      452      |     383      |                   |   160   |              |      800       |
|    *teflon* (2 single Xeon, 3.4ghz, 4gbyte, 64-bit)     |   290    |      406      |     402      |        642        |   192   |     169      |      880       |
|  *c0-4* (2 dual Opteron 275, 2.2ghz, 16gbyte, 64-bit)   |   339    |      420      |     411      |        494        |   155   |     157      |      831       |
| *dalco* (8 dual Opteron 880, 2.4ghz, 128gbyte, 64-bit)  |   328    |               |              |                   |   167   |              |      845       |

Following are timing results for parallel execution, again averaged over
four runs runs per task. In this set-up, the wall-clock time for a
parallel task is counted until the completion of all sub-tasks.

- |          |                  |                  |                      |                      |                 |                 |                   |                   |
|:--------:|:----------------:|:----------------:|:--------------------:|:--------------------:|:---------------:|:---------------:|:-----------------:|:-----------------:|
|  *node*  | **tadm (2-way)** | **tadm (4-way)** | **generate (2-way)** | **generate (4-way)** | **ape (2-way)** | **ape (4-way)** | **cheap (2-way)** | **cheap (4-way)** |
|   *mt*   |       516        |                  |         1280         |                      |                 |                 |       1593        |                   |
|   *cc*   |                  |                  |                      |                      |                 |                 |                   |                   |
|   *nm*   |                  |                  |                      |                      |                 |                 |                   |                   |
| *tiger*  |       380        |       416        |         391          |         455          |       166       |       175       |        831        |        892        |
| *teflon* |       327        |       556        |         416          |         743          |       186       |       309       |        869        |       1795        |
|  *c0-4*  |       336        |       348        |                      |                      |       155       |       159       |        828        |        837        |
| *dalco*  |                  |                  |                      |                      |                 |                 |                   |                   |

Finally, looking further at a somewhat unusual hardware configuration:

- |         |                  |                   |                      |                       |                 |                  |                   |                    |
|:-------:|:----------------:|:-----------------:|:--------------------:|:---------------------:|:---------------:|:----------------:|:-----------------:|:------------------:|
| *node*  | **tadm (8-way)** | **tadm (16-way)** | **generate (8-way)** | **generate (16-way)** | **ape (8-way)** | **ape (16-way)** | **cheap (8-way)** | **cheap (16-way)** |
| *dalco* |                  |                   |                      |                       |                 |                  |                   |                    |

# Discussion

# Acknowledgements
<update date omitted for speed>{% endraw %}