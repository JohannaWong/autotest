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

config = ConfigParser.ConfigParser()
config.read('./nose_tests/test_simvegas/conf/config.conf')
playerId = config.get('global', 'playerId')
url = config.get('global', 'url')

def test_red7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1000,3],       #20 7red
                [3,1000,3],
                [3,1000,3],
                [3,1007,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        
def test_zi7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1001,3],       #10 7zi
                [3,1001,3],
                [3,1001,3],
                [3,1008,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_blue7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1002,3],       #10 7blue
                [3,1002,3],
                [3,1002,3],
                [3,1009,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_7bar():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1003,3],       #10 7bar
                [3,1003,3],
                [3,1003,3],
                [3,1009,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_blue7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1002,3],       #10 7blue
                [3,1002,3],
                [3,1002,3],
                [3,1009,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
def test_blue7_bar_blue7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1002,3],     #blue7 bar  blue7  2   2X
                [3,1005,3],
                [3,1002,3],
                [3,1008,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_blue7_bar_blue7_no():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1000,3],     #red7 bar bar 5  20 no spin
                [3,1004,3],
                [3,1004,3],
                [3,1009,3]
            ]
        ] 
    }
        ret_loaded = get_response.Post_response(url,data)
def test_any7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1000,3],       #10 any 7 
                [3,1001,3],
                [3,1002,3],
                [3,1009,3]
            ]
        ]
    }  
        ret_loaded = get_response.Post_response(url,data)

def test_red7_red7():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1000,3],       #2 red7 red7 
                [3,1000,3],
                [3,1006,3],
                [3,1007,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_7bar_3bar_2bar():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1003,3],       #0.5   7bar  3bar  2bar
                [3,1004,3],
                [3,1005,3],
                [3,1010,3],
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

def test_7bar_3bar_2bar():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'40',
        "panels" : [
            [
                [3,1003,3],       #   7bar  3bar  2bar
                [3,1003,3],
                [3,1005,3],
                [3,1007,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)

        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))