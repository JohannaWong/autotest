#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
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
      '/exec_uitest',"exec_uitest"
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

        logui=Common.conlogs.Logger('uitestlog',"INFO","uilogger")
        logui.writeLog()
        logname=logui.log_Name()
        ui_test=UI_test.webconn.webconn(drivertype)
        ui_test_conn=ui_test.web_conn()
        runtime=ui_test_conn[0]
        passnum=ui_test_conn[1]
        failnum=ui_test_conn[2]
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






uitestapi=web.application(urls,globals())