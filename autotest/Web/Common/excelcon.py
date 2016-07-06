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
#			data="{"userid":"2440","faculty_id":"6"}"

			if method=='get':
				print "********method is get"
				# req=Common.get_cookie.getcookie()
				# cookie=req.melogin()
				# req.meget(url,cookie)


			elif method=='post':
				print "********method is post"
				req=Common.get_cookie.getcookie()
				cookie=req.melogin()
#				data=json.loads(data)
				print data
#				print data.get("userid")
				req.mepost(url,data,cookie)
				#re=request('POST','http://me.hxsd.mn/admin/ajax/get_all_specialties',data)
				#print re
			else:
				print "*****neithor get nor post"





def request(method,url,data):#请求的方法
        try:
            #strtime = datetime.datetime.now().microsecond
            strtime = time.time()
            #print strtime
            rq = urllib2.Request(url)
            
            rq.add_header("Content-Type","application/json")
            
            rq.get_method = lambda:method
            content = urllib2.urlopen(rq,data)
            endtime= time.time()
            cont = content.read()
            http_code = content.code
            #endtime = datetime.datetime.now().microsecond
            l =[]
            l.append(computing_time(strtime, endtime))
            l.append("httpcode:"+str(http_code))
            l.append(cont)
            return l
            #return self.computing_time(strtime, endtime),conten,http_code
            #return conten
        except Exception,e:
            return e


def computing_time(strtime,endtime):#计算时间
        total = endtime-strtime
        totaltime = 'time:'+str("%.3f"%total)
        return totaltime


if __name__=="__main__":
	ex=excelcon()
	ex.excon()




