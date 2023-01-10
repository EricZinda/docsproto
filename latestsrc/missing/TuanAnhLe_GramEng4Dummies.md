{% raw %}# Grammar Engineering for Dummies

Don't know where to start? Try to start here!

**\[This page is only a draft\]**

## Installation

Setup development environment can be a tricky tasks. Here are a few
useful pages:

- Install Emacs\
For Fedora (Redhat, etc.)  
  
      yum install emacs
  
  For Ubuntu (Debian, Mint, Pinguy, etc.)  
  
      sudo apt-get install emacs
- [Install Logon](https://blog.inductorsoftware.com/docsproto/tools/LogonInstallation) (you will have everything you
need to develop a grammar). If you use Fedora, read this guide
[LogonFedora](https://blog.inductorsoftware.com/docsproto/missing/LogonFedora).
- Start Emacs and try to run logon by pressing \[ESC\] then \[x\] then
type "logon" then hit \[ENTER\]
- Some useful keyboard shortcut for [Emacs/LKB](https://blog.inductorsoftware.com/docsproto/tools/LkbMode)

## The Matrix

Yay, I love this series!!! Oops, just kiddin'. The Matrix is a tool for
generating a toy grammar so you can play with it quickly.

<http://www.delph-in.net/matrix/customize/matrix.cgi>

## Make use of your grammars

If you want to use your grammar in production, you should use ACE. See
[this page](https://blog.inductorsoftware.com/docsproto/tools/AceTop) for everything about ACE. Basically what you want is
to download a copy of ACE from
[here](http://sweaglesw.org/linguistics/ace/), and then see [this
page](https://blog.inductorsoftware.com/docsproto/tools/AceUse) to know how to use it. A version of ACE (may be older) is
included with logon under the name answer and can be found at
\~/logon/bin/answer.

### Compile your grammar with ACE

For example, you want to compile my grammar
[VIRGO](https://github.com/letuananh/virgo), and you have it in the
**workspace** folder under your **home folder** (**\~/workspace/virgo**)
you can try:

    cd ~/workspace/virgo
    ace -g ace/config.tdl -G virgo.dat

NOTE: change virgo.dat to any name you want. Make sure you have a <span
class="u">*lowercase g*</span> for the first argument and *<span
class="u">uppercase G</span>* for the second argument. They are <span
class="u">**NOT**</span> interchangable.

To parse a sentence, use this:

    echo "chim bay." | ace -g virgo.dat -1Tf

### Write HPSG papers with LaTeX

Start ace with LUI mode:

    ace -g erg.dat -l

Click on any tree to open a bigger tree view and then press l (L)
button. The tree LaTeX code will be written into /tmp/ folder. This
method works for MRS diagrams as well. LUI mode can be used to debug
grammars as well. For example after LUI is started, :l bay can be used
to display lexical information of the intransitive verb "bay". More
information can be found in the page [AceLui](https://blog.inductorsoftware.com/docsproto/tools/AceLui)
<update date omitted for speed>{% endraw %}