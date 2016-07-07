#-*- encoding:utf-8 -*-

import xlsxwriter as wx
import xlrd
import sys
sys.path.append("..")
import os
import Common.get_cookie
import json
import time
import urllib2
import urllib

class excelcon:

	def excon(self):
		workbook=xlrd.open_workbook('meinterface.xlsx')
		sheet1=workbook.sheet_by_name('Sheet1')
		print sheet1.name,sheet1.nrows,sheet1.ncols
		print type(sheet1.nrows)

		for i in range(sheet1.nrows):
			id=sheet1.cell(i,0).value
			name=sheet1.cell(i,1).value
			method=sheet1.cell(i,2).value
			url=sheet1.cell(i,3).value
			data=sheet1.cell(i,4).value
			data=str(data)
			print id
			print name
			print method
			print url
			print data
			print type(data)

			if method=='get':
				print "********method is get"
				req=Common.get_cookie.getcookie()
				cookie=req.melogin()
				req.meget(url,cookie)


			elif method=='post':
				print "********method is post"
				req=Common.get_cookie.getcookie()
				cookie=req.melogin()
				data=eval(data)
				req.mepost(url,data,cookie)

			else:
				print "*****neithor get nor post"


if __name__=="__main__":
	ex=excelcon()
	ex.excon()




