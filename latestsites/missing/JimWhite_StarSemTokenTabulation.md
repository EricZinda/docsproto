{% raw %}Count of tokens that don't match either \[letter\|hyphen\]+ or digit+.

The main issue is that single quote is not handled at all consistently.
Words that have either a contraction or possessive-s appear in some
cases as a single token and in others as two tokens.

Other problems include a quotation mark being stuck to the word
initially. Also a few other punctuation oddities like "hotel.-" and
"year'66".

Contents

1. wisteria1.txt (2012-02-20)
2. wisteria2.txt (2012-02-20)
3. SEM-2012-SharedTask-CD-SCO-dev.txt
4. SEM-2012-SharedTask-CD-SCO-training.txt

## wisteria1.txt (2012-02-20)

<table data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: center;">1.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria1 s0 : 1. The Singular Experience of Mr. John Scott Eccles</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Dr.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria1 s58 : `` You are like my friend , Dr. Watson , who has a bad habit of telling his stories wrong end foremost .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">J.P.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria1 s334 : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr. Hynes Hynes , J.P. , Purdley Place ; Mr. James Baker Williams , Forton Old Hall ; Mr. Henderson , High Gable ; Rev. Joshua Stone , Nether Walsling .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Rev.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria1 s334 : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr. Hynes Hynes , J.P. , Purdley Place ; Mr. James Baker Williams , Forton Old Hall ; Mr. Henderson , High Gable ; Rev. Joshua Stone , Nether Walsling .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">_very_</td>
<td style="text-align: right;">1</td>
<td><p>wisteria1 s254 : `` There were , '' said he , `` one or two _very_ remarkable things .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'m</td>
<td style="text-align: right;">2</td>
<td><p>wisteria1 s61 : `` I 'm sure it must look very bad , Mr. Holmes , and I am not aware that in my whole life such a thing has ever happened before .</p>
<p>wisteria1 s211 : `` I 'm bound to say that I make nothing of the note except that there was something on hand , and that a woman , as usual was at the bottom of it . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">:</td>
<td style="text-align: right;">2</td>
<td><p>wisteria1 s195 : It says :</p>
<p>wisteria1 s333 : The telegram was a list of names and addresses :</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Mrs.</td>
<td style="text-align: right;">2</td>
<td><p>wisteria1 s64 : There was a bustle outside , and Mrs. Hudson opened the door to usher in two robust and official-looking individuals , one of whom was well known to us as Inspector Gregson of Scotland Yard , an energetic , gallant , and , within his limitations , a capable officer .</p>
<p>wisteria1 s257 : `` You will show these gentlemen out , Mrs. Hudson , and kindly send the boy with this telegram .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">!</td>
<td style="text-align: right;">3</td>
<td><p>wisteria1 s84 : `` Good God !</p>
<p>wisteria1 s85 : This is awful !</p>
<p>wisteria1 s153 : The foreign host , the foreign footman , the foreign cook , all had vanished in the night !</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">n't</td>
<td style="text-align: right;">3</td>
<td><p>wisteria1 s86 : You do n't mean -- you do n't mean that I am suspected ? ''</p>
<p>wisteria1 s337 : `` I do n't quite understand . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">o'clock</td>
<td style="text-align: right;">5</td>
<td><p>wisteria1 s132 : He apologized for having disturbed me so late , saying that it was nearly one o'clock .</p>
<p>wisteria1 s243 : `` He had been there since one o'clock .</p>
<p>wisteria1 s300 : The attempt , whatever it may be , is to come off , we will say , before one o'clock .</p>
<p>wisteria1 s340 : It is equally certain that this house cannot be more than a mile or two from Oxshott , since Garcia was walking in that direction and hoped , according to my reading of the facts , to be back in Wisteria Lodge in time to avail himself of an alibi , which would only be valid up to one o'clock .</p>
<p>wisteria1 s343 : It was nearly six o'clock before we found ourselves in the pretty Surrey village of Esher , with Inspector Baynes as our companion .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">`</td>
<td style="text-align: right;">7</td>
<td><p>wisteria1 s6 : `` How do you define the word ` grotesque ' ? ''</p>
<p>wisteria1 s312 : ` Our own colours , green and white . '</p>
<p>wisteria1 s314 : ` Green open , white shut . '</p>
<p>wisteria1 s316 : ` Main stair , first corridor , seventh right , green baize . '</p>
<p>wisteria1 s320 : She would not have said ` Godspeed ' had it not been so .</p>
<p>wisteria1 s321 : ` D ' -- that should be a guide . ''</p>
<p>wisteria1 s323 : I suggest that ` D ' stands for Dolores , a common female name in Spain . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'</td>
<td style="text-align: right;">8</td>
<td><p>wisteria1 s6 : `` How do you define the word ` grotesque ' ? ''</p>
<p>wisteria1 s161 : I called at Allan Brothers ' , the chief land agents in the village , and found that it was from this firm that the villa had been rented .</p>
<p>wisteria1 s312 : ` Our own colours , green and white . '</p>
<p>wisteria1 s314 : ` Green open , white shut . '</p>
<p>wisteria1 s316 : ` Main stair , first corridor , seventh right , green baize . '</p>
<p>wisteria1 s320 : She would not have said ` Godspeed ' had it not been so .</p>
<p>wisteria1 s321 : ` D ' -- that should be a guide . ''</p>
<p>wisteria1 s323 : I suggest that ` D ' stands for Dolores , a common female name in Spain . ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">;</td>
<td style="text-align: right;">8</td>
<td><p>wisteria1 s9 : `` There is surely something more than that , '' said he ; `` some underlying suggestion of the tragic and the terrible .</p>
<p>wisteria1 s28 : Life is commonplace , the papers are sterile ; audacity and romance seem to have passed forever from the criminal world .</p>
<p>wisteria1 s298 : `` Exactly , my dear Watson ; he might have proved an alibi .</p>
<p>wisteria1 s334 : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr. Hynes Hynes , J.P. , Purdley Place ; Mr. James Baker Williams , Forton Old Hall ; Mr. Henderson , High Gable ; Rev. Joshua Stone , Nether Walsling .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'s</td>
<td style="text-align: right;">9</td>
<td><p>wisteria1 s56 : I went to the house agents , you know , and they said that Mr. Garcia 's rent was paid up all right and that everything was in order at Wisteria Lodge . ''</p>
<p>wisteria1 s87 : `` A letter of yours was found in the dead man 's pocket , and we know by it that you had planned to pass last night at his house . ''</p>
<p>wisteria1 s98 : With a dubious glance at the inspector 's notebook , he plunged at once into his extraordinary statement .</p>
<p>wisteria1 s187 : It 's my way .</p>
<p>wisteria1 s201 : `` It is a woman 's writing , done with a sharp-pointed pen , but the address is either done with another pen or by someone else .</p>
<p>wisteria1 s229 : It was the envelope of this letter which gave us the dead man 's name and address .</p>
<p>wisteria1 s264 : `` Well , taken with the disappearance of the man 's companions , I should say that they were in some way concerned in the murder and had fled from justice . ''</p>
<p>wisteria1 s299 : We will suppose , for argument 's sake , that the household of Wisteria Lodge are confederates in some design .</p>
<p>wisteria1 s329 : An answer had arrived to Holmes 's telegram before our Surrey officer had returned .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Mr.</td>
<td style="text-align: right;">34</td>
<td><p>wisteria1 s0 : 1. The Singular Experience of Mr. John Scott Eccles</p>
<p>wisteria1 s36 : `` I have had a most singular and unpleasant experience , Mr. Holmes , '' said he .</p>
<p>wisteria1 s41 : `` Pray sit down , Mr. Scott Eccles , '' said Holmes in a soothing voice .</p>
<p>wisteria1 s52 : `` You are right , Mr. Holmes .</p>
<p>wisteria1 s56 : I went to the house agents , you know , and they said that Mr. Garcia 's rent was paid up all right and that everything was in order at Wisteria Lodge . ''</p>
<p>wisteria1 s61 : `` I 'm sure it must look very bad , Mr. Holmes , and I am not aware that in my whole life such a thing has ever happened before .</p>
<p>wisteria1 s66 : `` We are hunting together , Mr. Holmes , and our trail lay in this direction . ''</p>
<p>wisteria1 s68 : `` Are you Mr. John Scott Eccles , of Popham House , Lee ? ''</p>
<p>wisteria1 s72 : `` Exactly , Mr. Holmes .</p>
<p>wisteria1 s76 : `` We wish a statement , Mr. Scott Eccles , as to the events which led up to the death last night of Mr. Aloysius Garcia , of Wisteria Lodge , near Esher . ''</p>
<p>wisteria1 s93 : `` And it is my duty to warn Mr. Scott Eccles that it may be used against him . ''</p>
<p>wisteria1 s94 : `` Mr. Eccles was going to tell us about it when you entered the room .</p>
<p>wisteria1 s170 : But now , Mr. Inspector , I understand , from what you said when you entered the room , that you can carry the story on , and that some tragedy had occurred .</p>
<p>wisteria1 s173 : `` I am sure of it , Mr. Scott Eccles -- I am sure of it , '' said Inspector Gregson in a very amiable tone .</p>
<p>wisteria1 s179 : `` What do you say to that , Mr. Baynes ? ''</p>
<p>wisteria1 s182 : `` It was a dog-grate , Mr. Holmes , and he overpitched it .</p>
<p>wisteria1 s186 : `` I did , Mr. Holmes .</p>
<p>wisteria1 s188 : Shall I read it , Mr. Gregson ? ''</p>
<p>wisteria1 s194 : It is addressed to Mr. Garcia , Wisteria Lodge .</p>
<p>wisteria1 s204 : `` I must compliment you , Mr. Baynes , upon your attention to detail in your examination of it .</p>
<p>wisteria1 s212 : Mr. Scott Eccles had fidgeted in his seat during this conversation .</p>
<p>wisteria1 s214 : `` But I beg to point out that I have not yet heard what has happened to Mr. Garcia , nor what has become of his household . ''</p>
<p>wisteria1 s224 : `` This is very painful -- very painful and terrible , '' said Mr. Scott Eccles in a querulous voice , `` but it is really uncommonly hard on me .</p>
<p>wisteria1 s231 : I wired to Mr. Gregson to run you down in London while I examined Wisteria Lodge .</p>
<p>wisteria1 s232 : Then I came into town , joined Mr. Gregson , and here we are . ''</p>
<p>wisteria1 s234 : You will come round with us to the station , Mr. Scott Eccles , and let us have your statement in writing . ''</p>
<p>wisteria1 s236 : But I retain your services , Mr. Holmes .</p>
<p>wisteria1 s239 : `` I suppose that you have no objection to my collaborating with you , Mr. Baynes ? ''</p>
<p>wisteria1 s245 : `` But that is perfectly impossible , Mr. Baynes , '' cried our client .</p>
<p>wisteria1 s252 : By the way , Mr. Baynes , did you find anything remarkable besides this note in your examination of the house ? ''</p>
<p>wisteria1 s334 : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr. Hynes Hynes , J.P. , Purdley Place ; Mr. James Baker Williams , Forton Old Hall ; Mr. Henderson , High Gable ; Rev. Joshua Stone , Nether Walsling .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">?</td>
<td style="text-align: right;">44</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">''</td>
<td style="text-align: right;">113</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">``</td>
<td style="text-align: right;">122</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">.</td>
<td style="text-align: right;">298</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">,</td>
<td style="text-align: right;">332</td>
<td></td>
</tr>
</tbody>
</table>


## wisteria2.txt (2012-02-20)

<table data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: center;">'86</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s336 : Henderson he called himself , but I traced him back , Paris and Rome and Madrid to Barcelona , where his ship came in in '86 .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'d</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s298 : I 'd have a short life if he had his way -- the black-eyed , scowling , yellow devil . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'m</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s115 : `` I 'm sure , Watson , a week in the country will be invaluable to you , '' he remarked .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">2.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s0 : 2. The Tiger of San Pedro</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Co.</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s47 : A good deal of clothing with the stamp of Marx and Co. , High Holborn , had been left behind .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">_all_</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s187 : They were _all_ confederates in the same unknown crime .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">_he_</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s180 : The proof of this lies in the fact that it was _he_ who had arranged for the presence of Scott Eccles , which could only have been done for the purpose of an alibi .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">_not_</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s189 : But the attempt was a dangerous one , and if Garcia did _not_ return by a certain hour it was probable that his own life had been sacrificed .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">_we_</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s348 : But _we_ know .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">o'clock</td>
<td style="text-align: right;">1</td>
<td><p>wisteria2 s281 : It was about five o'clock , and the shadows of the March evening were beginning to fall , when an excited rustic rushed into our room .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'ll</td>
<td style="text-align: right;">3</td>
<td><p>wisteria2 s5 : `` I 'll knock at the window . ''</p>
<p>wisteria2 s26 : I 'll see it in my dreams . ''</p>
<p>wisteria2 s96 : `` And I 'll work it myself , Mr. Holmes .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'re</td>
<td style="text-align: right;">3</td>
<td><p>wisteria2 s81 : `` You 're right , Mr. Holmes .</p>
<p>wisteria2 s148 : `` You 're very kind , Mr. Holmes . ''</p>
<p>wisteria2 s159 : `` You 're welcome always to my news .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">:</td>
<td style="text-align: right;">3</td>
<td><p>wisteria2 s122 : I must admit , however , that I was somewhat surprised when , some five days after the crime , I opened my morning paper to find in large letters :</p>
<p>wisteria2 s129 : `` Apparently , '' said I as I read the following report :</p>
<p>wisteria2 s435 : Here is a quotation from Eckermann 's Voodooism and the Negroid Religions :</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'</td>
<td style="text-align: right;">4</td>
<td><p>wisteria2 s182 : I say ` criminal ' because only a man with a criminal enterprise desires to establish an alibi .</p>
<p>wisteria2 s238 : ` Sold his soul to the devil in exchange for money , ' says Warner , ` and expects his creditor to come up and claim his own . '</p>
<p>wisteria2 s438 : The more usual victims are a white cock , which is plucked in pieces alive , or a black goat , whose throat is cut and body burned . '</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">`</td>
<td style="text-align: right;">4</td>
<td><p>wisteria2 s182 : I say ` criminal ' because only a man with a criminal enterprise desires to establish an alibi .</p>
<p>wisteria2 s238 : ` Sold his soul to the devil in exchange for money , ' says Warner , ` and expects his creditor to come up and claim his own . '</p>
<p>wisteria2 s436 : `` ` The true voodoo-worshipper attempts nothing of importance without certain sacrifices which are intended to propitiate his unclean gods .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'ve</td>
<td style="text-align: right;">7</td>
<td><p>wisteria2 s142 : `` You 've seen the paper , Mr. Holmes ? '' he asked , holding one out to us .</p>
<p>wisteria2 s143 : `` Yes , Baynes , I 've seen it .</p>
<p>wisteria2 s282 : `` They 've gone , Mr. Holmes .</p>
<p>wisteria2 s284 : The lady broke away , and I 've got her in a cab downstairs . ''</p>
<p>wisteria2 s301 : `` Why , sir , you 've got me the very evidence I want , '' said the inspector warmly , shaking my friend by the hand .</p>
<p>wisteria2 s316 : `` I 've had a plain-clothes man waiting at the station all the week .</p>
<p>wisteria2 s337 : They 've been looking for him all the time for their revenge , but it is only now that they have begun to find him out . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">;</td>
<td style="text-align: right;">7</td>
<td><p>wisteria2 s29 : `` I know , sir , I know ; but it shook me , sir , and there 's no use to deny it .</p>
<p>wisteria2 s155 : `` No , sir ; I believe you mean well by me .</p>
<p>wisteria2 s164 : `` I did n't say so , Mr. Holmes ; I did n't say so .</p>
<p>wisteria2 s214 : `` These two men , close and confidential friends , are the centre of the household ; but there is one other person who for our immediate purpose may be even more important .</p>
<p>wisteria2 s341 : But another will come , and yet another , until some day justice will be done ; that is as certain as the rise of to-morrow 's sun . ''</p>
<p>wisteria2 s390 : At first they were of a mind to let him enter the house and to kill him as a detected burglar ; but they argued that if they were mixed up in an inquiry their own identity would at once be publicly disclosed and they would be open to further attacks .</p>
<p>wisteria2 s397 : In a sort of dream I remember being half-led , half-carried to the carriage ; in the same state I was conveyed to the train .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">!</td>
<td style="text-align: right;">9</td>
<td><p>wisteria2 s25 : Lord , sir , what a face it was !</p>
<p>wisteria2 s62 : `` Very interesting -- very interesting , indeed ! '' said Holmes , peering at this sinister relic .</p>
<p>wisteria2 s68 : `` Most interesting !</p>
<p>wisteria2 s105 : Au revoir and good luck ! ''</p>
<p>wisteria2 s127 : `` By Jove ! '' he cried .</p>
<p>wisteria2 s229 : `` Curious people , Watson !</p>
<p>wisteria2 s285 : `` Excellent , Warner ! '' cried Holmes , springing to his feet .</p>
<p>wisteria2 s303 : `` What !</p>
<p>wisteria2 s324 : The Tiger of San Pedro !</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">n't</td>
<td style="text-align: right;">17</td>
<td><p>wisteria2 s12 : It has been a long evening , and I do n't think my nerve is as good as it was . ''</p>
<p>wisteria2 s24 : I do n't know what made me look up , but there was a face looking in at me through the lower pane .</p>
<p>wisteria2 s30 : It was n't black , sir , nor was it white , nor any colour that I know but a kind of queer shade like clay with a splash of milk in it .</p>
<p>wisteria2 s33 : I tell you , sir , I could n't move a finger , nor get my breath , till it whisked away and was gone .</p>
<p>wisteria2 s35 : `` If I did n't know you were a good man , Walters , I should put a black mark against you for this .</p>
<p>wisteria2 s128 : `` You do n't mean that Baynes has got him ? ''</p>
<p>wisteria2 s144 : Pray do n't think it a liberty if I give you a word of friendly warning . ''</p>
<p>wisteria2 s147 : I do n't want you to commit yourself too far unless you are sure . ''</p>
<p>wisteria2 s154 : `` Do n't blame me . ''</p>
<p>wisteria2 s164 : `` I did n't say so , Mr. Holmes ; I did n't say so .</p>
<p>wisteria2 s169 : `` I ca n't make the man out .</p>
<p>wisteria2 s172 : But there 's something in Inspector Baynes which I ca n't quite understand . ''</p>
<p>wisteria2 s230 : I do n't pretend to understand it all yet , but very curious people anyway .</p>
<p>wisteria2 s269 : We ca n't let such a situation continue .</p>
<p>wisteria2 s297 : I sha n't forget the face at the carriage window as I led her away .</p>
<p>wisteria2 s320 : We ca n't arrest without her evidence , that is clear , so the sooner we get a statement the better . ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Mr.</td>
<td style="text-align: right;">20</td>
<td><p>wisteria2 s44 : Now , Mr. Holmes , with your permission , I will show you round the house . ''</p>
<p>wisteria2 s51 : `` But now , Mr. Holmes , I invite your attention to the kitchen . ''</p>
<p>wisteria2 s70 : But Mr. Baynes had kept his most sinister exhibit to the last .</p>
<p>wisteria2 s81 : `` You 're right , Mr. Holmes .</p>
<p>wisteria2 s87 : `` Curious , Mr. Baynes , very curious .</p>
<p>wisteria2 s96 : `` And I 'll work it myself , Mr. Holmes .</p>
<p>wisteria2 s131 : It will be remembered that Mr. Garcia , of Wisteria Lodge , was found dead on Oxshott Common , his body showing signs of extreme violence , and that on the same night his servant and his cook fled , which appeared to show their participation in the crime .</p>
<p>wisteria2 s142 : `` You 've seen the paper , Mr. Holmes ? '' he asked , holding one out to us .</p>
<p>wisteria2 s145 : `` Of warning , Mr. Holmes ? ''</p>
<p>wisteria2 s148 : `` You 're very kind , Mr. Holmes . ''</p>
<p>wisteria2 s150 : It seemed to me that something like a wink quivered for an instant over one of Mr. Baynes 's tiny eyes .</p>
<p>wisteria2 s151 : `` We agreed to work on our own lines , Mr. Holmes .</p>
<p>wisteria2 s156 : But we all have our own systems , Mr. Holmes .</p>
<p>wisteria2 s164 : `` I did n't say so , Mr. Holmes ; I did n't say so .</p>
<p>wisteria2 s206 : But Mr. Henderson , of High Gable , was by all accounts a curious man to whom curious adventures might befall .</p>
<p>wisteria2 s212 : His friend and secretary , Mr. Lucas , is undoubtedly a foreigner , chocolate brown , wily , suave , and catlike , with a poisonous gentleness of speech .</p>
<p>wisteria2 s282 : `` They 've gone , Mr. Holmes .</p>
<p>wisteria2 s291 : `` I watched at the gate , same as you advised , Mr. Holmes , '' said our emissary , the discharged gardener .</p>
<p>wisteria2 s305 : `` Why , Mr. Holmes , when you were crawling in the shrubbery at High Gable I was up one of the trees in the plantation and saw you down below .</p>
<p>wisteria2 s335 : `` If you look it up you will find that the San Pedro colours are green and white , same as in the note , Mr. Holmes .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'s</td>
<td style="text-align: right;">32</td>
<td><p>wisteria2 s4 : `` There 's a constable in possession , '' said Baynes .</p>
<p>wisteria2 s9 : `` What 's the matter , Walters ? '' asked Baynes sharply .</p>
<p>wisteria2 s15 : `` Well , sir , it 's this lonely , silent house and the queer thing in the kitchen .</p>
<p>wisteria2 s29 : `` I know , sir , I know ; but it shook me , sir , and there 's no use to deny it .</p>
<p>wisteria2 s43 : `` Well , '' said the inspector with a grave and thoughtful face , `` whoever he may have been , and whatever he may have wanted , he 's gone for the present , and we have more immediate things to attend to .</p>
<p>wisteria2 s53 : The table was piled with half-eaten dishes and dirty plates , the debris of last night 's dinner .</p>
<p>wisteria2 s80 : Inspector Baynes 's small eyes twinkled with pleasure .</p>
<p>wisteria2 s97 : It 's only due to my own credit to do so .</p>
<p>wisteria2 s150 : It seemed to me that something like a wink quivered for an instant over one of Mr. Baynes 's tiny eyes .</p>
<p>wisteria2 s152 : That 's what I am doing . ''</p>
<p>wisteria2 s161 : He chewed Downing 's thumb nearly off before they could master him .</p>
<p>wisteria2 s167 : That 's the agreement . ''</p>
<p>wisteria2 s172 : But there 's something in Inspector Baynes which I ca n't quite understand . ''</p>
<p>wisteria2 s179 : We may put aside this idea of Baynes 's that Garcia 's servants were concerned in the matter .</p>
<p>wisteria2 s186 : `` We can now see a reason for the disappearance of Garcia 's household .</p>
<p>wisteria2 s188 : If it came off when Garcia returned , any possible suspicion would be warded off by the Englishman 's evidence , and all would be well .</p>
<p>wisteria2 s219 : It is only within the last weeks that he has returned , after a year 's absence , to High Gable .</p>
<p>wisteria2 s231 : It 's a double-winged house , and the servants live on one side , the family on the other .</p>
<p>wisteria2 s232 : There 's no link between the two save for Henderson 's own servant , who serves the family 's meals .</p>
<p>wisteria2 s249 : I may add that Miss Burnet 's age and character make it certain that my first idea that there might be a love interest in our story is out of the question .</p>
<p>wisteria2 s266 : The woman 's disappearance counts for nothing , since in that extraordinary household any member of it might be invisible for a week .</p>
<p>wisteria2 s312 : Holmes laid his hand upon the inspector 's shoulder .</p>
<p>wisteria2 s341 : But another will come , and yet another , until some day justice will be done ; that is as certain as the rise of to-morrow 's sun . ''</p>
<p>wisteria2 s355 : This villain 's policy was to murder , on one pretext or another , every man who showed such promise that he might in time come to be a dangerous rival .</p>
<p>wisteria2 s368 : He little knew that the woman who faced him at every meal was the woman whose husband he had hurried at an hour 's notice into eternity .</p>
<p>wisteria2 s388 : How they murdered him I do not know , save that it was Murillo 's hand who struck him down , for Lopez had remained to guard me .</p>
<p>wisteria2 s424 : `` The object of the mulatto cook 's return ? ''</p>
<p>wisteria2 s428 : But the mulatto 's heart was with it , and he was driven back to it next day , when , on reconnoitering through the window , he found policeman Walters in possession .</p>
<p>wisteria2 s435 : Here is a quotation from Eckermann 's Voodooism and the Negroid Religions :</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">?</td>
<td style="text-align: right;">41</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">''</td>
<td style="text-align: right;">110</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">``</td>
<td style="text-align: right;">125</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">.</td>
<td style="text-align: right;">390</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">,</td>
<td style="text-align: right;">461</td>
<td></td>
</tr>
</tbody>
</table>


## SEM-2012-SharedTask-CD-SCO-dev.txt

<table data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: center;">'86</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s334 : Henderson he called himself , but I traced him back , Paris and Rome and Madrid to Barcelona , where his ship came in in '86 .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'Sold</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s236 : 'Sold his soul to the devil in exchange for money , ' says Warner , 'and expects his creditor to come up and claim his own . '</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'The</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s434 : " 'The true voodoo-worshipper attempts nothing of importance without certain sacrifices which are intended to propitiate his unclean gods .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'and</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s236 : 'Sold his soul to the devil in exchange for money , ' says Warner , 'and expects his creditor to come up and claim his own . '</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'clock</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s279 : It was about five o 'clock , and the shadows of the March evening were beginning to fall , when an excited rustic rushed into our room .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'criminal</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s180 : I say 'criminal ' because only a man with a criminal enterprise desires to establish an alibi .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'d</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s296 : I 'd have a short life if he had his way - the black-eyed , scowling , yellow devil . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'m</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch2 s116 : " I 'm sure , Watson , a week in the country will be invaluable to you , " he remarked .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Garcia's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s56 : I went to the house agents , you know , and they said that Mr . Garcia's rent was paid up all right and that everything was in order at Wisteria Lodge . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Holmes's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s328 : An answer had arrived to Holmes's telegram before our Surrey officer had returned .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">It's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s186 : It's my way .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">argument's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s298 : We will suppose , for argument's sake , that the household of Wisteria Lodge are confederates in some design .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">inspector's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s97 : With a dubious glance at the inspector's notebook , he plunged at once into his extraordinary statement .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">woman's</td>
<td style="text-align: right;">1</td>
<td><p>Wisteria_ch1 s200 : It is a woman's writing , done with a sharp-pointed pen , but the address is either done with another pen or by someone else .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">&amp;amp;gt;From</td>
<td style="text-align: right;">2</td>
<td><p>Wisteria_ch2 s72 : &amp;amp;gt;From under the sink he drew a zinc pail which contained a quantity of blood .</p>
<p>Wisteria_ch2 s331 : &amp;amp;gt;From that moment he had vanished from the world , and his identity had been a frequent subject for comment in the European press .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">I'm</td>
<td style="text-align: right;">2</td>
<td><p>Wisteria_ch1 s61 : " I'm sure it must look very bad , Mr . Holmes , and I am not aware that in my whole life such a thing has ever happened before .</p>
<p>Wisteria_ch1 s210 : " I'm bound to say that I make nothing of the note except that there was something on hand , and that a woman , as usual was at the bottom of it . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'ll</td>
<td style="text-align: right;">3</td>
<td><p>Wisteria_ch2 s5 : " I 'll knock at the window . "</p>
<p>Wisteria_ch2 s26 : I 'll see it in my dreams . "</p>
<p>Wisteria_ch2 s97 : " And I 'll work it myself , Mr . Holmes .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'re</td>
<td style="text-align: right;">3</td>
<td><p>Wisteria_ch2 s82 : " You 're right , Mr . Holmes .</p>
<p>Wisteria_ch2 s146 : " You 're very kind , Mr . Holmes . "</p>
<p>Wisteria_ch2 s157 : " You 're welcome always to my news .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">don't</td>
<td style="text-align: right;">3</td>
<td><p>Wisteria_ch1 s85 : You don't mean - - you don't mean that I am suspected ? "</p>
<p>Wisteria_ch1 s335 : " I don't quite understand . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">man's</td>
<td style="text-align: right;">3</td>
<td><p>Wisteria_ch1 s86 : " A letter of yours was found in the dead man's pocket , and we know by it that you had planned to pass last night at his house . "</p>
<p>Wisteria_ch1 s228 : It was the envelope of this letter which gave us the dead man's name and address .</p>
<p>Wisteria_ch1 s263 : " Well , taken with the disappearance of the man's companions , I should say that they were in some way concerned in the murder and had fled from justice . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">:</td>
<td style="text-align: right;">5</td>
<td><p>Wisteria_ch1 s194 : It says :</p>
<p>Wisteria_ch1 s332 : The telegram was a list of names and addresses : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr . Hynes Hynes , J . P . , Purdley Place ; Mr . James Baker Williams , Forton Old Hall ; Mr . Henderson , High Gable ; Rev . Joshua Stone , Nether Walsling .</p>
<p>Wisteria_ch2 s123 : I must admit , however , that I was somewhat surprised when , some five days after the crime , I opened my morning paper to find in large letters :</p>
<p>Wisteria_ch2 s127 : " Apparently , " said I as I read the following report :</p>
<p>Wisteria_ch2 s433 : Here is a quotation from Eckermann 's Voodooism and the Negroid Religions :</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">o'clock</td>
<td style="text-align: right;">5</td>
<td><p>Wisteria_ch1 s131 : He apologized for having disturbed me so late , saying that it was nearly one o'clock .</p>
<p>Wisteria_ch1 s242 : " He had been there since one o'clock .</p>
<p>Wisteria_ch1 s299 : The attempt , whatever it may be , is to come off , we will say , before one o'clock .</p>
<p>Wisteria_ch1 s338 : It is equally certain that this house cannot be more than a mile or two from Oxshott , since Garcia was walking in that direction and hoped , according to my reading of the facts , to be back in Wisteria Lodge in time to avail himself of an alibi , which would only be valid up to one o'clock .</p>
<p>Wisteria_ch1 s341 : It was nearly six o'clock before we found ourselves in the pretty Surrey village of Esher , with Inspector Baynes as our companion .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'ve</td>
<td style="text-align: right;">7</td>
<td><p>Wisteria_ch2 s140 : " You 've seen the paper , Mr . Holmes ? " he asked , holding one out to us .</p>
<p>Wisteria_ch2 s141 : " Yes , Baynes , I 've seen it .</p>
<p>Wisteria_ch2 s280 : " They 've gone , Mr . Holmes .</p>
<p>Wisteria_ch2 s282 : The lady broke away , and I 've got her in a cab downstairs . "</p>
<p>Wisteria_ch2 s299 : " Why , sir , you 've got me the very evidence I want , " said the inspector warmly , shaking my friend by the hand .</p>
<p>Wisteria_ch2 s314 : " I 've had a plain-clothes man waiting at the station all the week .</p>
<p>Wisteria_ch2 s335 : They 've been looking for him all the time for their revenge , but it is only now that they have begun to find him out . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">!</td>
<td style="text-align: right;">12</td>
<td><p>Wisteria_ch1 s84 : " Good God ! This is awful !</p>
<p>Wisteria_ch1 s152 : The foreign host , the foreign footman , the foreign cook , all had vanished in the night !</p>
<p>Wisteria_ch2 s25 : Lord , sir , what a face it was !</p>
<p>Wisteria_ch2 s63 : " Very interesting - very interesting , indeed ! " said Holmes , peering at this sinister relic .</p>
<p>Wisteria_ch2 s69 : " Most interesting !</p>
<p>Wisteria_ch2 s106 : Au revoir and good luck ! "</p>
<p>Wisteria_ch2 s125 : " By Jove ! " he cried .</p>
<p>Wisteria_ch2 s227 : " Curious people , Watson !</p>
<p>Wisteria_ch2 s283 : " Excellent , Warner ! " cried Holmes , springing to his feet .</p>
<p>Wisteria_ch2 s301 : " What !</p>
<p>Wisteria_ch2 s322 : The Tiger of San Pedro !</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">;</td>
<td style="text-align: right;">15</td>
<td><p>Wisteria_ch1 s9 : " There is surely something more than that , " said he ; " some underlying suggestion of the tragic and the terrible .</p>
<p>Wisteria_ch1 s28 : Life is commonplace , the papers are sterile ; audacity and romance seem to have passed forever from the criminal world .</p>
<p>Wisteria_ch1 s297 : " Exactly , my dear Watson ; he might have proved an alibi .</p>
<p>Wisteria_ch1 s332 : The telegram was a list of names and addresses : Lord Harringby , The Dingle ; Sir George Ffolliott , Oxshott Towers ; Mr . Hynes Hynes , J . P . , Purdley Place ; Mr . James Baker Williams , Forton Old Hall ; Mr . Henderson , High Gable ; Rev . Joshua Stone , Nether Walsling .</p>
<p>Wisteria_ch2 s29 : " I know , sir , I know ; but it shook me , sir , and there 's no use to deny it .</p>
<p>Wisteria_ch2 s153 : " No , sir ; I believe you mean well by me .</p>
<p>Wisteria_ch2 s162 : " I didn 't say so , Mr . Holmes ; I didn 't say so .</p>
<p>Wisteria_ch2 s212 : " These two men , close and confidential friends , are the centre of the household ; but there is one other person who for our immediate purpose may be even more important .</p>
<p>Wisteria_ch2 s339 : But another will come , and yet another , until some day justice will be done ; that is as certain as the rise of to-morrow 's sun . "</p>
<p>Wisteria_ch2 s388 : At first they were of a mind to let him enter the house and to kill him as a detected burglar ; but they argued that if they were mixed up in an inquiry their own identity would at once be publicly disclosed and they would be open to further attacks .</p>
<p>Wisteria_ch2 s395 : In a sort of dream I remember being half-led , halfcarried to the carriage ; in the same state I was conveyed to the train .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'t</td>
<td style="text-align: right;">17</td>
<td><p>Wisteria_ch2 s12 : It has been a long evening , and I don 't think my nerve is as good as it was . "</p>
<p>Wisteria_ch2 s24 : I don 't know what made me look up , but there was a face looking in at me through the lower pane .</p>
<p>Wisteria_ch2 s30 : It wasn 't black , sir , nor was it white , nor any colour that I know but a kind of queer shade like clay with a splash of milk in it .</p>
<p>Wisteria_ch2 s33 : I tell you , sir , I couldn 't move a finger , nor get my breath , till it whisked away and was gone .</p>
<p>Wisteria_ch2 s35 : " If I didn 't know you were a good man , Walters , I should put a black mark against you for this .</p>
<p>Wisteria_ch2 s126 : " You don 't mean that Baynes has got him ? "</p>
<p>Wisteria_ch2 s142 : Pray don 't think it a liberty if I give you a word of friendly warning . "</p>
<p>Wisteria_ch2 s145 : I don 't want you to commit yourself too far unless you are sure . "</p>
<p>Wisteria_ch2 s152 : " Don 't blame me . "</p>
<p>Wisteria_ch2 s162 : " I didn 't say so , Mr . Holmes ; I didn 't say so .</p>
<p>Wisteria_ch2 s167 : " I can 't make the man out .</p>
<p>Wisteria_ch2 s170 : But there 's something in Inspector Baynes which I can 't quite understand . "</p>
<p>Wisteria_ch2 s228 : I don 't pretend to understand it all yet , but very curious people anyway .</p>
<p>Wisteria_ch2 s267 : We can 't let such a situation continue .</p>
<p>Wisteria_ch2 s295 : I shan 't forget the face at the carriage window as I led her away .</p>
<p>Wisteria_ch2 s318 : We can 't arrest without her evidence , that is clear , so the sooner we get a statement the better . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'</td>
<td style="text-align: right;">19</td>
<td><p>Wisteria_ch1 s6 : " How do you define the word ' grotesque ' ? "</p>
<p>Wisteria_ch1 s160 : I called at Allan Brothers ' , the chief land agents in the village , and found that it was from this firm that the villa had been rented .</p>
<p>Wisteria_ch1 s311 : ' Our own colours , green and white . '</p>
<p>Wisteria_ch1 s313 : ' Green open , white shut . '</p>
<p>Wisteria_ch1 s315 : ' Main stair , first corridor , seventh right , green baize . '</p>
<p>Wisteria_ch1 s319 : She would not have said ' Godspeed ' had it not been so .</p>
<p>Wisteria_ch1 s320 : ' D ' - - that should be a guide . "</p>
<p>Wisteria_ch1 s322 : I suggest that ' D ' stands for Dolores , a common female name in Spain . "</p>
<p>Wisteria_ch2 s180 : I say 'criminal ' because only a man with a criminal enterprise desires to establish an alibi .</p>
<p>Wisteria_ch2 s236 : 'Sold his soul to the devil in exchange for money , ' says Warner , 'and expects his creditor to come up and claim his own . '</p>
<p>Wisteria_ch2 s436 : The more usual victims are a white cock , which is plucked in pieces alive , or a black goat , whose throat is cut and body burned . '</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'s</td>
<td style="text-align: right;">32</td>
<td><p>Wisteria_ch2 s4 : " There 's a constable in possession , " said Baynes .</p>
<p>Wisteria_ch2 s9 : " What 's the matter , Walters ? " asked Baynes sharply .</p>
<p>Wisteria_ch2 s15 : " Well , sir , it 's this lonely , silent house and the queer thing in the kitchen .</p>
<p>Wisteria_ch2 s29 : " I know , sir , I know ; but it shook me , sir , and there 's no use to deny it .</p>
<p>Wisteria_ch2 s43 : " Well , " said the inspector with a grave and thoughtful face , " whoever he may have been , and whatever he may have wanted , he 's gone for the present , and we have more immediate things to attend to .</p>
<p>Wisteria_ch2 s54 : The table was piled with half-eaten dishes and dirty plates , the debris of last night 's dinner .</p>
<p>Wisteria_ch2 s81 : Inspector Baynes 's small eyes twinkled with pleasure .</p>
<p>Wisteria_ch2 s98 : It 's only due to my own credit to do so .</p>
<p>Wisteria_ch2 s148 : It seemed to me that something like a wink quivered for an instant over one of Mr . Baynes 's tiny eyes .</p>
<p>Wisteria_ch2 s150 : That 's what I am doing . "</p>
<p>Wisteria_ch2 s159 : He chewed Downing 's thumb nearly off before they could master him .</p>
<p>Wisteria_ch2 s165 : That 's the agreement . "</p>
<p>Wisteria_ch2 s170 : But there 's something in Inspector Baynes which I can 't quite understand . "</p>
<p>Wisteria_ch2 s177 : We may put aside this idea of Baynes 's that Garcia 's servants were concerned in the matter .</p>
<p>Wisteria_ch2 s184 : " We can now see a reason for the disappearance of Garcia 's household .</p>
<p>Wisteria_ch2 s186 : If it came off when Garcia returned , any possible suspicion would be warded off by the Englishman 's evidence , and all would be well .</p>
<p>Wisteria_ch2 s217 : It is only within the last weeks that he has returned , after a year 's absence , to High Gable .</p>
<p>Wisteria_ch2 s229 : It 's a double-winged house , and the servants live on one side , the family on the other .</p>
<p>Wisteria_ch2 s230 : There 's no link between the two save for Henderson 's own servant , who serves the family 's meals .</p>
<p>Wisteria_ch2 s247 : I may add that Miss Burnet 's age and character make it certain that my first idea that there might be a love interest in our story is out of the question .</p>
<p>Wisteria_ch2 s264 : The woman 's disappearance counts for nothing , since in that extraordinary household any member of it might be invisible for a week .</p>
<p>Wisteria_ch2 s310 : Holmes laid his hand upon the inspector 's shoulder .</p>
<p>Wisteria_ch2 s339 : But another will come , and yet another , until some day justice will be done ; that is as certain as the rise of to-morrow 's sun . "</p>
<p>Wisteria_ch2 s353 : This villain 's policy was to murder , on one pretext or another , every man who showed such promise that he might in time come to be a dangerous rival .</p>
<p>Wisteria_ch2 s366 : He little knew that the woman who faced him at every meal was the woman whose husband he had hurried at an hour 's notice into eternity .</p>
<p>Wisteria_ch2 s386 : How they murdered him I do not know , save that it was Murillo 's hand who struck him down , for Lopez had remained to guard me .</p>
<p>Wisteria_ch2 s422 : " The object of the mulatto cook 's return ? "</p>
<p>Wisteria_ch2 s426 : But the mulatto 's heart was with it , and he was driven back to it next day , when , on reconnoitering through the window , he found policeman Walters in possession .</p>
<p>Wisteria_ch2 s433 : Here is a quotation from Eckermann 's Voodooism and the Negroid Religions :</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">?</td>
<td style="text-align: right;">85</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">"</td>
<td style="text-align: right;">470</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">.</td>
<td style="text-align: right;">750</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">,</td>
<td style="text-align: right;">793</td>
<td></td>
</tr>
</tbody>
</table>


## SEM-2012-SharedTask-CD-SCO-training.txt

<table data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: center;">'Phosphorus</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch14 s139 : '' 'Phosphorus !</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'Please</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s64 : It ran 'Please , please , as you are a gentleman , burn this letter , and be at the gate by ten o'clock .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'clock</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s173 : " You have confessed that you asked Sir Charles to be at the gate at ten o 'clock .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'d</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s46 : " I do n't pretend to know much about these things , and I 'd be a better judge of a horse or a steer than of a picture .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">'m</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s45 : " Well , I 'm glad to hear you say so , " said Sir Henry , glancing with some surprise at my friend .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'re</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s60 : We 're not likely to forget him . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">13th</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch8 s2 : Baskerville Hall , October 13th .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">14th</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch2 s77 : This is the Devon County Chronicle of May 14th of this year .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">15th</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s1 : Baskerville Hall , Oct . 15th .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">16th</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch10 s4 : October 16th .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">17th</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch10 s142 : October 17th .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Bradley's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch3 s148 : When you pass Bradley's , would you ask him to send up a pound of the strongest shag tobacco ?</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Didn't</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch7 s47 : " Didn't he get the telegram ?</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">He'll</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch10 s58 : " He'll break into no house , sir .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Isn't</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s317 : Isn't that the direction of the great Grimpen Mire ? "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Middleton's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s153 : I have established a right of way through the centre of old Middleton's park , slap across it , sir , within a hundred yards of his own front door .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Queen's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s162 : It will repay reading - - Frankland v . Morland , Court of Queen's Bench .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Selden's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s361 : Let him think that Selden's death was as Stapleton would have us believe .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Shipley's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s204 : My cab is out of Shipley's Yard , near Waterloo Station . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Stamford's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch3 s185 : After you left I sent down to Stamford's for the Ordnance map of this portion of the moor , and my spirit has hovered over it all day .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">They'll</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s31 : " They'll find they've started in to monkey with the wrong man unless they are careful .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">We're</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s318 : " We're at close grips at last , " said Holmes as we walked together across the moor .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">We've</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch14 s133 : '' We've laid the family ghost once and forever . ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">You're</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch14 s17 : '' You're mighty close about this affair , Mr . Holmes .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">[</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch2 s69 : " [ This from Hugo Baskerville to his sons Rodger and John , with instructions that they say nothing thereof to their sister Elizabeth . ] "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">]</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch2 s69 : " [ This from Hugo Baskerville to his sons Rodger and John , with instructions that they say nothing thereof to their sister Elizabeth . ] "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">argument's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s331 : But supposing , for argument's sake , that we had him arrested to-night , what on earth the better off should we be for that ?</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">bachelor's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s82 : " Do you think a woman could go alone at that hour to a bachelor's house ? "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">butler's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch6 s163 : I seemed to discern some signs of emotion upon the butler's white face .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">cabman's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s222 : Never have I seen my friend more completely taken aback than by the cabman's reply .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">companion's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch7 s150 : It turned me cold with horror , but my companion's nerves seemed to be stronger than mme .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">convict's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s198 : It was on his track , and not upon the convict's , that Frankland had stumbled .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">dog's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch1 s89 : The dog's jaw , as shown in the space between these marks , is too broad in my opinion for a terrier and not broad enough for a mastiff .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">fellow's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s291 : " And what is your theory of this poor fellow's death ? "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">gentleman's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s229 : " Yes , sir , that was the gentleman's name . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">gipsy's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch3 s234 : If the gipsy's evidence may be taken as true , he ran with cries for help in the direction where help was least likely to be .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">hart's-tongue</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch6 s70 : The wagonette swung round into a side road , and we curved upward through deep lanes worn by centuries of wheels , high banks on either side , heavy with dripping moss and fleshy hart's-tongue ferns .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">haven't</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch11 s159 : I haven't had such a day since I had Sir John Morland for trespass because he shot in his own warren . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">horse's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch2 s54 : Then the revellers rode close together , for a great fear was on them , but they still followed over the moor , though each , had he been alone , would have been right glad to have turned his horse's head .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">hotel.-</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch4 s176 : Now , look here , Mr . Holmes , it's half-past eleven now and I am going back right away to my hotel.-</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">husband's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch14 s235 : It helped us to realize the horror of this woman's life when we saw the eagerness and joy with which she laid us on her husband's track .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">indorsed'</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s197 : It is indorsed' Mr . and Mrs . Vandeleur , ' but you will have no difficulty in recognizing him , and her also , if you know her by sight .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">maid's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch2 s43 : Whereat Hugo ran from the house , crying to his grooms that they should saddle his mare and unkennel the pack , and giving the hounds a kerchief of the maid's , he swung them to the line , and so off full cry in the moonlight over the moor .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">mare's-tails</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch7 s241 : Would you mind getting that orchid for me among the mare's-tails yonder ?</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">minstrel's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch6 s177 : At one end a minstrel's gallery overlooked it .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">morning's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch10 s137 : I went at once to my room and drew up my report of the morning's conversation for Holmes .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">mother's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s241 : Then as he grew older he met wicked companions , and the devil entered into him until he broke my mother's heart and dragged our name in the dirt .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">naturalist's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s83 : The naturalist's angry gestures showed that the lady was included in his displeasure .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">sister's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s150 : We know now why Stapleton looked with disfavour upon his sister's suitor - even when that suitor was so eligible a one as Sir Henry .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">visitor's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch1 s11 : " But , tell me , Watson , what do you make of our visitor's stick ?</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">wasn't</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s252 : " Well , he wasn't altogether such an easy gentleman to describe .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">we've</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch4 s48 : " I don't know much about the tariff and things of that kind , " said he , " but it seems to me we've got a bit off the trail so far as that note is concerned . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">who's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s268 : " Who - - who's this ? " he stammered .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">wit's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s87 : His face was flushed with anger and his brows were wrinkled , like one who is at his wit's ends what to do .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">wouldn't</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch9 s118 : She was glad to meet me , but when she did it was not love that she would talk about , and she wouldn't have let me talk about it either if she could have stopped it .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">wretch's</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch12 s250 : The question now is , what shall we do with this poor wretch's body ?</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">year'66</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch13 s237 : Students of criminology will remember the analogous incidents in Godno , in Little Russia , in the year'66 , and of course there are the Anderson murders in North Carolina , but this case possesses some features which are entirely its own .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">you'll</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch5 s50 : Well , well , Mr . Holmes , you'll excuse my troubling you about such a trifle - "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">you're</td>
<td style="text-align: right;">1</td>
<td><p>HoundOfTheBaskervilles_ch4 s54 : " By thunder , you're right !</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'ve</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch13 s7 : " I 've been moping in the house all day since Watson went off in the morning , " said the baronet .</p>
<p>HoundOfTheBaskervilles_ch13 s27 : " We 've had one experience , as Watson has no doubt told you .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">He's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch6 s85 : He's been out three days now , and the warders watch every road and every station , but they've had no sight of him yet .</p>
<p>HoundOfTheBaskervilles_ch10 s209 : He's in hiding , too , but he's not a convict as far as I can make out .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">I'd</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch4 s183 : " I'd prefer to walk , for this affair has flurried me rather . "</p>
<p>HoundOfTheBaskervilles_ch5 s253 : I'd put him at forty years of age , and he was of a middle height , two or three inches shorter than you , sir .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">I'm</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch5 s271 : But I'm not easy in my mind about it . "</p>
<p>HoundOfTheBaskervilles_ch6 s56 : I tell you it is all as new to me as it is to Dr . Watson , and I'm as keen as possible to see the moor . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">You'll</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch9 s337 : " You'll be all right to-morrow . "</p>
<p>HoundOfTheBaskervilles_ch11 s191 : " You'll be surprised to hear that his food is taken to him by a child .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">You've</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch9 s105 : You've lived near me for some weeks , Watson .</p>
<p>HoundOfTheBaskervilles_ch10 s81 : " You've been so kind to us , sir , that I should like to do the best I can for you in return .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">baronet's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch9 s387 : The baronet's nerves were still quivering from that cry , which recalled the dark story of his family , and he was not in the mood for fresh adventures .</p>
<p>HoundOfTheBaskervilles_ch14 s128 : Lestrade thrust his brandy-flask between the baronet's teeth , and two frightened eyes were looking up at us .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">coroner's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch2 s110 : This explanation was borne out by the post-mortem examination , which showed long-standing organic disease , and the coroner's jury returned a verdict in accordance with the medical evidence .</p>
<p>HoundOfTheBaskervilles_ch2 s124 : My motive for withholding it from the coroner's inquiry is that a man of science shrinks from placing himself in the public position of seeming to indorse a popular superstition .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">couldn't</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch5 s237 : " Well , I couldn't be sure of that , but I dare say my fare knew all about it .</p>
<p>HoundOfTheBaskervilles_ch10 s120 : To rake this up couldn't help our poor master , and it's well to go carefully when there's a lady in the case .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">creature's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch14 s109 : '' Holmes emptied five barrels of his revolver into the creature's flank . ''</p>
<p>HoundOfTheBaskervilles_ch14 s121 : But the next instant Holmes had emptied five barrels of his revolver into the creature's flank .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">devil's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch3 s207 : " The devil's agents may be of flesh and blood , may they not ?</p>
<p>HoundOfTheBaskervilles_ch12 s237 : " Then the clothes have been the poor devil's death , " said he .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">doctor's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch2 s109 : No signs of violence were to be discovered upon Sir Charles's person , and though the doctor's evidence pointed to an almost incredible facial distortion - so great that Dr . Mortimer refused at first to believe that it was indeed his friend and patient who lay before him - it was explained that that is a symptom which is not unusual in cases of dyspnoea and death from cardiac exhaustion .</p>
<p>HoundOfTheBaskervilles_ch3 s1 : There was a thrill in the doctor's voice which showed that he was himself deeply moved by that which he told us .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">he's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch10 s209 : He's in hiding , too , but he's not a convict as far as I can make out .</p>
<p>HoundOfTheBaskervilles_ch14 s165 : No , no , he's gone by this time !</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">heaven's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch14 s38 : Creep forward quietly and see what they are doing - - but for heaven's sake don't let them know that they are watched ! ''</p>
<p>HoundOfTheBaskervilles_ch14 s131 : What , in heaven's name , was it ? ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">master's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch2 s106 : One fact which has not been explained is the statement of Barrymore that his master's footprints altered their character from the time that he passed the moor-gate , and that he appeared from thence onward to have been walking upon his toes .</p>
<p>HoundOfTheBaskervilles_ch7 s13 : It seemed to me that the pallid features of the butler turned a shade paler still as he listened to his master's question .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">won't</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch6 s118 : I'll have a row of electric lamps up here inside of six months , and you won't know it again , with a thousand candle-power Swan and Edison right here in front of the hall door . "</p>
<p>HoundOfTheBaskervilles_ch14 s81 : In half an hour we won't be able to see our hands in front of us . ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">yesterday's</td>
<td style="text-align: right;">2</td>
<td><p>HoundOfTheBaskervilles_ch4 s38 : Have you yesterday's Times , Watson ? "</p>
<p>HoundOfTheBaskervilles_ch4 s71 : As it was done yesterday the strong probability was that we should find the words in yesterday's issue . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Baskerville's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch2 s113 : It is understood that the next of kin is Mr . Henry Baskerville , if he be still alive , the son of Sir Charles Baskerville's younger brother .</p>
<p>HoundOfTheBaskervilles_ch3 s137 : You say that before Sir Charles Baskerville's death several people saw this apparition upon the moor ? "</p>
<p>HoundOfTheBaskervilles_ch6 s173 : My own was in the same wing as Baskerville's and almost next door to it .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Frankland's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch10 s171 : " She is Frankland's daughter . "</p>
<p>HoundOfTheBaskervilles_ch10 s188 : I am certainly developing the wisdom of the serpent , for when Mortimer pressed his questions to an inconvenient extent I asked him casually to what type Frankland's skull belonged , and so heard nothing but craniology for the rest of our drive .</p>
<p>HoundOfTheBaskervilles_ch14 s9 : It was a relief to me , after that unnatural restraint , when we at last passed Frankland's house and knew that we were drawing near to the Hall and to the scene of action .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">God's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch7 s163 : " For God's sake put such an idea out of your mind , " said he .</p>
<p>HoundOfTheBaskervilles_ch7 s231 : " But for God's sake do what I ask you .</p>
<p>HoundOfTheBaskervilles_ch10 s62 : For God's sake , sir , I beg of you not to let the police know that he is still on the moor .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Mortimer's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch3 s210 : Of course , if Dr . Mortimer's surmise should be correct , and we are dealing with forces outside the ordinary laws of Nature , there is an end of our investigation .</p>
<p>HoundOfTheBaskervilles_ch4 s144 : " I confess that I share Dr . Mortimer's belief that it will not be long before the missing boot is found . "</p>
<p>HoundOfTheBaskervilles_ch6 s45 : The journey was a swift and pleasant one , and I spent it in making the more intimate acquaintance of my two companions and in playing with Dr . Mortimer's spaniel .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Stapleton's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch7 s121 : I accepted Stapleton's invitation , and we turned together down the path .</p>
<p>HoundOfTheBaskervilles_ch10 s56 : Look at Mr . Stapleton's house , for example , with no one but himself to defend it .</p>
<p>HoundOfTheBaskervilles_ch12 s316 : Resisting Stapleton's offer of hospitality , Holmes and I set off to Baskerville Hall , leaving the naturalist to return alone .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">father's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch2 s39 : At last in the stress of her fear she did that which might have daunted the bravest or most active man , for by the aid of the growth of ivy which covered ( and still covers ) the south wall she came down from under the eaves , and so homeward across the moor , there being three leagues betwixt the Hall and her father's farm .</p>
<p>HoundOfTheBaskervilles_ch6 s54 : " I was a boy in my teens at the time of my father's death and had never seen the Hall , for he lived in a little cottage on the South Coast .</p>
<p>HoundOfTheBaskervilles_ch11 s201 : " I should say that it was much more likely that it was the son of one of the moorland shepherds taking out his father's dinner . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">night's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch9 s153 : All these things have by one night's work been thoroughly cleared .</p>
<p>HoundOfTheBaskervilles_ch9 s154 : I have said " by one night's work , " but , in truth , it was by two nights ' work , for on the first we drew entirely blank .</p>
<p>HoundOfTheBaskervilles_ch14 s230 : But the shock of the night's adventures had shattered his nerves , and before morning he lay delirious in a high fever under the care of Dr .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">they've</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch5 s31 : " They'll find they've started in to monkey with the wrong man unless they are careful .</p>
<p>HoundOfTheBaskervilles_ch5 s33 : I can take a joke with the best , Mr . Holmes , but they've got a bit over the mark this time . "</p>
<p>HoundOfTheBaskervilles_ch6 s85 : He's been out three days now , and the warders watch every road and every station , but they've had no sight of him yet .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">uncle's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch4 s154 : But as to my uncle's death - well , it all seems boiling up in my head , and I can't get it clear yet .</p>
<p>HoundOfTheBaskervilles_ch5 s60 : When taken in conjunction with your uncle's death I am not sure that of all the five hundred cases of capital importance which I have handled there is one which cuts so deep .</p>
<p>HoundOfTheBaskervilles_ch5 s136 : That was my poor uncle's idea .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">we'll</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch3 s212 : I think we'll shut that window again , if you don't mind .</p>
<p>HoundOfTheBaskervilles_ch12 s163 : But , by Heaven , if the worst has happened we'll avenge him ! "</p>
<p>HoundOfTheBaskervilles_ch14 s166 : But we'll search the house and make sure . ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">what's</td>
<td style="text-align: right;">3</td>
<td><p>HoundOfTheBaskervilles_ch9 s296 : " My God , what's that , Watson ? "</p>
<p>HoundOfTheBaskervilles_ch12 s255 : Halloa , Watson , what's this ?</p>
<p>HoundOfTheBaskervilles_ch12 s263 : But , dear me , what's this ?</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'ll</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch13 s30 : If you can muzzle that one and put him on a chain I 'll be ready to swear you are the greatest detective of all time . "</p>
<p>HoundOfTheBaskervilles_ch13 s49 : That 's a Kneller , I 'll swear , that lady in the blue silk over yonder , and the stout gentleman with the wig ought to be a Reynolds .</p>
<p>HoundOfTheBaskervilles_ch13 s96 : We 'll know before the day is out whether we have caught our big , leanjawed pike , or whether he has got through the meshes . "</p>
<p>HoundOfTheBaskervilles_ch13 s134 : " All right , then , I 'll stay . "</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Barrymore's</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch7 s30 : Obviously the first thing to do was to see the Grimpen postmaster and find whether the test telegram had really been placed in Barrymore's own hands .</p>
<p>HoundOfTheBaskervilles_ch7 s42 : " Well , he was up in the loft at the time , so that I could not put it into his own hands , but I gave it into Mrs . Barrymore's hands , and she promised to deliver it at once . "</p>
<p>HoundOfTheBaskervilles_ch9 s18 : But whatever the true explanation of Barrymore's movements might be , I felt that the responsibility of keeping them to myself until I could explain them was more than I could bear .</p>
<p>HoundOfTheBaskervilles_ch11 s135 : Barrymore's only indication had been that the stranger lived in one of these abandoned huts , and many hundreds of them are scattered throughout the length and breadth of the moor .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">We'll</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch4 s203 : We'll have a good look at him , if we can do no more . "</p>
<p>HoundOfTheBaskervilles_ch9 s32 : We'll sit up in my room to-night and wait until he passes . "</p>
<p>HoundOfTheBaskervilles_ch9 s344 : We'll see it through if all the fiends of the pit were loose upon the moor . "</p>
<p>HoundOfTheBaskervilles_ch11 s155 : We'll teach these magnates that they cannot ride roughshod over the rights of the commoners , confound them !</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">didn't</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch7 s45 : " If you didn't see him , how do you know he was in the loft ? "</p>
<p>HoundOfTheBaskervilles_ch9 s320 : Come now , Watson , didn't you think yourself that it was the cry of a hound ?</p>
<p>HoundOfTheBaskervilles_ch10 s52 : " I didn't think you would have taken advantage of it , Sir Henry - indeed I didn't . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">one's</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch6 s179 : With rows of flaring torches to light it up , and the colour and rude hilarity of an old-time banquet , it might have softened ; but now , when two blackclothed gentlemen sat in the little circle of light thrown by a shaded lamp , one's voice became hushed and one's spirit subdued .</p>
<p>HoundOfTheBaskervilles_ch7 s274 : The work to a man of my temperament was mechanical and uninteresting , but the privilege of living with youth , of helping to mould those young minds , and of impressing them with one's own character and ideals was very dear to me .</p>
<p>HoundOfTheBaskervilles_ch8 s5 : The longer one stays here the more does the spirit of the moor sink into one's soul , its vastness , and also its grim charm .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">that's</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch1 s113 : " Dear , dear , that's bad ! " said Holmes , shaking his head .</p>
<p>HoundOfTheBaskervilles_ch6 s86 : The farmers about here don't like it , sir , and that's a fact . "</p>
<p>HoundOfTheBaskervilles_ch12 s256 : It's the man himself , by all that's wonderful and audacious !</p>
<p>HoundOfTheBaskervilles_ch12 s261 : " Why , Dr . Watson , that's not you , is it ?</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">there's</td>
<td style="text-align: right;">4</td>
<td><p>HoundOfTheBaskervilles_ch4 s157 : " And now there's this affair of the letter to me at the hotel .</p>
<p>HoundOfTheBaskervilles_ch5 s208 : " Why there's no good my telling you things , for you seem to know as much as I do already , " said he .</p>
<p>HoundOfTheBaskervilles_ch10 s120 : To rake this up couldn't help our poor master , and it's well to go carefully when there's a lady in the case .</p>
<p>HoundOfTheBaskervilles_ch10 s218 : " There's foul play somewhere , and there's black villainy brewing , to that I'll swear !</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">(</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch1 s79 : Author of ' Some Freaks of Atavism ' ( Lancet 1882 ) .</p>
<p>HoundOfTheBaskervilles_ch1 s80 : ' Do We Progress ? ' ( Journal of Psychology , March , 1883 ) .</p>
<p>HoundOfTheBaskervilles_ch2 s32 : " Know then that in the time of the Great Rebellion ( the history of which by the learned Lord Clarendon I most earnestly commend to your attention ) this Manor of Baskerville was held by Hugo of that name , nor can it be gainsaid that he was a most wild , profane , and godless man .</p>
<p>HoundOfTheBaskervilles_ch2 s34 : It chanced that this Hugo came to love ( if , indeed , so dark a passion may be known under so bright a name ) the daughter of a yeoman who held lands near the Baskerville estate .</p>
<p>HoundOfTheBaskervilles_ch2 s39 : At last in the stress of her fear she did that which might have daunted the bravest or most active man , for by the aid of the growth of ivy which covered ( and still covers ) the south wall she came down from under the eaves , and so homeward across the moor , there being three leagues betwixt the Hall and her father's farm .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">)</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch1 s79 : Author of ' Some Freaks of Atavism ' ( Lancet 1882 ) .</p>
<p>HoundOfTheBaskervilles_ch1 s80 : ' Do We Progress ? ' ( Journal of Psychology , March , 1883 ) .</p>
<p>HoundOfTheBaskervilles_ch2 s32 : " Know then that in the time of the Great Rebellion ( the history of which by the learned Lord Clarendon I most earnestly commend to your attention ) this Manor of Baskerville was held by Hugo of that name , nor can it be gainsaid that he was a most wild , profane , and godless man .</p>
<p>HoundOfTheBaskervilles_ch2 s34 : It chanced that this Hugo came to love ( if , indeed , so dark a passion may be known under so bright a name ) the daughter of a yeoman who held lands near the Baskerville estate .</p>
<p>HoundOfTheBaskervilles_ch2 s39 : At last in the stress of her fear she did that which might have daunted the bravest or most active man , for by the aid of the growth of ivy which covered ( and still covers ) the south wall she came down from under the eaves , and so homeward across the moor , there being three leagues betwixt the Hall and her father's farm .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Don't</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch1 s96 : Don't move , I beg you , Watson .</p>
<p>HoundOfTheBaskervilles_ch4 s46 : " Don't you think that is an admirable sentiment ? "</p>
<p>HoundOfTheBaskervilles_ch4 s53 : ' You , ' ' your , ' ' your , ' ' life , ' ' reason , ' ' value , ' ' keep away , ' ' from the . ' Don't you see now whence these words have been taken ? "</p>
<p>HoundOfTheBaskervilles_ch9 s191 : " Don't ask me , Sir Henry - don't ask me !</p>
<p>HoundOfTheBaskervilles_ch12 s114 : Don't you think , Watson , that you are away from your charge rather long ?</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">That's</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch5 s40 : " That's just what I do mean to say .</p>
<p>HoundOfTheBaskervilles_ch5 s93 : " That's so , " said Baskerville .</p>
<p>HoundOfTheBaskervilles_ch5 s246 : That's how I come to know the name . "</p>
<p>HoundOfTheBaskervilles_ch9 s233 : " That's the truth , sir , " said Barrymore .</p>
<p>HoundOfTheBaskervilles_ch12 s63 : " That's better , " said he , seeing the shadow rise from my face .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">What's</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch4 s106 : What's this ? "</p>
<p>HoundOfTheBaskervilles_ch9 s104 : What's the matter with me , anyhow ?</p>
<p>HoundOfTheBaskervilles_ch10 s226 : What's he waiting for ?</p>
<p>HoundOfTheBaskervilles_ch12 s32 : What's this paper ?</p>
<p>HoundOfTheBaskervilles_ch14 s18 : What's the game now ? ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">friend's</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch6 s27 : " No , we have no news of any kind , " said Dr . Mortimer in answer to my friend's questions .</p>
<p>HoundOfTheBaskervilles_ch9 s85 : What all this meant I could not imagine , but I was deeply ashamed to have witnessed so intimate a scene without my friend's knowledge .</p>
<p>HoundOfTheBaskervilles_ch9 s132 : Our friend's title , his fortune , his age , his character , and his appearance are all in his favour , and I know nothing against him unless it be this dark fate which runs in his family .</p>
<p>HoundOfTheBaskervilles_ch12 s301 : I have no doubt that my friend's explanation will cover the facts .</p>
<p>HoundOfTheBaskervilles_ch14 s127 : Already our friend's eyelids shivered and he made a feeble effort to move .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">isn't</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch4 s55 : Well , if that isn't smart ! " cried Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch6 s89 : You see , it isn't like any ordinary convict .</p>
<p>HoundOfTheBaskervilles_ch6 s182 : " My word , it isn't a very cheerful place , " said Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch9 s136 : " l don't say now that he isn't a crazy man , " said Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch14 s80 : '' If he isn't out in a quarter of an hour the path will be covered .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">lady's</td>
<td style="text-align: right;">5</td>
<td><p>HoundOfTheBaskervilles_ch9 s133 : That his advances should be rejected so brusquely without any reference to the lady's own wishes and that the lady should accept the situation without protest is very amazing .</p>
<p>HoundOfTheBaskervilles_ch9 s146 : He would withdraw all opposition upon his part if I would promise for three months to let the matter rest and to be content with cultivating the lady's friendship during that time without claiming her love .</p>
<p>HoundOfTheBaskervilles_ch11 s27 : The freckles started out on the lady's face .</p>
<p>HoundOfTheBaskervilles_ch11 s53 : I knew already that Sir Charles Baskerville had made Stapleton his almoner upon several occasions , so the lady's statement bore the impress of truth upon it .</p>
<p>HoundOfTheBaskervilles_ch11 s127 : And yet the more I thought of the lady's face and of her manner the more I felt that something was being held back from me .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">n't</td>
<td style="text-align: right;">7</td>
<td><p>HoundOfTheBaskervilles_ch13 s9 : If I had n't sworn not to go about alone I might have had a more lively evening , for I had a message from Stapleton asking me over there . "</p>
<p>HoundOfTheBaskervilles_ch13 s11 : " By the way , I do n't suppose you appreciate that we have been mourning over you as having broken your neck ? "</p>
<p>HoundOfTheBaskervilles_ch13 s23 : I do n't know that Watson and I are much the wiser since we came down . "</p>
<p>HoundOfTheBaskervilles_ch13 s43 : " Watson wo n't allow that I know anything of art but that is mere jealousy because our views upon the subject differ .</p>
<p>HoundOfTheBaskervilles_ch13 s46 : " I do n't pretend to know much about these things , and I 'd be a better judge of a horse or a steer than of a picture .</p>
<p>HoundOfTheBaskervilles_ch13 s47 : I did n't know that you found time for such things . "</p>
<p>HoundOfTheBaskervilles_ch13 s248 : Ah , well , I do n't suppose you will forget your first visit . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">Holmes's</td>
<td style="text-align: right;">8</td>
<td><p>HoundOfTheBaskervilles_ch1 s105 : As he entered his eyes fell upon the stick in Holmes's hand , and he ran towards it with an exclamation of joy .</p>
<p>HoundOfTheBaskervilles_ch7 s49 : It seemed hopeless to pursue the inquiry any farther , but it was clear that in spite of Holmes's ruse we had no proof that Barrymore had not been in London all the time .</p>
<p>HoundOfTheBaskervilles_ch12 s61 : I was still rather raw over the deception which had been practised upon me , but the warmth of Holmes's praise drove my anger from my mind .</p>
<p>HoundOfTheBaskervilles_ch12 s122 : Holmes's voice sank as he answered :</p>
<p>HoundOfTheBaskervilles_ch12 s283 : By the way " - - his eyes darted again from my face to Holmes's - - " did you hear anything else besides a cry ? "</p>
<p>HoundOfTheBaskervilles_ch14 s0 : One of Sherlock Holmes's defects - - if , indeed , one may call it a defect - - was that he was exceedingly loath to communicate his full plans to any other person until the instant of their fullfilment .</p>
<p>HoundOfTheBaskervilles_ch14 s61 : Holmes's face was turned towards it , and he muttered impatiently as he watched its sluggish drift .</p>
<p>HoundOfTheBaskervilles_ch14 s101 : I was at Holmes's elbow , and I glanced for an instant at his face .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">o'clock</td>
<td style="text-align: right;">8</td>
<td><p>HoundOfTheBaskervilles_ch2 s101 : At twelve o'clock Barrymore , finding the hall door still open , became alarmed , and , lighting a lantern , went in search of his master .</p>
<p>HoundOfTheBaskervilles_ch3 s132 : At ten o'clock to-morrow , Dr . Mortimer , I will be much obliged to you if you will call upon me here , and it will be of help to me in my plans for the future if you will bring Sir Henry Baskerville with you . "</p>
<p>HoundOfTheBaskervilles_ch3 s154 : It was nearly nine o'clock when I found myself in the sitting-room once more .</p>
<p>HoundOfTheBaskervilles_ch4 s185 : " Then we meet again at two o'clock .</p>
<p>HoundOfTheBaskervilles_ch5 s206 : " Now , Clayton , tell me all about the fare who came and watched this house at ten o'clock this morning and afterwards followed the two gentlemen down Regent Street . "</p>
<p>HoundOfTheBaskervilles_ch9 s155 : I sat up with Sir Henry in his rooms until nearly three o'clock in the morning , but no sound of any sort did we hear except the chiming clock upon the stairs .</p>
<p>HoundOfTheBaskervilles_ch11 s64 : It ran 'Please , please , as you are a gentleman , burn this letter , and be at the gate by ten o'clock .</p>
<p>HoundOfTheBaskervilles_ch14 s66 : It is already ten o'clock .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">'s</td>
<td style="text-align: right;">9</td>
<td><p>HoundOfTheBaskervilles_ch13 s18 : " That 's lucky for him - - in fact , it 's lucky for all of you , since you are all on the wrong side of the law in this matter .</p>
<p>HoundOfTheBaskervilles_ch13 s20 : Watson 's reports are most incriminating documents . "</p>
<p>HoundOfTheBaskervilles_ch13 s49 : That 's a Kneller , I 'll swear , that lady in the blue silk over yonder , and the stout gentleman with the wig ought to be a Reynolds .</p>
<p>HoundOfTheBaskervilles_ch13 s64 : " There 's no doubt about the authenticity , for the name and the date , 1647 , are on the back of the canvas . "</p>
<p>HoundOfTheBaskervilles_ch13 s100 : And I have also communicated with my faithful Cartwright , who would certainly have pined away at the door of my hut , as a dog does at his master 's grave , if I had not set his mind at rest about my safety . "</p>
<p>HoundOfTheBaskervilles_ch13 s116 : The baronet 's face perceptibly lengthened .</p>
<p>HoundOfTheBaskervilles_ch13 s125 : I saw by the baronet 's clouded brow that he was deeply hurt by what he regarded as our desertion .</p>
<p>HoundOfTheBaskervilles_ch13 s198 : Here are three written descriptions by trustworthy witnesses of Mr . and Mrs . Vandeleur , who at that time kept St . Oliver 's private school .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Henry's</td>
<td style="text-align: right;">9</td>
<td><p>HoundOfTheBaskervilles_ch7 s117 : My first thought was that I should be by Sir Henry's side .</p>
<p>HoundOfTheBaskervilles_ch7 s305 : " I am Sir Henry's friend , and his welfare is a very close concern of mine .</p>
<p>HoundOfTheBaskervilles_ch7 s330 : That is Sir Henry's nature .</p>
<p>HoundOfTheBaskervilles_ch8 s59 : The Stapletons came in afterwards , and the good doctor took us all to the yew alley at Sir Henry's request to show us exactly how everything occurred upon that fatal night .</p>
<p>HoundOfTheBaskervilles_ch10 s228 : It means no good to anyone of the name of Baskerville , and very glad I shall be to be quit of it all on the day that Sir Henry's new servants are ready to take over the Hall . "</p>
<p>HoundOfTheBaskervilles_ch12 s84 : " Sir Henry's falling in love could do no harm to anyone except Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch12 s234 : Boots , shirt , cap - - it was all Sir Henry's .</p>
<p>HoundOfTheBaskervilles_ch12 s238 : " It is clear enough that the hound has been laid on from some article of Sir Henry's - - the boot which was abstracted in the hotel , in all probability - - and so ran this man down .</p>
<p>HoundOfTheBaskervilles_ch14 s247 : '' It is our friend Sir Henry's missing boot . ''</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">There's</td>
<td style="text-align: right;">9</td>
<td><p>HoundOfTheBaskervilles_ch4 s201 : " There's our man , Watson !</p>
<p>HoundOfTheBaskervilles_ch5 s261 : There's another one waiting for you if you can bring any more information .</p>
<p>HoundOfTheBaskervilles_ch6 s84 : " There's a convict escaped from Princetown , sir .</p>
<p>HoundOfTheBaskervilles_ch9 s116 : There's a light in a woman's eyes that speaks louder than words .</p>
<p>HoundOfTheBaskervilles_ch10 s57 : There's no safety for anyone untill he is under lock and key . "</p>
<p>HoundOfTheBaskervilles_ch10 s218 : " There's foul play somewhere , and there's black villainy brewing , to that I'll swear !</p>
<p>HoundOfTheBaskervilles_ch10 s224 : There's not a man would cross it after sundown if he was paid for it .</p>
<p>HoundOfTheBaskervilles_ch12 s333 : There's the devilish cunning of it !</p>
<p>HoundOfTheBaskervilles_ch14 s171 : '' There's someone in here , '' cried Lestrade .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">it's</td>
<td style="text-align: right;">9</td>
<td><p>HoundOfTheBaskervilles_ch3 s160 : " No , it's this poisonous atmosphere . "</p>
<p>HoundOfTheBaskervilles_ch4 s155 : You don't seem quite to have made up your mind whether it's a case for a policeman or a clergyman . "</p>
<p>HoundOfTheBaskervilles_ch4 s176 : Now , look here , Mr . Holmes , it's half-past eleven now and I am going back right away to my hotel.-</p>
<p>HoundOfTheBaskervilles_ch5 s38 : And now it's an old black one . "</p>
<p>HoundOfTheBaskervilles_ch5 s49 : " Mind it is , for it's the last thing of mine that I'll lose in this den of thieves .</p>
<p>HoundOfTheBaskervilles_ch5 s51 : " I think it's well worth troubling about . "</p>
<p>HoundOfTheBaskervilles_ch5 s98 : " At the same time , " said Baskerville , " it's clear enough that so long as there are none of the family at the Hall these people have a mighty fine home and nothing to do . "</p>
<p>HoundOfTheBaskervilles_ch7 s191 : " Yes , it's rather an uncanny place altogether .</p>
<p>HoundOfTheBaskervilles_ch10 s120 : To rake this up couldn't help our poor master , and it's well to go carefully when there's a lady in the case .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">woman's</td>
<td style="text-align: right;">9</td>
<td><p>HoundOfTheBaskervilles_ch2 s161 : " A man's or a woman's ? "</p>
<p>HoundOfTheBaskervilles_ch7 s307 : " A woman's whim , Dr . Watson .</p>
<p>HoundOfTheBaskervilles_ch9 s116 : There's a light in a woman's eyes that speaks louder than words .</p>
<p>HoundOfTheBaskervilles_ch9 s218 : It was a woman's voice , and Mrs . Barrymore , paler and more horror-struck than her husband , was standing at the door .</p>
<p>HoundOfTheBaskervilles_ch9 s251 : The woman's words came with an intense earnestness which carried conviction with them .</p>
<p>HoundOfTheBaskervilles_ch10 s94 : " And the woman's name ? "</p>
<p>HoundOfTheBaskervilles_ch10 s101 : It was from Coombe Tracey , and it was addressed in a woman's hand . "</p>
<p>HoundOfTheBaskervilles_ch11 s120 : The woman's story hung coherently together , and all my questions were unable to shake it .</p>
<p>HoundOfTheBaskervilles_ch14 s235 : It helped us to realize the horror of this woman's life when we saw the eagerness and joy with which she laid us on her husband's track .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">man's</td>
<td style="text-align: right;">10</td>
<td><p>HoundOfTheBaskervilles_ch1 s71 : " As to the latter part , I have no means of checking you , " said I , " but at least it is not difficult to find out a few particulars about the man's age and professional career . "</p>
<p>HoundOfTheBaskervilles_ch2 s161 : " A man's or a woman's ? "</p>
<p>HoundOfTheBaskervilles_ch3 s85 : " The original hound was material enough to tug a man's throat out , and yet he was diabolical as well . "</p>
<p>HoundOfTheBaskervilles_ch4 s241 : Could you swear to that man's face within the cab ? "</p>
<p>HoundOfTheBaskervilles_ch7 s25 : It was he who had been the first to discover the body of Sir Charles , and we had only his word for all the circumstances which led up to the old man's death .</p>
<p>HoundOfTheBaskervilles_ch8 s80 : At others he will with his own hands tear down some other man's gate and declare that a path has existed there from time immemorial , defying the owner to prosecute him for trespass .</p>
<p>HoundOfTheBaskervilles_ch8 s107 : I have always felt that there was something singular and questionable in this man's character , but the adventure of last night brings all my suspicions to a head .</p>
<p>HoundOfTheBaskervilles_ch9 s208 : The man's face became openly defiant .</p>
<p>HoundOfTheBaskervilles_ch12 s347 : Again , there was no direct connection between the hound and the man's death .</p>
<p>HoundOfTheBaskervilles_ch12 s349 : We heard it , but we could not prove that it was running upon this man's trail .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">I'll</td>
<td style="text-align: right;">11</td>
<td><p>HoundOfTheBaskervilles_ch4 s178 : I'll be able to tell you more clearly then how this thing strikes me . "</p>
<p>HoundOfTheBaskervilles_ch4 s184 : " I'll join you in a walk , with pleasure , " said his companion .</p>
<p>HoundOfTheBaskervilles_ch5 s47 : " Well , either that boot comes back before sundown or I'll see the manager and tell him that I go right straight out of this hotel . "</p>
<p>HoundOfTheBaskervilles_ch5 s49 : " Mind it is , for it's the last thing of mine that I'll lose in this den of thieves .</p>
<p>HoundOfTheBaskervilles_ch5 s158 : If you will come down to Baskerville Hall and see me through I'll never forget it . "</p>
<p>HoundOfTheBaskervilles_ch6 s118 : I'll have a row of electric lamps up here inside of six months , and you won't know it again , with a thousand candle-power Swan and Edison right here in front of the hall door . "</p>
<p>HoundOfTheBaskervilles_ch9 s115 : I tell you , Watson , I've only known her these few weeks , but from the first I just felt that she was made for me , and she , too - she was happy when she was with me , and that I'll swear .</p>
<p>HoundOfTheBaskervilles_ch9 s130 : Just tell me what it all means , Watson , and I'll owe you more than ever I can hope to pay . "</p>
<p>HoundOfTheBaskervilles_ch9 s338 : " I don't think I'll get that cry out of my head .</p>
<p>HoundOfTheBaskervilles_ch10 s218 : " There's foul play somewhere , and there's black villainy brewing , to that I'll swear !</p>
<p>HoundOfTheBaskervilles_ch11 s39 : " Well , I'll answer , " she said .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">can't</td>
<td style="text-align: right;">11</td>
<td><p>HoundOfTheBaskervilles_ch4 s154 : But as to my uncle's death - well , it all seems boiling up in my head , and I can't get it clear yet .</p>
<p>HoundOfTheBaskervilles_ch5 s32 : By thunder , if that chap can't find my missing boot there will be trouble .</p>
<p>HoundOfTheBaskervilles_ch5 s257 : " No , I can't say that . "</p>
<p>HoundOfTheBaskervilles_ch7 s304 : " But I can't forget them , Miss Stapleton , " said I .</p>
<p>HoundOfTheBaskervilles_ch9 s101 : " I can't say that he ever did . "</p>
<p>HoundOfTheBaskervilles_ch9 s109 : " He can't object to my worldly position , so it must be myself that he has this down on .</p>
<p>HoundOfTheBaskervilles_ch9 s137 : " I can't forget the look in his eyes when he ran at me this morning , but I must allow that no man could make a more handsome apology than he has done . "</p>
<p>HoundOfTheBaskervilles_ch10 s64 : You can't tell on him without getting my wife and me into trouble .</p>
<p>HoundOfTheBaskervilles_ch10 s95 : " I can't give you the name , sir , but I can give you the initials .</p>
<p>HoundOfTheBaskervilles_ch10 s167 : " There are a few gipsies and labouring folk for whom I can't answer , but among the farmers or gentry there is no one whose initials are those .</p>
<p>HoundOfTheBaskervilles_ch14 s65 : He can't be very long , now .</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">I've</td>
<td style="text-align: right;">12</td>
<td><p>HoundOfTheBaskervilles_ch4 s6 : I understand that you think out little puzzles , and I've had one this morning which wants more thinking out than I am able to give it . "</p>
<p>HoundOfTheBaskervilles_ch4 s152 : " Of course , I've heard of the hound ever since I was in the nursery .</p>
<p>HoundOfTheBaskervilles_ch5 s134 : I've had no time , for it was only yesterday that I learned how matters stood .</p>
<p>HoundOfTheBaskervilles_ch5 s196 : " I've driven my cab this seven years and never a word of complaint .</p>
<p>HoundOfTheBaskervilles_ch5 s200 : " Well , I've had a good day and no mistake , " said the cabman with a grin .</p>
<p>HoundOfTheBaskervilles_ch5 s269 : I've been checkmated in London .</p>
<p>HoundOfTheBaskervilles_ch6 s48 : " I've been over a good part of the world since I left it , Dr . Watson , " said he ; " but I have never seen a place to compare with it . "</p>
<p>HoundOfTheBaskervilles_ch7 s176 : I've heard it once or twice before , but never quite so loud . "</p>
<p>HoundOfTheBaskervilles_ch9 s115 : I tell you , Watson , I've only known her these few weeks , but from the first I just felt that she was made for me , and she , too - she was happy when she was with me , and that I'll swear .</p>
<p>HoundOfTheBaskervilles_ch10 s83 : I've never breathed a word about it yet to mortal man .</p>
<p>HoundOfTheBaskervilles_ch10 s197 : I've not heard of him since I left out food for him last , and that was three days ago . "</p>
<p>HoundOfTheBaskervilles_ch11 s156 : And I've closed the wood where the Fernworthy folk used to picnic .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">:</td>
<td style="text-align: right;">19</td>
<td><p>HoundOfTheBaskervilles_ch2 s19 : At the head was written : " Baskerville Hall , " and below in large , scrawling figures : " 1742 . "</p>
<p>HoundOfTheBaskervilles_ch2 s28 : Dr . Mortimer turned the manuscript to the light and read in a high , cracking voice the following curious , old-world narrative :</p>
<p>HoundOfTheBaskervilles_ch2 s80 : Our visitor readjusted his glasses and began :</p>
<p>HoundOfTheBaskervilles_ch2 s162 : Dr . Mortimer looked strangely at us for an instant , and his voice sank almost to a whisper as he answered :</p>
<p>HoundOfTheBaskervilles_ch4 s26 : It ran :</p>
<p>HoundOfTheBaskervilles_ch5 s90 : Very good , we will send a second wire to the postmaster , Grimpen : ' Telegram to Mr . Barrymore to be delivered into his own hand .</p>
<p>HoundOfTheBaskervilles_ch5 s181 : The first ran :</p>
<p>HoundOfTheBaskervilles_ch5 s184 : The second :</p>
<p>HoundOfTheBaskervilles_ch5 s245 : Only just as he was leaving he turned round and he said : ' It might interest you to know that you have been driving Mr . Sherlock Holmes . '</p>
<p>HoundOfTheBaskervilles_ch8 s3 : My dear Holmes :</p>
<p>HoundOfTheBaskervilles_ch9 s2 : M Y D E A R H O L M E S :</p>
<p>HoundOfTheBaskervilles_ch9 s91 : I explained everything to him : how I had found it impossible to remain behind , how I had followed him , and how I had witnessed all that had occurred .</p>
<p>HoundOfTheBaskervilles_ch10 s106 : It seemed to us to be a postscript at the end of the letter and it said : ' Please , please , as you are a gentleman , burn this letter , and be at the gate by ten o clock .</p>
<p>HoundOfTheBaskervilles_ch11 s270 : I raised it , and this was what I read , roughly scrawled in pencil : " Dr . Watson has gone to Coombe Tracey . "</p>
<p>HoundOfTheBaskervilles_ch12 s52 : I brought Cartwright down with me - - you remember the little chap at the express office - - and he has seen after my simple wants : a loaf of bread and a clean collar .</p>
<p>HoundOfTheBaskervilles_ch12 s122 : Holmes's voice sank as he answered :</p>
<p>HoundOfTheBaskervilles_ch12 s239 : There is one very singular thing , however : How came Selden , in the darkness , to know that the hound was on his trail ? "</p>
<p>HoundOfTheBaskervilles_ch13 s157 : It ran :</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">It's</td>
<td style="text-align: right;">19</td>
<td><p>HoundOfTheBaskervilles_ch4 s153 : It's the pet story of the family , though I never thought of taking it seriously before .</p>
<p>HoundOfTheBaskervilles_ch4 s174 : It's a big thing for a man to have to understand and to decide at one sitting .</p>
<p>HoundOfTheBaskervilles_ch5 s274 : It's an ugly business , Watson , an ugly dangerous business , and the more I see of it the less I like it .</p>
<p>HoundOfTheBaskervilles_ch6 s116 : " It's no wonder my uncle felt as if trouble were coming on him in such a place as this , " said he .</p>
<p>HoundOfTheBaskervilles_ch6 s117 : " It's enough to scare any man .</p>
<p>HoundOfTheBaskervilles_ch6 s142 : " It's just as I imagined it , " said Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch7 s151 : " It's gone ! " said he . " The mire has him .</p>
<p>HoundOfTheBaskervilles_ch7 s153 : It's a bad place , the great Grimpen Mire . "</p>
<p>HoundOfTheBaskervilles_ch7 s183 : It's the mud settling , or the water rising , or something . "</p>
<p>HoundOfTheBaskervilles_ch7 s188 : " It's a very rare bird - practically extinct - in England now , but all things are possible upon the moor .</p>
<p>HoundOfTheBaskervilles_ch7 s190 : " It's the weirdest , strangest thing that ever I heard in my life . "</p>
<p>HoundOfTheBaskervilles_ch9 s298 : It's a sound they have on the moor .</p>
<p>HoundOfTheBaskervilles_ch10 s84 : It's about poor Sir Charles's death . "</p>
<p>HoundOfTheBaskervilles_ch10 s217 : " It's all these goings-on , sir , " he cried at last , waving his hand towards the rain-lashed window which faced the moor .</p>
<p>HoundOfTheBaskervilles_ch12 s256 : It's the man himself , by all that's wonderful and audacious !</p>
<p>HoundOfTheBaskervilles_ch14 s62 : '' It's moving towards us , Watson . ''</p>
<p>HoundOfTheBaskervilles_ch14 s98 : It's coming ! ''</p>
<p>HoundOfTheBaskervilles_ch14 s132 : '' It's dead , whatever it is , '' said Holmes .</p>
<p>HoundOfTheBaskervilles_ch14 s161 : '' It's a thousand to one against our finding him at the house , '' he continued as we retraced our steps swiftly down the path .</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Charles's</td>
<td style="text-align: right;">24</td>
<td><p>HoundOfTheBaskervilles_ch2 s93 : Their evidence , corroborated by that of several friends , tends to show that Sir Charles's health has for some time been impaired , and points especially to some affection of the heart , manifesting itself in changes of colour , breathlessness , and acute attacks of nervous depression .</p>
<p>HoundOfTheBaskervilles_ch2 s102 : The day had been wet , and Sir Charles's footmarks were easily traced down the alley .</p>
<p>HoundOfTheBaskervilles_ch2 s109 : No signs of violence were to be discovered upon Sir Charles's person , and though the doctor's evidence pointed to an almost incredible facial distortion - so great that Dr . Mortimer refused at first to believe that it was indeed his friend and patient who lay before him - it was explained that that is a symptom which is not unusual in cases of dyspnoea and death from cardiac exhaustion .</p>
<p>HoundOfTheBaskervilles_ch2 s111 : It is well that this is so , for it is obviously of the utmost importance that Sir Charles's heir should settle at the Hall and continue the good work which has been so sadly interrupted .</p>
<p>HoundOfTheBaskervilles_ch2 s132 : " Within the last few months it became increasingly plain to me that Sir Charles's nervous system was strained to the breaking point .</p>
<p>HoundOfTheBaskervilles_ch2 s150 : " On the night of Sir Charles's death Barrymore the butler who made the discovery , sent Perkins the groom on horseback to me , and as I was sitting up late I was able to reach Baskerville Hall within an hour of the event .</p>
<p>HoundOfTheBaskervilles_ch3 s89 : You tell me in the same breath that it is useless to investigate Sir Charles's death , and that you desire me to do it . "</p>
<p>HoundOfTheBaskervilles_ch3 s97 : I speak now not as a medical man but as a trustee and executor of Sir Charles's will . "</p>
<p>HoundOfTheBaskervilles_ch5 s78 : Barrymore , Sir Charles's butler , is a man with a full , black beard . "</p>
<p>HoundOfTheBaskervilles_ch5 s100 : " Did Barrymore profit at all by Sir Charles's will ? " asked Holmes .</p>
<p>HoundOfTheBaskervilles_ch5 s121 : " Since Rodger Baskerville , Sir Charles's younger brother died unmarried , the estate would descend to the Desmonds , who are distant cousins .</p>
<p>HoundOfTheBaskervilles_ch5 s129 : " And this man of simple tastes would be the heir to Sir Charles's thousands . "</p>
<p>HoundOfTheBaskervilles_ch5 s177 : Setting aside the whole grim story , of Sir Charles's death , we had a line of inexplicable incidents all within the limits of two days , which included the receipt of the printed letter , the black-bearded spy in the hansom , the loss of the new brown boot , the loss of the old black boot , and now the return of the new brown boot .</p>
<p>HoundOfTheBaskervilles_ch6 s52 : Poor Sir Charles's head was of a very rare type , half Gaelic , half Ivernian in its characteristics .</p>
<p>HoundOfTheBaskervilles_ch6 s110 : The lodge was a ruin of black granite and bared ribs of rafters , but facing it was a new building , half constructed , the first fruit of Sir Charles's South African gold .</p>
<p>HoundOfTheBaskervilles_ch6 s169 : Sir Charles's generosity has given us the means to do so .</p>
<p>HoundOfTheBaskervilles_ch10 s84 : It's about poor Sir Charles's death . "</p>
<p>HoundOfTheBaskervilles_ch10 s104 : Only a few weeks ago she was cleaning out Sir Charles's study - it had never been touched since his death - and she found the ashes of a burned letter in the back of the grate .</p>
<p>HoundOfTheBaskervilles_ch10 s116 : But I expect if we could lay our hands upon that lady we should know more about Sir Charles's death . "</p>
<p>HoundOfTheBaskervilles_ch10 s221 : " Look at Sir Charles's death !</p>
<p>HoundOfTheBaskervilles_ch11 s51 : One was Mr . Stapleton , a neighbour and intimate friend of Sir Charles's .</p>
<p>HoundOfTheBaskervilles_ch11 s59 : " Not on the very day of Sir Charles's death ? "</p>
<p>HoundOfTheBaskervilles_ch11 s115 : I knew Sir Charles's generosity , and I thought that if he heard the story from my own lips he would help me . "</p>
<p>HoundOfTheBaskervilles_ch12 s338 : " There is Sir Charles's death . "</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">don't</td>
<td style="text-align: right;">30</td>
<td><p>HoundOfTheBaskervilles_ch3 s9 : I don't suppose I should have done so had I not known this legend . "</p>
<p>HoundOfTheBaskervilles_ch3 s212 : I think we'll shut that window again , if you don't mind .</p>
<p>HoundOfTheBaskervilles_ch4 s48 : " I don't know much about the tariff and things of that kind , " said he , " but it seems to me we've got a bit off the trail so far as that note is concerned . "</p>
<p>HoundOfTheBaskervilles_ch4 s122 : " I don't know much of British life yet , for I have spent nearly all my time in the States and in Canada .</p>
<p>HoundOfTheBaskervilles_ch4 s155 : You don't seem quite to have made up your mind whether it's a case for a policeman or a clergyman . "</p>
<p>HoundOfTheBaskervilles_ch5 s39 : " What ! you don't mean to say ? "</p>
<p>HoundOfTheBaskervilles_ch5 s44 : Speak out , man , and don't stand staring ! "</p>
<p>HoundOfTheBaskervilles_ch5 s54 : " I just don't attempt to explain it .</p>
<p>HoundOfTheBaskervilles_ch5 s58 : " Well , I don't profess to understand it yet .</p>
<p>HoundOfTheBaskervilles_ch5 s255 : I don't know as I could say more than that . "</p>
<p>HoundOfTheBaskervilles_ch6 s86 : The farmers about here don't like it , sir , and that's a fact . "</p>
<p>HoundOfTheBaskervilles_ch6 s130 : " You don't mind my driving straight home , Sir Henry ? " said Dr . Mortimer .</p>
<p>HoundOfTheBaskervilles_ch6 s184 : I don't wonder that my uncle got a little jumpy if he lived all alone in such a house as this .</p>
<p>HoundOfTheBaskervilles_ch7 s180 : You don't believe such nonsense as that ? " said I .</p>
<p>HoundOfTheBaskervilles_ch9 s90 : " You don't mean to say that you came after me in spite of all ? "</p>
<p>HoundOfTheBaskervilles_ch9 s136 : " l don't say now that he isn't a crazy man , " said Sir Henry .</p>
<p>HoundOfTheBaskervilles_ch9 s191 : " Don't ask me , Sir Henry - don't ask me !</p>
<p>HoundOfTheBaskervilles_ch9 s297 : " I don't know .</p>
<p>HoundOfTheBaskervilles_ch9 s328 : You don't believe it , do you , Watson ? "</p>
<p>HoundOfTheBaskervilles_ch9 s334 : I don't think that I am a coward , Watson , but that sound seemed to freeze my very blood .</p>
<p>HoundOfTheBaskervilles_ch9 s338 : " I don't think I'll get that cry out of my head .</p>
<p>HoundOfTheBaskervilles_ch10 s78 : But , after what we have heard I don't feel as if I could give the man up , so there is an end of it .</p>
<p>HoundOfTheBaskervilles_ch10 s87 : " No , sir , I don't know that . "</p>
<p>HoundOfTheBaskervilles_ch10 s195 : " I don't know , sir .</p>
<p>HoundOfTheBaskervilles_ch10 s210 : I don't like it , Dr . Watson - I tell you straight , sir , that I don't like it . "</p>
<p>HoundOfTheBaskervilles_ch10 s215 : Tell me , frankly , what it is that you don't like . "</p>
<p>HoundOfTheBaskervilles_ch11 s182 : " You don't mean that you know where he is ? " said I .</p>
<p>HoundOfTheBaskervilles_ch12 s265 : Not - - don't tell me that it is our friend Sir Henry ! "</p>
<p>HoundOfTheBaskervilles_ch14 s38 : Creep forward quietly and see what they are doing - - but for heaven's sake don't let them know that they are watched ! ''</p></td>
</tr>
<tr class="odd">
<td style="text-align: center;">;</td>
<td style="text-align: right;">42</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">'</td>
<td style="text-align: right;">63</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">''</td>
<td style="text-align: right;">165</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">!</td>
<td style="text-align: right;">182</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">?</td>
<td style="text-align: right;">514</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">"</td>
<td style="text-align: right;">2578</td>
<td></td>
</tr>
<tr class="odd">
<td style="text-align: center;">,</td>
<td style="text-align: right;">3197</td>
<td></td>
</tr>
<tr class="even">
<td style="text-align: center;">.</td>
<td style="text-align: right;">3224</td>
<td></td>
</tr>
</tbody>
</table>

<update date omitted for speed>{% endraw %}