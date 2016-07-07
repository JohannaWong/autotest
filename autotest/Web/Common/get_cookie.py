#-*- encoding:utf-8 -*-
import sys
import requests
import requests.cookies
reload(sys)
sys.setdefaultencoding("utf8")

class getcookie:
    def melogin(self):
        username='qiuzhaokun'
        pwd='qiuzhaokun'

        data1={'username':username,'password':pwd}

        session=requests.session()

        loginurl="http://me.hxsd.mn/admin/user/check_login"
        data="username=qiuzhaokun&password=qiuzhaokun"

        result=session.post(loginurl,data=data1)

        #print session.cookies
        #print requests.utils.dict_from_cookiejar(session.cookies)
        mecookies=requests.utils.dict_from_cookiejar(session.cookies)
        #print result.headers
        #print result.content
        return mecookies

    def getstarwork(self,mecookies):
        url="http://me.hxsd.mn/admin/goodworks/lists"
        result=requests.get(url,cookies=mecookies)
        #print result.content
    def getcampus(self,mecookies):
        url="http://me.hxsd.mn/admin/ajax/getCampus"
        result=requests.get(url,cookies=mecookies)
        print "get Campus"
        print result
        print result.content

    def getterms(self,mecookies):
        print mecookies
        url="http://me.hxsd.mn/admin/ajax/getTerms"
        result=requests.get(url,cookies=mecookies)
        print "Get Terms"
        print result
        print result.content

    def getFaculty(self,mecookies):
        url="http://me.hxsd.mn/admin/ajax/getFaculty"
        result=requests.get(url,cookies=mecookies)
        print "get getFaculty"
        print result
        print result.content

    def getallspecialities(self,mecookies):
        url="http://me.hxsd.mn/admin/ajax/get_all_specialties"
        data={'userid':"2440",'faculty_id':"6"}
        result=requests.post(url,data=data,cookies=mecookies)
        print "get specialities"
        print result
        print result.content

    def getcampusclass(self,mecookies):
        url='http://me.hxsd.mn/admin/ajax/get_campus_clazz'
        data={'campusid':"1",'userid':"2440"}
        result=requests.post(url,data=data,cookies=mecookies)
        print 'getcampusclass'
        print result
        print result.content


    def mepost(self,url,data,mecookies):
        result=requests.post(url,data=data,cookies=mecookies)
        print result
        print result.content
        return result

    def meget(self,url,mecookies):
        result=requests.get(url,cookies=mecookies)
        print result
        print result.content
        return result




if __name__=="__main__":
    req=getcookie()
    cookie=req.melogin()
    print cookie
    # req.getstarwork(cookie)
    # req.getcampus(cookie)
    # req.getterms(cookie)
    # req.getFaculty(cookie)
    # req.getallspecialities(cookie)
    # req.getcampusclass(cookie)
    url='http://me.hxsd.mn/admin/ajax/get_campus_clazz'
    data={"campusid":"1","userid":"2440"}
    req.mepost(url,data,cookie)
