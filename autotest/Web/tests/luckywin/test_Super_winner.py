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

# config = ConfigParser.ConfigParser()
# config.read('../conf/config.conf')
# playerId = config.get('global', 'playerId')
# url = config.get('global', 'url')

def test_jackpot(playerId,url):
        #global playerId
        #global url
        #global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":'35',
        "panels" : [
              [3,1003,3],
              [3,1002,3],
              [3,1003,3]
        ]
}
        ret_loaded = get_response.Post_response(url,data)
        print ret_loaded
        return ret_loaded
        #assert ret_loaded[0]['panels'][0]["chips"] == 58000
        #assert_equals(ret_loaded[0]['panels'][0]["chips"] , 0,msg="chips=%s not 0" % (ret_loaded[0]['panels'][0]["chips"]))
        #assert_equals(ret_loaded[0]['freeSpins'][0]["leftFreeSpin"],10,msg="Freespin=%s not 10" % (ret_loaded[0]['freeSpins'][0]["leftFreeSpin"]))