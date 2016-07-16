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
import Action
import xlsxwriter as wx
import xlrd
import xlwt
import Common.conlogs
import Common.confile


#默认得安装一个火狐浏览器
class execuiexcel:

	def __init__(self,drivertype,excelname):
		self.drivertype=drivertype
		self.excelname=excelname

	def web_conn(self):
		PASS=0
		FAIL=0
		# log=Common.conlogs.Logger('log',"INFO","mylogger")
		# logname=log.log_Name()
		# logging.error("jajajajajajaja")
		# print logname
		# log.writeLog()

		t=datetime.datetime.now()
		starttime=datetime.datetime.now()
		action=Action.Action(self.drivertype)
		excelfile='../Web/UI_test/upload/'+self.excelname
		workbook=xlrd.open_workbook(excelfile)
		sheet1=workbook.sheet_by_name('Sheet1')
		try:

			for i in range(1,sheet1.nrows):
				id=sheet1.cell(i,0).value
				defname=sheet1.cell(i,1).value
				xpath=sheet1.cell(i,2).value
				keys=sheet1.cell(i,3).value
				print id,defname,xpath,keys
				f = getattr(action, defname)
				result=f(xpath,keys)
				if result=='pass':
					PASS=PASS+1
				elif result=='fail':
					FAIL=FAIL+1
				sheet1.put_cell(i,4,1,result,0)
			logname=action.getfilename()
				
		finally:
			action.closedriver()

		endtime=datetime.datetime.now()
		totaltime=endtime-starttime
		usetime=str(endtime-starttime)
		hour=usetime.split(':').pop(0)
		minute=usetime.split(':').pop(1)
		second=usetime.split(':').pop(2)
		totaltime=float(hour)*60*60+float(minute)*60+float(second)
		totaltime=str(totaltime)+"s"
		return (totaltime,PASS,FAIL,logname)

if __name__=="__main__":
	con=execuiexcel()
	result=con.web_conn()
	print result



