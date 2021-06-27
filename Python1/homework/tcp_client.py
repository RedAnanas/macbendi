#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time


for i in range(5):
    # 构造一个tcp连接对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    client.connect(('localhost', 555))
    msg = '第%d次，消息内容。' % (i + 1)
    # 发送消息。注意这里有二种方法可以用
    client.send(msg.encode())
    # client.send(str.encode(msg))
    client.close()
    time.sleep(2)
