# Creat by wangyang  2015-8-6
import json
import urllib
import urllib2
#import nose.tools 
from collections import OrderedDict


def Post_response(url,data):
    post_data = urllib.urlencode(data)
    req = urllib2.urlopen(url, post_data,timeout = 10)
    content = req.read()
    # print json.dumps(ret_loaded,indent=4,ensure_ascii=False)
    return content

def Post_Json_response(url,data):
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        #response = urllib2.urlopen(req, json.dumps(data,sort_keys=True),timeout=5)
        response = urllib2.urlopen(req, json.dumps(data),timeout=5)
        rjson = response.read()
        return rjson

def Get_response(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, timeout=2)
    ret_json = response.read()
    ret_loaded = json.loads(ret_json)
    # print json.dumps(ret_loaded,indent=4,ensure_ascii=False)
    return ret_loaded
