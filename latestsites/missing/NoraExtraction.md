{% raw %}# Overview

Many packages exist for text extraction from PDF, some based on OCR-like
techniques (primarily for scanned documents), others working as limited
PDF interpreters, reading out a pure text stream from 'digitally born'
documents. One of the more widely used packages appears to be Apache
[PDFBox](http://incubator.apache.org/pdfbox/), which we will evaluate as
our baseline—parallel to much ongoing work in the international ACL
community.

## Other tools

Until the PDF/UA standard is approved, we should assess and consider
other open-source tools, such as
[PDFtoHTML](http://pdftohtml.sourceforge.net/),
[Poppler](http://poppler.freedesktop.org/), and
[PDFMiner](http://www.unixuser.org/~euske/python/pdfminer/index.html).
For a smaller sample of NORA documents, it may also make sense to
contrastively look at non-open tools like [A-PDF Text
Extractor](http://a-pdf.com/text/index.htm) and Adobe Acrobat. Some of
these packages were briefly discussed at the 2009 DELPH-IN Summit;
please see the [discussion
notes]() for
details.

Summary of DELPH-IN's thoughts plus the ones of
[TobiasLanghoff](/TobiasLanghoff) (to be expanded):

- Free software:
  - [Apache PDFBox](http://incubator.apache.org/pdfbox/) - Java (can
retrieve layout information)
  - [PJX](http://www.etymon.com/epub.html) - Java (probably easy to
integrate with our code), GPL
  - [PDF Clown](http://sourceforge.net/projects/clown/) - Java, GPL
(doesn't support Unicode properly; plans to support hyphenation
in the future)
  - [Poppler](http://poppler.freedesktop.org/) - C, GPL (Francis's
favorite)
  - [PDFMiner](http://www.unixuser.org/~euske/python/pdfminer/index.html) -
Python (Mike's favorite: "Good unicode support. Turned out to be
useful to use font family for identifying consequent text blocks
and font sizes for identifying further logical text structure
(like headings, text body, captions, etc.)")
- Non-free:
  - [JPedal](http://java-source.net/open-source/pdf-libraries/jpedal) -
Java (GPL but expensive)
  - [A-PDF Text Extractor](http://a-pdf.com/text/index.htm)
(freeware)
  - Adobe Acrobat
  - <http://www.glyphandcog.com/XpdfText.html> Xpdf text is a C++
library that extracts plain text from PDF files. (source
licence)
- [List of
tools](http://desktoppub.about.com/od/pdfextractionsofware/PDF_Extraction_Software.htm)
- [Orbeon](http://www.orbeon.com/ops/doc/processors-pdf-extraction) is
an extractor that produces XML; could be nice either as a tool or as
a model for own possible structuring of the extracted text.

-- In order to easily integrate with our NORA Java API, we should
probably primarily concentrate on Java libraries. In addition, the
primary feature we need is probably good Unicode and font support; our
corpus is big and diverse.

PDF Clown looks fine, but its Unicode support isn't done (it doesn't
provide an explicit support to glyph-to-character mapping yet). Testing
it on (some of) our PDF files left something to be desired for that
reason. They plan to support hyphenation in the future, apparently, but
don't at the moment. PJX looks interesting, but it doesn't seem to be
actively maintained (last release 2006). It's not clear how actively
maintained Apache PDFBox is either (it's still incubating, after all),
but its font support is much more developed than PJX's (with its
[FontBox](/FontBox) package), which makes it a fair choice for us. We
should however plan to use PDFBox 0.7 soon, which is what's used in the
DFKI package.

# Report on the first scrapes

We have currently made two tools: A [TextGrabber](/TextGrabber) which
will setup PDFBox for extraction and start it. This method is *naive* in
the sense that no differentation is made on the pdfs and it does not do
any parameter setting.

We have also made an automated pipeline,
[DirTreeWalker](/DirTreeWalker), which uses our
[TextGrabber](/TextGrabber). It will extract all the pdfs in a given
directory and make textfiles in another. This is paralellized to make
use of more cores if they are available. This also do data gathering on
any errors encountered during scraping.

The source code and docs for these projects are available at
\~johanbev/wescience0/ on login.ifi. The files are readable for
everyone, but one could also do git clone \~johanbev/wescience0/ to get
just the src. Please contact johanbev or tobiasvl if you have trouble
setting up the build/run environment on your machine.

## Results of scrapes

We have deployed our stack on ps.titan. Everything is available at
\~johanbev/wescience0/TextGrabber, including all the different jars
(java libraries) we need to run pdfbox etc. We have also deployed java
1.6 to the same machine. Please observe how environment variables are
set up in run.sh which sits in this folder.

Currently a complete scrape takes about 45 minutes on ps.titan.
Resulting text resides at /logon/scratch/johanbev/raw-output/. We have
9129 files in /logon/scratch/nora/pdf, however not all of these are
PDFs; checking reveals that there are at least 120 of these files which
are not PDFs, but various other formats; see
NoraInspection for more details on these files. 17
files are also empty (0 bytes).

Of the actual pdfs only 15 fail completely to be extracted with our
current stack, and of those 15 one is encrypted.

Here is what file has to say about the files in our corpus:

          1 ASCII text
          9 Bio-Rad .PIC Image File 20517 x 17988, 12589 images in file
         17 empty
          5 HTML document text
          1 ISO-8859 English text
          2 ISO-8859 text, with CRLF line terminators
          1 LaTeX 2e document text
          1 Microsoft ASF
         67 Microsoft Office Document
          1 Minix filesystem (big endian),, 65059 zones
          2 OpenDocument Text
          2 PDF document, version 1.1
        400 PDF document, version 1.2
       1981 PDF document, version 1.3
       4985 PDF document, version 1.4
        793 PDF document, version 1.5
        833 PDF document, version 1.6
          2 PDF document, version 1.7
          1 PostScript document text conforming at level 3.0
          5 Rich Text Format data, version 1,
          4 Rich Text Format data, version 1, ANSI
          5 UTF-8 Unicode English text
          1 UTF-8 Unicode text
          4 Zip archive data, at least v1.0 to extract
          5 Zip archive data, at least v2.0 to extract

So our current stack can operate at 99.8% of the proper PDFs in our
corpus. However, this number does not reflect the *quality* of the
extracted text, which could be garbled in many different ways. We are
currently investigating various tools for automated checking extraction
quality, ref Johan's e-mail to the list.

Here is what file has to say about our extracts:

       6066 UTF-8 Unicode English text
       1632 UTF-8 Unicode text
        603 data
        323 ASCII text
        135 empty
         86 UTF-8 Unicode C program text
         82 UTF-8 Unicode Java program text
         47 UTF-8 Unicode C++ program text
         37 UTF-8 Unicode English text, with very long lines
         33 ASCII text, with very long lines
         19 UTF-8 Unicode text, with very long lines
         16 ASCII English text
         14 UTF-8 Unicode mail text
          4 MED_Song
          4 character Computer Graphics Metafile
          3 UTF-8 Unicode news text
          3 UTF-8 Unicode English text, with CRLF, CR, LF line terminators
          2 UTF-8 Unicode English text, with CR, LF line terminators
          2 UTF-8 Unicode C++ program text, with very long lines
          2 PC bitmap data
          2 binary Computer Graphics Metafile
          2 ASCII English text, with very long lines
          1 UTF-8 Unicode text, with CRLF, CR, LF line terminators
          1 StuffIt Deluxe Segment (data)
          1 Squish message area data file (12611 messages)
          1 Macintosh Application (data)
          1 'diff' output text
          1 bzip compressed data, version
          1 Bio-Rad .PIC Image File 12594 x 8245, 17930 images in file
          1 ASCII C++ program text, with very long lines
          1 Apple Old Partition data block size

Most probably files that have been classified as text (minus those with
long lines) are reasonable. Everything else is dubious. Those classified
as English are probably of usable quality. We should do spot checking on
these. My guess is that there still could be blocks of gibberish in
those.

## List of produced files

These files might have interest to others:

- /logon/johanbev/wescience0/ (on ps)
  
  - TextGrabber/ - The currently deployed version of our grabber.
  - report1/ - Metadata and breakdowns of results
    
    - errors.log - Complete log of all 135 files which failed
extraction for any reason.
    - extracted.out - Result of running file on all the extracted
texts.
    - extracted.uniq - Breakdown of that result.
    - non-pdfs.txt - Breakdown of files in our corpus which are
not PDFs.
    - empty\_pdfs.txt - PDF files in our corpus that are empty (0
bytes).
    - files\_with\_errors.txt - Exception stacks on all the
remaining 15 files.
    - pdfs.out - Result of running file on all pdfs on the corpus.
    - pdfs.uniq - Breakdown of that result.
    - suspicious.out - Result on running file on *suspicious*
files.
- \~johanbev/wescience0/ (on login.ifi) - Root of my current projdir
and git repo.
  
  - TextGrabber/ Working set of our grabber.
- /logon/tobiasvl/ligature.txt - Example lines of missing ligatures

# TextGrabber Pipeline Stages

- Depager

Depager removes page-numbers around the page-break-metatag <span
title="Cannot load macro p">&lt;&lt;p&gt;&gt;</span>, which had not yet
been taken up by Debox, ie same font-size.

- Deboxer

This stage adds meta-tags for all boxes in the document, with position
and font size information. It then strips away the tags, but adds to the
XML structure those boxes where the font size changes, in an attempt to
recognize titles, footnotes, and other non-body text.

- Deligature

(WRITE DESCRIPTION)

- Dehyphenation

(WRITE DESCRIPTION)

- Detect language

This language detection stage adds XML tags where each page in the PDF
document is assigned a languge tag, and the confidence score for this
laguage tag. This score is currently derived for the Google Language
API, but this may be changed later.

The confidence score, together with the language can e.g. be used to
decide if the page contains real text, or just gibbrish. If the Language
Detection comes up with a language which is unlikly to occur, and with a
very low confidence score, we can choose to not feed this page to
Lucene.

Example:

&lt;page number="320" lang="en" conf="0.787"&gt; Online edition (c) 2009
Cambridge UP 296 14 Vector space classification ... &lt;/page&gt;

- Repair Windows 1252

This stage remaps the Windows-1252 utf-8 codepoints (just square-glyphs)
to the proper UTF-8 codepoints. They were probably originally included
by mistaking Windows-1252 for ISO-8859-1(5).

Last update: 2021-06-03 by Olga Zamaraeva [[edit](https://github.com/delph-in/docs/wiki/NoraExtraction/_edit)]{% endraw %}