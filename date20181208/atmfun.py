#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/8 13:24
# software: PyCharm

import pymysql
import pymysql.connections
def getConn(hostname='localhost',username='root',password='root',database='atm'):
        conn = pymysql.connect(hostname, username, password, database)
        return conn

#账号检查是否存在，存在返回True
def check_acc(acc_name):
    sql = 'select acc_name from acc_info'
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()

    for i in result:
        for j in i:
            if j == acc_name:
                return True
    else:
        return False

def check_pass(acc_name,acc_pass):#传入用户名密码判断密码是否正确，如正确返回True
    sql = 'select acc_pass from acc_info where acc_name="%s"'%(acc_name)
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    for i in result:
        if i == acc_pass:
            return True
        else:
            return False

def inquire(acc_name):#传入用户名返回元祖
    sql = 'select balance from acc_info where acc_name="%s"' % (acc_name) #查
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result

def add_user(acc_name, acc_pass, balance):#增加账户密码金额
    sql = 'insert into acc_info values("%s","%s",%d)' % (acc_name, acc_pass, balance)  # 增
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def amend_balance(blances,acc_name):#根据账户名修改金额返回Ture

    sql = 'update acc_info set balance=%d where acc_name="%s"' % (blances, acc_name)
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return True