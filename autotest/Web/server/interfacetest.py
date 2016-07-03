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


reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"interfacetest",
      '/exec_interfacetest',"exec_interfacetest"
     )

m_config = gl.GL_CONFIG

class interfacetest:
    def GET(self):
        result="hahahahahahahahahahahahah"
        print "hahahahahahuitestuitestuiterst"
        return render.interfacetest(result)

class exec_interfacetest:
    def POST(self):
        gl.GL_WEBINPUT=web.input()
        return render.interfacetest("hahaha")



interfacetestapi=web.application(urls,globals())