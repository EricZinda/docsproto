{% raw %}Some notes on the [StarSEM 2012 shared
task](http://www.clips.ua.ac.be/sem2012-st-neg/).

# Training data

3,640 sentences with 989 instances of negation.

99 instances have no scope; 92 instances have a discontinuous scope that
is not bridged by the cue.

392 instances have no event.

Collins' coverage of the training data is 99.4%.

Collins can't lemmatise contractions, e.g. can't = &lt;unknown&gt;

## Some examples

Following [Morante et al's
(2011)](http://www.clips.ua.ac.be/annotation-of-negation-cues-and-their-scope-guidelines-v10)
conventions of **bold** for cues, <span class="u">underline</span> for
scope and *italic* for events.

HoundOfTheBaskervilles\_ch1, s1. prefixal cue, weirdness

1. Mr. Sherlock Holmes, who was usually very late in the mornings, save
upon <span class="u">those</span> not **in**<span class="u">frequent
occasions when he was up all night</span>, was seated at the
breakfast table.
2. Mr. Sherlock Holmes, who was usually very late in the mornings, save
upon <span class="u">those</span> **not** <span class="u">infrequent
occasions when he was up all night</span>, was seated at the
breakfast table.
3. Mr. Sherlock Holmes, <span class="u">who *was*</span> usually <span
class="u">very *late* in the mornings,</span>} **save** <span
class="u">upon those not infrequent occasions when he was up all
night</span>, was seated at the breakfast table.

HoundOfTheBaskervilles\_ch1, s12, prefixal cue

Since <span class="u">we have been so</span> **un**<span
class="u">*fortunate* as to miss him</span> and have no notion of his
errand, this accidental souvenir becomes of importance.

HoundOfTheBaskervilles\_ch1, s67: discontinuous scope

If <span class="u">he was</span>i n the hospital and yet **not** <span
class="u">on the staff</span> he could only have been a house-surpeon or
a house-physician: little more than a senior student.

HoundOfTheBaskervilles\_ch1, s8: weirdness

It is my experience that it is only an amiable man in this world who
receives testimonials, only <span class="u">an</span> **un***ambitious*
<span class="u">one who abandons a London career for the country</span>,
and only an absent-minded one who leaves his stick and not his
visiting-card after waiting an hour in your room.

HoundOfTheBaskervilles\_ch1, s89: discontinuous scope

<span class="u">The dog's jaw</span>, as shown in the space between
these marks, <span class="u">is</span> too broad in my opinion for a
terrier and **not** *<span class="u">broad</span>*<span class="u">
enough for a mastiff</span>.

HoundOfTheBaskervilles\_ch3, s235: Multi-word cue, discontinuous scope

Then, again, whom was he waiting for that night, and why was <span
class="u">he *waiting* for him</span> in the yew alley **rather than**
<span class="u">in his own house</span>?"

HoundOfTheBaskervilles\_ch4, s154: contracted cue

But as to my uncle's death: well, it all seems boiling up in my head,
and <span class="u">I *can*</span>**'t** <span class="u">get it clear
yet</span>.

HoundOfTheBaskervilles\_ch4, S194: weirdness

**Not for the world**, my dear Watson.

Last update: 2012-02-10 by JonathonRead [[edit](https://github.com/delph-in/docs/wiki/StarSEM/_edit)]{% endraw %}