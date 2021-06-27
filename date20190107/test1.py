#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/1/7 17:09
# software: PyCharm
import jpype # 引入jpype模块
jvmPath = jpype.getDefaultJVMPath() # 指定jvm的默认路径
jpype.startJVM(jvmPath) # 通过jpype启动jvm
jpype.java.lang.System.out.println("hello world!") # 通过jpype执行Java代码
jpype.shutdownJVM() # 关闭jvm
