# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:37:14 2018

"""
'''
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数
'''
#解法0：
import time
myD={1:'a',2:'b'}
for key ,value in dict.items(myD):
    print(key,value)
time.sleep(1) #暂停1秒
#解法1：输出过程中会显示出来暂停，这种解法更正确
import time
l = [1,2,3,4]
for i in range(len(l)):
    print(l[i])
    time.sleep(2)