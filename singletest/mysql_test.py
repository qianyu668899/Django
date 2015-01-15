# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb    
   
#连接    
conn=MySQLdb.connect(host="localhost",user="root",passwd="qianyu",db="test",charset="utf8")  
conn.autocommit(1)
cursor = conn.cursor()    
'''   
#写入    
sql = "insert into user(id, name,created) values(%s, %s,%s)"   
param = (1,"qianyu",int(time.time()))    
n = cursor.execute(sql,param)    
print "executed statement: ",n  
#conn.commit() #this is very important
#query
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    for r in row:    
        print "r:", r 
''' 
#更新 
sql = "update user set name=%s where id=1"   
param = ("qianyu")    
n = cursor.execute(sql,param)    
print n    

'''   
#查询    
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    for r in row:    
        print r    
   
#删除    
sql = "delete from user where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
   
'''
#关闭
cursor.close() 
conn.close()  