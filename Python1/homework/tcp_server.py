#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket


# 构建一个tcp连接对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 555))
# 这个是服务器端连接队列的长度
server.listen(5)
while True:
    # 服务器端构造一个阻塞，等待接收客户端的消息
    con = server.accept()
    print(con[0].recv(1024).decode())
