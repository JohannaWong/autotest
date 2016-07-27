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

def test_Forest_Mania():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'38',
        "panels" : [
            [
                [1008,1001,1008,2],     #free spin
                [1002,1008,2,1010],
                [1007,1002,1005,2],
                [1009,1002,1010,1003],
                [1003,1009,1001,1005]
            ],
            [
                [1004,1007,1001,1008],   #wild
                [1005,1004,1006,1],
                [1007,1002,1005,2],
                [1,1,1,1],
                [1002,1006,1003,1009]
            ],
            [
                [1004,1006,1000,1009],   #tager
                [1000,1000,1000,1009],
                [1005,1004,1000,1001],
                [1000,1000,1000,1000],
                [1008,1006,1,1007]
            ],
            [
                [1008,1001,1008,2],     #no free spin
                [1002,1008,1000,1010],
                [1007,1002,1005,2],
                [1009,1002,1010,1003],
                [1003,1009,1001,1005]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))