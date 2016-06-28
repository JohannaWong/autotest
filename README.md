# autotest
something about test

本程序工作环境：py27
需要安装的py插件: nosetest,selenium,webpy,mysql（注意版本）

1.构建mysql
  运行DBDECLARE文件夹下的sql文件，来构建DB

2.ui自动化测试
  a.当firefox版本过高或过低时，无法使用
  b.使用chrome浏览器时，将tools文件夹下的对应版本的driver放到对应的路径下，并修改..\Web\UI_test\webconn.py下路径
    chromedriver="C:\Users\wangjichong\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
  c.
