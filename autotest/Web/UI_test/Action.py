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

	def __init__(self,drivertype):

		self.drivertype=drivertype
		print self.drivertype
		self.log=Common.confile.confile("uitestlog")
		self.logname=self.log.getfilename()

		if int(self.drivertype)==1:
			chromedriver="C:\Users\Johanna\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
			os.environ["webdriver.chrome.driver"]=chromedriver
			self.driver=webdriver.Chrome(chromedriver)
		elif int(self.drivertype)==2:
			self.driver = webdriver.Firefox()
		else:
			self.driver = webdriver.Firefox()
		time.sleep(2)
		try:
			self.log.writefile("open webdriver")
			self.driver.maximize_window()
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:浏览器启动失败！")
			self.log.writefile("=====================")

	def getfilename(self):
		return self.logname

	def get(self,xpath,keys):
		try:
			self.log.writefile(u"打开链接"+keys)
			self.driver.get(keys)
			result='pass'
		except Exception,e:
			self.log.writefile("====================")
			self.log.writefile(u"ERROR:访问链接失败: "+keys)
			self.log.writefile("====================")
			result='fail'
		return result


	def sendkeys(self,xpath,keys):
		try:
			self.log.writefile(u"操作：赋值")
			self.log.writefile(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
			result='pass'
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:赋值xpath操作失败："+xpath)
			self.log.writefile("=====================")
			result='true'
		try:
			self.log.writefile(u"赋值为："+keys)
			location.send_keys(keys)
			result='pass'
		except Exception,e:
			self.log.writefile("======================")
			self.log.writefile(u"ERROR:赋值失败："+keys)
			self.log.writefile("======================")
			result='fail'
		return result

	def click(self,xpath,keys):
		try:
			self.log.writefile(u"操作：点击")
			self.log.writefile(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
			result='pass'
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:赋值xpath操作失败："+xpath)
			self.log.writefile("=====================")
			result='fail'
		try:
			self.log.writefile("点击成功")
			location.click()
			result='pass'
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:点击失败！")
			self.log.writefile("=====================")
			result='true'
		return result


	def gettext(self,xpath,keys):
		try:
			time.sleep(2)
			self.log.writefile(u"操作：获取文本")
			self.log.writefile(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
			result='pass'
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:赋值xpath操作失败："+xpath)
			self.log.writefile("=====================")
			result='fail'
		try:
			text=location.text
			self.log.writefile(u"获取值成功，值为:"+location.text)
			print text
			result='pass'
		except Exception,e:
			self.log.writefile("====================")
			self.log.writefile(u"ERROR:获取文本失败")
			self.log.writefile("====================")
			result='fail'
		return result



	def getattribute(self,xpath,keys):
		try:
			self.log.writefile(u"操作：获取元素属性")
			self.log.writefile(u"xpath:"+xpath)
			location=self.driver.find_element_by_xpath(xpath)
			result='pass'
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:赋值xpath操作失败："+xpath)
			self.log.writefile("=====================")
			result='fail'
		try:
			text=location.get_attribute(keys)
			self.log.writefile(u"获取值成功，值为:"+text)
			result='pass'
		except Exception,e:
			self.log.writefile("====================")
			self.log.writefile(u"ERROR:获取文本失败")
			self.log.writefile("====================")
			result='fail'
		return result

	def asserttitle(self,xpath,keys):
		try:
			time.sleep(2)

			assert keys in self.driver.title
			self.log.writefile("断言成功，title中存在 :"+keys)
			result='pass'
		except:
			self.log.writefile("====================")
			self.log.writefile(u"ERROR:断言失败，title中不存在:"+keys)
			self.log.writefile("====================")
			result='fail'
		return result

	def element_displayed(self,xpath,keys):
		try:
			display=self.driver.find_element_by_xpath(xpath).is_displayed()
			self.log.writefile("元素正常显示"+xpath)
			result='pass'
		except:
			self.log.writefile("=======================")
			self.log.writefile(u"ERROR:元素"+xpath+":"+display)
			self.log.writefile("=======================")
			result='fail'
		return result



	def closedriver(self):
		try:
			self.driver.close()
			self.driver.quit()
			self.log.closefile()
		except Exception,e:
			self.log.writefile("=====================")
			self.log.writefile(u"ERROR:浏览器关闭失败")
			self.log.writefile("=====================")


if __name__=="__main__":
	# log=Common.conlogs.Logger('log',"INFO","mylogger")
	# log.writeLog()
	action=Action(1)
	action.get("","https://www.baidu.com/")
	action.asserttitle("","百度一下")
	action.sendkeys("//*[@id='kw']",u'一箭双雕啊')
	action.click("//*[@id='su']","")
	action.asserttitle("","百度搜索")
	action.closedriver()
