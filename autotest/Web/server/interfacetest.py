#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import os
import server
import web
from Common import *
import Common.dbconn
import ConfigParser
import gl
import json
import MySQLdb
import json
import logging
import interfacetest


reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"interfacetest",
      '/exec_interfacetest',"exec_interfacetest",
      '/upload',"upload"
     )

m_config = gl.GL_CONFIG

class interfacetest:
    def GET(self):
        result="hahahahahahahahahahahahah"
        print "hahahahahahuitestuitestuiterst"
        Dir='./interfacetest/upload'
        filename=[]
        for file in os.listdir(Dir):
            filename.append(file)
        print filename

        return render.interfacetest(result,filename)


class exec_interfacetest:
    def POST(self):
        gl.GL_WEBINPUT=web.input()
        print gl.GL_WEBINPUT
        print gl.GL_WEBINPUT.getcookis
        print gl.GL_WEBINPUT.excelname
        req=interfacetest.execinterfaceexcel.excelcon()
        req.excon()

        # if gl.GL_WEBINPUT.getcookis=='1':
            

        return render.interfacetest("hahaha",filename)



class upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<span style="color: red;font-weight:bold;" >注意暂时不要上传中文名字文件</a></span>
<br/>
<br/>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        print os.getcwd()
        filedir = './interfacetest/upload' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            print filepath
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        #shutil.copy(x.myfile.file.read(),filedir)
        raise web.seeother("../interfacetest")



interfacetestapi=web.application(urls,globals())