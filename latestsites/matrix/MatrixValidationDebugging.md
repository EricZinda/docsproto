{% raw %}The way to debug these "no asterisk errors": Go into deffile.py to the
place where the "Create Grammar" button is being created. Instead of
passing in "len(errors) &gt; 0" as the last argument to html\_input()
(which disables the button if there are any errors), pass in "False"
instead. Then you can click the "Create Grammar" button and see the
old-style list-of-error-messages page. (sfd 6/29/09)

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}