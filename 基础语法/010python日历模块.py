# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:34:47 2018

"""
'''
python 日历（Calendar）模块
此模块的函数都是日历相关的，例如打印某月的字符月历
星期一是默认的每周第一天，星期天是默认的最后一天
更改设置需调用calendar.setfirstweekday()函数
'''
序号	函数及描述
1	calendar.calendar(year,w=2,l=1,c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c
每日宽度间隔为w字符,每行长度为21* W+18+2* C,l是每星期行数
print(calendar.calendar(2018,w=2,l=1,c=6))
2	calendar.firstweekday( )
返回当前每周起始日期的设置,默认情况下，首次载入caendar模块时返回0，即星期一
print(calendar.firstweekday()) #0
3	calendar.isleap(year)
是闰年返回True，否则为false;
print(calendar.isleap(2018)) #False
4	calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数;
print('88年至18年期间总共%s个闰年'%calendar.leapdays(1988,2018))#8个
5	calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行
print(calendar.month(2018,3,w=2,l=1))
'''输出
     March 2018
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
'''
每日宽度间隔为w字符,每行的长度为7* w+6,l是每星期的行数
6	calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表,每个子列表装载代表一个星期的整数,
Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始
print(calendar.monthcalendar(2018,3))
'''
[[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18],
 [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 0]]
'''
7	calendar.monthrange(year,month)
返回两个整数,第一个是该月的第一天是星期几，第二个是该月的天数,
日从0（星期一）到6（星期日）;月从1到12
print(calendar.monthrange(2018,3)) #输出 (3, 31)3月份第一天是周四，共31天

8	calendar.prcal(year,w=2,l=1,c=6)
相当于 print calendar.calendar(year,w,l,c).

9	calendar.prmonth(year,month,w=2,l=1)
相当于 print calendar.calendar（year，w，l，c）

10	calendar.setfirstweekday(weekday)
设置每周的起始日期码,0（星期一）到6（星期日）

11	calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，
返回该时刻的时间戳（1970纪元后经过的浮点秒数）
12	calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）,月份为 1（一月） 到 12（12月）
print(calendar.weekday(2018,3,10)) #输出5，即3月10号是周六
