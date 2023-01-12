{% raw %}The purpose of this page is to document problems and solutions related
to LogonInstallation that can apply to any Linux
distribution. Distribution-specific troubleshooting pages can be found
at:

- LogonUbuntu
- LogonRedhat

## PVM issues

When running LOGON software, ensure that the LOGON-packaged version of
PVM is used and not a locally installed version. Sometimes problems can
be solved by clearing the \*.pvm\* files in $LOGONTMP (make sure running
instances of pvmd3 are closed first).

### "can't gethostbyname"

(From the mailinglist thread starting here:
<http://lists.delph-in.net/archive/itsdb/2011-August/000116.html>)

If LOGON is giving errors such as the following, then PVM is failing to
start:

    libpvm [pid27468] /tmp/.pvm.socket.goodmami: No such file or directory
    libpvm [pid27468] /tmp/.pvm.socket.goodmami: No such file or directory
    libpvm [pid27468] /tmp/.pvm.socket.goodmami: No such file or directory
    libpvm [pid27468]: pvm_mytid(): Can't contact local daemon
    libpvm [pid27468]: pvm_register(): Can't contact local daemon
    pvm_register(): unable to initialize virtual machine.

Try running pvmd3 directly from the command line. If you get an error
like the following, then it is likely your /etc/hosts file is not setup
correctly:

    $ ~/Development/logon/lingo/lkb/bin/linux.x86.64/pvmd3
    [pvmd pid6810] 09/01 14:36:00 master_config() goodmami-tablet: can't
    gethostbyname
    [pvmd pid6810] 09/01 14:36:00 pvmbailout(0)

The problem is that pvmd3 cannot resolve the $HOSTNAME (in this case
"goodmami-tablet") to an address. Inspect /etc/hosts, and if it looks
like the following:

    127.0.0.1               localhost.localdomain localhost
    ::1             localhost6.localdomain6 localhost6

...then change it to look like this (of course, replace
"goodmami-tablet" with your $HOSTNAME):

    127.0.0.1               localhost.localdomain localhost goodmami-tablet
    ::1             localhost6.localdomain6 localhost6

Last update: 2011-09-14 by MichaelGoodman [[edit](https://github.com/delph-in/docs/wiki/LogonTroubleshooting/_edit)]{% endraw %}