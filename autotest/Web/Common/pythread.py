#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import datetime
import time
import threading
from time import ctime,sleep
import web
import Stress_test
import Stress_test.test_cooking_tournament
import ConfigParser
reload(sys)
sys.setdefaultencoding("utf8")

#myreq_target=Stress_test.test_cooking_tournament.test_cooking_tournament
#myreq=Stress_test.test_cooking_tournament.test_cooking_tournament()

def execthreads(threadnum,myreq,myreq_target):
	#定义thread中需要传递的args:myreq_args
	#myreq_args=Stress_test.test_word_tournament.init_token()
	#获取接口的响应时间及错误数
	#myreq=Stress_test.test_cooking_tournament.test_cooking_tournament()
	#定义thread中需要传递的target:myreq_target
	#myreq_target=Stress_test.test_cooking_tournament.test_cooking_tournament
	
	threads=[]
	thinktime=0

	starttime=datetime.datetime.now()

	for i in range(threadnum):
		#t=threading.Thread(target=myreq_target,args=('%s' %myreq_args,))
		t=threading.Thread(target=myreq_target)
		threads.append(t)

	for t in threads:
		time.sleep(thinktime)
		print "thread '%s'" %t
		t.setDaemon(True)
		t.start()
	t.join()

	endtime=datetime.datetime.now()

	print "all over %s" %ctime()

	time.sleep(3)
	print "HAHAHAHAHAHAHA"
	print myreq

	AverageTime="{:.3f}".format(float(sum(myreq[0]))/float(len(myreq[0]))) 
	print "Average Response Time %s ms.\n" %AverageTime

	usetime=str(endtime-starttime)
	hour=usetime.split(':').pop(0)
	minute=usetime.split(':').pop(1)
	second=usetime.split(':').pop(2)
	totaltime=float(hour)*60*60+float(minute)*60+float(second)
	totaltime=totaltime-float(threadnum*thinktime)
	errors=len(myreq[1])

	print "threads number:'%s'\n" %threadnum
	print "totaltime:'%s' s.\n" %(totaltime)
	print "errors:%d.\n"%(len(myreq[1]))
	return (AverageTime,threadnum,totaltime,errors)


# if __name__=='__main__':
# 	execthreads(1,myreq,myreq_target)