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
		try:
			chromedriver="C:\Users\Johanna\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			self.driver=webdriver.Chrome(chromedriver)
			logging.info("open webdriver")
			self.driver.maximize_window()
		except Exception,e:
			logging.error("=====================")
			logging.error(u"浏览器启动失败！")
			logging.error("=====================")

	def get(self,url):
		try:
			logging.info(u"打开链接"+url)
			self.driver.get(url)
		except Exception,e:
			logging.error("====================")
			logging.error(u"访问链接失败: "+url)
			logging.error("====================")


	def sendkeys(self,xpath,keys):
		try:
			logging.info(u"操作：赋值")
			logging.info(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
		except Exception,e:
			logging.error("=====================")
			logging.error(u"赋值xpath操作失败："+xpath)
			logging.error("=====================")
		try:
			logging.info(u"赋值为："+keys)
			location.send_keys(keys)
		except Exception,e:
			logging.error("======================")
			logging.error(u"赋值失败："+keys)
			logging.error("======================")

	def click(self,xpath):
		try:
			logging.info(u"操作：点击")
			logging.info(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
		except Exception,e:
			logging.error("=====================")
			logging.error(u"赋值xpath操作失败："+xpath)
			logging.error("=====================")
		try:
			location.click()
		except Exception,e:
			logging.error("=====================")
			logging.error(u"点击失败！")
			logging.error("=====================")


	def gettext(self,xpath):
		try:
			logging.info(u"操作：获取文本")
			logging.info(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
		except Exception,e:
			logging.error("=====================")
			logging.error(u"赋值xpath操作失败："+xpath)
			logging.error("=====================")
		try:
			text=location.text
			logging.info(u"获取值成功，值为:"+location.text)
		except Exception,e:
			logging.error("====================")
			logging.error(u"获取文本失败")
			logging.error("====================")



	def getattribute(self,xpath,keys)
		try:
			logging.info(u"操作：获取元素属性")
			logging.info(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
		except Exception,e:
			logging.error("=====================")
			logging.error(u"赋值xpath操作失败："+xpath)
			logging.error("=====================")
		try:
			text=location.get_attribute(keys)
			logging.info(u"获取值成功，值为:"+text)
		except Exception,e:
			logging.error("====================")
			logging.error(u"获取文本失败")
			logging.error("====================")

	def closedriver(self):
		try:
			self.driver.close()
			self.driver.quit()
		except Exception,e:
			logging.error("=====================")
			logging.error(u"浏览器关闭成功")
			logging.error("=====================")


if __name__=="__main__":
	# log=Common.conlogs.Logger('log',"INFO","mylogger")
	# log.writeLog()
	action=Action()
	action.get("https://www.baidu.com/")
	action.sendkeys("//*[@id='kw']",u'一箭双雕啊')
	action.click("//*[@id='su']")
	action.getresult()
	action.closedriver()
