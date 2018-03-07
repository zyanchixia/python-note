# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:03:21 2018

"""
#python变量类型，变量存储在内存中的值
#1：变量赋值，不需要类型声明，每个变量在使用前都必须赋值，变量赋值后该变量才会被创建
#等号 = 用来给变量赋值
counter = 100 #赋值整型变量
miles = 100.0 #浮点型
name = 'John' #字符串
print (counter)
print(miles)
print(name)

#2：多个变量赋值
a=b=c=1 #创建一个整型对象，值为1，3个变量被分配到相同的内存空间上
a,b,c = 1,2,'john' #一 一对应

#3：标准数据类型
Numbers#（数字）
String#（字符串）
List#（列表）
Tuple#（元组）
Dictionary#（字典）

#4：数字：数字数据类型用于存储数值，它们是不可改变的数据类型
#Python支持四种不同的数字类型：
int#（有符号整型）
long#（长整型[也可以代表八进制和十六进制]）
float#（浮点型）
complex#（复数）

#5：字符串：由数字，字母，下划线组成的一串字符
s='a1a2..an' (n>=0)
a = ilovepython
a[1:5] #输出结果 love,下标从0开始计算
str = 'hello world'
print(str + ' pa') # 输出连接的字符串 hello world pa
print(str[2:])# 输出从第三个字符开始的字符串 llo world
print(str *2)# 输出字符串两次 hello worldhello world



