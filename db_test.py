#!/usr/bin/python
from tarantool import Connection
import types

c = Connection(host = "104.154.26.64", port = 3301)
#user = 'usr', password = '123', 
print c._recv