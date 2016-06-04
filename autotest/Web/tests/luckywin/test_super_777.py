# Creat by wangyang  2015-8-6

# -*- coding: utf-8 -*-
import json
from urllib import urlencode
import urllib2
from nose.tools import assert_equals
import sys
sys.path.append("../")
import get_response
import ConfigParser

# config = ConfigParser.ConfigParser(playerId,url)
# config.read('../conf/config.conf')
# playerId = config.get('global', 'playerId')
# url = config.get('global', 'url')
subjectId = '42'

def test_7(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1001,3],       #7red
                [3,1001,3],
                [3,1001,3]
            ],
            [
                [3,1002,3],       # 7lan
                [3,1002,3],
                [3,1002,3]
            ],
            [
                [3,1000,3],       # 7yin
                [3,1000,3],
                [3,1000,3]
            ],
            [
                [3,1000,3],       # any 7
                [3,1001,3],
                [3,1002,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded

def test_bar(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1003,3],       #3bar
                [3,1003,3],
                [3,1003,3]
            ],
            [
                [3,1004,3],       #2bar
                [3,1004,3],
                [3,1004,3]
            ],
            [
                [3,1005,3],       #bar
                [3,1005,3],
                [3,1005,3]
            ],
            [
                [3,1003,3],       #any bar
                [3,1004,3],
                [3,1005,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded      

def test_wild_no(playerId,url):
        #global playerId
       # global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1001,3],       #until wild
                [3,1,3],
                [3,1001,3]
            ],
            [
                [3,1002,3],       
                [3,1003,3],
                [3,1004,3]
            ],
            [
                [3,1002,3],       
                [3,1003,3],
                [3,1004,3]
            ],
            [
                [3,1002,3],       
                [3,1003,3],
                [3,1004,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded

def test_wild(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1101,3],       #3*wild*2
                [3,1,3],
                [3,1102,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded

def test_3_wild(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1101,3],       #3*7gold
                [3,1000,3],
                [3,1001,3]
            ],
            [
                [3,1101,3],       #3*3*7gold
                [3,1000,3],
                [3,1101,3]
            ],
            [
                [3,1101,3],       #3*3*7gold
                [3,1000,3],
                [3,1101,3]
            ],
            [
                [3,1101,3],       #3*3*7red
                [3,1001,3],
                [3,1101,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded


def test_2_wild(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1102,3],       #2*2*red7
                [3,1001,3],
                [3,1102,3]
            ],
            [
                [3,1102,3],       #2*2*bar
                [3,1005,3],
                [3,1102,3]
            ],
            [
                [3,1101,3],       #3*2*red7
                [3,1001,3],
                [3,1102,3]
            ],
            [
                [3,1102,3],       #3*2*2bar
                [3,1004,3],
                [3,1101,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded


