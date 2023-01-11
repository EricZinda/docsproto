{% raw %}# Spanish Resource Grammar

## General information
Montserrat Marimon developed the Spanish Resource Grammar (see References).

## Setting up SRG
0. For now: Linux only, due to the FreeLing dependency, which is tricky to set up for a Mac OS.
1. Check out a copy of SRG from github: https://github.com/delph-in/srg. (Note: Do not use the older SVN copy because that would require extra steps.)
2. Install [freeling](https://nlp.lsi.upc.edu/freeling/index.php/node/30), picking the correct deb package for your ubuntu version. For example, for Ubuntu 20, pick freeling-4.2-focal-amd64.deb . 
3. To check the Freeling is working: try typing something like `analyze -f es.cfg` and then type in a Spanish sentence, like `El gato duerme`. You should see something like:

```
el gato duerme.
el el DA0MS0 1
gato gato NCMS000 1
duerme dormir VMIP3S0 0.989241
. . Fp 1
```
4. There is a script, under `util/`, which maps tags from Freeling with rules in the SRG using [YY input mode](https://github.com/delph-in/docs/wiki/PetInput#yy-input-mode). See intended usage in `util/srg-yy.sh`
5. Make sure you have a recent version of [ACE](https://github.com/delph-in/docs/wiki/AceInstall) installed.
6. [Compile](https://github.com/delph-in/docs/wiki/AceUse#compiling-the-grammar) the grammar using ACE.
7. Run the script with the sample sentence file, making sure the `srg-yy.sh` script has the correct path to the ACE-compiled grammar. Note: You may want to create your own copy of the script (e.g. `my-srg-yy.sh`); do not then check it into the repository.
8. Without the script, to try parsing one specific sample sentence directly (simply as an example), start ACE: `ace -g srg.dat -1Tf -y --yy-rules` and try the following input:

```
(42, 0, 1, <0:2>, 1, "mi" "mi", 0, "dp1css") (43, 1, 2, <4:8>, 1, "perro" "perro", 0, "ncms000") (44, 2, 3, <9:15>, 1, "dormir" "duerme", 0, "vmip3s0")
```

9. To use the graphical interface for the output, [install LUI](https://github.com/delph-in/docs/wiki/AceLui) and use the flag sequence -1Tlf instead of -1Tf in step 8 above. Right now, there is no way of using the LUI interface with the `srg-yy.sh` script.

## References
[Marimon 2010. The Spanish Resource Grammar.](https://aclanthology.org/L10-1411/)

[Marimon 2013. The Spanish DELPH-IN Grammar.](https://link.springer.com/article/10.1007/s10579-012-9199-7)

Last update: 2022-07-27 by Olga Zamaraeva [[edit](https://github.com/delph-in/docs/wiki/SrgTop/_edit)]{% endraw %}