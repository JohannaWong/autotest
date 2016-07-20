#-*- encoding:utf-8 -*-
import web
import sys
import os
import code
import re

condb=web.database(dbn='mysql',user="root", pw="111111",db="slot")
class checkcase:
	#定义getdir方法，遍历tests文件夹下的文件件夹名字，并写入dirlist列表中，同时如果DB的productline表中不存在，则执行插入操作
	def getdir(self):
		#建立数据库连接
		global condb
		#定义homedir，为tests文件夹
		# homedir=os.getcwd()
		# homedir=os.path.join(homedir,"tests")
		homedir=".\\tests"
		#定义dirlist，用于存放tests下的文件夹名字
		dirlist=[]
		#遍历tests文件夹下的所有子文件及子文件夹，因为还有py文件，所以此处要排除
		for pathname in os.listdir(homedir):
			#拼出子文件夹及文件路径，用于判断是否是文件
			childpath=os.path.join(homedir,pathname)
			#如果不是文件，为文件夹
			if os.path.isfile(childpath)==False:
				#查询一下，判断此项目是否已经存在
				productlist_name=condb.query("select id from productline where productline_name='%s'" %pathname)
				#因为执行数据库查询，得到的是一个iterator类型，所以判断得到结果的长度是否为0，为0则表示在db中不存在，为新增的，执行插入及写init操作
				if len(productlist_name)==0:   
					#写init操作
					fsock = open(homedir+"\__init__.py", "a")   #如果init文件中没有这个项目，则新增
					fsock.write("\nimport "+pathname)
					fsock.close()
					#写库操作
					condb.insert('productline',productline_name='%s' %pathname)#如果在数据库中没有该项目~则新增一个项目
				#将写有项目写入dirlist，写在if外，包括了所有已存在的、不存在的项目，是全的，用于getfilename方法中，遍历使用，此入写入的是全路径
				dirlist.append(childpath)

		return dirlist


#以“test_”开头的case文件，属于需要读取的文件，其他文件不读
	def getfilename(self):
		#建立数据库连接
		global condb
		#执行getdir()方法，初始化项目同时，得到所有项目的的路径
		dirlist=self.getdir()
		#遍历tests文件夹下所有的项目
		for filedir in dirlist:
			# homedir=os.getcwd()
			# homedir=os.path.join(homedir,"tests")
			#定义根目录homedir
			homedir=".\\tests"
			#利用replace方法，去掉其他的路径，只得到项目名字
			dirname=filedir.replace("%s" %homedir,"").replace("\\","")
			#获取项目的productid
			productid=condb.query("select id from productline where productline_name='%s'" %dirname)
			#productid为iterator类型，只可遍历一次不能，不能保存，后面想继续使用此值，需要将其保存到productid中
			for i in productid:
				productid=int(i.id)

			print "LLLLLLLLLLLLLLLLLLLLLLLLLLLOOK"


			#如果路径下没有文件，跳出循环，去请求下一个项目文件夹，返回0
			if len(os.listdir(filedir))==0:
				return 0
			#如果没有跳出循环，则证明是有文件存在的，则遍历此项目下所有文件，
			for filename in os.listdir(filedir):
				#如果文件中有'test_'，则证明为用例文件
				if 'test_' in filename: #用例入库
					print filedir
					#filename，例如,test_slot.py or test_slot.pyc，则执行split，以.为分割，得到数据的第一个数据，即test_slot，此处缺点是相同的用例可能要判断两次，因为还有pyc文件
					casename=filename.split(".")[0]
					#查询一下，这个case在数据库中是否已经存在
					condb_caseid=condb.query("select caseid from cases where casename ='%s' and productid = '%s'" %(casename,productid))
					#拼出用例的全路径
					casefiledir=os.path.join(filedir,filename)
					print casefiledir
					#如果此case文件在数据库中不存在的话，添加一条
					if len(condb_caseid)==0:
						#执行插入操作
						condb.insert('cases',casename='%s' %casename,productid='%d' %productid)
						#插入后，把caseid读出来
						condb_caseid=condb.query("select caseid from cases where casename='%s'" %casename)
						#由于，condb_caseid为iterator类型，后面需要使用此值，将值保存到caseid中
						for j in condb_caseid:
							caseid=int(j.caseid)
							#执行getdefname()方法，遍历此用例文件下所有的方法，如果方法不存在则执行插入操作
							self.getdefname(casefiledir,caseid)
						#写入init文件
						fsock = open(filedir+"\__init__.py", "a")   #写入每个文件夹的init文件中，初始化用例
						fsock.write("\nimport "+casename)
						fsock.close()
					#如果此case文件在数据库中已经存在的话，则查出caseid，执行getdefname()方法，如果用例下有新增方法则执行插入操作
					else:
						condb_caseid=condb.query("select caseid from cases where casename='%s'" %casename)
						for j in condb_caseid:
							caseid=int(j.caseid)
							self.getdefname(casefiledir,caseid)
						

		return 0



#以test开头的方法，视为合法的方法
	def getdefname(self,filename,caseid):
		global condb
		#定义defname，用于存放读出来的方法名
		defname=[]
		#打开这个方法文件
		fr=open(filename)
		#逐行读取文件内容
		for line in fr.readlines():
			#如果此行包含test开头的方法，则将方法名从line中分割出来
			if 'def test' in line:
				line=line.split("(")
				line=line[0].replace("def ","")
				defname.append(line)
		#遍历此case文件中所有def，如果数据库中没有的话，则insert一条
		for dname in defname:
			condb_defid=condb.query("select defid from def where defname='%s' and caseid='%s'" %(dname,caseid))
			if len(condb_defid)==0:
				condb.insert('def',defname='%s' %dname,caseid='%d' %caseid)
			else:
				print "EEEEEEEEEEEEEEESIXT"

		return defname





	# def condb(self):
	# 	condb=web.database(dbn='mysql',user="root", pw="111111",db="slot")
	# 	return condb

		
if __name__=="__main__":

	c2=checkcase()
	c2.getfilename()
