{% raw %}This is the version from 10.03.2016

# Background

The instructions on this page are intended to provide a step by step
installation of a lap+galaxy instance with:

- Abel Cluster Support
- FEIDE Authetification
- POSTGRES Data Storage
- Gold Accounting

# Server Preparation

In this section I will briefly describe the preparation of the server in
term of additional services that are not related to Galaxy and LAP. This
services must be present in order to do various actions like HTTP Proxy
and connection to Abel.

## Installing Postgres

PostgresSQL is the database used to store users data. The database is
provided by UIO DB Hotell

To install Postgres on Fedora/Redhat use the following command:

    yum install postgresql postgresql-server postgresql-devel postgresql-contrib

For test purposes you can initialize postgres server on local machine
that can be used by galaxy. This server will be replaced in the
production and development version of LAP. The local installation of
posgres should have an enabled ssl.

## Install Apache

The Apache server serves as a proxy and aggregate for both galaxy and
gold interfaces. It is used also from the module for Feide
authentication.

1\. Install apache server and appropriate mods.

    yum install httpd mod_ssl mod_auth_kerb mod_nss mod_proxy_html

## Install Node.js

Node.js is the library used by Galaxy to compile Javascript files. The
library verifies the dependencies downloads javascripts and creates a
compact version of the scripts in the /static folder of Galaxy.

    sudo yum install npm 
    
    sudo npm install -g grunt grunt-cli

## Slurm

The slurm library is used to send jobs to the cluster. Prerequisites:
your server should have a network card with the appropriate submit
network.

1\. Download and install the latest libraries provided by USIT admins.
Go to the nh machine. Get the following rpms:

    #In the directory /export/rocks/install/contrib/
    
    munge-<version>.x86_64.rpm
    munge-libs-<version>.x86_64.rpm
    munge-devel-<version>.x86_64.rpm
    
    slurm-<version>.x86_64.rpm
    slurm-munge-<version>.x86_64.rpm
    slurm-plugins-<version>.x86_64.rpm
    slurm-perlapi-<version>.x86_64.rpm

N.B. I think that maybe you should have an USIT account to do this. I
will verify this. If needed this libraries can be put in our SVN.

2\. Download configuration files from /etc/munge and /etc/slurm. And
start munge

    service munge start

3\. Ensure that the lap user and the slurm user have the same UID and
GUD as on Abel. The easy way is to copy the corresponding lines from
/etc/shadow

4\. Download and install drma-slurm. This version is modified to include
additional parameter working directory.

    yum install gperf
    
    git clone https://<username>@bitbucket.usit.uio.no/scm/ft/drmaa.git
    
    cd drmaa
    
    yum install ragel-6.6-2.3.x86_64.rpm
    
    cd  slurm-drmaa-1.0.6
    
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/slurm/lib64
    
    
    ./configure --with-slurm-inc=/opt/slurm/include/  --with-slurm-lib=/opt/slurm/lib64/ --prefix=/site/drmaa/ --enable-debug
    
    make 
    make install

5\. Modify the network resolve files

In resolve.conf add:

    nameserver 10.110.1.1

In hosts add:

    10.110.1.1      nielshenrik.local nielshenrik

6\. Test the connection with the following script:

    open (OUT, ">$ARGV[0]");
    
    system("sleep 60");
    my $time = localtime();
    print OUT  "The time is $time\n";
    
    close( OUT );
    
    # End of script

In order the test to work create the following file
/etc/slurm\_drmaa.conf

    job_categories: {
                           default: "--account=staff --time=00:01:00 --mem-per-cpu=1000 --comment=hello",
    
                    },

Run the test:

    export SLURM_DRMAA_CONF=/etc/slurm_drmaa.conf
    
    /site/drmaa/bin/drmaa-run test.pl output

## Gold Instalation

Download the local copy of modified Gold software from:
<https://bitbucket.usit.uio.no/scm/ft/gold-usit-repository.git>.

1\. Compile Gold.

    yum install libpqxx-devel.x86_64 libpqxx.x86_64
    
    yum install perl-DBD-Pg.x86_64
    
    
    cd  gold-usit-repository
    
    chmod +x usit/bin/*
    
    
    usit/bin/create-empty-dirs.sh
    
    ./configure --prefix=/opt/gold --with-db=Pg --with-log-dir=/opt/gold/log --with-perl-libs=local --with-gold-libs=local --with-cgi-bin=/var/www/cgi-bin/gold
    
    make

2\. Install Gold. Supper User account is required.

    sudo su
    
    make deps
    
    make gui
    
    make install
    
    make install gui

3\. Edit the configuration files. Go to the directory /opt/gold/etc/. In
the file goldd.conf:

    super.user = root    
    
    database.datasource = DBI:Pg:dbname=<DATABASE_NAME>;host=<DATABASE_HOST>
    database.user = <USERNAME>
    database.password = <PASSWORD>

In file gold.conf. Un comment the following fragment.

    # account.show = Id,Name,Amount,Projects,Users,Machines,Description
    # allocation.show = Id,Account,Active,StartTime,EndTime,Amount,CreditLimit,Deposited
    # balance.show = Id,Name,Amount,Reserved,Balance,CreditLimit,Available
    # job.show = Id,JobId,User,Project,Machine,Queue,QualityOfService,Stage,Charge,Processors,Nodes,WallDuration,StartTime,EndTime,Description
    # machine.show = Name,Active,Architecture,OperatingSystem,Description
    # project.show = Name,Active,Users,Machines,Description
    # quotations.show = Id,Amount,Job,Project,User,Machine,StartTime,EndTime,WallDuration,Uses,ChargeRates,Description
    # reservation.show = Id,Name,Amount,StartTime,EndTime,Job,User,Project,Machine,Accounts,Description
    # transaction.show = Id,Object,Action,Actor,Name,Child,JobId,Amount,Delta,Account,Project,User,Machine,Allocation,Count,Description
    # user.show = Name,Active,CommonName,PhoneNumber,EmailAddress,DefaultProject,Description

4\. Initialize the database

    psql -d <DATABASE> -h <DBHOSTNAME> -U <DBUSERNAME> < /installation-path/bank.sql

5\. Create virtual host for gold in httpd. Make Gold authentication
keys.

    make auth_key 
    
    
    # Generate private key 
    openssl genrsa -out ca.key 1024
    
    # Generate CSR 
    openssl req -new -key ca.key -out ca.csr
    
    # Generate Self Signed Key
    openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
    
    # Move the files to the correct locations
    mkdir /etc/httpd/conf.d/gold_keys/
    
    mv ca.crt /etc/httpd/conf.d/gold_keys/gold.crt
    mv ca.key /etc/httpd/conf.d/gold_keys/gold.key

Open ssl.conf and add the following fragment:

    <VirtualHost *:443>
             DocumentRoot /var/www/cgi-bin/gold/
             DirectoryIndex index.cgi
             ServerName gold.<HOSTNAME>
             ServerAdmin <YOUR EMAIL>
             ErrorLog logs/gold-error_log
             TransferLog logs/gold-access_log
             SSLEngine on
             SSLCertificateFile /etc/httpd/conf.d/gold_keys/gold-server.crt
             SSLCertificateKeyFile /etc/httpd/conf.d/gold_keys/gold-server.key
             SetEnvIf User-Agent ".*MSIE.*" nokeepalive ssl-unclean-shutdown
    </VirtualHost>

Open httpd.conf and add the following fragment:

    Alias /cgi-bin/gold "/var/www/cgi-bin/gold"
    
    <Directory "/var/www/cgi-bin">
        AllowOverride None
        Options  +ExecCGI
        AddHandler cgi-script .cgi .pl
        Order allow,deny
        Allow from all
    </Directory>

6\. Allow the default user for Galaxy to run GOLD scripts. Create the
file /etc/sudoers.d/lap

    #
    # the LAP system user can issue GOLD commands without password and tty
    #
    Defaults:<USER> !requiretty
    Cmnd_Alias GOLD = /opt/gold/bin/*
    laportal <HOSTNAME>=(root) NOPASSWD: GOLD

7\. Initialize Gold for usage.

Create a default machine

    ./gmkmachine -d "Linux Cluster at UiO" Abel-Galaxy

Create the Organization (project owner) for the default Galaxy project -
root@laporal

    ./goldsh Organization Create Name='root@laportal'

Create the default project - gx\_default

    ./gmkproject -d "Galaxy Default Project" gx_default --createAccount=False -o root@laportal

Crate a test user

    ./gmkuser -u kouylekov@gmail.com -d "test user" -p gx_default

N.B. The user must have the same email as the user in galaxy.

Add the created user to the default project gx\_default

    ./gchproject --addUsers kouylekov@gmail.com -p gx_default

Create an account for the user

    ./gmkaccount -p gx_default -u kouylekov@gmail.com

Deposit 200 hours in the account. The a parameter is determined by the
output of the previous command.

    ./gdeposit -a 1 -h 200

## MongoDB

As a prerequisite to LAP installation, there must be a MongoDB database
available for access by the LAP user. Some notes on how MongoDB is
configured on the LAP servers is available on the
LapDevelopment/MongoDB, but for local installations

- Install MongoDB via your package manager, e.g.
  
        yum install mongodb-server
- Confirm that the database directory (/var/lib/mongodb/ by default)
is available;
- Optionally, review MongoDB settings (e.g. in /etc/mongodb.conf and
/etc/sysconfig/mongod);
- Start the server and optionally enable automated start-up, e.g.
  
        /etc/init.d/mongodb start

By default, MongoDB initially allocates database space relatively
generously (at around three gigabytes, it appears). If disk space is at
a premium (as can be the case on a laptop :-), consider adding the
--smallfiles option to the start-up sequence of the MongoDB server.

# Download LAP

On the (non-Galaxy) LAP side, the following components are required: the
LAP Tree, Library, tool descriptions, and (optionally) operational
scripts.

      cd /home/laportal
      svn co http://user@svn.emmtee.net/lap/trunk/tree
      cd 
      svn co http://user@svn.emmtee.net/lap/trunk/tools
      svn co http://user@svn.emmtee.net/lap/trunk/operation

# Create Environment Variables File

Create a file with the name env.sh in /home/laportal that contains all
the environment variables needed to run LAP

      export LAPTREE=/home/laportal/tree
      export LAPLIBRARY=/home/laportal/library
      export LAPSTORE=mongodb://127.0.0.1:27017/lapstore

# Galaxy

In early 2016, there are several versions of Galaxy in use with LAP.
However, development focus now shifts towards the 2015.03 release, and
there is a pre-configured snapshot available in SVN with local
extensions (e.g. custom datatypes) and the basic configuration to use
the LAP Tool descriptions (assuming the above locations):

      cd /home/laportal
      svn co http://svn.emmtee.net/lap/trunk/local/galaxy

When using this version, no symbolic links should be required (assuming
the LAP components reside in the recommended location), i.e.
config/galaxy.ini already points to the LAP tool configuration:

      tool_config_file = /home/laportal/tools/config.xml
      tool_path = /home/laportal/tools

To start Galaxy:

      cd /home/laportal/galaxy
      ./run.sh > main.log

At this point, with a bit of luck, the built-in Galaxy web server will
be listening at http://localhost:8080.

Except for (currently, a small number of) LAP-specific extensions, this
Galaxy version corresponds to the following release:

      git clone https://github.com/galaxyproject/galaxy/
      cd galaxy
      git checkout release_15.03

# Enable SSL in Galaxy

The following commands are used to enable SSL connection in Galaxy. This
connection is required by the Hotell database servers. To do this you
must recompile the module psycopg2. The recompilation is done with the
following procedure.

1\. Install the postgresql client and server (we need the server only to
compile the postgresql ssl module!! Don't start the server)

    yum install postgresql-server.x86_64 postgresql-devel.x86_64 postgresql.x86_64

2\. Install also the following libraries to in order to compile the
module

    yum install gcc redhat-rpm-config python-devel.x86_64 python27-python-setuptools.noarch

3\. Download the psycog python pack needed for the SSL connection with
the DB. It might already exist but it is not compiled for SSL. The
package is available at: <http://initd.org/psycopg>. (Verified version
is 2.6.1. the current release)

4\. Modify the setup.py as follows: just before the line

    from distutils.core import setup, Extension

add the following lines

    import pkg_resources
    from scramble_lib import *

5\. Compile the package.

    #Indicates the path of the scaramble lib
    export PYTHONPATH=/home/laportal/galaxy/scripts/scramble/lib
    python setup.py bdist_egg

6\. The compilation creates an pscyog2-&lt;VERSION-ARCH&gt;.egg in the
dist folder. The egg must be placed in Galaxy default egg directory
galaxy/eggs/.

7\. Update the file egs.ini with the correct versions of psycopg2

# Configure Apache for Galaxy

The Apache server serves as a proxy and aggregate for both galaxy and
gold interfaces. It is used also from the module for Feide
authentication.

1\. Edit the file /etc/httpd/conf/httpd.conf. Redirect the root to SSL
443 port.

    <VirtualHost _default_:80>
      RewriteEngine on
      ReWriteCond %{SERVER_PORT} !^443$
      RewriteRule ^/(.*) https://%{HTTP_HOST}/$1 [NC,R,L]
    </VirtualHost>

Allow static pages to be loaded by apache.

    <Directory /home/laportal/galaxy/static/>
            Options Indexes FollowSymLinks
            AllowOverride None
            Require all granted
    </Directory>

Update the CGI section.

    Alias /cgi-bin/gold "/var/www/cgi-bin/gold"
    
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
    
    <Directory "/var/www/cgi-bin">
        AllowOverride None
        Options  +ExecCGI
        AddHandler cgi-script .cgi .pl
        Order allow,deny
        Allow from all
    </Directory>

2\. Add the following rewrite rules to the virtual host in
/etc/httpd/conf.d/ssl.conf

    <VirtualHost _default_:443>
    
    ...
    
    RewriteEngine on
    RewriteRule ^/static/style/(.*) /home/laportal/galaxy/static/june_2007_style/blue/$1 [L]
    RewriteRule ^/static/scripts/(.*) /home/laportal/galaxy/static/scripts/packed/$1 [L]
    RewriteRule ^/static/(.*) /home/laportal/galaxy/static/$1 [L]
    RewriteRule ^/favicon.ico /home/laportal/galaxy/static/favicon.ico [L]
    RewriteRule ^/robots.txt /home/laportal/galaxy/static/robots.txt [L]
    RewriteRule ^(.*) http://127.0.0.1:8080$1 [P]
    
    ...

4\. Optionally you can generate SSL keys for the certificate check if
mod\_ssl and open\_ssl are installed, if not install them.

    yum install mod_ssl
    yum install openssl.x86_64

Create keys and certificates

    # Generate private key 
    openssl genrsa -out ca.key 1024
    
    # Generate CSR 
    openssl req -new -key ca.key -out ca.csr
    
    # Generate Self Signed Key
    openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
    
    # Move the files to the correct locations
    cp ca.crt /etc/pki/tls/certs/galaxy.server.crt
    cp ca.key /etc/pki/tls/private/galaxy.server.key
    cp ca.csr /etc/pki/tls/private/galaxy.server.csr

To use them appropriately modify the ssl.conf file.

# LAP Specific Configuration

## MongoDB

### LAP Store Configuration

For the time being, at least, we assume that all annotations (by all LAP
users) share one database and one database user; to initially create the
database and user:

      mongo --verbose -u laportal -p '????????' admin
    
      use lapstore
      db.addUser({ user: "lapstore", pwd: "????????", roles: [ "readWrite" ] })

### Interactive Database Inspection and Manipulation

To connect to the LAP Store using the MongoDB Shell:

      mongo --verbose -u lapstore -p '????????' lapstore

To inspect the contents of a specific collection (use show collections
or db.getCollectionNames() for the selection):

      db[db.getCollectionNames()[0]].find().pretty()

To drop all collections, i.e. free up storage space; this will render
all Galaxy files in all user histories (i.e. receipts, referring to
collections) useless, thus must only be used on development instances:

      db.getCollectionNames().forEach(function(foo) { if (foo.indexOf("system.") == -1) db[foo].drop(); })

Last update: 2016-06-20 by MilenKouylekov [[edit](https://github.com/delph-in/docs/wiki/LapDevelopment_ServerDeployment/_edit)]{% endraw %}