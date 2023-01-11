{% raw %}# Background

Linux distributions differ, particularly so in the selection of tools
and libraries pre-installed in standard configurations. This page
provides Fedora-specific information related to installing and operating
the LOGON infrastructure (for general installation guidelines, please
see the LogonInstallation page). The information on
this page is user-provided documentation. As you extend or revise the
page, please take care to spell out (a) the specific problem to be
addressed, including observable symptoms; (b) the exact platform (32- or
64-bit) and version of the distribution affected; and (c) the exact
procedure to be applied for fixing the problem.

See also: LogonUbuntu \| LogonArch \|
LogonInstallation

# 32-Bit Compatibility Libraries

Check your Fedora version

    [tuananh@localhost ~]$ uname -ro
    4.5.5-300.fc24.x86_64 GNU/Linux

On Fedora 24, 64-bit version, install these:

    dnf install -y libpng.i686
    dnf install -y motif.i686 fontconfig.i686 libpng12.i686 libXext.i686 libjpeg-turbo.i686 libX11.i686 libXpm.i686 libXt.i686 libXmu.i686 libXft.i686

if you see this error message

    The downloaded packages were saved in cache until the next successful transaction.
    You can remove cached packages by executing 'dnf clean packages'.
    Error: Transaction check error:
      file /usr/share/licenses/libpng/LICENSE from install of libpng-2:1.6.23-1.fc24.i686 conflicts with file from package libpng-2:1.6.21-2.fc24.x86_64
      file /usr/share/man/man5/png.5.gz from install of libpng-2:1.6.23-1.fc24.i686 conflicts with file from package libpng-2:1.6.21-2.fc24.x86_64

You may try to update libpng 64-bit version

    dnf update libpng

If you can't use answer (built-in version of ACE) with yzlui, it means
that yzlui binary is not in the PATH, try adding this to your \~/.bashrc
file, logout and login again:

    export PATH=$PATH:~/logon/lingo/lkb/bin/linux.x86.64

Now try

    answer -g erg.dat -l

With this, you will have most of the logon running, including TSDB++ and
Emacs' LkbMode. However, some menus in LKB are still not
accessible, e.g. LKB\\View\\Type Hierarchy

    Error: Received signal number 11 (Segmentation fault)
      [condition type: SYNCHRONOUS-OPERATING-SYSTEM-SIGNAL]
    
    Restart actions (select using :continue):
     0: Return to Lkb Top command level
     1: Lkb Top top level
     2: Exit Lkb Top
     3: Abort entirely from this (lisp) process.
    
    [changing package from "COMMON-LISP-USER" to "TSDB"]
    [Current process: start-lkb-frame]

# Fedora 31 (64-Bit)

      dnf install -y libnsl motif xorg-x11-fonts-*

Last update: 2019-11-24 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LogonFedora/_edit)]{% endraw %}