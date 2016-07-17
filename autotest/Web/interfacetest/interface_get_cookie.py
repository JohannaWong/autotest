#-*- encoding:utf-8 -*-
import sys
import requests
import requests.cookies
reload(sys)
sys.setdefaultencoding("utf8")

class getcookie:
    def __init__(self,url,username,pwd):
        self.username=username
        self.pwd=pwd
        self.url=url

    def login(self):
        data1={'username':self.username,'password':self.pwd}
        session=requests.session()
        #loginurl="http://me.hxsd.mn/admin/user/check_login"
        result=session.post(self.url,data=data1)
        cookies=requests.utils.dict_from_cookiejar(session.cookies)
        print cookies['user_info']
        return cookies

