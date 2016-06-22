# Creat by wangyang  2015-8-6

# -*- coding: utf-8 -*-
import json
from urllib import urlencode
import urllib2
import random
#from nose.tools import assert_equals
import sys
import get_response
import ConfigParser
import time
from time import ctime,sleep

times=[]
error=[]

def init_token():

        deviceId =random.randint(10000000,99999999)
        url_token = "https://slots-team-test-server-v0.tuanguwen.com:9443/auth/token?deviceId='%s' "%deviceId
        response = get_response.Get_response(url_token)   #token
        re_token = response[0]
        times = response[1]
        token=re_token['data']['token']
        return (token,times)


def test_cooking_tournament():
        facebookid = random.randint(1000000,9999999)
        score = random.randint(500,1000)
        get_token = init_token()
        token = get_token[0]
        leaderBoardId_1 ="cookingmania_level_305"
        leaderBoardId_2 ="cookingmania_level_306"
        url_word_tournament = "https://slots-team-test-server-v0.tuanguwen.com:9443/leaderboard/update?facebookId="'%s'"&facebookToken="'%s'%(facebookid,token)
        data = [
            {
                "leaderBoardId":"%s"%leaderBoardId_1,
                "score": "%s"%score
            },
            {
                "leaderBoardId":"%s"%leaderBoardId_2,
                "score": "%s"%score
            }
        ]
        re_word_tournament = get_response.Post_Json_response(url_word_tournament,data) #get tournament
        responsetime=re_word_tournament[1]+get_token[1]   #toke_time+post_time
        times.append(responsetime)
       
        print re_word_tournament[0]
        if re_word_tournament[0]['errno']!=0:
            error.append("0")
        return(times,error)


if __name__=="__main__":
     test_cooking_tournament()