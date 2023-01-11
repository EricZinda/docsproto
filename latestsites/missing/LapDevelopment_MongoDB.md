{% raw %}# Initial Setup

The database is stored on a dedicated partition (on the SSD RAID); to
prepare and mount the filesystem:

      mkfs.ext4 /dev/ssdvg/mongo
      mount /var/lib/mongo

To install the WiredTiger version of the database, enable the MongoDB
[community
edition](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/).
Install the server, client, and libraries:

      yum -y install mongodb-org

In /etc/mongod.conf, enable incoming connections from the ABEL-internal
network address of the portal node (e.g. 10.110.0.158 for at.local) and
require authentication:

    net:
      bindIp: 127.0.0.1,10.110.0.158
    
    security:
      authorization: enabled

Activate the service by default (i.e. at boot(7) time) and start the
database:

      chkconfig mongod on
      /etc/init.d/mongod start

Finally, create a database user laportal with administrator rights:

      mongo --authenticationDatabase admin
    
      use admin
      db.createUser( { user: "laportal", pwd: "????????", roles: [ "userAdminAnyDatabase" ] } )

# Starting, Stopping, and Restarting the Database Server

      sudo /etc/init.d/mongod start|stop|restart

# LAP Store Configuration

For the time being, at least, we assume that all annotations (by all LAP
users) share one database and one database user; to initially create the
database and user:

      mongo --verbose -u laportal -p '????????' admin
    
      use lapstore
      db.createUser({ user: "lapstore", pwd: "????????", roles: [ "readWrite" ] })

# Interactive Database Inspection and Manipulation

To connect to the LAP Store using the MongoDB Shell:

      mongo --verbose -u lapstore -p '????????' lapstore

To inspect the contents of a specific collection (use show collections
or db.getCollectionNames() for the selection):

      db[db.getCollectionNames()[0]].find().pretty()

To drop all collections, i.e. free up storage space; this will render
all Galaxy files in all user histories (i.e. receipts, referring to
collections) useless, thus must only be used on development instances:

      db.getCollectionNames().forEach(function(foo) { if (foo.indexOf("system.") == -1) db[foo].drop(); })

# Rotating Log Files

It appears that the community edition (in version 3.0 and upwards) does
not rotate log files itself; look into how to regularly issue the
logRotate command or send a USR1 signal.
<update date omitted for speed>{% endraw %}