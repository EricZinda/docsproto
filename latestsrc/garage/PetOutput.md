{% raw %}# Redirecting Pet's Output

For historical reasons, cheap doesn't send its output to STDOUT
(although it really should). You can get at the output by redirecting
STDERR, an example is given below:

    cat input.text | cheap -limit=10000 -mrs=xml japanese.grm &> output.xml

To get more output, increase the verbosity.

Last updated: commit 334494d7fe40040caa8f0f3268e3ef6a764b318a
Author: EricZinda <ericz@inductorsoftware.com>
Date:   Tue Oct 25 13:59:11 2022 -0700

    Updated ERDW_StructureForNewDocsSite (markdown)
{% endraw %}