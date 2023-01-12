{% raw %}# Reading List

- Yao-zhong Zhang, Takuya Matsuzaki, & Jun’ichi Tsujii (2010).
[Forest-guided Supertagger
Training](http://www.aclweb.org/anthology/C/C10/C10-1144.pdf).
COLING 2010

RD: Superficially relevant, but not really comparable. As far as I
understand, they use a CFG approximation of the parse forest as a filter
when training the supertagger to 'speed up' the perceptron training
process. It doesn't actually speed it up, but they get more accurate
tags after the same number of iterations as the baseline perceptron, but
each iteration takes 25-70 times longer... They didn't show how accurate
the baseline perceptron without the forest filtering was when run for
the same amount of time. As I understand it, in the limit, both methods
should reach the same answer. It's basically the same CFG-filter they
use at the input of their parser. We'd get similar information (except
exact, not approximate) by extracting tag sequences from the top 500
parses if we wanted to use it in training, but that is going to depend
on how we train the model, and I didn't think we were planning to look
at pointwise tag classifiers?

# Relevant stuff from ASR

## ASR analogy

Aim: (argmax) P(Labels\|Obs) = P(Obs\|Labels)P(Labels)/P(Obs)

|                      |                                                |                                                     |
|----------------------|------------------------------------------------|-----------------------------------------------------|
|                      | ASR                                            | Supertags                                           |
| Obs                  | acoustic slice                                 | tokens (words)                                      |
| Labels               | words                                          | supertags                                           |
| Hidden States        | subphone x in word y                           | ??                                                  |
| Data Characteristics | obs combinations/label: low, \#labels: v. high | obs combinations/label: v. high, \#labels: moderate |

- acoustic slides are smaller than the subphones, and the states
self-loop to 'use up' all the input observations
- Viterbi algorithm for ASR actually computes most likely sequence of
states, not words. Approximation falls down when there are many
pronunciations per word (\~ many realisations per tag). Solution is
either multi-pass decoding, using n-best list Viterbi or word
lattice plus re-ranking, or A\* decoding.
- Lexical chart is already an n-best set/word lattice?

## non-Viterbi ASR

### A\* decoding

I've never looked at this before, but from a quick read it seems like it
could be a structure for the varying length observations + length
penalty idea Erik was talking about. Partial path hypothesis agenda
scored by

Score(partial path) = P(partial path) + h\*(partial path)

where P(partial path) is P(Obs\_so\_far\|Tags\_so\_far)P(Tags\_so\_far)
and h\*(partial path) is an estimation of the score from the rest of the
sequence, which could just be proportional to the length of the sequence
remaining.

### MMIE training

Maximum Mutual Information Estimation, which is the same as conditional
max likelihood: discriminatively train the HMM. Does this negate the
problem of using varying tokenisations of the observation sequence,
since its not trying to estimate the joint probability anymore?
(Assuming we'd just sum over what was in the lexical chart.)

### More complicated

- [A probabilistic framework for segment-based speech
recognition](http://www.sls.csail.mit.edu/sls/publications/2003/glass.csl2003.pdf)
Glass(2003): uses varying length segments, rather than constant
acoustic frames
- [Graphical model architectures for speech
recognition](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.8512&rep=rep1&type=pdf)
Bilmes & Bartels (2005): I've been meaning to look at hierarchical
models since I talked about them with Mark Johnson 2 years ago,
maybe I should actually read this :slightly\_smiling\_face:

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/LatticeSupertagging/_edit)]{% endraw %}