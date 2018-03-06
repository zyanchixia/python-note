# -*- coding: utf-8 -*-
'''
Created on Mon Mar  5 16:47:20 2018

'''
'''
题目：暂停一秒输出，并格式化当前时间。
'''
#解法0：
import time,datetime
time.sleep(1)
TIME=datetime.datetime.now()
print(TIME.strftime('%Y-%m-%d %H:%M:%S'))
#解法1：
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)#暂停1秒
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#解法2：
import time
time1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)#暂停1秒
time2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time1,time2)