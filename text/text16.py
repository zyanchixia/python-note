# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:41:21 2018

"""
'''
题目：输出指定格式的日期
程序分析：使用 datetime 模块
'''
import datetime
print(datetime.date.today())#返回2018-03-06
print(datetime.date.today().strftime('%d/%m/%Y'))#06/03/2018
print(datetime.date(1941,1,5))#创建日期对象1941-01-05

import time
print(time.time()) #1520315335.6204917
print(time.localtime())
#time.struct_time(tm_year=2018, tm_mon=3, tm_mday=6, tm_hour=13, tm_min=48, 
#tm_sec=55, tm_wday=1, tm_yday=65, tm_isdst=0)
print(time.asctime())#Tue Mar  6 13:48:55 2018
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#2018-03-06 13:48:55