#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import os
import server
import web
from Common import *
import Common.dbconn
import ConfigParser
import gl
import json
import MySQLdb
import json
import logging
import tests.luckywin
import time

ISOTIMEFORMAT='%Y-%m-%d %H:%M:%S'

reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"zjpostman",
      '/exec_zjpostman',"exec_zjpostman",
     )

m_config = gl.GL_CONFIG

class zjpostman:
    def GET(self):
        product_line=gl.GL_DB.select('productline')
        return render.zjpostman(product_line)



class exec_zjpostman:

    def get_productline(self):
        productline_id = gl.GL_WEBINPUT.productline_id
        test_url = gl.GL_DB.query("select productline_url from productline where id = " + productline_id )
        url = []
        for item in test_url:
            item_dict1 = item.productline_url
            url.append(item_dict1)
        return url[0]

    def POST(self):
        gl.GL_WEBINPUT=web.input()
        print gl.GL_WEBINPUT
        url=self.get_productline()
        playerid=str(gl.GL_WEBINPUT.playerid)
        subjectid=str(gl.GL_WEBINPUT.subjectid)
        data=gl.GL_WEBINPUT.postdata.replace("(","").replace(")","")
        print url
        print playerid
        print type(playerid)
        print subjectid
        
        #！！！下面请重点注意，data中输入的中括号数量决定着data的执行
        #data输入为[3,1000,3],[3,1000,3][3,1000,3]时,，加"[[]]"
        data="[[%s]]"% data

        #data输入为[[3,1000,3],[3,1000,3][3,1000,3]],加一个'[]'
        #data="[%s]" % data

        #data输入为[[[3,1000,3]]]，直接eval，最终都要eval
        try:
            data=eval(data)
        except Exception,e:
            req="data格式错误:%s" %e
        finally:
            pass
        data_dict={"playerId":"","subjectId":"","panels" :""}
        data_dict["playerId"] = playerid
        data_dict["subjectId"]=subjectid
        data_dict["panels"]=data
        print data_dict

        try:
            req=tests.luckywin.get_response.Post_response(url,data_dict)
            t=time.strftime( ISOTIMEFORMAT, time.localtime(time.time()))
            req=t+" : "+req
        except Exception,e:
            t=time.strftime( ISOTIMEFORMAT, time.localtime(time.time()))
            req=t+"  Error:%s" % e
        finally:
            pass
        return req


        # if gl.GL_WEBINPUT.getcookis=='1':

        # return render.zjpostman("hahaha","filename")




zjpostmanapi=web.application(urls,globals())