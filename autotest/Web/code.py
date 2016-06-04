#-*- encoding:utf-8 -*-
import tests
import tests.luckywin
import web
from Common import *
import Common.dbconn
import sys
import ConfigParser
import gl
import json
import MySQLdb
import json
reload(sys)
sys.setdefaultencoding("utf8")
#from Web import luckywin
urls=(
      '/','index',
      '/hello','hello',
      '/slot','slot',
      '/execslot','execslot',
      '/ajaxgetprojects','ajaxgetprojects',
      '/ajax_get_case','ajax_get_case')

m_config = gl.GL_CONFIG
render=web.template.render('templates/')


#class index:
  #  def GET(self):
    #    return render.hello("Hello World!")
    
#wy的slot项目

class slot:
    def GET(self):
        #conn=Common.dbconn.conndb("127.0.0.1","root","111111","slot",3306)
        #finished=gl.GL_DB.query('select * from tasks order by taskid desc;')
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
        product_line=gl.GL_DB.select('productline')
        print product_line
        caseinfo=gl.GL_DB.select('cases')
        definfo=gl.GL_DB.select('def')
        print caseinfo
        
        return render.slot(finished,product_line,caseinfo,definfo)

class execslot:

    #gl.GL_WEBINPUT=web.input()

    def get_productline(self):
        gl.GL_WEBINPUT=web.input()
        productline_id = gl.GL_WEBINPUT.productline_id
        test_url = gl.GL_DB.query("select productline_url from productline where id = " + productline_id )
        url = []
        for item in test_url:
            item_dict1 = item.productline_url
            url.append(item_dict1)
        return url[0]

    def get_product_name(self):
        gl.GL_WEBINPUT=web.input()
        productline_id = gl.GL_WEBINPUT.productline_id
        test_name = gl.GL_DB.query("select  productline_name from productline where id = " + productline_id )
        name = []
        for item in test_name:
            item_dict1 = item.productline_name
            name.append(item_dict1)
        #print "000000000000000"
       # print name[0]
        return name[0]

    def get_case_name(self):
        gl.GL_WEBINPUT=web.input()
        test_case = gl.GL_DB.query("select * from cases where caseid=" + gl.GL_WEBINPUT.case_id )
        result = []
        for item in test_case:
            item_dict = item.casename
            result.append(item_dict)
        return result[0] 

    def get_def_name(self):
        gl.GL_WEBINPUT=web.input()

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

    def do_case(self):
        gl.GL_WEBINPUT=web.input()
        project_name=self.get_product_name()    #项目名
        test_url=self.get_productline()            #项目对应的测试地址
        case_name = self.get_case_name()       #case脚本名
        def_name = self.get_def_name()         #case中对应函数名
        player_id = self.get_playerid()               #玩家id

        if def_name == "all":           #如果选择all
            test_def = gl.GL_DB.query("select * from def where caseid=" + gl.GL_WEBINPUT.case_id )
            result = []
            print "what happend"
            for item in test_def:    #从查出的字典里循环每条结果
                def_name = item.defname
                def_id = item.defid
                print def_name
                f = getattr(getattr(getattr(tests, project_name), case_name), def_name) 
                result = f(player_id,test_url)
                gl.GL_DB.insert('tasks',productid=gl.GL_WEBINPUT.productline_id,caseid=gl.GL_WEBINPUT.case_id,defid=def_id,playerid=gl.GL_WEBINPUT.playerid,result=result)
                print "11111111111111"
                print result


        else:
            f = getattr(getattr(getattr(tests, project_name), case_name), def_name) 
            result = f(player_id,test_url)
            print str(f)
            print type(result)
            print "wolegequwolegequ"
            print result
            gl.GL_DB.insert('tasks',productid=gl.GL_WEBINPUT.productline_id,caseid=gl.GL_WEBINPUT.case_id,defid=gl.GL_WEBINPUT.def_id,playerid=gl.GL_WEBINPUT.playerid,result=result)


    def POST(self):

        self.do_case()
        raise web.seeother('/slot') 

class ajaxgetprojects:   #页面根据项目联动case
    def GET(self):
        gl.GL_WEBINPUT=web.input()
        print "***********"
        caseslist = gl.GL_DB.query("select * from cases where productid=" + gl.GL_WEBINPUT.productline_id)
        result = []
        for item in caseslist:
            item_dict = {"caseid":item.caseid,"casename":item.casename}
            result.append(item_dict)
        #print result
        print "############"
        encodedjson = json.dumps(result)
        return encodedjson

class ajax_get_case:     #页面根据case联动def
    def GET(self):
        gl.GL_WEBINPUT=web.input()
        print "***********"
        caseslist = gl.GL_DB.query("select * from def where caseid=" + gl.GL_WEBINPUT.case_id)
        result = []
        for item in caseslist:
            item_dict = {"defid":item.defid,"defname":item.defname}
            result.append(item_dict)
        #print result
        print "############"
        encodedjson = json.dumps(result)
        return encodedjson
    
#读web.conf文件
def _init_config():
    cf = ConfigParser.ConfigParser()
    cf.read("web.conf")
    m_config['db_ip'] = cf.get("db","ip")
    m_config['db_user'] = cf.get("db","user")
    m_config['db_pwd'] = cf.get("db","password")
    m_config['db_name'] = cf.get("db","dbname")
    m_config['db_port'] = cf.get("db","port")

#初始化case文件
#def _init_case():
   # func_names = dir(luckywin.test_Forest_Mania)
  #  print func_names;

#定义全局变量DB及读取模板
def _init_web_component():
    gl.GL_DB = web.database(dbn='mysql',user=m_config['db_user'], pw=m_config['db_pwd'],db=m_config['db_name'])
    gl.GL_RENDER = web.template.render('templates/')      
       
if __name__=="__main__":
   # _init_case()
    _init_config()
    _init_web_component()
    app=web.application(urls,globals())
    app.run()
