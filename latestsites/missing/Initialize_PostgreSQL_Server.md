{% raw %}# HOW TO initialize PostgreSQL server

- [PostgreSQL server](http://www.postgresql.org/download/) version 7.4
or above must be running either on the local machine or remotely
over a TCP/IP port. You should use the --locale=C option when
initializing the server with initdb.
- Create user accounts.
- Configure access privileges.
- Restart PostgreSQL server.

## Create User Accounts

- \[Linux\] Open a shell as user postgres. E.g.

<!-- -->


    [user@localhost]$ su
    [root@localhost]$ su postgres
    [postgres@localhost]$

- Create a database user lexdb who will manage the database. E.g.
\[Linux\]

{{{\[postgres@localhost\]$ createuser -U postgres --createdb
--no-adduser lexdb CREATE USER}}}

- \[Optional\] If you wish to use password authentication add the -P
option.

<!-- -->


- Create a user account for yourself (substitute your shell login for
USERNAME below). E.g. \[Linux\]

{{{\[postgres@localhost\]$ createuser -U postgres --no-createdb
--no-adduser USERNAME CREATE USER}}}

- \[Optional\] If you wish to use password authentication add the -P
option.

## Configure Access Privileges

### PostgreSQL server running on local machine

- Ensure the [access privilege configuration
file](http://www.postgresql.org/docs/7.4/interactive/client-authentication.html#AUTH-PG-HBA-CONF)
\[Linux\] $PGDATA/pg\_hba.conf contains the following lines:

{{{\# TYPE DATABASE USER IP-ADDRESS IP-MASK METHOD

local all all trust host all all 127.0.0.1 255.255.255.255 trust}}}

- \[Optional\] If you wish to use password authentication replace
trust with md5.

<!-- -->


- TCP/IP must be enabled. Uncomment the line for TCP/IP in \[Linux\]
$PGDATA/postgresql.conf so that it reads:

tcpip\_socket = true

- By default the server will run on port 5432. To use another port set
the PSQL [environment
variable](http://www.postgresql.org/docs/7.4/interactive/libpq-envars.html)
PGPORT.

### PostgreSQL server on remote machine

- Allow remote access to the server by adding lines of the following
form to access privilege configuration file \[Linux\]
$PGDATA/pg\_hba.conf:

host    all         all        IP\_ADDRESS    255.255.255.255     md5

- \[Optional\] If you wish to use password authentication replace
trust with md5.

<!-- -->


- TCP/IP must be enabled. Uncomment the line for TCP/IP in \[Linux\]
$PGDATA/postgresql.conf so that it reads:

tcpip\_socket = true

- By default the server will run on port 5432. To use another port set
the environment variable PGPORT.

Last update: 2011-10-09 by anonymous [[edit](https://github.com/delph-in/docs/wiki/Initialize_PostgreSQL_Server/_edit)]{% endraw %}