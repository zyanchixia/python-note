# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:48:40 2018

"""
'''
Time 模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的

序号	函数及描述
1	time.altzone
返回格林威治西部的夏令时地区的偏移秒数
如果该地区在格林威治东部会返回负值（如西欧，包括英国）
对夏令时启用地区才能使用
2	time.asctime([tupletime])
接受时间元组并返回一个可读的形式为
"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串
3	time.clock( )
用以浮点数计算的秒数返回当前的CPU时间
用来衡量不同程序的耗时，比time.time()更有用
在第一次调用的时候，返回的是程序运行的实际时间
以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
4	time.ctime([secs])
作用相当于asctime(localtime(secs))，未给参数相当于asctime()
5	time.gmtime([secs])
接收时间戳（1970纪元后经过的浮点秒数）
   并返回格林威治天文时间下的时间元组t,注：t.tm_isdst始终为0
6	time.localtime([secs])
接收时间戳（1970纪元后经过的浮点秒数）,
并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
7	time.mktime(tupletime)
接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）
8	time.sleep(secs)--推迟执行的秒数
推迟调用线程的运行，secs指秒数
9	time.strftime(fmt[,tupletime])
语法:time.strftime(format[, t])
接收以时间元组，并返回以可读字符串表示的当地时间，格式由format决定
10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
根据fmt的格式把一个时间字符串解析为时间元组
11	time.time( )
返回当前时间的时间戳（1970纪元后经过的浮点秒数）
12	time.tzset()
根据环境变量TZ重新初始化时间相关设置 
'''
2	time.asctime([tupletime])
import time 
t = time.localtime()
print('time.asctime(t): %s',%time.asctime(t))
#输出结果 time.asctime(t):Mon Mar 12 17:08:59 2018
8	time.sleep(secs)--推迟执行的秒数
print('start:%s'%time.ctime())
time.sleep(5)
print('end:%s'%time.ctime())

9	time.strftime(fmt[,tupletime])
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))