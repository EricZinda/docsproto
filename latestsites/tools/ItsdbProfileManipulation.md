{% raw %}# Page Status

This page presents user-supplied information, hence may be inaccurate in
some details, or not necessarily reflect use patterns anticipated by the
[\[incr tsdb()\]](http://www.delph-in.net/itsdb) developers. This page
was initiated by [FrancisBond](https://blog.inductorsoftware.com/docsproto/summits/FrancisBond); please feel free to make
additions or corrections as you see fit. However, before revising this
page, one should be reasonably confident of the information given being
correct.

# Compressing a Test Suite

The **File\|Compress** menu compresses a profile by gzipping the files
that contain the data (i.e. all files with non-zero size except
**relations**). After being compressed [\[incr
tsdb()\]](http://www.delph-in.net/itsdb) treats the data as read-only:
you can still browse , analyse and compare, but cannot reparse or
treebank. The status is set to **ro** (read-only). There is no way to
undo this from inside [\[incr tsdb()\]](http://www.delph-in.net/itsdb).
If you wish to decompress then you must ungzip the files externally.

A quick way of compressing a profile in this way using a shell is
(assuming you are in the profile):

     find . -size +0 -type f -not -name 'relations' -exec gzip {} \;
<update date omitted for speed>{% endraw %}