# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:58:08 2018

"""
'''
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]
'''
#解法0：
a = [1,2,3]
b = a[:]
print(b)
#解法1：
import copy
a = [1,2,3]
b = a.copy()
print(b)
#解法2：
l = [1,2,3,4]
p = []
for i in range (len(l)):
    p.append(l[i])
print(p) #使用for循环出列表元素
#解法3：简单暴力直接
a = [1,2,3,4]
b = a*1
print(b)
#解法4：表1拓展到表2中
l1 = [1,2,3,4]
l2 = []
l2.extend(l1)
print(l2)