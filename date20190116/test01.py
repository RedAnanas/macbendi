#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/16 11:22
# software: PyCharm

import socket
import time

for i in range(5):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect('192.168.2.161',554)
    msg="第%d次" %(i+1)
    client.send(str.encode(msg))
    client.close()
    time.sleep(2)


