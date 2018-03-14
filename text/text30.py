# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:25:13 2018
"""
'''
题目：一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同
'''
#解法0：
a = input('请输入一个数字:\n')
b = a [::-1]  #反向全部切出
#c = a [:] 正向全部切出
if a == b:
    print('%s 是回文数'%a)
else:
    print('%s 不是回文数'%a)
    
#解法1：根据回文数的特点，但局限，不仅限于5位数
a = input('请输入一个5位数:')
if a[0] ==a[4] and a[1]==a[3]:
    print('%s是一个回文数'%a)
else:
    print('%s 不是一个回文数'%a)
    
    

#解法2：列表反转来判断
a = input('请输入一个数字:')
li1 = []
li2 = []
for i in a:
    li1.append(i)
    li2.append(i)
li2.reverse()#li2列表反转
print(li1,li2)
if li1 == li2:
    print('%s 是一个回文数'%a)
else:
    print('%s 不是一个回文数'%a)