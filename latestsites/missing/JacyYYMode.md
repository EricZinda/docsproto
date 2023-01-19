{% raw %}# Segmenting and Tagging Japanese

You can run Japanese through a script, to get segmented tagged input,
which is then used by the parser to help deal with unknown words.

Contents

1. [Segmenting and Tagging Japanese](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
   1. [jpn2yy.py](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
      1. [YY Mode with ACE](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
   2. [Install](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
      1. [mecab binary](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
      2. [mecab python wrapper](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)
      3. [test](https://blog.inductorsoftware.com/docsproto/missing/JacyYYMode)

## jpn2yy.py

You can run this script (under jacy/utils) independently, using the
following pipeline.

    $ echo "グッドマンが寝る。" | python utils/jpn2yy.py 
    (0, 0, 1, <0:5>, 1, "グッドマン", 0, "null", "名詞-固有名詞-組織:n-n" 1.0)(1, 1, 2, <5:6>, 1, "が", 0, "null", "助詞-格助詞-一般:n-n" 1.0)(2, 2, 3, <6:8>, 1, "寝る", 0, "null", "動詞-自立:一段-基本形" 1.0)

This YY code can be used as the input of ACE. Note that ACE uses the -y
option for invoking the YY mode.

    $ ace -g ace/config.tdl -G jacy.dat
    $ echo "グッドマンが寝る。" | python utils/jpn2yy.py | ace -g jacy.dat -y1Tf 2>/dev/null
    SENT: (yy mode)
    [ LTOP: h0
    INDEX: e2 [ e TENSE: pres MOOD: indicative PROG: - PERF: - ASPECT: default_aspect PASS: - SF: prop ]
    RELS: < [ def_q_rel<0:5> LBL: h4 ARG0: x3 RSTR: h5 BODY: h6 ]
     [ named_rel<0:5> LBL: h7 CARG: "グッドマン" ARG0: x3 ]
     [ "_neru_v_rel"<6:8> LBL: h1 ARG0: e2 ARG1: x3 ] >
    HCONS: < h0 qeq h1 h5 qeq h7 >
    ICONS: < e2 non-topic x3 > ]

### YY Mode with ACE

We can run jpn2yy.py with ACE and ART. In that case, the pipeline should
be carefully described. The following is a sample
(<http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python/7608205>).

    if __name__ == '__main__':
        import sys
        while True:
            line = ""
            try:
                line = sys.stdin.readline()
            except (KeyboardInterrupt, IOError):
                break
            if not line: break
            print line.strip()
            sys.stdout.flush()

Now, you can run the ART and ACE with the YY mode.

    $ mkprof -s /path/to/skeleton /path/to/profile-to-write
    $ art -Ya "python utils/jpn2yy.py | ace -g jacy.dat -y" /path/to/profile-to-write

## Install

In order to use the YY mode as the input pipeline of Jacy, three items
need to be installed on your machine; viz. (1) mecab, (2) mecab
dictionary, and (3) mecab python wrapper.

For ubuntu

    sudo apt-get install python-mecab
    sudo apt-get install mecab-ipadic-utf8

### mecab binary

From source:

    wget https://mecab.googlecode.com/files/mecab-0.996.tar.gz
    tar xvf mecab-0.996.tar.gz 
    mv mecab-0.996 mecab
    cd mecab
    ./configure 
    sudo make
    sudo make check
    sudo make install

=== mecab dictionary == =

    wget https://mecab.googlecode.com/files/mecab-ipadic-2.7.0-20070801.tar.gz
    tar xvf mecab-ipadic-2.7.0-20070801.tar.gz 
    mv mecab-ipadic-2.7.0-20070801 mecab-ipadic
    cd mecab-ipadic
    ./configure --with-charset=utf8
    make
    make install

### mecab python wrapper

    wget https://mecab.googlecode.com/files/mecab-python-0.996.tar.gz
    tar xvf mecab-python-0.996.tar.gz 
    mv mecab-python-0.996 mecab-python
    cd mecab-python
    sudo python setup.py build
    sudo python setup.py install

### test

    >>> import MeCab
    >>> m = MeCab.Tagger('-Ochasen')
    >>> print m.parse('私は昨日、引っ越ししました。')

Last update: 2016-11-05 by FrancisBond [[edit](https://github.com/delph-in/docs/wiki/JacyYYMode/_edit)]{% endraw %}