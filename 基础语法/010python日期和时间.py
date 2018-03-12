# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:37:37 2018

"""
'''
python提供了一个 time 和 calendar 模块可以用于格式化日期和时间
时间间隔是以秒为单位的浮点小数
'''
import time
ticks = time.time()
print('当前时间戳为：',ticks) #当前时间戳为： 1520840367.7318447
#时间元组：很多Python函数用一个元组装起来的9组数字处理时间
'''
属性	   字段	      值
tm_year	4位数年  	2008
tm_mon 	  月	    1 到 12
tm_mday	  日	    1到31
tm_hour	小时	    0到23
tm_min  	分钟	    0到59
tm_sec  	秒	    0到61 (60或61 是闰秒)
tm_wday	一周的第几日	0到6 (0是周一)
tm_yday	一年的第几日	1到366 (儒略历)
tm_isdst	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''
localtime = time.localtime(time.time())
print('本地时间为:',localtime)

#获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print('本地时间为:',localtime) # Mon Mar 12 16:16:54 2018

#格式化日期：使用 time 模块的 strftime 方法来格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtiem()))
## 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))
## 将格式字符串转换为时间戳
a = 'Sat Mar 28 22:24:24 2016'
print(time.mktime(time.strftime(a,'%a %b %d %H:%M:%S %Y')))

#获取某月日历
import calendar
cal = calendar.month(2018,1)
print('以下输出2018年1月份的日历:',cal)
'''以下输出2018年1月份的日历:  
January 2018
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31'''
