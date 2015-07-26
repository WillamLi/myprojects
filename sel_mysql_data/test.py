#!/bin/python
import threading
import urllib2
import json

def a(ip):
    au=urllib2.urlopen(ip).read()
    print au
    au_j=json.loads(au)    
    print au_j
    print au_j["data"]


a("http://180.153.191.128:33516/chart_data")
