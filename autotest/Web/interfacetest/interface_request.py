#-*- encoding:utf-8 -*-
import sys
import requests
import requests.cookies
reload(sys)
sys.setdefaultencoding("utf8")

class interface_request:
    def __init__(self,url,data,cookies):
        self.url=url
        self.data=data
        self.cookies=cookies

    def post(self):
        result=requests.post(self.url,data=self.data,cookies=self.cookies)
        print result
        print result.content
        return result

    def get(self):
        result=requests.get(self.url,cookies=self.cookies)
        print result
        print result.content
        return result

    def post_withoutcookie(self):
        result=requests.post(self.url,self.data)
        print result
        print result.content
        return result

    def get_withoutcookie(self):
        result=requests.get(self.url)
        print result
        print result.content
        return result