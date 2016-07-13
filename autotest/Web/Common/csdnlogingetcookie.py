#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import os,time
import sys
sys.path.append("..")
import web
import datetime

#默认得安装一个火狐浏览器
class webconn:
	def __init__(self,drivertype):
		self.drivertype=drivertype


	def web_conn(self):  
		PASS=0
		FAIL=0
		t=datetime.datetime.now()
		starttime=datetime.datetime.now()

		if int(self.drivertype)==1:
			chromedriver="C:\Users\Johanna\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			driver=webdriver.Chrome(chromedriver)
		elif int(self.drivertype)==2:
			driver = webdriver.Firefox()
		else:
			driver = webdriver.Firefox()
		try:

			driver.get('https://passport.csdn.net/account/login')
			time.sleep(2)
			assert u'帐号登录' in driver.title

			driver.find_element_by_id("username").send_keys(u"felixir@qq.com")
			print "输入用户名felixir@qq.com"

			driver.find_element_by_id("password").send_keys(u"123qwe")
			print "输入密码123qwe"

			driver.find_element_by_class_name("logging").click()
			time.sleep(2)

			assert u'全球最大中文' in driver.title

			dic_cookie={}

			driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbb'})
			for cookie in driver.get_cookies():
				print "%s -> %s" %(cookie['name'],cookie['value'])
				dic_cookie[cookie['name'].encode("UTF-8")]=cookie['value'].encode("UTF-8")

			print "cookie cookie cookie cookie cookie"
			#dic_cookie=eval(dic_cookie)

			print dic_cookie
			#cookie=driver.get_cookies()


			PASS=PASS+1
		except Exception,e:
			print(str(Exception)+":"+str(e))
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
		return (totaltime,PASS,FAIL)

if __name__=="__main__":
	con=webconn(1)
	result=con.web_conn()



