#coding=utf-8
from __future__ import division
from __future__ import unicode_literals
import os 

try:
    import json
except importError:
    import simplejson as json


print os.path.isdir(r'F:\workspace\python')

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = json.dumps(data)
print json

print 10/3
print isinstance('中文', unicode)
print isinstance('am I an unicode?', unicode)