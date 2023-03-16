{% raw %}Create a directory for the tools and for the result

    mkdir dkpro
    mkdir dkpro/tools
    mkdir dkpro/result

Download the code:

    cd dkpro/tools
    
    git pull https://github.com/kouylekov-usit/dkpro-core.git
    git pull https://github.com/dkpro/dkpro-meta.git
    
    svn co http://svn.emmtee.net/ltg/snug/milen/lap-jar-builder
    
    svn co http://svn.emmtee.net/ltg/snug/milen/dkpro-lap

Execute the script in the "lap-jar-builder" folder

    cd dkpro
    tools/lap-jar-builder/lap-jar-builder/jarbuild.sh dkpro/tools dkpro/result

Last update: 2016-12-19 by MilenKouylekov [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_DKPROCompilation/_edit)]{% endraw %}