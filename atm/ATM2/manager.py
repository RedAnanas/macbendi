#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 14:36
# software: PyCharm

import pymysql

def getConn(hostname='localhost',username='root',password='root',database='atm'):
    conn = pymysql.connect(hostname,username,password,database)
    return conn

#账号检查
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
    # for i in result:
    #     j = str(list(i))[2:-2]
    #     if j == acc_name:
    #         return True
    # else:
    #     return False

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

def update_acc(balance, acc_name):
    sql = 'update acc_info set balance=%d where acc_name="%s"' % (balance, acc_name)
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)

    conn.commit()
    conn.close()
    return True

def get_balan(acc_name):#传入用户名返回元组
    sql = 'select balance from acc_info where acc_name="%d"' % (acc_name)
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()

    return result

# def draw_mon():
