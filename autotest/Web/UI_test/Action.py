#-*- encoding:utf-8 -*-
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
reload(sys)
sys.setdefaultencoding("utf8")

class Action:

	def __init__(self):
			chromedriver="C:\Users\wangjichong\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			self.driver=webdriver.Chrome(chromedriver)
			logging.info("open webdriver")

	def get(self,url):
		print "url"+url
		logging.info(u"打开链接"+url)
		self.driver.get(url)


	def sendkeys(self,xpath,keys):
		logging.info(u"操作：赋值")
		logging.info(u"xpath:"+xpath)
		logging.info(u"赋值为："+keys)
		self.driver.find_element_by_xpath(xpath).send_keys(keys)

	def click(self,xpath):
		logging.info(u"操作：点击")
		logging.info(u"xpath:"+xpath)
		self.driver.find_element_by_xpath(xpath).click()

	def getresult(self):
		time.sleep(2)
		logging.info(u"操作：获取结果")
		#logging.info(u"xpath:"+xpath)
		result=self.driver.find_element_by_class_name("nums").text
		logging.info(u"结果为："+result)

	def closedriver(self):
		self.driver.close()
		self.driver.quit()


if __name__=="__main__":
	# log=Common.conlogs.Logger('log',"INFO","mylogger")
	# log.writeLog()
	action=Action()
	action.get("https://www.baidu.com/")
	action.sendkeys("//*[@id='kw']",u'一箭双雕啊')
	action.click("//*[@id='su']")
	action.getresult()
	action.closedriver()
