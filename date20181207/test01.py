#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 9:42
# software: PyCharm

#对atm数据库的acc_info表进行增删改查操作
import pymysql
import pymysql.connections

#创建数据库连接，生成数据库连接对象
def getConn(hostname='localhost',username='root',password='root',database='atm'):
        conn = pymysql.connect(hostname, username, password, database)
        return conn

conn=getConn()
#创建游标对象准备用于执行sql
cur=conn.cursor()
#将sql语句写成字符串
sql="insert into acc_info values ('admin','123','1000')"#增
#sql = "update acc_info set balance=2000 where acc_name='admin'" #删
#sql = "delete from acc_info where acc_name='admin'" #改
#sql = "select * from acc_info " #查

#执行sql语句
cur.execute(sql)

#使用数据库连接对象提交数据
result = cur.fetchall()  #查询返回的结果是元组
print(result)

#提交（查询时不用提交）
conn.commit()

#关闭连接
conn.close()














