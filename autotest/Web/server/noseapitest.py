#-*- encoding:utf-8 -*-

import sys
sys.path.append("..")
import tests
import tests.luckywin
import tests.check_case
import server
import web
import ConfigParser
import gl
import json
import MySQLdb
import json
import logging
import os
import Common

reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"noseapitest",
      '/execnoseapitest',"execnoseapitest",
      '/nosetestresult',"nosetestresult"
)

m_config = gl.GL_CONFIG

class noseapitest:
    def GET(self):
        print "HAHAHAHAHAHAHAHA"

        return render.noseapitest()

class execnoseapitest:
    def GET(self):
      print "^^^^^^^^^^^^^^^JOAN^^^^^^^^^^^^"
      rnose=Common.nose_html.runnose()
      print "++++++++++++++++ANNA+++++++++++++++"
      return render.noseapitest()

class nosetestresult:
    def GET(self):
        noseresult=web.input()
        resultfilepath=".\\nose_tests\\result.html"
        if os.path.exists(resultfilepath):
            print resultfilepath
            render1=web.template.render('nose_tests/')
            return render1.result()
        else:
            result=u"对不起，找不到文件"



noseapitestapi=web.application(urls,globals())