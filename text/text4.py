# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:32:41 2018

"""
'''
#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
#特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''  
#解法0       
year = int(input('年:\n'))
month = int(input('月:\n'))
day = int(input('日:\n'))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366]#闰年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365]#平年
#年份可被4整除，或年数是100的整数倍的话需要被400整除，否则是平年
if((year%4==0)and(year%100!=0) or (year%100==0)and(year%400==0)):
    Dth=months1[month-1]+day
else:
    Dth=months2[month-1]+day
print('是该年的第%d天'%Dth)

#解法1：
p = [31,28,31,30,31,30,31,31,30,31,30,31]#平年
r = [31,29,31,30,31,30,31,31,30,31,30,31]#闰年
year = int(input('年:\n'))
month = int(input('月:\n'))
day = int(input('天:\n'))
#判断平闰年
if year % 100==0:
    if year % 400==0:
        d = r
    else:
        d = p
else:
    if year % 4 ==0 :
        d = r
    else:
        d = p
#计算天数
days = sum(d[0:month-1])+day
print('%d.%d.%d是%d年的第%s天'%(year,month,day,year,days))