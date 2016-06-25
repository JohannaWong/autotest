#-*- coding: UTF-8 -*-
import sys
import MySQLdb
from _sqlite3 import Row
#连接数据库
class conndb:
    def __init__(self,host,user,passwd,db,port):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        self.port=port
    
    def condb(self,tmp):
        Con=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=3306)
        cursor=Con.cursor()
        cursor.execute("SET NAMES 'gbk'")
        self.tmp=tmp
        sql=self.tmp.decode('utf8').encode('gbk')
        cursor.execute(sql)
        row=cursor.fetchall()
        print row
        return row
        cursor.close()
        Con.close()
        
# if "__main__"==__name__:
#     conn=conndb("127.0.0.1","root","111111","slot",3306)
#     sql="select * from cases"
#     conn.condb(sql)
    