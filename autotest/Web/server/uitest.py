#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import os
import tests.luckywin
import tests.check_case
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
import UI_test


reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"uitest",
      '/exec_uitest',"exec_uitest",
      '/uiresult',"uiresult"
     )

m_config = gl.GL_CONFIG

class uitest:
    def GET(self):
        result=gl.GL_DB.query("select * from uiresult order by id desc")
        print "hahahahahahuitestuitestuiterst"
        return render.uitest(result)

class exec_uitest:
    def POST(self):

        gl.GL_WEBINPUT=web.input()
        drivertype=gl.GL_WEBINPUT.webdriver

        uilog=Common.confile.confile("uitestlog")
        logname=uilog.getfilename()
        str="i can't do it,sorry!\n"
        ui_test=UI_test.webconn.webconn(drivertype)
        ui_test_conn=ui_test.web_conn()
        runtime=ui_test_conn[0]
        passnum=ui_test_conn[1]
        failnum=ui_test_conn[2]
        logs=ui_test_conn[3]
        logging.info(logs)

        for i in logs:
            str=str+i+'\n'

        uilog.writefile(str)
        uilog.closefile()

        gl.GL_DB.insert("uiresult",runtime=runtime,passnum=passnum,failnum=failnum,log=logname)

        resultsql=gl.GL_DB.query("select * from uiresult order by id desc")
        result=[]
        for item in resultsql:
            item_dict={"id":item.id,"runtime":item.runtime,"pass":item.passnum,"fail":item.failnum,"check":item.log}
            result.append(item_dict)
        encodedjson=json.dumps(result)
        logging.info("SSSSSSSLLLLLLLLLLLOOOOOOOOOOOWWWWWWWWWWWW")
        logging.info(encodedjson)
        return encodedjson

class uiresult:
    def GET(self):
        uiresult=web.input()
        print uiresult.id
        resultfilepath=gl.GL_DB.query("select log from uiresult where id ="+ uiresult.id)
        for i in resultfilepath:
            resultfilepath=i.log
            print i.log

        if os.path.exists(resultfilepath):
            result=open(resultfilepath,'rb').read()
            print result

        else:
            result=u"对不起，找不到文件"

        return render.uitestresult(result)






uitestapi=web.application(urls,globals())