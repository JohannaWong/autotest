#-*- coding: UTF-8 -*-
import web
import sys
sys.path.append("..")
import os
import code
import re
import time

logDir=r"..\\Web\\logs"
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



