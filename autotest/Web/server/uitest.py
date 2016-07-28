#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import os
import tests.luckywin
import tests.check_case
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
import UI_test
import shutil
from shutil import copy


reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"uitest",
      '/exec_uitest',"exec_uitest",
      '/uiresult',"uiresult",
      '/upload',"upload"
     )

m_config = gl.GL_CONFIG

class uitest:
    def GET(self):
        result=gl.GL_DB.query("select * from uiresult order by id desc")
        Dir='./UI_test/upload'
        filename=[]
        for f_file in os.listdir(Dir):
            print "namenamenamenamename:"+f_file
            filename.append(f_file)
        print "filenamefilename:"
        print filename

        return render.uitest(result,filename)

class exec_uitest:
    def POST(self):

        gl.GL_WEBINPUT=web.input()
        drivertype=int(gl.GL_WEBINPUT.webdriver)
        excelname=gl.GL_WEBINPUT.excelname
        print drivertype
        print excelname

        ui_test=UI_test.execuiexcel.execuiexcel(drivertype,excelname)
        ui_test_conn=ui_test.web_conn()

        runtime=ui_test_conn[0]
        passnum=ui_test_conn[1]
        failnum=ui_test_conn[2]
        logname=ui_test_conn[3]


        gl.GL_DB.insert("uiresult",runtime=runtime,passnum=passnum,failnum=failnum,log=logname)

        resultsql=gl.GL_DB.query("select * from uiresult order by id desc")
        result=[]
        for item in resultsql:
            item_dict={"id":item.id,"runtime":item.runtime,"pass":item.passnum,"fail":item.failnum,"check":item.log}
            result.append(item_dict)
        encodedjson=json.dumps(result)
        logging.info("SSSSSSSLLLLLLLLLLLOOOOOOOOOOOWWWWWWWWWWWW")
        logging.info(encodedjson)
        return encodedjson

class uiresult:
    def GET(self):
        uiresult=web.input()
        print uiresult.id
        resultfilepath=gl.GL_DB.query("select log from uiresult where id ="+ uiresult.id)
        for i in resultfilepath:
            resultfilepath=i.log
            print i.log

        if os.path.exists(resultfilepath):
            result=open(resultfilepath,'rb').read()
            print result

        else:
            result=u"对不起，找不到文件"

        return render.uitestresult(result)



class upload:

    def POST(self):
        x = web.input()
        filedir = './UI_test/upload' # change this to the directory you want to store the file in.
        if 'file' in x: # to check if the file-object is created
            filepath=x.uicase.replace('\\','/') # replaces the windows-style slashes with linux ones.
            ffilename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ ffilename,'wb') # creates the file where the uploaded file should be stored

            fout.write(x.file) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        #shutil.copy(x.myfile.file.read(),filedir)
        

        ui=uitest()
        ui.GET()

        return 1



uitestapi=web.application(urls,globals())