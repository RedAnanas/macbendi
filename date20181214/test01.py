#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/14 11:28
# software: PyCharm
import socket

if __name__ == '__main__':
    #1.创建socket对象
    s=socket.socket()
    #2.通过socket对象绑定ip和port
    s.bind(("127.0.0.1", 8855))
    #3.开启监听，listen(len)len指队列长度
    s.listen(5)
    #4.准备接收数据
    print("监听开始，开始准备接收信息。。。。。")
    # address是元组，第一个是字符串形式的ip，第二个是数字形式的客户端的端口号
    c,address=s.accept()
    c.send("连接已建立！".encode("utf8"))
    while 1:
        #5.接到信息后给客户端反馈
        content=c.recv(1024).decode("utf8")
        c.send("信息已收到！".encode("utf8"))
        print('客户端的ip是' + address[0] + '端口号是' + str(address[1]) + '发送的消息是' + content)
        if content=="quit":
            c,address=s.accept()

    #6.关闭资源
    s.close()