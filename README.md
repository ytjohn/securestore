Secure Storage
==============

[![Build Status](https://secure.travis-ci.org/ytjohn/securestore.png?branch=master)](https://travis-ci.org/ytjohn/securestore)

This module will store AES-256 encrypted strings (called tokens) in an sqlite
database. If access is gained to the datastore, the contents can not be read.

Additionally, this is designed to be part of a larger system. Individual
tokens are identified only by a row number. Another system will associate
individual token ids with its target.

Security relies on OS level access control to files.

1. The token database and the access key are stored in locations only
accessible to root or a restricted user.

2. The securestore.py file is set to read-only.

3. An entry in /etc/sudoers should be used to execute securestore.py by
 certain group members, while the securestore.py file is set only readable
 by root.

4. A securestore shell script is availble that runs "sudo securestore.py"
and passes all arguments.



Secure root files:
 /usr/local/secure/bin/passmanager  (python)
 /usr/local/secure/data/passmanager.db (sqlite db)

Insecure files:
 /usr/local/bin/passmanager (shell script)




