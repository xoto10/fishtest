#!/usr/bin/python

# indexes.py - example commands to create / drop indexes


import copy
import os
import random
import math
import time
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

runs = db['runs']
old_runs = db['old_runs']

chunk_size = 1000


# Example commands to create indexes:

runs.ensure_index([('finished', ASCENDING), ('last_updated', DESCENDING)])

runs.ensure_index([('tasks.pending', ASCENDING)],
                  partialFilterExpression = { 'tasks': { '$elemMatch': {'pending': True} } } )
runs.ensure_index([('tasks.active', ASCENDING)],
                  partialFilterExpression = { 'tasks': { '$elemMatch': {'active': True} } } )

# Example commands to drop indexes:
#runs.drop_index([('tasks.pending')])


