{% raw %}# Overview

In order to select the most effective method of text extract and
parameterize text correction, it is relevant to distinguish the various
ways in which the PDF documents in the NORA collection were produced,
e.g. use of LaTeX, vs. M$ Word, vs. other word processing tools. In the
LaTeX world, for example, it may matter which specific approach was used
to output PDF, e.g. latex plus dvips plus ps2pdf, vs. pdflatex, vs.
integrated tools like MiKTeX. Likewise, when using Word, results may
vary according to which specific software version was used, or depending
on whether Adobe Distiller or another tool for PDF creation was applied.
When it comes to font choices and character encodings, it might also
turn out that more basic properties of the original environment used for
PDF creation are relevant, e.g. the choice of operating system (Linux
vs. Windows, say) and default locale settings.

Presumably many dozens or hundreds of distinct software environments
were at play in the production of the NORA PDF files, and hopefully most
of this variation will be irrelevant for the WeScience<sub>0</sub>
effort. Furthermore, only quite limited information about the original
environment is recorded in the PDF files, hence it may at times be
impossible to give exact answers to the dimensions of variation listed
above. However, we need to find out what information about the
production process actually *is* available in PDF files, and we will
need a simple tool to inspect PDF meta information and extract relevant
parameters. It is possible that some of the text extraction tools for
PDF (see the [NoraExtraction](https://blog.inductorsoftware.com/docsproto/missing/NoraExtraction) page) can be put to use in
this task too.

# Preliminary Notes

A report on observations in the extraction of PDF documents can be
downloaded here:
<http://folk.uio.no/gisley/wescience0/ola-duokonvnot1.pdf>

# Metadata Survey

"Producer/Creator" fields from circa 3056 documents:
<http://heim.ifi.uio.no/olasba/nora/metadata-sort1.txt>

grep -i word metadata-sort1.txt \| wc -l  yields 1784 entries where Word
was involved in some way. The occurrences of "tex" work out to 259,
"ghostscript" to 557.

A rough survey of this metadata was not obviously helpful. There's a
great variety of different versions, and significant differences just
among, e.g., the four documents produced with MiKTeX -- the great
versatility of TeX may actually work against us, and the large
percentage of documents from Word may actually make things easier.

# Pathological Documents

Documents that are impaired or unreadable due to unconventional font
encoding:

- [67495](http://www.duo.uio.no/sok/work.html?WORKID=67495)
(Svendsen 2007) - GPL Ghostscript 8.54 (very curious gibberish,
mixing two styles)
- [70059](http://www.duo.uio.no/sok/work.html?WORKID=70059)
(Bendiksen 2008) - TeX, AFPL Ghostscript 6.50
- [78191](http://www.duo.uio.no/sok/work.html?WORKID=78191)
(Ulvestad 2008) - GPL Ghostscript SVN PRE-RELEASE 8.61
- [78892](http://www.duo.uio.no/sok/work.html?WORKID=78892)
(Hanssen 2008) - (Unknown), AFPL Ghostscript 8.51
- [86557](http://www.duo.uio.no/sok/work.html?WORKID=86557)
(Brændshøi 2008) - TeX, pdfTeX-1.40.3

Ghostscript documents which only feature unconverted glyphs on their
front pages:

- [65770](http://www.duo.uio.no/sok/work.html?WORKID=65770)
(Thoresen 2007) - "x1x14x2x24x14x9x5x11x26x27x13x14x2x4x2x8"
- [74555](http://www.duo.uio.no/sok/work.html?WORKID=74555) (Furuheim
& Aasen 2008) - "x27x18x24x19x24x25x17x28x10
x22x24x21x19x26x10x24x21"
- [79895](http://www.duo.uio.no/sok/work.html?WORKID=79895)
(Pedersen 2008) - "D4CPCRCZCTD8 CPD2CPD0DDDECTD6 [D3D2](/D3D2) CPD2"
- [61749](http://www.duo.uio.no/sok/work.html?WORKID=61749)
(Johansen 2007) - Actual control characters. PScript5.dll Version
5.2.2, GNU Ghostscript 7.06

In all these cases, other documents with an identical Creator field did
not suffer similar problems.

Spacing issues:

- [88173](http://www.duo.uio.no/sok/work.html?WORKID=88173)
(Lungo 2008) - Every space is replaced by the string "g561". The
producer is Acrobat Distiller 8.1.0.
- [79764](http://www.duo.uio.no/sok/work.html?WORKID=79764)
(Berg 2008) - Newline appears after most characters, resulting in an
extremely vertical document.

Blank/unconverted documents:

- [79631](http://www.duo.uio.no/sok/work.html?WORKID=79631)
(Huse 2008) - TeX, GPL Ghostscript SVN PRE-RELEASE 8.61
- [82351](http://www.duo.uio.no/sok/work.html?WORKID=82351)
(blomskold?) - LaTeX with hyperref package, pdfTeX-1.40.3

For a more comprehensive list, observe the last screenfuls of
ls -lS /logon/scratch/johanbev/raw-output/  

# Breakdown of naive scrape 17/9

Not looking too bad. Of our \~9000 pdfs, only 205 *failed* to be
extracted. Here *fail* means our current pipeline had to exit with an
error for some reason. There is still many files with a lot of
extraction artifacts.

## Table of errors encountered

|         |                               |
|---------|-------------------------------|
| **Num** | **Error**                     |
| 72      | [BouncyCastle](/BouncyCastle) |
| 12      | No versioninfo                |
| 111     | WrappedIO                     |
| 10      | Misc                          |

The [BouncyCastle](/BouncyCastle) error is caused by a missing jar-file
which is related to encryption. This jar could probably be integrated
before next scrape.

WrappedIO looks like problems with non-conforming pdfs. Much more on
this on next scrape.

There are still some number of misc. errors most with either zipping or
encodings.

**Results are available at /logon/scratch/johanbev/raw-output with log
at /logon/scratch/johanbev/errors.log**

## Non-PDF files in the corpus

The 111 errors above are not surprising considering
grep -iv '\\.pdf$' links.txt  reveals 103 files did not originally have
a .pdf extension. (Full listing in
<http://heim.ifi.uio.no/olasba/nora/non-pdfs.txt>) These break down as
follows:

|        |     |       |     |
|--------|-----|-------|-----|
| .zip   | 8   | .html | 5   |
| .doc   | 65  | .htm  | 1   |
| .docm  | 1   | .tex  | 3   |
| .rtf   | 8   | .ps   | 1   |
| .odt   | 2   | .wmv  | 1   |
| (none) | 8   |       |     |

A quick comparison of grep -v bouncycastle errors.log with non-pdfs
indicates that these are largely the very files that cause
WrappedIOException.

(HTML files sometimes cause versioninfo errors, sometimes
WrappedIOException.)

The only non-.pdf files that do not come out with a filesize of 0 are
18821, 16425, 15446, 16511, 1250, 8995, 10685 — these are seven out of
the eight files that did not originally have any extension. The eighth,
22431, is apparently a Word document.

# Breakdown of new scrape 21/9

*more to follow*

We now have a paralellized scraper which speed thins up quite a bit
(8x). There are now 135 failed documents. Considering 103 of these
actually are not PDFs this is not bad at all.
[BouncyCastle](/BouncyCastle) is now integrated into our stack so we can
decrypt the 72 encrypted pdfs from our 17/9 scrape. 71 of those did
decyrpt with the empty key "", ie. only one was properly encrypted. We
now need to decide if we are entitled to decrypt documents (even with
the empty key).

There are still 32 pdfs which failed to extract. PDFBox was able to
extract metadata from 8 of these files. A detailed file of this will be
made available at \~johanbev/wescience0/metadata-scrape2.txt .

**These 40 files are suspicious and should be further investigated**

These files generated errors, and are not present in Olas not-a-pdf
list, \~johanbev/wescience0/suspicious. On a quick glance , most of
these look like nonconforming pdfs.

# Detecting scanned-in documents

Using a build of pdfBox that has been instructed to signal pagebreaks
with form feed characters, it's possible to mark documents likely to
have been scanned in (without copyable text) simply by looking for
documents that are empty beyond the first page. These are listed in
<http://heim.ifi.uio.no/olasba/nora/scannd-empty.log> — 329 files are
identified, with no false positives.

Additionally, documents can be heuristically identified depending on how
many short lines (&lt;20 bytes) they contain; listings follow of
documents with more than
[70%](http://heim.ifi.uio.no/olasba/nora/scannd-0.7.log),
[60%](http://heim.ifi.uio.no/olasba/nora/scannd-0.6.log) and
[50%](http://heim.ifi.uio.no/olasba/nora/scannd-0.5.log) short lines.

Source code in /logon/olasba/bin/detectscannd03.pl .

# Ligature errors

Some documents have font encoding errors that result in ligatures
(combined ff, fi, etc) not being parsed. 19 example files can be found
in /logon/tobiasvl/ligature\_pdfs.txt - these files all have "ffi"
ligatures missing (the lines themselves can be found in
/logon/tobiasvl/ligature.txt), and have been found by grepping for
"ecient", the word "efficient" without the ligature gone.

Most of these files have explicit glyph problems (with the error message
"Bad bounding box in Type 3 glyph"). The cause for this is unknown, and
the DFKI code has the same problem.

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/NoraInspection/_edit)]{% endraw %}