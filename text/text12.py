# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:20:18 2018

"""
'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数'''
#解法0：集合解法
l = []
for i in range(101,200):
    for j in range(2,i-1):
        if i % j ==0:
            break
    else:
        l.append(i)#append() 方法用于在列表末尾添加新的对象
print(l)
print('总数为:%d'%len(l))

#解法1：
from math import sqrt
count=0
pn=1
for i in range(101,200):
    k = int(sqrt(i))
    for j in range(2,k+1):
        if i%j ==0:
            pn=0
            break
    if pn ==1:
        count +=1
        print(i)
    pn=1
print('total number is %d'%count)