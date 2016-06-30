#-*- encoding:utf-8 -*-
import tests
import tests.luckywin
import tests.check_case
import server
import web
from Common import *
import Common.dbconn
import sys
import ConfigParser
import gl
import json
import MySQLdb
import json
import server.hello_jc
import server.slot
import server.stress
import server.uitest
import Common.conlogs
reload(sys)
sys.setdefaultencoding("utf8")
#from Web import luckywin
urls=('/','index',
      '/hello',server.hello_jc.helloapi,
       '/slot',server.slot.slotapi,
       '/stress',server.stress.stressapi,
       '/uitest',server.uitest.uitestapi
       )

m_config = gl.GL_CONFIG
render=web.template.render('templates/')

class index:
    def GET(self):
        return render.hello("Hello World!")
    
#wy的slot项目

    
#读web.conf文件
def _init_config():
    cf = ConfigParser.ConfigParser()
    cf.read("web.conf")
    m_config['db_ip'] = cf.get("db","ip")
    m_config['db_user'] = cf.get("db","user")
    m_config['db_pwd'] = cf.get("db","password")
    m_config['db_name'] = cf.get("db","dbname")
    m_config['db_port'] = cf.get("db","port")


#定义全局变量DB及读取模板
def _init_web_component():
    gl.GL_DB = web.database(dbn='mysql',user=m_config['db_user'], pw=m_config['db_pwd'],db=m_config['db_name'])
    gl.GL_RENDER = web.template.render('templates/')      
       
if __name__=="__main__":
   # _init_case()
    _init_config()
    _init_web_component()
    log=Common.conlogs.Logger('log',"INFO","mylogger")
    log.writeLog()
    app=web.application(urls,globals())
    app.run()

