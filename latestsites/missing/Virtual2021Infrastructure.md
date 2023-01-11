{% raw %}Moderators: Olga Zamaraeva, Michael Wayne Goodman, Alexandre Rademaker

Scribe: Emily M. Bender
* * *

For set up, see [slides](https://github.com/delph-in/docs/raw/main/summits/2021/delph-in_infrastructure.pdf)

[Note taking began partway through.]

EMB: Admins group should make proposal to SC re what kinds of decisions are admins only, and which SC, and how that communication will go.

Tuan Ahn: Suggests FAQ page, in the wiki, including info on who to contact with what kind of questions.

Olga: We have FAQs for specific projects, but not for GitHub yet.

Tuan Ahn: FAQ on how to use this wiki.

Tuan Ahn: One of the first questions I want to ask, is if I want to make some changes to the wiki, who do I contact? For example, the welcome page still has 

EMB: The ethos of the wiki has been generally "it's a wiki, please edit", with the exception of a few pages (e.g. the welcome page), which used to be proteced by ACL constraints on editing. I guess now that will just have to be a community consensus (and about far fewer pages).

Glenn: So the consensus on recent pages is that it can't happen?

MWG: Can, but not convenient. Wiki could be published as pages and then could work out how to do recent changes, but that would be our own work. Could also reimplement FortuneCookies. For other code, can set up things to fire whenever things are committed (Glenn: action, in the github parlance?), not sure if can do that for wikis but cron job equivs are possible.

Tuan Ahn: Maybe there's a service that can pull from public repos to make web page adn that would show the recent changes.

Alexandre: Want to emphasize the importance of a good review of the content of the wiki and its organization. I had to read the pages during the migration --- saw lots of info that could be better organized, better linked. As a community it would be nice if we can put some effort into revising info/contents. For example the contents we have for Summits. The structure is quite well defined: schedule, participants, notes. Maybe could create templates for this, maybe even outside the wiki.

Olga: Example: LogonParis breaks the connection from ParisX for the discussions there.

Glenn: Shouldn't there have been an actual hierarchical structure rather than just a prefix?

Olga: I think that's what Alexandre was arguing for.

EMB (in chat): This is a page I've maintained over the years with links to all discussions about MRS: https://github.com/delph-in/docs/wiki/RmrsDiscussions

Alexandre: Also within pages -- blocks of code not well marked up in the original MoinMoin (or tables) that couldn't be imported. This is why I'm calling for the attention of the community. Look at the pages where you care more and try to do some improvement. Also, the wiki in GitHub allows for different mark ups. Should we be flexible, or insist on a convention?

Olga: Would being flexible complicate future migration?

Alexandre: Yes, but sometimes I miss org mode. I didn't use it because I wanted to make things more consistent.

Dan: Some of these aren't meant to be dynamic, but rather archives of our work in the past. They are meant to be kept stable as a record of what happened then. There might be value both in organization and in accuracy to pull such pages out into an archive (where they aren't editable, or not as easily editable). The wiki is a great place to build those pages for the current pages but we might want to think about asking something (PC each year?) to archive them afterwards with the consistency you're talking about. Would be nice to have a first-class distinction between dynamic and archived pages.

Olga: That sounds like maybe a summit-specific repository, that could be published as a website.

Alexandre: Good point. When looking at things, I had the temptation to fix things in the old pages. It took me a while to understand that this is history---not appropriate to go back and change names that had since changed.

Olga: It's just because the wiki serves several purposes. It also serves the purpose of creating documentation---it hosts communication that should be updated.

Francis: Some of these practices, it would be good if they could be documented in an FAQ like Tuan Ahn suggested. How I've seen us using MoinMoin in the past is that sometimes things start off as a discussion and then someone copies that content to serve as the seed of documentation of something. Sometimes it would be good when we do that to put a disclaimer + a pointer to more current info. If we did have ideas of maybe a template saying "This is part of a Summit, so don't change it" v. "This something we'd like to keep updated more". Some of these are quite subtle: LogonParis is the correct name -- it's the Logon release associated with Paris, not the discussion of Logon at the Paris Summit. But these conventions are not well documented and probably not consistently followed. A little bit of guidance would probably help there. At NTU, I've been encouraging students to try and update pages as they do their work to try and keep things up to date, but of course it's a neverending struggle. One things we could look at is trying to do something like Google Summer of Code to get someone to reorg with real technical writers, but even supervising that is a fair bit of work.

MWG: Re ownership role: Happy to hand this over to the community and step back from managing it.

Olga: I think what's needed is more clarity and I'm sure we can develop the right practices that suit us.


Last update: 2021-07-20 by emilymbender [[edit](https://github.com/delph-in/docs/wiki/Virtual2021Infrastructure/_edit)]{% endraw %}