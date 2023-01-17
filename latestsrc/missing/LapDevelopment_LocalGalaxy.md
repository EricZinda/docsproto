{% raw %}This guide assumes a checkout of <http://svn.emmtee.net/lap/trunk> to
somewhere sensible. If your setup is different, some things will
necessarily have to change.

# Bash setup

Add the following to your .bashrc and re-source it (or start a fresh
shell):

    export LAPTREE=/path/to/lap/tree
    export LAPLIBRARY=/path/to/lap/library
    . $LAPTREE/etc/dot.bashrc
    unset LAPSTORE

# MongoDB

Some notes on how MongoDB is configured on the LAP servers is available
on the LapDevelopment/MongoDB.

- Install MongoDB via your package manager (or from source, whatever
floats your boat); on Ubuntu, the package is simply called mongodb.
- Create a directory for MongoDB's files. I use \~/mongodb
- Start the server: mongodb --dbpath \~/mongodb. If disk space is at a
premium (by default, MongoDB wants to create 3GB of stuff initially)
the --smallfiles option is your friend.

**[ToDo](/ToDo)** Once LAPSTORE is unset, how will LAP know how to talk
to the annotation database (oe; 14-jan-15)?

# Galaxy

We also need a clean Galaxy, as the production instance has some changes
to make things work nice with Abel and such.

This assumes you install galaxy side-by-side with the production
instance (that is, in the root of the SVN checkout). If you want
something else, the file manipulation commands will necessarily have to
be different.

- Check out the appropriate revision of Galaxy:
hg clone -r 5c789ab4144a http://bitbucket.org/galaxy/galaxy-dist
- Copy the tool config from the production instance to your checkout:
cp galaxy/tool\_conf.xml\* galaxy-dist/
- Remove the default tools: rm -r galaxy-dist/tools
- Symlink in the LAP tools: ln -s $PWD/tools galaxy-dist/tools
- In the galaxy-dist directory, run the file run.sh

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
<update date omitted for speed>{% endraw %}