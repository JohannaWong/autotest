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
        #print result.content
        #print result
        return mecookies


    def getstarwork(self,mecookies):
        url="http://me.hxsd.mn/admin/goodworks/lists"
        result=requests.get(url,cookies=mecookies)
        print result.content


    def jobtable(self):
        url='http://job.hxsd.test/reportconsultantweek/getwork'
        data={"termid":"146","week":"1","campusid":"13","consultants":"2320"}

        session=requests.session()

        header={'Cookie':"w8h9xlastvisit=1462350710; w8h9xlastactivity=0; w8h9xuserid=2619; w8h9xpassword=d6d66ec823a0a0eefd770cecdee9f52b; f304flastvisit=1464589411; f304flastactivity=0; f304fuserid=2398; f304fpassword=ec8c16544f2924e7b9f94c2466ec1be8; ci_session=RLQfMSArxab%2B5bX49kvwA20mG0yefaswDd%2B5DfoMQhJ0xQ3EwKQIcppv%2FeAQDzqM5mODkeepyn1lzT4EotqOUxANvvnJdIY0JlvOUxaP07%2B3QjFxDsYXAm7IHDZ4yrokVMEjIzT8FrU8%2BgTLD%2BQSc3NJseZe7NmyNSLEcpJVJBIlu%2BYeApgsrMHdYaMr7nkgPxuqLQerxbzZ6gvEacExrSs1KGN%2FzsJUXZETiB3utk8Zzw3qU3iL8d9Dv4Iri7Z4U4qzbOJAY5PEoq1g49dCUZ1Dhw1H1DOAOpwamdbHC6ERRB0sblPwh771BTUQRrUOmDLBlUPQjkHN9%2BrSveATAX4rnGyXK1Ld0JqASkpfPjcVtq2Lkgi4eFRiqxNAivLwf92e29ce2e70961efb181fb7b01a494a05ca4180; user_info=53p%2Bg0G%2Bv3aGywdp6OuM3qC2mTLTEPT697zXPu8vB8VyTWCaQ3%2Fx6ifvcGfzNZO%2FEhUdRHZ17k3K9ZaLQ7Da1nisq51Q7x1yub0quMJk7%2Bf1qPlAWcRwWObkR9nkRTGQAYqQ9JrZXru47KhhYbefBwwlKVXZqbrtzGxve%2BdBZHlArFxnr%2F7hfvt207wU%2Bkf8mi0H18jmkydUXey%2F0o5XDw%3D%3D"}

        result=session.post(url,data=data,cookies=header)

        print result.text.decode('utf-8').encode('utf-8')


if __name__=="__main__":
    req=getcookie()
    cookie=req.melogin()
    req.getstarwork(cookie)
