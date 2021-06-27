#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/14 16:05
# software: PyCharm
import socket
if __name__ == '__main__':
    # 1.创建socket对象
    s=socket.socket()
    # 2.建立和服务器的连接
    s.connect(("127.0.0.1",8855))
    # 3.获取服务端发送的连接信息.使用recv(byteNum)接收的字节数
    content=s.recv(1024).decode("utf8")
    print(content)
    while 1:
        ms=input("请输入你想说的话：")
        s.send(ms.encode("utf8"))
        if ms=="quit":
            break
        content=s.recv(1024).decode("utf8")
        print(content)
    s.close()