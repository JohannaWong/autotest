#-*- encoding:utf-8 -*-

import xlsxwriter as wx
import xlrd
import sys
sys.path.append("..")
import os
import json
import time
import urllib2
import urllib
import interface_get_cookie
import interface_request
import ui_get_cookie
import get_response

class excelcon:

	def excon(self):
		workbook=xlrd.open_workbook('./upload/slotinterface.xlsx')
		sheet1=workbook.sheet_by_name('Sheet1')
		print sheet1.name,sheet1.nrows,sheet1.ncols
		print type(sheet1.nrows)

		for i in range(1,sheet1.nrows):
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
				# getcookie=interface_get_cookie.getcookie("youurl","yourusername","youpwd")
				# cookie=getcookie.login()
				data=list(data)
				print data
				req=interface_request.interface_request(url,data,"")
				req.get_withoutcookie()


			elif method=='post':
				print "********method is post"
				# getcookie=interface_get_cookie.getcookie("youurl","yourusername","youpwd")
				# cookie=getcookie.login()
				#data=json.dumps(data)
				#url="http://slots-team-test-new.tuanguwen.com:7310/SlotServer/tpanel"
				print("hahahaha")
				data=eval(data)
				print data
				result = get_response.Post_response(url,data)
				print result
				

			else:
				print "*****neithor get nor post"
			return "hahaha"


if __name__=="__main__":
	req=excelcon()
	req.excon()




