#-*- encoding:utf-8 -*-
import sys
import requests
import requests.cookies
reload(sys)
sys.setdefaultencoding("utf8")

class melogin:
    def melogin(self):
        username='qiuzhaokun'
        pwd='qiuzhaokun'

        data1={'username':username,'password':pwd}

        session=requests.session()

        loginurl="http://me.hxsd.mn/admin/user/check_login"
        data="username=qiuzhaokun&password=qiuzhaokun"

        result=session.post(loginurl,data=data1)

        #print result.headers
        print session.cookies
        #print requests.utils.dict_from_cookiejar(session.cookies)
        print result.cookies
        #result="hahahahahaha"
        print result

    def jobtable(self):
        url='http://job.hxsd.test/reportconsultantweek/getwork'
        data={"termid":"146","week":"1","campusid":"13","consultants":"2320"}

        session=requests.session()

        header={'Cookie':"w8h9xlastvisit=1462350710; w8h9xlastactivity=0; w8h9xuserid=2619; w8h9xpassword=d6d66ec823a0a0eefd770cecdee9f52b; f304flastvisit=1464589411; f304flastactivity=0; f304fuserid=2398; f304fpassword=ec8c16544f2924e7b9f94c2466ec1be8; ci_session=RLQfMSArxab%2B5bX49kvwA20mG0yefaswDd%2B5DfoMQhJ0xQ3EwKQIcppv%2FeAQDzqM5mODkeepyn1lzT4EotqOUxANvvnJdIY0JlvOUxaP07%2B3QjFxDsYXAm7IHDZ4yrokVMEjIzT8FrU8%2BgTLD%2BQSc3NJseZe7NmyNSLEcpJVJBIlu%2BYeApgsrMHdYaMr7nkgPxuqLQerxbzZ6gvEacExrSs1KGN%2FzsJUXZETiB3utk8Zzw3qU3iL8d9Dv4Iri7Z4U4qzbOJAY5PEoq1g49dCUZ1Dhw1H1DOAOpwamdbHC6ERRB0sblPwh771BTUQRrUOmDLBlUPQjkHN9%2BrSveATAX4rnGyXK1Ld0JqASkpfPjcVtq2Lkgi4eFRiqxNAivLwf92e29ce2e70961efb181fb7b01a494a05ca4180; user_info=53p%2Bg0G%2Bv3aGywdp6OuM3qC2mTLTEPT697zXPu8vB8VyTWCaQ3%2Fx6ifvcGfzNZO%2FEhUdRHZ17k3K9ZaLQ7Da1nisq51Q7x1yub0quMJk7%2Bf1qPlAWcRwWObkR9nkRTGQAYqQ9JrZXru47KhhYbefBwwlKVXZqbrtzGxve%2BdBZHlArFxnr%2F7hfvt207wU%2Bkf8mi0H18jmkydUXey%2F0o5XDw%3D%3D"}

        result=session.post(url,data=data,cookies=header)

        print result.text.decode('utf-8').encode('utf-8')
    def weibo(self):
        url='http://weibo.com/aj/mblog/add?ajwvr=6&__rnd='
        data={"location":"v6_content_home","appkey":"","style_type":"1","pic_id":"","text":"jiekoutesthahahaha","pdetail":"","rank":"0","rankid":"","module":"stissue","pub_source":"main_","pub_type":"dialog","_t":"0"}
        session=requests.session()
        headers={"Host": "weibo.com",
        "Connection": "keep-alive",
        "Content-Length": "141",
        "Origin": "http://weibo.com",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "SINAGLOBAL=4593802595045.418.1440588224013; wb_bub_hot_3514966693=1; YF-Page-G0=0acee381afd48776ab7a56bd67c2e7ac; _s_tentry=-; Apache=333693018183.1121.1467639333475; ULV=1467639333486:33:3:1:333693018183.1121.1467639333475:1467442937631; UOR=,,www.baidu.com; YF-V5-G0=02157a7d11e4c84ad719358d1520e5d4; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; WBStore=8ca40a3ef06ad7b2|undefined; SCF=Ano4uPHlkXmngvqFIpKJReDBprMv80UDvJVGPn7HfIUNQCXVqtym9vbEmBq5TO0NssnkJAcTASuiGpPinViUUng.; SUB=_2A256fhm4DeTxGeVL6lYY9ijKwj-IHXVZCgxwrDV8PUNbmtBeLXDikW-JQ6QSs4nCUympniIszXJuQR2CNA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWu9orNd93jfQBYjEMz5ObM5JpX5K2hUgL.FoefeKB4Soqc1Ke2dJLoI0qLxKMLB.2LBKzLxKML1-2L1hBLxK.LB.zL1hBLxKML1-2L1hBLxKMLB.zLB.qLxKML1-2L1hBt; SUHB=0N2l6NeCt-CszI; ALF=1499176296; SSOLoginState=1467640296; un=597073156@qq.com; wvr=6"

        }
        header={'Cookie':"SINAGLOBAL=4593802595045.418.1440588224013; wb_bub_hot_3514966693=1; YF-Page-G0=0acee381afd48776ab7a56bd67c2e7ac; _s_tentry=-; Apache=333693018183.1121.1467639333475; ULV=1467639333486:33:3:1:333693018183.1121.1467639333475:1467442937631; UOR=,,www.baidu.com; YF-V5-G0=02157a7d11e4c84ad719358d1520e5d4; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; WBStore=8ca40a3ef06ad7b2|undefined; SCF=Ano4uPHlkXmngvqFIpKJReDBprMv80UDvJVGPn7HfIUNQCXVqtym9vbEmBq5TO0NssnkJAcTASuiGpPinViUUng.; SUB=_2A256fhm4DeTxGeVL6lYY9ijKwj-IHXVZCgxwrDV8PUNbmtBeLXDikW-JQ6QSs4nCUympniIszXJuQR2CNA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWu9orNd93jfQBYjEMz5ObM5JpX5K2hUgL.FoefeKB4Soqc1Ke2dJLoI0qLxKMLB.2LBKzLxKML1-2L1hBLxK.LB.zL1hBLxKML1-2L1hBLxKMLB.zLB.qLxKML1-2L1hBt; SUHB=0N2l6NeCt-CszI; ALF=1499176296; SSOLoginState=1467640296; un=597073156@qq.com; wvr=6"}
        result=session.post(url,data=data,headers=headers)
        print result
        print result.text
        print result.content


if __name__=="__main__":
    req=melogin()
    #req.melogin()

    req.weibo()