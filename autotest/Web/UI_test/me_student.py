#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
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

		chromedriver="C:\Users\wangjichong\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
		os.environ["webdriver.chrome.driver"]=chromedriver
		driver=webdriver.Chrome(chromedriver)

		try:
			driver.get('http://me.hxsd.mn/admin/user/login.html')
			time.sleep(4)
			assert u'用户登录' in driver.title

			driver.find_element_by_name("username").send_keys("qiuzhaokun")

			driver.find_element_by_name("password").send_keys("qiuzhaokun")

			driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/button').click()

			assert '系统设置' in driver.title
			PASS=PASS+1
			time.sleep(10)
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

if __name__=="__main__":
	con=webconn(1)
	result=con.web_conn()



