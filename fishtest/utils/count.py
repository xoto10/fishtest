import copy
import os
import random
import math
import time
import pprint
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient, ASCENDING, DESCENDING

from userdb import UserDb
from actiondb import ActionDb
from regressiondb import RegressionDb
from views import parse_tc

import stat_util

db_name='fishtest_new'

# MongoDB server is assumed to be on the same machine, if not user should use
# ssh with port forwarding to access the remote host.
conn = MongoClient(os.getenv('FISHTEST_HOST') or 'localhost')
db = conn[db_name]
userdb = UserDb(db)
actiondb = ActionDb(db)
regressiondb = RegressionDb(db)

actions = db['actions']
runs = db['runs']
system_indexes = db['system.indexes']
users = db['users']
old_runs = db['old_runs']

chunk_size = 1000


# count items in each collection
# > db.getCollectionNames()
# [ "actions", "runs", "system.indexes", "users" ]

a = actions.count()
r = runs.count()
si = system_indexes.count()
u = runs.count()

print "actions.count()  " + str(r)
print "runs.count()     " + str(a)
print "sysind.count()   " + str(si)
print "users.count()    " + str(u)


