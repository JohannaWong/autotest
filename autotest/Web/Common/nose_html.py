#-*- encoding:utf-8 -*-
from nose.plugins.plugintest import run_buffered as run  
from nose_htmloutput import HtmlOutput
import nose_htmloutput
import unittest
import sys
sys.path.append("../")  
import os
reload(sys)
sys.setdefaultencoding("utf8")

#要执行的文件为outfile
def runnose():
	#homedir=".\\nose_tests"
	homedir="./nose_tests/"
	result=homedir+"result.html"
	output='./nose_tests/'
	print "@@@@@@@@@@@@@@@@@@@@@@@@@ELSA@@@@@@@@@@@@@@@"
	os.system("nosetests -v -s --with-html --html-file="+result+" " +output)
	print "#####################SNOWBAAL##################"


if __name__=="__main__":
	rnose=runnose()