{% raw %}# Background

Working with a lattice of lexical hypotheses and an (über)tagger, we
seek to develop a filtering function that discards unlikely hypotheses.
The formalisation of the lexical filtering process may be found
[here](http://dl.dropbox.com/u/680530/WeSearch/Lexical%20Filtering/formalisation.pdf).

# TNT output for filtering of LE types

One such filter function maps PTB tags output from the TNT tagger onto
LE Types. Mappings may be derived intuitively from inspection of a
[confusion
matrix](http://dl.dropbox.com/u/680530/WeSearch/Lexical%20Filtering/tnt.le.confusion.pdf)
detailing the choices of TNT with respect to LE types.

An alternative approach is to find mappings based on the preferred
outcomes of lexical filtering, (i.e. gains in parser efficiency versus
losses in parser accuracy and coverage). These outcomes may be
approximated by examining the relations between TNT precision, TNT
recall and the ambiguity of LE types.

Frequency of LE types in JH0:

|          |               |
|----------|---------------|
| **type** | **frequency** |
| n        | 1,134,661     |
| p        | 498,443       |
| v        | 454,513       |
| d        | 335,667       |
| aj       | 332,243       |
| c        | 182,759       |
| av       | 145,290       |
| cm       | 33,618        |
| pp       | 34,496        |
| pt       | 3,864         |

Plots of the TNT performance on the most frequent LE types

<http://dl.dropbox.com/u/680530/WeSearch/Lexical%20Filtering/roc.png>

A plot of the precision vs. lexical items filtered for each handled LE
type:

<http://dl.dropbox.com/u/680530/WeSearch/Lexical%20Filtering/filtering.png>

Effective threshold ranges for LE Types:

|          |         |                   |                   |         |                   |                   |
|----------|---------|-------------------|-------------------|---------|-------------------|-------------------|
| **type** | **min** | **min-precision** | **min-filtering** | **max** | **max-precision** | **max-filtering** |
| n        | 0.35    | 0.93639           | 493184            | 1.00    | 0.94253           | 210876            |
| v        | 0.47    | 0.94183           | 217656            | 1.00    | 0.96008           | 130873            |
| p        | 0.35    | 0.89550           | 1196773           | 1.00    | 0.94866           | 708213            |
| d        | 0.59    | 0.92464           | 408522            | 1.00    | 0.93566           | 318760            |
| aj       | 0.36    | 0.73078           | 629913            | 1.00    | 0.90287           | 276468            |
| av       | 0.30    | 0.63747           | 430465            | 1.00    | 0.74478           | 115081            |

# Related Work

- Driden, R. (2009), [Using Lexical Statistics to Improve HPSG
Parsing](http://www.dridan.com/research/papers/dridan-phdthesis.pdf),
PhD Thesis, Saarland University
- Ninomiya, T., Matsuzaki, T., Miyao, Y., Tsuruoka, Y and Tsujii, J.
(2010). HPSG Parsing with a Supertagger. In Bunt, H., Merlo, P., and
Nivre, J. (Eds.): [Trends in Parsing Technology: Dependency Parsing,
Domain Adaptation, and Deep
Parsing](http://www.springerlink.com/content/978-90-481-9351-6).
Springer, pp. 243-256.

Last update: 2011-11-08 by JonathonRead [[edit](https://github.com/delph-in/docs/wiki/WeSearch_LexicalFiltering/_edit)]{% endraw %}