{% raw %}# Background

Most LAP development happens on locally installed instances, e.g.
‘private’ laptops or desktop. The instructions on this page are intended
to support developers in creating their own instance. Over time, we hope
the same recipe will be applicable for the ‘deployment’ (on a new
system) requirement that is part of certification as a CLARIN ‘A
Service’.

# Environment

It appears that most Galaxy development is done on RedHat Enterprise
Linux (RHEL) installations, its ‘clones’ like CentOS, and its community
look-alike Fedora. In principle, there should be no major obstacles to
getting everything working in other Linux distributions, for example
ArchLinux, Debian, or Ubuntu, but we have at times encountered
distribution-related obstacles, for example in the ‘mix’ of versions
that results from the automated downloading of Python eggs by Galaxy.
Whenever possible, we recommend as the path of least resistance an
environment compatible with RHEL6. In early 2016, LAP is only available
for the 64-bit x86 architectures.

To maximally isolate LAP development from other activities, we recommend
creation of a separate account; in the notes below, we assume the user
laportal with its home directory in /home/laportal/. When installing
into a different target directory, some of the path names given below
*and* coded into the LAP-customized Galaxy configuration will need to be
adapted. Alternatively, it might be possible to ‘mimic’ the directory
structure below through a set of symbolic links in /home/laportal/.

# MongoDB

As a prerequisite to LAP installation, there must be a MongoDB database
available for access by the LAP user. Some notes on how MongoDB is
configured on the LAP servers is available on the
LapDevelopment/MongoDB page, but for local
installations the following might just work

Install MongoDB via your package manager, e.g.

      yum -y install mongodb-server

Confirm that the database directory (/var/lib/mongodb/ by default) is
available and, optionally, review MongoDB settings (e.g. in
/etc/mongodb.conf and /etc/sysconfig/mongod).

Start the server and optionally enable automated start-up, e.g.

      /etc/init.d/mongod start
      chkconfig mongod on

By default, MongoDB initially allocates database space relatively
generously (at around three gigabytes, it appears). If disk space is at
a premium (as can be the case on a laptop :-), consider adding the
--smallfiles option to the start-up sequence of the MongoDB server.

# Download LAP

On the (non-Galaxy) LAP side, the following components are required: the
LAP Tree, Library, tool descriptions, and (optionally) operational
scripts.

      cd /home/laportal
      svn co http://svn.emmtee.net/lap/trunk/tree
      svn co http://svn.emmtee.net/lap/trunk/library
      svn co http://svn.emmtee.net/lap/trunk/tools
      svn co http://svn.emmtee.net/lap/trunk/operation

# Galaxy

In early 2016, there are several versions of Galaxy in use with LAP.
However, development focus now shifts towards the 2015.03 release, and
there is a pre-configured snapshot available in SVN with local
extensions (e.g. custom datatypes) and the basic configuration to use
the LAP Tool descriptions (assuming the above locations):

      cd /home/laportal
      svn co http://svn.emmtee.net/lap/trunk/local/galaxy

When using this version, no symbolic links should be required (assuming
the LAP components reside in the recommended location), i.e.
config/galaxy.ini already points to the LAP tool configuration:

      tool_config_file = /home/laportal/tools/config.xml
      tool_path = /home/laportal/tools

To start Galaxy:

      cd /home/laportal/galaxy
      ./run.sh 2>&1 | tee main.log

At this point, with a bit of luck, the built-in Galaxy web server will
be listening at http://localhost:8080.

Except for (currently, a small number of) LAP-specific extensions, this
Galaxy version corresponds to the following release:

      git clone https://github.com/galaxyproject/galaxy/
      cd galaxy
      git checkout release_15.03

# Shell Set-Up

Add the following to .bashrc (in your home directory) and re-source it,
or start a fresh shell, for the changes to take effect:

      export LAPTREE=/home/laportal/tree
      export LAPLIBRARY=/home/laportal/library
      export LAPSTORE=mongodb://127.0.0.1:27017/lapstore

In principle, it might seem desirable to enable the full LAP set-up,
i.e. source dot.bashrc from the LAP Tree. However, we believe it is
desirable to keep separate the Python interpreters used to run Galaxy
vs. the one in the LAP Tree (all LAP tools will always run with the
LAP-internal Python interpreter). As things stand currently, sourcing
dot.bashrc from the LAP tree will prepend the LAP binaries to the search
PATH environment variable, so one would first have to take additional
measures to make sure Galaxy executes using the system version of
Python. Maybe a virtual Python environment would help and, if so, should
be mandated?

# LAP-Specific Web Content

LAP provides some modifications to Galaxy JavaScript code as well as
additional non-Galaxy web content (e.g. brat), which need to be
accessible through the web server. For first-time installation:

      cd /home/laportal
      svn co http://svn.emmtee.net/lap/trunk/www
      cd www/client
      npm install
      grunt

The grunt command will copy the modified files into the Galaxy static/
directory. To also make the non-Galaxy content available, add a
RewriteRule to the web server, as follows:

      RewriteRule ^/lap/(.*) /home/laportal/www/lap/$1 [L]

# Troubleshooting

On Debian Sid the first run fails with the following message:

    WebError 0.8a couldn't be downloaded automatically.  You can try
    building it by hand with:
      python scripts/scramble.py -e WebError
    Fetch failed.

- Run the indicated command python scripts/scramble.py -e WebError
- Run run.sh again

On Ubuntu 14.04, the first run of run.sh fails when downloading eggs.
This seems to be a version conflict between the system Python's version
of some library and what Galaxy wants. It can be fixed by doing the
first invocation in a virtualenv:

- Make sure virtualenv is installed:
sudo apt-get install python-virtualenv
- Set up a virtualenv: virtualenv --no-site-packages galaxy\_env
- Activate it: . galaxy\_env/bin/activate
- Run run.sh again

The server should now start, and subsequent runs should not require the
virtualenv.

**[ToDo](/ToDo)** And what about our custom data types (oe; 14-jan-16)?

**[ToDo](/ToDo):** tool\_conf and tool\_path in config/galaxy.ini; pick
up datatypes

# Test Suite

Relevant parts of the repository:

    trunk/library/python/lap/test.py
    /home/emanuel/work/lap/trunk/tree/tests/function/{eng.t|eng.txt|...}

Before committing changes, developers must make sure that all tests
pass. To run all tests, from the top level trunk directory, run:

    make

Each test in trunk/tree/tests/function/ runs a workflow. To create a new
test:

    touch tree/tests/function/{example.t,example.txt}

First we need to populate example.txt we some text to process (in the
appropriate language). Then we can write the actual test in example.t.

Say that we have just implemented a new POS tagger, hunpos, and we want
to make sure that it plays nicely with the rest of the tools in LAP; a
good test workflow is going to run first all the preprocessing tools
needed by the POS tagger, then a tool that depends on it, and finally an
export tool so that we can make sure we are getting sane output.

The file example.t will look like this:

    from lap.test import TestContext
    from lap.utils import laptree
    
    # Notice how the parameter of the TestContext() 
    # object is equal to the number of tests; 
    # 6 for 6 check_tool() calls.
    with TestContext(6) as ctx:
        # the check tool function returns a LAP receipt 
        # that is then used as input for the next processing step
        upload = ctx.check_python('import/lap/text.py', 
                                  [laptree('tests/function/eng.txt'), None])
        segmented = ctx.check_tool('nltk', 
                                   upload, 
                                   __process__='punkt')
        repp = ctx.check_tool('repp', 
                              segmented, 
                              segmenter="nltk_punkt", 
                              style="ptb")
        tagged = ctx.check_tool('hunpos', 
                                repp, 
                                model='eng_wsj.model',
                                segmenter='nltk_punkt', 
                                tokenizer='repp')
        parsed = ctx.check_tool('maltparser', 
                                tagged, 
                                segmenter="nltk_punkt",
                                tokenizer="repp", 
                                pos="hunpos", 
                                model="bm_sp_opt.mco")
        ctx.check_tool('export', 
                       parsed, 
                       __process__='tsv', 
                       sentence='any', 
                       token='any', 
                       format='CoNLL-X')

Notice how the parameter of the [TestContext](/TestContext)() object is
equal to the number of tests: 6 for 6 check\_tool() calls. Also note
that check\_tool() calls return LAP receipts, which are then used as
input for downstream tools.

We can now run make from the trunk directory and the test will be run
together with the rest of the tests in trunk/tree/tests/function/.
However, when debugging we should run the verbose version of the tests,
which prints all output (stdout, stderr, receipts and exported files) to
stdout.

Running the verbose version of example.t from trunk/:

    LAP_TESTS_VERBOSE=1 tree/python/lap/python tree/tests/function/example.t

Last update: 2016-09-02 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_Deployment/_edit)]{% endraw %}