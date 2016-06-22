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
import ConfigParser
import gl
import json
import MySQLdb
import json
import logging

reload(sys)
sys.setdefaultencoding("utf8")
render=web.template.render('templates/')
urls=('',"slot",
      '/execslot','execslot',
      '/ajaxgetprojects','ajaxgetprojects',
      '/ajax_get_case','ajax_get_case',
      '/ajax_check_case','ajax_check_case',
      '/ajax_ReSubmit','ajax_ReSubmit')

m_config = gl.GL_CONFIG

class slot:
    def GET(self):
        print "HAHAHAHAHAHAHAHA"
        conn=Common.dbconn.conndb("127.0.0.1","root","111111","slot",3306)
        finished=gl.GL_DB.query('select * from tasks order by taskid desc;')
        sql=("select tasks.taskid as taskid,productline.productline_name as productline_name,"
             "cases.casename as casename,def.defname as defname,tasks.playerid as playerid,tasks.result as result "
             "from tasks "
             "RIGHT JOIN def "
             "on tasks.defid=def.defid "
             "RIGHT JOIN cases "
             "on tasks.caseid=cases.caseid "
             "RIGHT JOIN productline "
             "on tasks.productid=productline.id "
             "where tasks.taskid is not null "
             "ORDER BY tasks.taskid DESC "
             "LIMIT 20"
            )
        finished=gl.GL_DB.query(sql)
        logging.info(finished)
        product_line=gl.GL_DB.select('productline')
        logging.info(product_line)
        print product_line
        caseinfo=gl.GL_DB.select('cases')
        definfo=gl.GL_DB.select('def')
        print caseinfo
        
        return render.slot(finished,product_line,caseinfo,definfo)

class execslot:

    #gl.GL_WEBINPUT=web.input()

    def get_productline(self,productid):
        productline_id = gl.GL_WEBINPUT.productline_id
        test_url = gl.GL_DB.query("select productline_url from productline where id = " + productline_id )
        url = []
        for item in test_url:
            item_dict1 = item.productline_url
            url.append(item_dict1)
        return url[0]

    def get_product_name(self,productid):
        productline_id = gl.GL_WEBINPUT.productline_id
        test_name = gl.GL_DB.query("select  productline_name from productline where id = " + productline_id )
        name = []
        for item in test_name:
            item_dict1 = item.productline_name
            name.append(item_dict1)
        #print "000000000000000"
       # print name[0]
        return name[0]

    def get_case_name(self,caseid):
        test_case = gl.GL_DB.query("select * from cases where caseid=" + gl.GL_WEBINPUT.case_id )
        result = []
        for item in test_case:
            item_dict = item.casename
            result.append(item_dict)
        return result[0] 

    def get_def_name(self,defid):

        if gl.GL_WEBINPUT.def_id =="1":     
             return "all"
        else:
            test_def = gl.GL_DB.query("select * from def where defid=" + gl.GL_WEBINPUT.def_id )
            result = []
            for item in test_def:
                item_dict = item.defname
                result.append(item_dict)
            return result[0]


    def get_playerid(self):
        gl.GL_WEBINPUT=web.input()
        player_id = gl.GL_WEBINPUT.playerid 
        return player_id 

    def do_case(self,project_name,case_name,def_name,player_id): #执行用例
        test_productline_url = gl.GL_DB.query("select productline_url from productline where productline_name='%s' "%project_name)
        url = []
        for item in test_productline_url:
            item_dict1 = item.productline_url
            url.append(item_dict1)
        test_url = url[0]

        if def_name == "all":           #如果选择all
            test_def = gl.GL_DB.query("select * from def where caseid=" + gl.GL_WEBINPUT.case_id )
            result = []
            print "what happend"
            for item in test_def:    #从查出的字典里循环每条结果
                def_name = item.defname
                def_id = item.defid
                print def_name
                try:
                    f = getattr(getattr(getattr(tests, project_name), case_name), def_name) 
                    result = f(player_id,test_url)
                    gl.GL_DB.insert('tasks',productid=gl.GL_WEBINPUT.productline_id,caseid=gl.GL_WEBINPUT.case_id,defid=def_id,playerid=gl.GL_WEBINPUT.playerid,result=result)
                    pass
                except Exception, e:
                    print e

        else:
            f = getattr(getattr(getattr(tests, project_name), case_name), def_name)      #从tests文件夹里选取项目，case以及def
            result = f(player_id,test_url)
            print "l o V e U~"
            productline_id=gl.GL_DB.query("select id from productline where productline_name='%s'" %project_name)

            for i in productline_id:
                productline_id=int(i.id)
            case_id=gl.GL_DB.query("select caseid from cases where casename='%s' and productid='%d'"  % (case_name,productline_id))

            for j in case_id:
                case_id=int(j.caseid)
            def_id=gl.GL_DB.query("select defid from def where defname='%s' and caseid='%d'" % (def_name,case_id) )

            for k in def_id:
                def_id=int(k.defid)
            playerid=player_id

            gl.GL_DB.insert('tasks',productid=productline_id,caseid=case_id,defid=def_id,playerid=playerid,result=result)


    def POST(self):  #获取从页面输入的值
        gl.GL_WEBINPUT=web.input()
        project_name=self.get_product_name(gl.GL_WEBINPUT.productline_id)    #项目名
        test_url=self.get_productline(gl.GL_WEBINPUT.productline_id)            #项目对应的测试地址
        case_name = self.get_case_name(gl.GL_WEBINPUT.case_id)       #case脚本名
        def_name = self.get_def_name(gl.GL_WEBINPUT.def_id)         #case中对应函数名
        player_id = self.get_playerid()               #玩家id

        self.do_case(project_name,case_name,def_name,player_id)
        #raise web.seeother('../slot') 
        sql=("select tasks.taskid as taskid,productline.productline_name as productline_name,"
             "cases.casename as casename,def.defname as defname,tasks.playerid as playerid,tasks.result as result "
             "from tasks "
             "RIGHT JOIN def "
             "on tasks.defid=def.defid "
             "RIGHT JOIN cases "
             "on tasks.caseid=cases.caseid "
             "RIGHT JOIN productline "
             "on tasks.productid=productline.id "
             "where tasks.taskid is not null "
             "ORDER BY tasks.taskid DESC "
             "LIMIT 20"
            )
        resultsql=gl.GL_DB.query(sql)
        result=[]
        for item in resultsql:
            item_dict={"taskid":item.taskid,"productline_name":item.productline_name,"casename":item.casename,"defname":item.defname,"playerid":item.playerid,"result":item.result}
            result.append(item_dict)
        encodedjson=json.dumps(result)
        print "JOANANANANANANANANANANA"
        print encodedjson
        logging.info(encodedjson)
        return  encodedjson


class ajaxgetprojects:   #页面根据项目联动case
    def GET(self):
        gl.GL_WEBINPUT=web.input()
        caseslist = gl.GL_DB.query("select * from cases where productid=" + gl.GL_WEBINPUT.productline_id)
        result = []
        for item in caseslist:
            item_dict = {"caseid":item.caseid,"casename":item.casename}
            result.append(item_dict)
        encodedjson = json.dumps(result)
        return encodedjson


class ajax_get_case:     #页面根据case联动def
    def GET(self):
        gl.GL_WEBINPUT=web.input()
        print "so cool ,i like this page~~~ wahahahah"
        caseslist = gl.GL_DB.query("select * from def where caseid=" + gl.GL_WEBINPUT.case_id)
        result = []
        for item in caseslist:
            item_dict = {"defid":item.defid,"defname":item.defname}
            result.append(item_dict)
        #print result
        print "why do u made it until 6/4 morning 5:51???????????"
        encodedjson = json.dumps(result)
        return encodedjson


class ajax_check_case:     #初始化case
    def GET(self):
        c2=tests.check_case.checkcase()
        c2.getfilename()



class ajax_ReSubmit:       #从结果中提交
    def POST(self):
        gl.GL_WEBINPUT=web.input()
        project_name=web.input().product_name
        case_name=web.input().case_name
        def_name=web.input().def_name
        player_id=web.input().playerid
        print case_name
        print project_name

        execslot().do_case(project_name,case_name,def_name,player_id)

    
#读web.conf文件
# def _init_config():
#     cf = ConfigParser.ConfigParser()
#     cf.read("web.conf")
#     m_config['db_ip'] = cf.get("db","ip")
#     m_config['db_user'] = cf.get("db","user")
#     m_config['db_pwd'] = cf.get("db","password")
#     m_config['db_name'] = cf.get("db","dbname")
#     m_config['db_port'] = cf.get("db","port")


# #定义全局变量DB及读取模板
# def _init_web_component():
#     gl.GL_DB = web.database(dbn='mysql',user=m_config['db_user'], pw=m_config['db_pwd'],db=m_config['db_name'])
#     gl.GL_RENDER = web.template.render('templates/')      


slotapi=web.application(urls,globals())