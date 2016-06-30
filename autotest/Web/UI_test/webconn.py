#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time
import sys
sys.path.append("..")
from Common import *
import Common.conlogs
import web
import logging
import datetime

#默认得安装一个火狐浏览器
class webconn:
	def __init__(self,drivertype):
		self.drivertype=drivertype


	def web_conn(self):  
		PASS=0
		FAIL=0
		logs=[]
		t=datetime.datetime.now()
		starttime=datetime.datetime.now()

		if int(self.drivertype)==1:
			chromedriver="C:\Users\Johanna\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			driver=webdriver.Chrome(chromedriver)
			logs.append("open firefoxdriver")
		elif int(self.drivertype)==2:
			driver = webdriver.Firefox()
		else:
			driver = webdriver.Firefox()


		try:

			logging.info("open firefox driver")
			driver.get('http://www.python.org')
			logging.info("open pythonorg homepage")
			logs.append("open pythonorg homepage")
			time.sleep(3)
			assert 'Python' in driver.title
			logging.info("if the driver title has the word 'Python'")
			logs.append("if the driver title has the word 'Python'")
			elem = driver.find_element_by_name('q')
			logging.info("fined element by name 'q'")	
			logs.append("fined element by name 'q'")
			elem.send_keys('pycon')
			logging.info("insert pycon")
			logs.append("insert pycon")
			elem.send_keys(Keys.RETURN)
			logging.info("enter")
			logs.append("enter")
			assert 'No results found.' not in driver.page_source
			logging.info("make sure there is no 'No results found'")
			logs.append("make sure there is no 'No results found'")
			logging.info("success")
			logs.append("test1 success")
			PASS=PASS+1
		except Exception,e:
			logging.error(str(Exception)+":"+str(e))
			logs.append(str(Exception)+":"+str(e))
			FAIL=FAIL+1
		finally:
			driver.close()
			driver.quit()

		endtime=datetime.datetime.now()
		totaltime=endtime-starttime
		usetime=str(endtime-starttime)
		hour=usetime.split(':').pop(0)
		minute=usetime.split(':').pop(1)
		second=usetime.split(':').pop(2)
		totaltime=float(hour)*60*60+float(minute)*60+float(second)
		totaltime=str(totaltime)+"s"
		return (totaltime,PASS,FAIL,logs)

# if __name__=="__main__":
# 	con=webconn()
# 	result=con.web_conn()
# 	# logging.info(result[0])
# 	# logging.info(result[1])
# 	# logging.info(result[2])
# 	print result[0]
# 	print result[1]
# 	print result[2]

