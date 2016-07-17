# autotest
something about test

本程序工作环境：py27
需要安装的py模块: nosetest,selenium,webpy,mysql（注意版本）,requests,xlsxwriter

1.构建mysql
  运行DBDECLARE文件夹下的sql文件，来构建DB

2.ui自动化测试
  a.当firefox版本过高或过低时，无法使用
  b.使用chrome浏览器时，将tools文件夹下的对应版本的driver放到对应的路径下，并修改..\Web\UI_test\webconn.py下路径
    chromedriver="C:\Users\wangjichong\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
  c.支持excel上传和下载，UI自动化测试用例只需要写在excel中就可以，上传后，会自动刷新出上传的文件，可以选择进行运行

3.接口测试
  使用requests库，对于一些简单的只通过cookies验证的小网站，可以获取cookies进行某些接口测试
  某些需要动态口令的接口，有没有什么好的方法。
  某些固定的可以写在excel中，读写进行。支持手动写入cookie、输入用户名密码获得cookie，或者通过接口读取到cookie
  
4.xlsxwriter,xlrd
  操作excel
  eval，将字符串转化为字典
