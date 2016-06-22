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

reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"uitest"
     )

m_config = gl.GL_CONFIG

class uitest:
    def GET(self):
        return render.uitest();



uitestapi=web.application(urls,globals())