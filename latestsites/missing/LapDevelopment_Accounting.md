{% raw %}# General Background

A key property of LAP is scalability, i.e. the ability to transparently
submit jobs on the Norwegian national high-performance computing cluster
[ABEL](http://www.uio.no/english/services/it/research/hpc/abel/) (which
is operated at the University of Oslo). Through the standard Galaxy
in-browser user interface, tools and workflows can be configured to
execute on ABEL compute nodes; this tight integration, as well as
general principles for the allocation of compute resources, follows the
model of the [LifePortal](https://lifeportal.uio.no/) computing
services.

# Resource Allocation

LAP developers have met with members of the LifePortal community and the
Notur Resource Allocation Committee (RFK) to understand the parameters
of existing usage constraints and policies and to design a LAP-specific
allocation policy. For the LAP prototype in the 2014 and 2015 allocation
periods, we will ‘borrow’ core hours from the pre-existing Notur
projects nn9106k (and maybe xa9910k), which are managed by
StephanOepen. Starting with the allocation period
2016.1, LAP will apply for a dedicated Notur project.

While we are working to establish the service, LAP will experiment with
a generous adaptation of the LifePortal model, where (a) individual
users (including non-Norwegian ones) with a CLARIN association are
granted a standard quota of 10,000 cpu hours per six-month period; (b)
users or groups of users can apply for LAP projects, where a project
typically can receive an allocation of up to 200,000 cpu hours per
period; (c) users or groups of users can independently acquire Notur
allocations, which they can transparently use for LAP computation. In
the 2014 start-up phase, project requests of type (b) are evaluated by a
(preliminary) LAP Resource Allocation Committee, comprised of
StephanOepen and ErikVelldal.

# Accounting and Reporting

From the very beginning, it will be important to account accurately for
resource usage on ABEL: While jobs submitted through LAP will run as the
laportal system user on ABEL, their resource consumption must be traced
back to Galaxy users and LAP tools or workflows. For this purpose, LAP
will maintain its own GOLD accounting database, just like the
LifePortal, and also expects to make use of the same reporting
mechanisms.

# Technical Set-Up

# GOLD Administrator Interface

Last update: 2016-01-23 by StephanOepen [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_Accounting/_edit)]{% endraw %}