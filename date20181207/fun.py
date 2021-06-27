#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 13:21
# software: PyCharm
import pymysql
import pymysql.connections
def getConn(hostname='localhost',username='root',password='root',database='atm'):
        conn = pymysql.connect(hostname, username, password, database)
        return conn

def update(sql):#更新函数
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def inquire(acc_name):#查询函数
    sql = "select * from acc_info " #查
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    # 使用数据库连接对象提交数据
    result = cur.fetchall()  # 查询返回的结果是元组
    conn.close()

def add_user(acc_name, acc_pass, balance):#增加函数
    sql = 'insert into acc_info values("%s","%s",%d)' % (acc_name, acc_pass, balance)  # 增
    update(sql)

def amend_balance(acc_name,balance):#修改函数

    sql =  'update acc_info set balance=%d where acc_name="%s"'%(balance,acc_name) #改
    update(sql)

def amend_balance(acc_name):#删除函数

    sql = 'delete from acc_info where acc_name="%s"' % acc_name #删
    update(sql)
