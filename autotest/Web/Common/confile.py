#-*- coding: UTF-8 -*-
import web
import sys
sys.path.append("..")
import os
import code
import re
import time

logDir=r"..\\logs"
ISOTIMEFORMAT='%Y%m%d%H%M%S'

class confile:
	def __init__(self,filename):
		self.filename=filename
		self.filename=logDir+r"\\"+self.filename+str(time.strftime(ISOTIMEFORMAT))+".txt"
		print self.filename
		self.fc=open(self.filename,'w+')

	def getfilename(self):
		print self.filename
		return self.filename


	def writefile(self,str):
		self.fc.write(str+'\n')


	def closefile(self):
		self.fc.close()


# if __name__=="__main__":
# 	conf=confile("jctest")
# 	conf.getfilename()
# 	conf.writefile("whereareyou")
# 	conf.writefile("hellohellohellohellohellohellohello")
# 	conf.writefile("i don't know")
# 	conf.closefile()

