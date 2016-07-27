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


def test_wild():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'30',
        "panels" : [
            [
                [3,1002,3],         #5 respin
                [3,1102,3],
                [3,1003,3]
            ],
            [
                [1001,3,1],         #double wild
                [3,1003,3],
                [3,1101,3]
            ],
            [
                [1,3,1002],         #triple wild
                [3,1,3],
                [1101,3,1003]
            ],
            [
                [3,1002,3],        #no respin
                [1103,3,1002],
                [1001,3,1]
            ],
            [
                [3,1,3],     #  3*2*3
                [3,1101,3],
                [3,1,3]
            ],
            [
                [6,3,6],            #jackpot
                [6,3,6],
                [6,3,6]
            ],
            [
                [3,1002,3],        #2 respin
                [3,1103,3],
                [1001,3,1]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))


def test_Respin():
        global playerId
        global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'30',
        "panels" : [
            [
                [3,1002,3],         #5 respin
                [3,1102,3],
                [3,1003,3]
            ],
            [
                [6,3,3],         #5 respin
                [3,3,3],
                [6,6,3]
            ]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded