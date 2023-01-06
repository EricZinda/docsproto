{% raw %}# Overview

## Font encodings

### Identity-H

Documents with a font encoding of 'Identity-H' would seem to warrant
special attention. This encoding usually indicates a particular kind of
mix-and-match of characters, resulting in problems such as regular
hyphens being rendered with the Unicode U+00AD 'soft hyphen'.

This affects 54 files in our current corpus. It would seem to be related
to the "CID" encoding mentioned below; see also
<http://indesignsecrets.com/cid-identity-h-fonts-are-back.php>

## Detecting gibberish

On many stretches of text where pdfBox is unable to map glyphs to
normative code points, it instead numbers the glyphs and outputs them in
the form "g81g72g81g3g82g80g3g76g81g86g87" etc. The letter may be g, a,
x etc. It may also come out as strings like 'glyph', 'afii' (in
connection with Arabic glyphs) or 'cid' (seen only in documents made on
a Mac).

Most of these unmapped glyphs can be found with the regex
\\d((\[A-Za-z\]+)\\d+){3}  — this matches runs of three of characters
and digits right next to each other. A high proportion of text on this
form indicates that the document is mostly unreadable (or entirely
concerned with chemical reactions; some false positives like this are to
be expected).

Classification of documents, sorted by score:
<http://heim.ifi.uio.no/olasba/nora/anonglyphs06.log>

(The middle column is the string or letter that most frequently marks
out the unmapped glyphs.)

Source code: <http://heim.ifi.uio.no/olasba/nora/findanonglyph06.pl.txt>

- <sup>—Ola, 13 Oct</sup>
<update date omitted for speed>{% endraw %}