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

subjectId = "60102"

def test_free_spin(playerId,url):

        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [1,2,1,1],                              #free spin
                [1003,2,1008,1005],
                [1,1,2,1009],
                [1008,1007,1006,1003],
                [1105,1104,1103,1102],
                [2,1009,1105,1104]
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
                [1003,1009,1000,1004],              #AAA
                [1008,1005,1009,1004],
                [1009,1005,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
            ],
            [
                [1003,1009,1000,1005],              #KKK
                [1008,1005,1009,1004],
                [1009,1005,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
           ],
           [
                [1003,1009,1000,1006],              #QQQQ
                [1008,1006,1009,1004],
                [1009,1006,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
           ],
           [
                [1003,1009,1000,1007],              #jjj
                [1008,1007,1009,1004],
                [1009,1007,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
           ],
           [
                [1003,1009,1000,1007],              #jjjjjj
                [1008,1007,1009,1004],
                [1009,1007,1000,1004],
                [1002,1007,1,1],
                [1005,1007,1004,2],
                [1006,1007,1009,1008]
           ],
           [
                [1003,1008,1000,1007],              #10*3
                [1008,1007,1008,1004],
                [1008,1007,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
           ],
           [
                [1003,1009,1000,1009],              #9*3
                [2,1009,1009,2],
                [1008,1009,1000,1004],
                [1002,1006,1,1],
                [1005,1002,1004,2],
                [1006,1006,1009,1008]
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
                [1001,1005,1009,1006],  #Mana Potion 
                [1,1000,1005,1002],
                [1000,1009,1001,1008],
                [1005,1,1009,2],
                [1009,1001,1001,1009],
                [1009,1,1002,1009]
            ],
            [
                [1000,1005,1009,1006],   #Magic Circle
                [1,1000,1005,1002],
                [1000,1009,1004,1008],
                [1005,1,1009,2],
                [1009,1004,1001,1009],
                [1009,1,1002,1009]
            ],
            [
                [1002,1005,1009,1006],     #Magic Book
                [1,1000,1005,1002],
                [1000,1009,1002,1008],
                [1005,1,1009,2],
                [1009,1002,1001,1009],
                [1009,1,1002,1009]
            ]
        ]
        }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded
