# Creat by wangyang  2015-8-6

# -*- coding: utf-8 -*-
import json
from urllib import urlencode
import urllib2
#from nose.tools import assert_equals
import sys
sys.path.append("../")
import get_response
import ConfigParser

# config = ConfigParser.ConfigParser()
# config.read('../conf/config.conf')
# playerId = config.get('global', 'playerId')
# url = config.get('global', 'url')


def test_252(playerId,url):
        #global playerId
        #global url
        #global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'41',
        "panels" : [
            [
                [3,1103,3],         #2*5*2
                [3,1,3],
                [3,1103,3]
            ],
            [
                [3,1103,3],         #2*4*2
                [3,1101,3],
                [3,1103,3]
            ],
            [
                [1001,3,1001],         #4x
                [3,1102,3],
                [1001,3,1001]
            ],
            [
                [1001,3,1001],         #5x
                [3,1,3],
                [1001,3,1001]
            ],
            [
                [3,1103,3],         #5x 2x
                [3,1,3],
                [1001,3,1001]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))

def test_777(playerId,url):
        #global playerId
        #global url
        #global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'41',
        "panels" : [
            [
                [3,1000,3],         #r7r7r7
                [3,1000,3],
                [3,1000,3]
            ],
            [
                [3,1001,3],         #p7p7p7
                [3,1001,3],
                [3,1001,3]
            ],
            [
                [3,1002,3],         #b7b7b7
                [3,1002,3],
                [3,1002,3]
            ],
            [
                [3,1003,3],         #w7w7w7
                [3,1003,3],
                [3,1003,3]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))

def test_7bar(playerId,url):
        #global playerId
        #global url
        #global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'41',
        "panels" : [
            [
                [3,1000,3],         #any7
                [3,1003,3],
                [3,1001,3]
            ],
            [
                [3,1002,3],         #any7
                [3,1003,3],
                [3,1003,3]
            ],
            [
                [3,1004,3],         #3bar
                [3,1004,3],
                [3,1004,3]
            ],
            [
                [3,1005,3],         #2bar
                [3,1005,3],
                [3,1005,3]
            ],
            [
                [3,1006,3],         #barbarbar
                [3,1006,3],
                [3,1006,3]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))


def test_other(playerId,url):
        #global playerId
        #global url
        #global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'41',
        "panels" : [
            [
                [3,1003,3],         #w7 3bar 3bar
                [3,1004,3],
                [3,1004,3]
            ],
            [
                [3,1003,3],         #w7 3bar 2bar
                [3,1004,3],
                [3,1002,3]
            ],
            [
                [3,1003,3],         #w7 3bar 2bar
                [3,1003,3],
                [3,1006,3]
            ],
            [
                [3,1004,3],         #any bar
                [3,1005,3],
                [3,1006,3]
            ],
            [
                [3,1000,3],         #r7 5x r7
                [3,1,3],
                [3,1000,3]
            ],
            [
                [3,1103,3],         #2x bar bar
                [3,1006,3],
                [3,1006,3]
            ],
            [
                [3,1000,3],         #r7 4x b7
                [3,1101,3],
                [3,1002,3]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))