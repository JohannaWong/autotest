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

subjectId = "60101"

def test_free_spin(playerId,url):
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [1001,1002,1001,1004],   #free spin
                [1008,1,1003,1007],
                [2,1006,1006,1006],
                [1003,1003,2,1007],
                [1008,2,1003,1006]
            ]
        ]
        }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded

def test_convention(playerId,url):
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [1008,1006,1005,1005],
                [1005,1002,1004,1006],
                [1007,1006,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
            ],
            [
                [1008,1005,1005,1005],
                [1005,1002,1004,1005],
                [1007,1005,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
           ],
           [
                [1008,1007,1005,1005],
                [1005,1002,1004,1007],
                [1007,1007,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
           ],
           [
                [1008,1008,1005,1005],      #1008 
                [1005,1002,1004,1008],
                [1007,1008,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
           ],
           [
                [1008,1002,1005,1005],      #1002
                [1005,1002,1004,1008],
                [1007,1002,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
           ],
           [
                [1008,1000,1005,1005],      #1000
                [1005,1000,1004,1008],
                [1007,1000,1001,1007],
                [1000,1000,1000,1000],
                [1008,1004,1005,1004]
           ],
           [
                [1008,1001,1005,1005],      #1001
                [1005,1001,1004,1008],
                [1007,1001,1001,1007],
                [1000,1001,1000,1000],
                [1008,1004,1001,1004]
           ],
           [
                [1008,1003,1005,1005],      #1003
                [1005,1003,1004,1008],
                [1007,1003,1001,1007],
                [1000,1003,1000,1000],
                [1008,1004,1001,1004]
           ],
           [
                [1008,1004,1005,1005],      #1004
                [1005,1001,1004,1008],
                [1007,1004,1001,1007],
                [1000,1001,1004,1000],
                [1008,1004,1004,1004]
           ]
        ]
        }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))

def test_wild(playerId,url):
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [1008,1001,1,1],              #wild 1006
                [1006,1005,1004,1005],
                [1006,1002,1007,1002],
                [1007,1005,1004,1004],
                [1008,1,1004,1000]
            ],
            [
                [1,1,1,1],
                [2,1006,1003,1007],         #wild
                [1005,1007,1005,1004],
                [1006,1002,1007,1003],
                [1004,1007,1007,1007]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded
