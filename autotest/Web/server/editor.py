#-*- encoding:utf-8 -*-
import sys
sys.path.append("..")
import tests
import tests.luckywin
import tests.check_case
import server
import web
from Common import *
import Common.dbconn
import Common.conlogs
import ConfigParser
import gl
import json
import MySQLdb
import json
import logging
import os
sys.setdefaultencoding("utf8")

urls = ("", 'case_editor',
        "/check_file",'check_file',
        "/AJAX_Save_file", 'AJAX_Save_file')

render = web.template.render('templates/')
project_name = ""
case_name = ""


class case_editor:

    def GET(self):
        global project_name
        global case_name
        gl.GL_WEBINPUT=web.input()
        print web.input()
        taskid=gl.GL_WEBINPUT.taskid
        project_name=gl.GL_DB.query('SELECT productline_name from productline LEFT JOIN tasks on productline.id=tasks.productid where taskid='+taskid)
        for i in project_name:
            project_name=i.productline_name
        case_name=gl.GL_DB.query('SELECT casename from cases LEFT JOIN tasks on cases.caseid=tasks.caseid where taskid='+taskid)
        for i in case_name:
            case_name=i.casename
        path = sys.path[0]
        file_path = path+"/tests/"+project_name+'/'+case_name+'.py'
        file_path=file_path.replace('\\',r'\\').replace('/',r'\\')
        print file_path
        print os.path.exists(file_path)
        file_object = open(file_path, 'r+')
        try:
            all_text = file_object.read()
            print "hohohohohohohoho"
            print repr(all_text)
        finally:
            file_object.close()
            return render.Case_editor(all_text,project_name,case_name)


class check_file():
    def GET(self):
        gl.GL_WEBINPUT=web.input()
        print web.input()
        taskid=gl.GL_WEBINPUT.taskid
        project_name=gl.GL_DB.query('SELECT productline_name from productline LEFT JOIN tasks on productline.id=tasks.productid where taskid='+taskid)
        for i in project_name:
            project_name=i.productline_name
        case_name=gl.GL_DB.query('SELECT casename from cases LEFT JOIN tasks on cases.caseid=tasks.caseid where taskid='+taskid)
        for i in case_name:
            case_name=i.casename
        path = sys.path[0]
        file_path = path+"/tests/"+project_name+'/'+case_name+'.py'
        file_path=file_path.replace('\\',r'\\').replace('/',r'\\')
        if(os.path.exists(file_path)):
             return taskid
        else:
            return "0"


class AJAX_Save_file:

    """docstring for AJAX_Save_file:"""

    def POST(self):
        path = sys.path[0]
        global project_name
        global case_name
        print project_name
        print case_name
        file_path = path+"/tests/"+project_name+'/'+case_name+'.py'
        file_path=file_path.replace('\\',r'\\').replace('/',r'\\')
        file_path_tmp=path+"/tests/"+project_name+'/'+case_name+'_tmp.py'
        file_path_tmp=file_path_tmp.replace('\\',r'\\').replace('/',r'\\')
        print file_path_tmp
        result=[]
        x = web.input()
        print x
        if 'file_Value' in x:
            try:
                fout_tmp = open(file_path_tmp, 'wb')
                # writes the uploaded file to the newly created file.
                fout_tmp.write(x.file_Value)
            finally:
                fout_tmp.close()
                command="pylint -E %s" % file_path_tmp
                result=os.popen(command).readlines()
                os.remove(file_path_tmp)

        if len(result)>0:
            encodedjson=json.dumps(result)
            return encodedjson
        else:
            if 'file_Value' in x:  # to check if the file-object is created
            # replaces the windows-style slashes with linux ones.
            # splits the and chooses the last part (the filename with
            # extension)
            # creates the file where the uploaded file should be stored
                try:
                    fout = open(file_path, 'wb')
                    # writes the uploaded file to the newly created file.
                    print "ohahaha"
                    print repr(x.file_Value)
                    fout.write(x.file_Value)
                
                finally:
                    fout.close()# closes the file, upload complete.
            return "1"


editorapi = web.application(urls, locals())
