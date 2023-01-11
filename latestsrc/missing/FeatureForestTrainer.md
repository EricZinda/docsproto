{% raw %}## Feature Forest Trainer

This page describes an experimental tool created by
[WoodleyPackard](/WoodleyPackard) to train maximum entropy models for
statistical disambiguation. The *.mem* files produced by this method are
compatible with ACE and may also work with other tools,
although they are missing some metadata (if you discover they don't work
with some tool and you want them to, and especially if you know why, I'd
be happy to hear).

This as-yet unnamed tool uses the method of Miyao and Tsujii (2002),
which trains a discriminative model using a packed representation of the
full parse forest. This is in contrast to the traditional method of
building parse selection models employed by DELPH-IN, i.e. using TADM
with an explicitly enumerated top-500 list. Although the feature-forests
method is arguably more principled (although there are also ways in
which it is less principled -- for instance depending on the packing
method employed when building the forest, the negative training data may
effectively include derivations which would not fully unify),
empirically the resulting models perform no better (or worse) than those
produced the traditional way.

The profiles used as input to the full-forest trainer take up
substantially less disk space than a top-500 list; however, due to some
details of the feature-forest algorithm, the memory used while training
can sometimes exceed that used by a top-500 trainer.

## Using the Tool

The source code is available through subversion at:
<http://sweaglesw.org/a/svn/feature-forest/trunk/>

To compile it, you'll need the following additional dependencies
installed: libace (installed by "make install" in the ACE source tree),
liba (<http://sweaglesw.org/a/svn/liba/trunk/>), libtsdb
(<http://sweaglesw.org/a/svn/libtsdb/trunk/>), and mela
(<http://sweaglesw.org/a/svn/mela/trunk/>).

To build a model, you need (at least) three things: an ACE grammar
image, a TSDB profile with gold annotations, and a TSDB profile
containing the complete parse forest. These can be the same profile, but
usually aren't. Usage is best demonstrated by an example. You'll need
two separate terminals open:

    terminal-one$ ./ffmaster 1 mrs.mem
    waiting for 1 workers to connect on port 2577...

And then:

    terminal-two$ ./ffworker my-grammar/grammar.dat my-grammar/tsdb/forests/mrs my-grammar/tsdb/gold/mrs localhost

You should see some output from *ffworker* for each item in the profile
as the forests are loaded, and then output from both programs as they
cooperate to perform the numerical optimization. If all goes well, both
will terminate (pretty quickly in this case, since *mrs* is not a very
big dataset), and *mrs.mem* will be written.

## Using the Model

You can edit the *maxent-model* configuration option in your grammar's
*config.tdl* and then reload the grammar. Alternately, you can pass
--maxent=mrs.mem to recent versions of ACE.
<update date omitted for speed>{% endraw %}