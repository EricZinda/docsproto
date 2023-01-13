{% raw %}**NB:** The content of this page refers to the [MoinMoin](http://moin.delph-in.net/) markup language.
For GitHub markdown language used here, see e.g.: [Mastering markdown](https://guides.github.com/features/mastering-markdown/).    

# Original page begins below:

    #pragma section-numbers off
    #acl All:admin,read,write,delete,revert
    ##language:en

This page tries to use each supported markup element at least once.

    '''Index'''
    [[TableOfContents(2)]]

**Index**

Contents

1. [Headers](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
   1. [Header 2](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
2. [Font styles](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
   1. [Syntax Hilighting](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
3. [Smileys](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
4. [Hyperlinks](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
   1. [Internal](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
   2. [External](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
   3. [Escaping WikiNames](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
5. [Blockquote](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
6. [Bullet list](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
7. [Numbered list](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
8. [Descriptions + Definitions](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
9. [Code display](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
10. [Tables](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    1. [General table layout and HTML like
options](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    2. [Cell width](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    3. [Spanning rows and columns](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    4. [Alignment](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    5. [Colors](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
    6. [CSV Tables](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
11. [Rules](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)
12. [Macros](https://blog.inductorsoftware.com/docsproto/missing/SyntaxReference)

# Headers

## Header 2

### Header 3

#### Header 4

##### Header 5

# Font styles

    Normal text, ''emphasized'', '''strong''', __underline__, ,,subscript,,, ^superscript^, `typewriter` and {{{typewriter

.}}}

Normal text, *emphasized*, **strong**, <span class="u">underline</span>,
<sub>subscript</sub>, <sup>superscript</sup>, typewriter and typewriter.

## Syntax Hilighting

- ```
     1 # python code
     2 print code.colorize("abc", 1 + 1)
  ```

# Smileys

|            |                      |     |            |                           |     |            |                      |     |            |                 |
|------------|----------------------|-----|------------|---------------------------|-----|------------|----------------------|-----|------------|-----------------|
| **Markup** | **Display**          |     | **Markup** | **Display**               |     | **Markup** | **Display**          |     | **Markup** | **Display**     |
| X-(        | :rage:               |     | :D         | :grin:                    |     | &lt;:(     | :mask:               |     | :o         | :anguished:     |
| :(         | :confused:           |     | :)         | :slightly\_smiling\_face: |     | B\)        | :sunglasses:         |     | :))        | :rofl:          |
| ;)         | :wink:               |     | /!\\       | :warning:                 |     | &lt;!&gt;  | :warning:            |     | (!)        | :bulb:          |
| :-?        | :stuck\_out\_tongue: |     | :\\        | :confounded:              |     | &gt;:&gt;  | :imp:                |     | \|)        | :monocle\_face: |
| :-(        | :frowning\_face:     |     | :-)        | :smiley:                  |     | B-)        | :nerd\_face:         |     | :-))       | :rofl:          |
| ;-)        | :wink:               |     | \|-)       | :pensive:                 |     | (./)       | :white\_check\_mark: |     | {OK}       | :ok:            |
| {X}        | :x:                  |     | {i}        | :information\_source:     |     | {1}        | :one:                |     | {2}        | :two:           |
| {3}        | :three:              |     | {\*}       | :star:                    |     | {o}        | :star:               |     |            |                 |

# Hyperlinks

## Internal

     * MoinMoin
     * MoinMoin/TextFormatting
     * MoinMoin/InstallDocs 
     * ../InstallDocs 
     * /SubPage
     * Self:InterWiki

- MoinMoin
- MoinMoin/TextFormatting
- MoinMoin/InstallDocs
- [../InstallDocs](/InstallDocs)
- [/SubPage](/SyntaxReference/SubPage)
- InterWiki

<!-- -->


    [#anchorname Anchor Link]

[Anchor Link](/SyntaxReference#anchorname)

## External

     * http://moin.sourceforge.net/
     * [http://moin.sourceforge.net/]
     * [http://moin.sourceforge.net/ MoinMoin Sourceforge Homepage]
     * [^http://moin.sourceforge.net/ MoinMoin Sourceforge Homepage - in new window]
     * [http://moin.sourceforge.net/moinmoin.gif]
     * http://moin.sourceforge.net/moinmoin.gif
     * [http://moin.sourceforge.net/moinmoin.gif moinmoin.gif]
     * MeatBall:InterWiki
     * wiki:MeatBall/InterWiki
     * [wiki:MeatBall/InterWiki]
     * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]
     * [file://servername/full/path/to/file/filename%20with%20spaces.txt Click here to read filename with spaces.txt]
     * jh@web.de

- <http://moin.sourceforge.net/>
- <http://moin.sourceforge.net/>
- [MoinMoin Sourceforge Homepage](http://moin.sourceforge.net/)
- \[^<http://moin.sourceforge.net/> MoinMoin Sourceforge
Homepage - in new window\]
- <http://moin.sourceforge.net/moinmoin.gif>
- <img src="http://moin.sourceforge.net/moinmoin.gif" title="http://moin.sourceforge.net/moinmoin.gif" class="external_image" alt="http://moin.sourceforge.net/moinmoin.gif" />

- [moinmoin.gif](http://moin.sourceforge.net/moinmoin.gif)
- [InterWiki](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")
- [InterWiki](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")
- [InterWiki](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")
- [InterWiki page on
MeatBall](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")
- [Click here to read filename with
spaces.txt](file://servername/full/path/to/file/filename%20with%20spaces.txt)
- <mailto:jh@web.de>

## Escaping WikiNames

    Wiki''''''Name
    Wiki``Name

WikiName WikiName

# Blockquote

     This is indented
      Even more

- This is indented
  - Even more

# Bullet list

     * item 1
    
     * item 2, with gap
     * item 3
       * item 3.1

- item 1
- item 2, with gap
- item 3
  - item 3.1

# Numbered list

     1. item 1
       i. item 1
       i. item 2

1. item 1
   1. item 1
   2. item 2

<!-- -->


     1. item 2
       a. item 1
       a. item 2

1. item 2
   1. item 1
   2. item 2

# Descriptions + Definitions

     Term:: Description
     Label:: Definition

Term\
Description

Label\
Definition

# Code display

- line 1
indented 4 characters

# Tables

## General table layout and HTML like options

     ||||||<tablewidth="80%">'''Heading'''||
     ||cell 1||cell2||cell 3||
     ||<rowspan=2> spanning rows||||<bgcolor='#E0E0FF'> spanning 2 columns||
     ||<rowbgcolor="#FFFFE0">cell2||cell 3||

- |               |                    |        |
|:-------------:|:------------------:|:------:|
|  **Heading**  |                    |        |
|    cell 1     |       cell2        | cell 3 |
| spanning rows | spanning 2 columns |        |
|               |       cell2        | cell 3 |

## Cell width

     || narrow ||<:99%> wide ||

- |        |      |
|--------|:----:|
| narrow | wide |

## Spanning rows and columns

     ||<|2> 2 rows || row 1 ||
     || row 2 ||
     ||<-2> row 3 over 2 columns ||

- |                      |       |
|:--------------------:|-------|
|        2 rows        | row 1 |
|                      | row 2 |
| row 3 over 2 columns |       |

## Alignment

     ||<(> left ||<^|3> top ||<v|3> bottom ||
     ||<:> centered ||
     ||<)> right ||

- |          |     |        |
|:---------|:---:|:------:|
| left     | top | bottom |
| centered |     |        |
| right    |     |        |

## Colors

     ||<#FF8080> red ||<#80FF80> green ||<#8080FF> blue ||

- |     |       |      |
|-----|-------|------|
| red | green | blue |

## CSV Tables

|          |          |          |
|----------|----------|----------|
| **Col1** | **Col3** | **Col4** |
| 1        | 3        | 4        |
| a        | c        | d        |

- |          |          |          |
|----------|----------|----------|
| **Col1** | **Col3** | **Col4** |
| 1        | 3        | 4        |
| a        | c        | d        |

# Rules

    --- (not a rule)
    ----
    -----
    ------
    -------
    --------
    ---------
    ----------
    -------------------------------------------- (not thicker than 10)

--- (not a rule)

* * *

* * *

* * *

* * *

* * *

* * *

* * *

* * *

(not thicker than 10)

# Macros

    [[Anchor(anchorname)]]
    '''[[PageCount]]''' pages
    [[RandomPage]]

**1267** pages [JacyInstallation](https://blog.inductorsoftware.com/docsproto/grammars/JacyInstallation)

Last update: 2021-06-07 by Olga Zamaraeva [[edit](https://github.com/delph-in/docs/wiki/SyntaxReference/_edit)]{% endraw %}