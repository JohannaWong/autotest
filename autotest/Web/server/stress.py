#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import Stress_test
import server
import web
from Common import *
import Common.dbconn
import ConfigParser
import gl
import json
import MySQLdb
import json
import Common.pythread
import logging

reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('','stress',
	  "/execstress","execstress"
	)
m_config = gl.GL_CONFIG
script=[
	"test_cooking_tournament",
	"test_word_tournament"
	]

class stress:
	global script
	def GET(self):
		result=gl.GL_DB.query('select * from stress_tasks order by id desc')
		return render.stress(result,script)


class execstress:

	def get_case_name(self):
		gl.GL_WEBINPUT=web.input()
		case_name=gl.GL_WEBINPUT.script_id
		return case_name

	def POST(self):
		gl.GL_WEBINPUT=web.input()
		logging.info("web.input:")
		logging.info(web.input())
		#当选择运行次数时
		if gl.GL_WEBINPUT.exec_type=="1":
			exec_set="运行次数:"+gl.GL_WEBINPUT.run_counts
			run_counts=int(gl.GL_WEBINPUT.run_counts)/int(gl.GL_WEBINPUT.threads)
			all_times=0
			case_name=self.get_case_name()
			def_name = case_name

			# myreq=Stress_test.test_cooking_tournament.test_cooking_tournament()
			# myreq_target=Stress_test.test_cooking_tournament.test_cooking_tournament
			myreq_target = getattr(getattr(Stress_test, case_name),def_name)
			print "1111111111111111111111111"
			print myreq_target
			myreq=myreq_target()
			print "222222222222222222222"
			for i in range(int(run_counts)):
				pythread=Common.pythread.execthreads(int(gl.GL_WEBINPUT.threads),myreq,myreq_target)
				all_times=float(pythread[0])+all_times
			#print float(sum(averagetime[0]))
			api_times=float(all_times)/float(run_counts)
			gl.GL_DB.insert('stress_tasks',scriptname=gl.GL_WEBINPUT.script_id,threadnum=pythread[1],averagetime=api_times,totaltime=pythread[2],errors=pythread[3],exec_set=exec_set)

		#当选择运行时间时
		else:
			return 0


		#raise web.seeother('../stress')
		resultsql=gl.GL_DB.query('select * from stress_tasks order by id desc')
		result=[]
		for item in resultsql:
			item_dict={"id":item.id,"scriptname":item.scriptname,"exec_set":item.exec_set,"threadnum":item.threadnum,"averagetime":item.averagetime,"totaltime":item.totaltime,"errors":item.errors}
			result.append(item_dict)
		encodedjson=json.dumps(result)
		logging.info("stress encodedjson")
		logging.info(encodedjson)
		return  encodedjson



stressapi=web.application(urls,globals())