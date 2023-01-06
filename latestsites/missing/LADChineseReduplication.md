{% raw %}Scribed by Luís

FZZ - we had difficulties trying to implement the reduplication
phenomenon, for both semantic repression and HPSG syntactic formalism.
This reduplication can be applied to verb and adjectives, but also
classifiers and other classes (even if less frequently).

When adjectives are reduplicates, for example, some studies mention an
intensified or more vivid meaning. e.g. 红 hong (red) &gt; 红红 honghong
(A &gt; AA) 干净 ganjing (clean) &gt; 干干净净 ganganjingjing (very
clean) ( AB &gt; AABB)

After going through reduplication these words cannot undergo degree
modification (very, too, extremely, etc.). \* 很 hen (very) + 干干静静
ganganjingjing (very clean) - is ungrammatical But: 非常 feichang
(extremely) + 非常 feichang (extremely) + 干净 ganjing (clean) - is
grammatical

We’re currently analysing AABB types of reduplication by adding another
REL (redup\_rel) to the semantics; In the semantic representation we end
up with one non reduplicated predicate (e.g. ganjing) linked to a
redup\_rel.

But there are other patterns. ABB, for example, is similar in some ways
(for instance it cannot be modified for degree). But for words like
绿油油 lüyouyou (green-oil-oil) has the the interpretation of ‘bright
green’,

GuyE: is it only in the specific case where you see this collocation?
Since 绿油 ‘lüyou’ (green-oil) cannot stand alone…

FZZ: I was tempted to separate an analyse this as 绿 lü (green) + 油油
youyou (oil-oil), but we ended up not doing this because its not very
productive. For now we’re treating these cases are as a different
lexical type. There are other reduplication patterns for adjectives, but
they are not so productive as AABB…

FCB: How productive are they?

FZZ: Academia Sinica treats these adjectives as stative verbs. But I
checked them, and not all these stative verbs can undergo this
reduplication. I think only about 50% would

For verb reduplication there are also a few patterns: AA, ABAB, ABB,
etc.

我们 women (we) 聊聊 liaoliao (chat-chat)

This kind of reduplication has been referred to add a “tentative” aspect
by Li and Thompson. But there are other kind of reduplication patterns
where something can come between the reduplicated words. They keep the
same meaning of a “tentative” aspect, but add some other information
(e.g. like it’s past/perfective).

A 一 yi (one) A, A 了 le (PRF marker) A, A 了 le (PRF marker) 一 yi
(one) A, A A 看 kan (see/try), ….. Some of these refer to events that
happened in the past A 了 A, A 了 一 A. And AA 看 has the added meaning
“of try”.

GuyE: can you say 吃吃饭 chi chi fan (eat-eat-rice, but eat-rice is
often considered lexicalized ‘to eat’ )?

FZZ: yes, this is an instance of AAB reduplication.

JSio: In Chinese you can also reduplicate a CL to get the meaning of
‘every’, and most classifiers can do this (sortal and mensural). But
there is a difference between Mandarin and Cantonese, suppose you have
CL-CL student very smart (every student is very smart), in mandarin you
can’t say it like this…

FZZ: you can… 个 个 ge-ge (CL-CL) 学生 xuesheng (student) is also
possible in mandarin, but it’s not the most frequent form.

GuyE/JSio/SSG: How about the scope resolution of 个 个 ge-ge (CL-CL)
学生 xuesheng (student) 都 dou (all) Joanna: 都 can have a couple of
different readings: ‘even’ and ‘all’; so it can mean ‘all the students
(have eaten)’, or ‘even the students (have eaten)’

FCB: We might step back from CLs to discuss more general questions. For
example: If you have a 2 character word with the form AB, how can we
produce things like AABB/ABAB?

EB: I’m not sure you can… You cannot do open arbitrary/ class
reduplication in FSTs;

DanF: I bet you that I can write a rule on LKB to build an inflected
form of a 2 letter word, basically from xy to xxyy!

FCB: My understanding was that we couldn’t, so if we can it would be
good to know. The second question is how to we decide between do a
lexical rule online and just listing them (doing them offline)? For some
of these types we have less than 200 entries that can undergo
reduplication. Even if we end up with different entries, we can make
them uniform. In Chinese we now have ‘first character’ as a feature
(because we are using this for various other things).

GuyE: Can orthography be a list of characters?

FCB/EB/DF: we could have it as a list of characters. EB: But Im pretty
sure the lkb morphology is only looking at one item in that list.

DanF: If we can list them (all the reduplicated lexical entries), we can
spend our time doing some more exciting. We lose some generalisation,
but that’s ok… We can do this using the irregs table, since keeping them
in two places is a burden for maintenance.

GE: Do these class AABB reduplications have changed properties? Are
there any other things that apply to this class only?

FCB: We are making the strong claim that that they share a predicate
(clean AB) is the same predicate as AABB, but with a very. It’s probably
true that there are exceptions…

Dan: I know Berthold is doing something that copies and carries on
copying thing… so it must be possible! Doubling is something we must be
able to do (e.g. bat &gt; batting), the is a rule that says copy the
letter! It is sustained in the core engine of LKB.

LMC: How are these reduplications usually segmented by the segmentation
tools?

SSG: It’s inconsistent! Reduplications are most common in speech, so
they don’t appear much in the available corpora used to train the
segmentation. The Stanford tools tend not to work well of reduplication.

FCB: We need to do it as a post process.

FZZ: In the cases where we have patterns like: A 一 yi (one) A, A 了 le
(PRF marker) A, A 了 le (PRF marker) 一 yi (one) A, A A 看 kan
(see/try)… How to do treat these?

FCB: If we don’t want to have two predicates in the semantics, we don’t
yet know what to do.

GuyE: Is the form ‘A 了 le (PRF marker) A’ productive?

FZZ: Probably not…

GuyE: How about applying some kind of reentrancy with the phonology?

FCB: We’ll be discussing this for A NOT A, but I don’t know how to do
it…

MikeG: There is at least on example, the word for chewy (that in Chinese
is used Q, at least in Taiwan), and you can reduplicate it.

FCB: If there is one new word every 50 years is ok not to worry about
them…

SSG: Currently we are using a feature FCHAR (first character) WCHAR
(whole string) LENGTH (1, 2 or more than 2).

FZZ: I think this could be done with a function somewhere else.

DanF: We could make STEM to be language specific (configurable), and
that when you give a multi token stem, it is analogous to what we do
with MWE. And we could treat this STEM as a list. It becomes a first
class object. And then we would not need to maintain the F and W CHAR.

GuyE: Again the idea of reentrancy would apply here.

FCB: I feel we’re breaking something if we do that. We’re taking
something of the RELS list. By definition is the RELS list of the mother
is the sum of the daughter’s

EB: I would be pleasantly surprised if the morphology machinery allows
this.

FCB: If the morphology machinery does’t allow, there are other ways…

EB: You have a few forms for the verbs… the ones that were showing in
the middle you want do to the reduplication and the infixing in one
rule.

FZZ: This reduplication is actually not very present in our working
corpus, so dealing with this won’t give much coverage boost.

DAN: How about chat logs?

FZZ: Too noisy… They even create acronyms that get popular for a period
of time…

FCB: Summarising: we’re still not quite clear if we understand how
powerful the morphology is in our current system. But we’re confident
that using lexical rules are the way to go (even if they are only
triggered by irregular forms). That answered most of our questions. It
would be nice to sit down and see if we could implement this in the
morphology in the next days. And it would also be nice to further
discuss the CL reduplication (because they are much more general),

GuyE: Doing it in the syntax could also be nice to try.

DanF: It really breaks the semantics!

EB: It breaks monotonicity.

SSG: We didn’t discuss about the semantics of this intensification! The
‘redup\_x\_rel’ the reduplication adds, introduces a degree modifier.
And there are many (很, 非常, etc.), but I’m not even sure if it’s
necessary.

FCB: What we would like to do is if we’re translating into Chinese, if
we have ‘very + adj’, the the intensifier in Chinese would be either 很
hen (very) or reduplication.

EB: But isn’t 很 hen (very) sometimes used without introducing the
semantics of ‘very’?

FCB: We probably need something else do differentiate the dummy 很 and
the intensifier 很.

GuyE: How about 这个不好那个好 zhe-ge-bu-hao-na-ge-hao
(this-one-not-good-that-one-good)? You don’t really need to use the
predicative 很 all the time.

FZZ: Yes, that is possible. All these problems are actually related to
‘A-NOT-A’.

FCB: For Indonesian we also get reduplication of adjectives, but the
semantics are different?

DavidM: Depends on the adjective and depends on the context.

FCB: does it also work for Multi-word adjectives? (e.g. green-blue)

DavidM: Yes, you can reduplicate that.

FZZ: also in Singlish ‘eyes small-small’ (cute’ishly small)
<update date omitted for speed>{% endraw %}