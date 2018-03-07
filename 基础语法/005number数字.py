# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:39:33 2018

"""
'''
python Number(数字)
Python Number 数据类型用于存储数值
数据类型是不允许改变的，这就意味着如果改变Number数据类型的值，
将重新分配内存空间
'''
#删除一些Number对象引用
del var1[,var2[var3[...]]]
#del单个或多个对象
del var
del var_a,var_b
'''
python支持4种不同的数值类型：
整数型 int
长整型 long integers:无限大小的整数，整数最后是一个大写或小写的L
浮点型 float point real values:由整数和小数部分组成
浮点型可使用科学计数法表示2.5e2=2.5*10**2=250
复数 complec numbers :由实数部分和虚数部分组成，可用a+bj或者comple(a,b)
来表示，其中a，b都是浮点型
'''
int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串