# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:51:34 2018

@author: zhangyanhong
"""
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'
'''
#解法0：for循环
import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():#isalpha() 方法检测字符串是否只由字母组成
        letters +=1
    elif c.isspace():#isspace() 方法检测字符串是否只由空格组成
        space +=1
    elif c.isdigit():#isdigit() 方法检测字符串是否只由数字组成
        digit +=1
    else:
        others +=1
print('char = %d,space= %d,digit= %d,others= %d'%(letters,space,digit,others))

#解法1：lambda函数也叫匿名函数，即，函数没有具体的名称
s = input('请输入一个字符串:\n')
list = [0,0,0,0]
temp = [lambda i: 1 if (i.isalpha()) else 0,
        lambda i:1 if (i.isspace()) else 0,
        lambda i:1 if (i.isdigit()) else 0]
for i in s:
    list[0] += temp[0](i)#字母
    list[1] += temp[1](i)#空格
    list[2] += temp[2](i)#数字
    list[3] =len(s)-list[0]-list[1]-list[2]#其他字符
print('该字符串包含:字母%d个,空格%d个,数字%d个,其他字符%d个'
      %(list[0],list[1],list[2],list[3]))




