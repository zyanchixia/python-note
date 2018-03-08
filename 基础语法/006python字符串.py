# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:51:24 2018

"""
'''
字符串是 Python 中最常用的数据类型，我们可以使用引号('或")来创建字符串
'''
#ptyhon 访问字符串中的值：
#Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用;
#访问子字符串，可以使用方括号来截取字符串

var1 = 'Hello World!'
var2 = "Python Runoob"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#python字符串更新：可以对已存在的字符串进行修改，并赋值给另一个变量
var1 = 'Hello World!'

print ("更新字符串 :- ", var1[:6] + 'Runoob!') #更新字符串 :-  Hello Runoob!

#python转义字符:需要在字符中使用特殊字符时，python用反斜杠(\)转义字符
'''
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出
'''

