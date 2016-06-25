# Creat by wangyang  2015-8-6
import json
import urllib
import urllib2
import socket
#import nose.tools 
from collections import OrderedDict
import time
from time import ctime,sleep

socket.setdefaulttimeout(300) 

def Post_response(url,data):
    post_data = urllib.urlencode(data)
    req = urllib2.urlopen(url, post_data,timeout = 10)
    content = req.read()
    # print json.dumps(ret_loaded,indent=4,ensure_ascii=False)
    return content

def Post_Json_response(url,data):
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        start=time.time()

        response = urllib2.urlopen(req, json.dumps(data),timeout=20)
        rjson = response.read() 

        end=time.time()
        ret_loaded = json.loads(rjson)
        return (ret_loaded,float(end-start)/1000)

def Get_response(url):
        req = urllib2.Request(url)
        start=time.time()

        response = urllib2.urlopen(req, timeout=20)
        ret_json = response.read()

        end=time.time()
        ret_loaded = json.loads(ret_json)
        # print json.dumps(ret_loaded,indent=4,ensure_ascii=False)
        return (ret_loaded,float(end-start)/1000)
