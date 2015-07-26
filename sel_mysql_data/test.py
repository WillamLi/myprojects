#!/bin/python
import threading
import urllib2
import json
from time import ctime,sleep

def a(ip):
    au=urllib2.urlopen(ip).read()
    print au
    au_j=json.loads(au)    
    print au_j
    print au_j["t"]

iplist=["http://180.153.191.128:33516/chart_data","http://180.153.191.128:33516/chart_data"]

threads=[]
for i in iplist:
    print ctime()
    t=threading.Thread(target=a,args=(i,))
    threads.append(t)
    print threads

for t in threads:
    t.start()

for t in threads:
    t.join()

print "t:",ctime()
#a("http://180.153.191.128:33516/chart_data")
