{% raw %}You can run INDRA using Answer Constraint Engine (ACE) (see
[AceTop](https://blog.inductorsoftware.com/docsproto/tools/AceTop)).

INDRA can be compiled using the following command.

    $ ace -g ace/config.tdl -G ind.dat

When parsing sentences, the Linguistic User Interface (LUI) can be
invoked by using an option -l (see [AceOptions](https://blog.inductorsoftware.com/docsproto/tools/AceOptions) and
[LkbLui](https://blog.inductorsoftware.com/docsproto/tools/LkbLui)).

    $ ace -g ind.dat -l

You can use the YY mode for your input of parsing.

Option -T is used to show MRSes and option -f to format each EP on its
own line when printing MRSes. For example, to see the MRSes for *anjing
menggonggong* "dogs bark":

    $ echo "anjing menggonggong" | ace -g ind.dat -Tf

Option -e is used to generate all possible sentences from the MRSes.

    $ echo "anjing menggonggong" | ace -g ind.dat -Tf | ace -g ind.dat -e
<update date omitted for speed>{% endraw %}