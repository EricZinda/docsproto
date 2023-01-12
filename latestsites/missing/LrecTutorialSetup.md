{% raw %}# English Resource Semantics: Getting Started

This page describes how to get the support software for the ERS tutorial
onto your computer. We recommend tutorial attendees start with the
[VirtualBox](/VirtualBox) appliance, to reduce variability for hands-on
portions of the tutorial.

## VirtualBox Appliance

Here are the steps to get started with the VirtualBox appliance:

1. Install the VirtualBox installer, either from
<http://virtualbox.org> or from the tutorial USB key. You may be
prompted to (automatically) install drivers or be warned that
Microsoft has not tested the software.
2. Obtain the LREC appliance OVA file, either from
[here](http://uakari.ling.washington.edu/knoppixlkb/lrec/old/LREC_Appliance_Test_Build.ova)
or from the tutorial USB key.
3. Launch VirtualBox and choose "Import Appliance..." from the File
menu.
4. Select the .ova file and follow the onscreen instructions; default
options are fine. You will need at least 2GB of additional RAM
beyond what your OS and other running programs require, and 8GB of
hard disk space.
5. Select the new virtual machine and start it up.
6. Once the VM has booted (be patient - you may see a black screen in
the VM for a minute or two on first startup), select "Terminal
Emulator" from the menu (blue icon) in the upper left corner.

Known issues: Windows users who have Hyper-V/Hypervision will have to
uninstall it (or maybe just disable it) to run the VM (coreinfo.exe may
be useful in checking what is happening - see also
<http://superuser.com/a/768845>). If you obtain an error about USB 2.0
support, install the [VirtualBox](/VirtualBox) extensions (just download
and launch the extensions, no need to reimport the appliance). If you
get an error about 64-bit mode, you may need to enable virtualization in
the BIOS of your laptop (a symptom of this is that the Acceleration Tab
is greyed out in Settings / System in [VirtualBox](/VirtualBox)).

## Other Options

If you use Linux or MacOS X, you can install the ACE parser/generator
and the English Resource Grammar natively on your machine (i.e. without
using VirtualBox); however, file names and support software may not be
configured as assumed for the tutorial. The [ACE
homepage](http://sweaglesw.org/linguistics/ace/) has the relevant links
and some instructions; you may also find AceTop (in particular
AceInstall and AceLui) useful.

Serious users will also find the so-called LOGON tree of interest. This
collection of software includes tools for grammar engineering,
converting between output formats, inspecting and annotating treebanks,
parsing and generating, and more. See ErgProcessing and
LogonTop (especially LogonInstallation)
for instructions and more details.

## Acknowledgements

The above instructions for setting up VirtualBox are largely inspired by
[these
instructions](http://depts.washington.edu/uwcl/twiki/bin/view.cgi/Main/KnoppixLKBVboxApp)
for KnoppixLKB. Our thanks go to David Brodbeck for his assistance in
preparing the tutorial VirtualBox appliance.

## Tutorial Slides

The slides used in the LREC tutorial are temporarily
[here](http://www.cl.cam.ac.uk/~aac10/papers/ERS-slides.pdf)
<update date omitted for speed>{% endraw %}