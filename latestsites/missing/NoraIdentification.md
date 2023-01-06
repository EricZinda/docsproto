{% raw %}# Overview

Language classification

## Status

### 13 Oct

A quick experiment with
[Lingua::Identify](http://search.cpan.org/~ambs/Lingua-Identify-0.23/lib/Lingua/Identify.pm)
yielded promising results with little effort. Most documents were
classified as either English or Norwegian, which was as expected; text
files containing gibberish tended to be assigned random languages such
as Afrikaans or Somali. The most potential for error seem to be in the
files classified as French and Swedish.

The full results are in
<http://heim.ifi.uio.no/olasba/nora/noralang.log> (or
\~olasba/noralang.log on ps). Note that the "confidence score" is
relative to the other possible languages; a high score doesn't
necessarily mean it's not gibberish, as described in
<http://search.cpan.org/~ambs/Lingua-Identify-0.23/lib/Lingua/Identify.pm#confidence>.

This list has been used to categorize my working copy of the converted
text in /logon/scratch/olasba/nora0908/logon/scratch/nora/pdf/

#### Details

The biggest problem with Lingua::Identify was a large percentage of
Norwegian texts getting misclassified as Turkish; this was rectified by
eliminating 'tr' as a possible language:

Lingua::Identify::deactivate\_language('tr');

The most accurate methods for separating Norwegian from English seemed
to be 4-grams (strictly speaking, 4-graphs) and stopwords.

my @guess = langof({method=&gt;{smallwords=&gt;0.8, ngrams4=&gt;1.2}}, $text);

Sourcecode is in
<http://heim.ifi.uio.no/olasba/nora/identifylang03.pl.txt>

- <sup>—Ola</sup>

### Misclassifications

\#10743 ([Krog 2006](http://www.duo.uio.no/sok/work.html?WORKID=46068))
- Misfiled under English (contains a large percentage of quotes and loan
words)
<update date omitted for speed>{% endraw %}