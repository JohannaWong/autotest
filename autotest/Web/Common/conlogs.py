#-*- coding: UTF-8 -*-
import logging
import logging.handlers
import sys
import os
import time

logDir=r"..\\Web\\logs"
logName=logDir+r"\\"+"consolg.log"
ISOTIMEFORMAT='%Y%m%d%H%M%S'

class Logger():
	def __init__(self,logName,logLevel,logger):
		#创建一个logger实例
		self.logger=logging.getLogger(logger)
		self.logger.setLevel(logging.INFO)
		self.logger_ch=logging.getLogger()
		self.logger_ch.setLevel(logging.INFO)

		#判断log文件夹下有文件的话，就删掉，防止日志文件生成太多
		# for t in os.listdir(logDir):
		# 	logs=logDir+r"\\"+t
		# 	print logs
		# 	os.remove(logs)

		self.logName=logDir+r"\\"+logName+str(time.strftime(ISOTIMEFORMAT))+".txt"
		#生成日志方法一,判断名字是否存在,存在则删除
		if os.path.exists(self.logName):
			os.remove(self.logName)

		# 定义一个Handler打印INFO及以上级别的日志到sys.stderr,输出到控制台
		ch=logging.StreamHandler()
		ch.setLevel(logLevel)
	#创建一个handler，用于写入日志文件，handler可以把日志内容写到不同的路径下

		fh=logging.FileHandler(self.logName,'w')
		fh.setLevel("WARNING")
		# 设置日志打印格式
		formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
		logging.basicConfig(filename=self.logName,filemode="w")
		
		ch.setFormatter(formatter)
		fh.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
		self.logger.addHandler(fh)
		self.logger_ch.addHandler(ch)


	def writeLog(self):
		return self.logger

	def log_Name(self):
		return self.logName



# if __name__=="__main__":
# 	log=Logger('log',"INFO","mylogger")
# 	log.writeLog()
