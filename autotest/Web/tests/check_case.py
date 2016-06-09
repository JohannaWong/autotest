#-*- encoding:utf-8 -*-
import web
import sys
import os
import code
import re
class checkcase:

	def getdir(self):
		homedir=os.getcwd()
		homedir=os.path.join(homedir,"tests")
		dirlist=[]
		for pathname in os.listdir(homedir):
			childpath=os.path.join(homedir,pathname)			
			if os.path.isfile(childpath)==False:
				print childpath
				productlist_name=self.condb().query("select id from productline where productline_name='%s'" %pathname)
				if len(productlist_name)==0:
					self.condb().insert('productline',productline_name='%s' %pathname)
				dirlist.append(childpath)

		return dirlist


#以“test_”开头的case文件，属于需要读取的文件，其他文件不读
	def getfilename(self):
		dirlist=self.getdir()
		#遍历tests文件夹下所有的项目
		for filedir in dirlist:
			#从当前项目的路径下得到数据库中此项目的id
			homedir=os.getcwd()
			homedir=os.path.join(homedir,"tests")
			dirname=filedir.replace("%s" %homedir,"").replace("\\","")
			productid=self.condb().query("select id from productline where productline_name='%s'" %dirname)
			#productid不能保存，需要将其保存到productid中
			for i in productid:
				productid=int(i.id)

			print "LLLLLLLLLLLLLLLLLLLLLLLLLLLOOK"


			#如果路径下没有文件，跳出循环，返回0
			if len(os.listdir(filedir))==0:
				return 0

			for filename in os.listdir(filedir):

				if 'test_' in filename:
					print filedir
					casename=filename.split(".")
					casename=casename[0]
					print casename
					condb_caseid=self.condb().query("select caseid from cases where casename ='%s'" %casename)
					#print condb_caseid[0].caseid
					print len(condb_caseid)
					

					casefiledir=os.path.join(filedir,filename)
					print casefiledir
					#如果此case文件在数据库中不存在的话，添加一条
					if len(condb_caseid)==0:
						self.condb().insert('cases',casename='%s' %casename,productid='%d' %productid)
						condb_caseid=self.condb().query("select caseid from cases where casename='%s'" %casename)
						for j in condb_caseid:
							caseid=int(j.caseid)
					    	self.getdefname(casefiledir,caseid)
					else:
						condb_caseid=self.condb().query("select caseid from cases where casename='%s'" %casename)
						for j in condb_caseid:
							caseid=int(j.caseid)
							self.getdefname(casefiledir,caseid)
						

		return 0



#以test开头的方法，视为合法的方法
	def getdefname(self,filename,caseid):
		defname=[]
		fr=open(filename)
		for line in fr.readlines():
			if 'def test' in line:
				line=line.split("(")
				line=line[0].replace("def ","")
				print("GGGGGGGGGGGGGGGGGOD")
				print line
				defname.append(line)
		#遍历此case文件中所有def，如果数据库中没有的话，则insert一条
		for dname in defname:
			condb_defid=self.condb().query("select defid from def where defname='%s'" %dname)
			#
			if len(condb_defid)==0:
				self.condb().insert('def',defname='%s' %dname,caseid='%d' %caseid)
			else:
				print "EEEEEEEEEEEEEEESIXT"

		return defname





	def condb(self):
		condb=web.database(dbn='mysql',user="root", pw="111111",db="slot")
		return condb


if __name__=="__main__":

	c2=checkcase()
	c2.getfilename()
