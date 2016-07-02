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

		if int(self.drivertype)==1:
			chromedriver="C:\Users\Johanna\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			driver=webdriver.Chrome(chromedriver)
			logs.append("open webdriver")
		elif int(self.drivertype)==2:
			driver = webdriver.Firefox()
		else:
			driver = webdriver.Firefox()


		try:

			logging.info("open webdriver")
			driver.get('https://www.baidu.com/')
			logging.info("open baidu.com")
			logs.append("open baidu.com")
			time.sleep(4)
			assert u'百度一下' in driver.title
			# driver.find_element_by_link_text(u"登录").click()
			# time.sleep(2)
			# logs.append(u"点击登录")
			# login_name=driver.find_element_by_id("TANGRAM__PSP_8__userName")
			# login_name.send_keys('w2256367')
			# logs.append(u"输入用户名:w2259367")
			# login_pwd=driver.find_element_by_id("TANGRAM__PSP_8__password")
			# login_pwd.send_keys("19870918")
			# logs.append(u"输入密码")
			# time.sleep(2)
			# driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
			# print "1111111111111"
			# #assert 'w2259367' in driver.find_element_by_class_name("s-user-name-top").text
			# logs.append(u"登录成功")
			# print "222222222222222"

			driver.find_element_by_id("kw").send_keys(u"一箭双雕啊")
			logs.append(u"输入关键字‘一箭双雕啊’")
			print "333333333333"

			driver.find_element_by_id("su").click()
			logs.append("点击搜索")
			print "444444444444"
			time.sleep(2)

			assert u'百度搜索' in driver.title

			googleresult=driver.find_element_by_class_name("nums").text
			logs.append(u"结果为"+googleresult)

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

if __name__=="__main__":
	con=webconn(1)
	result=con.web_conn()



