{% raw %}Some notes on the [StarSEM 2012 shared
task](http://www.clips.ua.ac.be/sem2012-st-neg/). I've used similar
annotation conventions to our previous work, with &lt;&gt; for cues, {}
for scope and now \[\] for events. For papers though we should probably
follow [Morante et al's
(2011)](http://www.clips.ua.ac.be/annotation-of-negation-cues-and-their-scope-guidelines-v10)
conventions of **bold** for cues, <span class="u">underline</span> for
scope and *italic* for events.

# Baselines

## Scope Resolution (gold cues)

- Entire sentence, except initial/final punctuation: P=64.20 R=17.59
F1=27.61
- From cue to left and right punctuation or sentence boundary:
P=97.95, R=32.36, F1=48.65

# Pseudo-CoNNL format

The files are provided in CONLL format, with the first 7 columns
corresponding to:

1. Book\_Chapter
2. Sentence number within chapter
3. token number within sentence
4. word
5. lemma
6. part-of-speech
7. syntax

If the sentence does not have negations:

- 8\. \*\*\*

Otherwise there are three columns per negation:

- (8,11,14, ...) word (or part of word) that is part of the cue
- (9,12,15, ...) word (or part of word) that is part of the scope
- (10,13,16, ...) word (or part of word) that is part of the event

# New data

3,644 sentences with 986 instances of negation.

98 instances have no scope; 93 instances have a discontinuous scope that
is not bridged by the cue.

Of the remaining 795 instances, 439 are aligned with some constituent in
the C&J parses. Applying out bioscope slackening heuristics:

- constituent final punctuation (+93)
- constituent initial punctuation (+37)
- initial adverbs when not the cue (+9)
- scope starts with cue when it is a noun (-1)
- scope does not start with an auxiliary (-6)

Applying only the beneficial heuristics leaves us with an alignment rate
of 72.7%.

The following are listings of instances with: [no
scope](http://dl.dropbox.com/u/680530/WeSearch/StarSem/null.txt),
[discontinuous
scope](http://dl.dropbox.com/u/680530/WeSearch/StarSem/discontinuous.txt),
[scope that is not aligned with a
constituent](http://dl.dropbox.com/u/680530/WeSearch/StarSem/unaligned.txt)
and [scope that is aligned with a
constituent](http://dl.dropbox.com/u/680530/WeSearch/StarSem/aligned.txt)---
in which instances are delimited by double newlines; the first line is
an instance identifier comprised of: chapter &lt;TAB&gt; sentence in
chapter &lt;TAB&gt; negation in sentence. The second line is the tokens
of the sentence, where cues are indicated with &lt; &gt;, scope with {
}, and the most specific subsuming constituent of the scope with \_ \_.

Additional slackening heuristics for CD:

- if a non-NP node on path from cue to subsumer has a sibling CC,
scope starts before CC
- move in from initial CC, UH, ADVP or INTJ

Current alignment rate is 81.6% of continuous scopes.

## Instances of cues

|              |                      |                |     |                 |                  |             |
|--------------|----------------------|----------------|-----|-----------------|------------------|-------------|
| **TRAINING** |                      |                |     | **DEVELOPMENT** |                  |             |
| Freq.        | Cue                  | PoS            |     | Freq.           | Cue              | PoS         |
| 326          | not                  | RB             |     | 39              | not              | RB          |
| 139          | no                   | DT             |     | 27              | no               | DT          |
| 72           | un\*                 | JJ             |     | 20              | n't              | RB          |
| 65           | n't                  | RB             |     | 16              | nothing          | NN          |
| 59           | never                | RB             |     | 12              | un\*             | JJ          |
| 59           | no                   | UH             |     | 11              | never            | RB          |
| 55           | nothing              | NN             |     | 7               | without          | IN          |
| 27           | no                   | RB             |     | 5               | im\*             | JJ          |
| 24           | without              | IN             |     | 4               | nor              | CC          |
| 22           | \*not                | RB             |     | 4               | in\*             | JJ          |
| 20           | \*less               | JJ             |     | 4               | no               | UH          |
| 17           | in\*                 | JJ             |     | 3               | un\*             | RB          |
| 16           | im\*                 | JJ             |     | 3               | \*less           | JJ          |
| 12           | none                 | NN             |     | 2               | neither\_\*\_nor | DT\_\*\_CC  |
| 6            | nor                  | CC             |     | 1               | nobody           | NN          |
| 4            | in\*                 | RB             |     | 1               | in\*             | RB          |
| 4            | un\*                 | RB             |     | 1               | dis\*            | VBN         |
| 4            | \*less\*             | RB             |     | 1               | dis\*            | NN          |
| 4            | ir\*                 | JJ             |     | 1               | save             | IN          |
| 3            | \*less               | NN             |     | 1               | ir\*             | JJ          |
| 3            | dis\*                | NN             |     | 1               | \*not            | NN          |
| 2            | im\*                 | RB             |     | 1               | no\_\*\_nor      | DT\_\*\_CC  |
| 2            | nowhere              | RB             |     | 1               | \*n\*            | RB          |
| 2            | neither\_\*\_nor     | DT\_\*\_CC     |     | 1               | more             | JJR         |
| 2            | \*not                | NN             |     | 1               | im\*             | NN          |
| 2            | \*not                | VBD            |     | 1               | neither          | DT          |
| 2            | prevent              | VB             |     | 1               | no\_more         | DT\_RBR     |
| 2            | \*not                | VBP            |     | 1               | by\_no\_means    | IN\_DT\_NNS |
| 2            | on\_the\_contrary    | IN\_DT\_NN     |     | 1               | un\*             | VBN         |
| 2            | by\_no\_means        | IN\_DT\_NNS    |     |                 |                  |             |
| 1            | rather\_than         | RB\_IN         |     |                 |                  |             |
| 1            | by\_no\_means        | IN\_DT\_VBZ    |     |                 |                  |             |
| 1            | nobody               | NN             |     |                 |                  |             |
| 1            | ir\*                 | RB             |     |                 |                  |             |
| 1            | fail                 | VBP            |     |                 |                  |             |
| 1            | no\*                 | NN             |     |                 |                  |             |
| 1            | un                   | IN             |     |                 |                  |             |
| 1            | absence              | NN             |     |                 |                  |             |
| 1            | nothing\_at\_all     | NN\_IN\_DT     |     |                 |                  |             |
| 1            | neglected            | VBN            |     |                 |                  |             |
| 1            | dis\*                | VBN            |     |                 |                  |             |
| 1            | refused              | VBD            |     |                 |                  |             |
| 1            | no                   | NNP            |     |                 |                  |             |
| 1            | in\*                 | NNS            |     |                 |                  |             |
| 1            | un\*                 | IN             |     |                 |                  |             |
| 1            | ir\*                 | NN             |     |                 |                  |             |
| 1            | not\_the             | RB\_DT         |     |                 |                  |             |
| 1            | not\_for\_the\_world | RB\_IN\_DT\_NN |     |                 |                  |             |
| 1            | save                 | VB             |     |                 |                  |             |
| 1            | except               | VB             |     |                 |                  |             |
| 1            | \*less\*             | JJ             |     |                 |                  |             |
| 1            | unusual              | JJ             |     |                 |                  |             |
| 1            | \*less\*             | NN             |     |                 |                  |             |
| 1            | un\*                 | NN             |     |                 |                  |             |
| 1            | dis\*                | JJ             |     |                 |                  |             |
| 1            | not\_\*\_not         | RB\_\*\_RB     |     |                 |                  |             |
| 1            | un\*                 | VBN            |     |                 |                  |             |

# Old Data

3,640 sentences with 989 instances of negation.

99 instances have no scope; 92 instances have a discontinuous scope that
is not bridged by the cue.

Of the remaining 798 instances, 80 are aligned with some constituent.
Applying our bioscope slackening heuristics:

- constituent final punctuation (+437)
- constituent initial punctuation (+70)
- initial adverbs when not the cue (+8)
- scope starts with cue when it is a noun (+2)
- scope does not start with an auxiliary (-9)

Applying only the beneficial heuristics leaves us with an alignment rate
of 73.4%.

...

371 instances have no event; 14 instances have discontinuous events. In
6 instances the event lies outside of the scope---these seem to be
annotation errors:

- ... only {an} &lt;un&gt;\[ambitious\] {one who abandons a London
career for the country} ...
- ... {an} &lt;un&gt;\[justifiable\] {intrusion}, ...
- {It} &lt;never&gt; \[recovered\] {from the blow}, ...
- "But {I} \[can\]&lt;'t&gt; {forget them}, Miss Stapleton," said I.
- ... and means to \[spare\] &lt;no&gt; {pains or expense} to restore
the grandeur of his family.
- Coming down with an &lt;un&gt;\[signed\] {warrant}.

...

Collins' coverage of the training data is 99.4% (21 of 3,640 sentence).
In those 21 there are 10 instances of negation, for example:

- "Know then that in the time of the Great Rebellion (the history of
which by the learned Lord Clarendon I most earnestly commend to your
attention) this Manor of Baskerville has held by Hugo of that name,
nor &lt;can&gt; {\[it\] be gainsaid that he was a most wild,
profane, and {\[god\]}&lt;less&gt; man}.

## Tokenisation issues

|              |          |                 |          |
|:------------:|:--------:|:---------------:|:--------:|
| **Training** |          | **Development** |          |
|  **Freq.**   | **Word** |    **Freq.**    | **Word** |
|      35      |  don't   |       17        |    't    |
|      11      |  can't   |        3        |  don't   |
|      7       |   n't    |                 |          |
|      6       |  isn't   |                 |          |
|      5       |  didn't  |                 |          |
|      2       | couldn't |                 |          |

Of the training data bigrams ending in n't there are:

- 4 do n't
- 1 did n't
- 1 had n't
- 1 wo n't

Of the development data bigrams ending in 't there are:

- 7 don 't
- 4 can 't
- 3 didn 't
- 1 couldn 't
- 1 shan 't
- 1 wasn 't

There is a full listing of tokens containing punctuation here:
[JimWhite/StarSemTokenTabulation](https://blog.inductorsoftware.com/docsproto/missing/JimWhite_StarSemTokenTabulation).

## Some examples

HoundOfTheBaskervilles\_ch1, s1. prefixed cue, weirdness

- Mr. Sherlock Holmes, who was usually very late in the mornings, save
upon {those} not &lt;in&gt;{frequent occasions when he was up all
night}, was seated at the breakfast table.
- Mr. Sherlock Holmes, who was usually very late in the mornings, save
upon {those} &lt;not&gt; {infrequent occasions when he was up all
night}, was seated at the breakfast table.
- Mr. Sherlock Holmes, {who was} usually {very late in the mornings,}
&lt;save&gt; {upon those not infrequent occasions when he was up all
night}, was seated at the breakfast table.

HoundOfTheBaskervilles\_ch1, s12, prefixed cue

- Since {we have been so} &lt;un&gt;{\[fortunate\]\] {as to miss him}
and have no notion of his errand, this accidental souvenir becomes
of importance.

HoundOfTheBaskervilles\_ch1, s67: discontinuous scope

- If {he was} in the hospital and yet &lt;not&gt; {on the staff} he
could only have been a house-surpeon or a house-physician: little
more than a senior student.

HoundOfTheBaskervilles\_ch1, s8: weirdness

- It is my experience that it is only an amiable man in this world who
receives testimonials, only {an} &lt;un&gt;\[ambitious\] {one who
abandons a London career for the country}, and only an absent-minded
one who leaves his stick and not his visiting-card after waiting an
hour in your room.

HoundOfTheBaskervilles\_ch1, s89: discontinuous scope

- {The dog's jaw}, as shown in the space between these marks, {is} too
broad in my opinion for a terrier and &lt;not&gt; {\[broad\] enough
for a mastiff}.

HoundOfTheBaskervilles\_ch3, s235: Multi-word cue, discontinuous scope

- Then, again, whom was he waiting for that night, and why was {he
\[waiting\] for him} in the yew alley &lt;rather than&gt; {in his
own house}?"

HoundOfTheBaskervilles\_ch4, s154: contracted cue

- But as to my uncle's death: well, it all seems boiling up in my
head, and {I \[can\]}&lt;'t&gt; {get it clear yet}.

HoundOfTheBaskervilles\_ch4, s233: Abbreviation of "number" tagged as
negation

- {No.} 2704 is our man .

# Instances of cues

|      |                      |                |
|------|----------------------|----------------|
| Frq. | Cue                  | POS            |
| 346  | not                  | RB             |
| 137  | no                   | DT             |
| 71   | un                   | JJ             |
| 64   | no                   | UH             |
| 58   | never                | RB             |
| 55   | nothing              | NN             |
| 36   | n't                  | RB             |
| 24   | without              | IN             |
| 22   | less                 | JJ             |
| 18   | no                   | RB             |
| 17   | in                   | JJ             |
| 16   | im                   | JJ             |
| 12   | none                 | NN             |
| 8    | n't                  | JJ             |
| 6    | 't                   | RB             |
| 6    | n't                  | VB             |
| 5    | n't                  | NN             |
| 5    | no                   | NNP            |
| 5    | ir                   | JJ             |
| 4    | nor                  | CC             |
| 4    | un                   | RB             |
| 4    | less                 | RB             |
| 4    | in                   | RB             |
| 3    | dis                  | NN             |
| 3    | not                  | VB             |
| 3    | less                 | NN             |
| 2    | '&lt;NULL&gt;'       | '&lt;NULL&gt;' |
| 2    | not                  | JJ             |
| 2    | un                   | NN             |
| 2    | not                  | NN             |
| 2    | un                   | IN             |
| 2    | nowhere              | RB             |
| 2    | by\_no\_means        | IN\_DT\_NN     |
| 2    | prevent              | VB             |
| 2    | n't                  | NNP            |
| 2    | 't                   | NN             |
| 2    | im                   | RB             |
| 2    | on\_the\_contrary    | IN\_DT\_NN     |
| 1    | rather\_than         | RB\_IN         |
| 1    | nobody               | NN             |
| 1    | been                 | VBN            |
| 1    | fail                 | VBP            |
| 1    | neither\_\*\_nor     | CC\_\*\_CC     |
| 1    | absence              | NN             |
| 1    | other                | JJ             |
| 1    | nothing\_at\_all     | NN\_IN\_DT     |
| 1    | can                  | MD             |
| 1    | neglected            | VBN            |
| 1    | ir                   | RB             |
| 1    | un                   | VBG            |
| 1    | refused              | VBD            |
| 1    | the                  | DT             |
| 1    | yet                  | RB             |
| 1    | never                | NNP            |
| 1    | save                 | VBP            |
| 1    | not\_for\_the\_world | RB\_IN\_DT\_NN |
| 1    | un                   | VBN            |
| 1    | signs                | NNS            |
| 1    | in                   | NNS            |
| 1    | no                   | JJ             |
| 1    | unusual              | JJ             |
| 1    | dis                  | VBN            |
| 1    | neither\_\*\_nor     | DT\_\*\_CC     |
| 1    | by\_no\_means        | IN\_RB\_VBZ    |
| 1    | not\_\*\_not         | RB\_\*\_RB     |
| 1    | except               | IN             |
| 1    | dis                  | JJ             |

## Top 20 frequent tokens and pos for events (&gt;=4 instances)

The full list is
[here](http://dl.dropbox.com/u/680530/WeSearch/StarSem/events.csv).
There are 367 token/pos types.

|          |          |         |
|----------|----------|---------|
| **Frq.** | **Word** | **POS** |
| 51       | could    | MD      |
| 25       | can      | RB      |
| 19       | have     | VBP     |
| 14       | had      | VBD     |
| 12       | know     | VB      |
| 10       | know     | VBP     |
| 7        | able     | JJ      |
| 7        | seen     | VBN     |
| 6        | happy    | JJ      |
| 5        | pleasant | JJ      |
| 5        | like     | IN      |
| 5        | sign     | NN      |
| 5        | say      | VB      |
| 5        | man      | NN      |
| 4        | likely   | JJ      |
| 4        | heard    | VBN     |
| 4        | saw      | VBD     |
| 4        | can      | MD      |
| 4        | possible | JJ      |
| 4        | known    | JJ      |
<update date omitted for speed>{% endraw %}