{% raw %}Discussion: Parse ranking, reliability/stability of evaluation metrics
Moderator: Rebecca Dridan

Motivation: the study of differences in parsing various domains and
genres does not show stable improvements.

According to sentence accuracy (SA) measure, i.e. exact match, parsing
accuracy on Linux domain seems to be worse than on NLP, but with another
metric, PE, results are opposite. It is rather evident that the results
are correlated with sentence length.

Range within the same domain is quite large (compared to the differences
between various domains and genres)

The range for the DeepBank is smaller. Maybe because
Wikipedia data has more style and content variation. The range on PTB
[ParseEval](/ParseEval) is less than our on DeepBank

0.3 difference of F1 is a significant improvement on Deepbank. But we
get 0.3 training on different parts of WeScience corpus.

The question is how to present results to a larger community?

* * *

Woodley: if the variation cross-fold is large, it does not necessarily
mean that results are meaningless.

Joao: The ranking of the WS01 is very similar for PE and SA. Maybe the
first split is easier.

Francis: could it be that the first WS01 was done with a more fixed
grammar, e.g. more phenomena that occur in that fold was included in the
grammar?

Dan: while treebanking WS01 more time was spent on learning about domain
and making relevant extensions to the grammar to adapt it to frequent
phenomena that affect performance of the grammar. E.g. adaptation to
phrases like “500 Australian pounds”

It is possible that Dan added more phenomena to the grammar from the
first fold than from the other folds. Imagine almost every sentence in
one of the WS sections contains some Spanish words. Since the grammar is
not adapted for linguistics, the coverage would drop significantly.

Guy: Have you tried some measure of correlation (like R-measure)? If the
numbers are different does not mean that correlation is strong.

Bec: What is expected variation? Is the sentence length the main
indicator about the accuracy? We observe bigger drop for the longer
sentences

Tim: Test stability of these things. E.g. significance test in context
of MT evaluation. What absolute difference in numbers is going to be
significant?

Antske: Maybe the evaluations are way too vague? Could we only look at
what kinds of things we get right?

Woodley: I ran experiment taking WS profiles and breaking them down. The
range of the exact match was 5%. It could be related to the model.

Francis: We used exact match. We also did (unlabeled) bracketing
accuracy which was high and the differences were small. Bec: Sentence
accuracy is more correlated with domain than bracketing metric. Can we
have any confidence in difference in parsing performance of parser on
different domains and genres?

Guy: Hypothesis testing? Whether differences are random or not?

Bec: The differences are not statistically significant, but sort of
repeatable.

Guy: Maybe repetitivity is significant?

Stephan: Sentence accuracy is more sensitive metric but it was usually
applied to the in-domain results.

Francis: Have you tried normalization to sentence length?

Bec: Does very badly on short sentences because they are not sentences.

Guy: Statistical model that models sentence length with respect to
parsing performance?

Tim: Did smth similar. Normalizing vector of the sentence length.

Bec: Any standard ways to do that?

Tim: Do the same evaluation for e.g. Stanford parser and other parsers
and see how they are affected.

Bec: Perhaps the problem is that we do not have a clear definition of a
domain. The unsatisfiying definition of domain we arrive at in these
experiments is sentence length.

Emily: To play devil's advocate for a bit: You say you're looking for
differences between domains, and it seems like you've found one in
sentence length. Maybe what you want is a way to acknowledge that, and
then take it out so you can see what other differences there are?

Bec: is thinking to pick sentences of the same length from different
domains and see results for them

Guy: Performance as a function of sentence length. Inference on
performance on each domain according to sentence length. Then compute
distributions and compare cross-domain. Maybe it will remove the
sentence length effect.

Bec: It looks like people do not do this.

David: get numbers across all domains

Tim: comparison with other parsers. How to compare if you don't get any
parse at all? E.g. Berkeley has imperfect coverage. Maybe normalization
to coverage.

Bec: We can take intersection of everything that was parsed.

Rebecca concludes that the way to go is to find a sentence length-biased
evaluation metric.
<update date omitted for speed>{% endraw %}