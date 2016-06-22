#-*- encoding:utf-8 -*-
print "hellohellojcjcjcjcjcjcj"
import web
import sys
#sys.setdefaultencoding("utf8")
urls=(  	"",'repos',
          '/','hello_jc')
render=web.template.render('templates/')

class repos:
	def GET(self):
		raise web.seeother("/")

class hello_jc:
    def GET(self):
        #conn=Common.dbconn.conndb("127.0.0.1","root","111111","slot",3306)
        #finished=gl.GL_DB.query('select * from tasks order by taskid desc;')
        
        return "wohejiahahahahah"
    def POST(self):
    	return "wodejia"


helloapi=web.application(urls,locals())