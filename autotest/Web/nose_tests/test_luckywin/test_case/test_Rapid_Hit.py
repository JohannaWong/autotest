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
config.read('./nose_tests/test_luckywin/conf/config.conf')
playerId = config.get('global', 'playerId')
url = config.get('global', 'url')


def test_Rapid_Hit():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'33',
        "panels" : [
            [
                [1006,1000,1008,6],      #free spin 
                [1008,1002,2,1001],
                [1004,1001,2,1006],
                [1006,2,1002,1008],
                [1006,1004,1008,1007]
            ],
            [
                [1006,1,1008,1001],       #wild  
                [1000,1004,1006,1008],
                [1006,1003,1005,1005],
                [1004,1001,1007,1003],
                [1000,1007,1006,1004]
            ],
            [
                [1007,6,1006,1000],    #9 rapid
                [6,6,1007,1005],
                [1007,6,6,1001],
                [6,1001,1008,6],
                [1007,6,6,1008]
            ],
            [
                [1007,6,1006,1000],    #6 rapid
                [6,6,1007,1005],
                [1007,6,6,1001],
                [6,1001,1008,1006],
                [1007,1006,1004,1008]
            ],
            [
                [1007,1004,1006,1000],    #3 rapid
                [6,6,1007,1005],
                [1007,1002,1004,1001],
                [6,1001,1008,1006],
                [1007,1006,1004,1008]
            ],
            [
                [1006,1000,1008,6],       #no free spin
                [1008,1002,1005,1001],
                [1004,1001,2,1006],
                [1006,2,1002,1008],
                [1006,1004,1008,1007]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))

def wild5():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'33',
        "panels" : [
            [
                [1006,1,1008,1001],       #5wild  
                [1000,1,1006,1008],
                [1006,1,1005,1005],
                [1004,1,1007,1003],
                [1000,1,1006,1004]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)