# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:34:23 2018
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁,
问第4个人岁数，他说比第3个人大2岁,问第三个人，又说比第2人大两岁,
问第2个人，说比第一个人大两岁,最后问第一个人，他说是10岁
请问第五个人多大？
"""
#解法0
def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n-1)+2 
    return c
print(age(5)) 

#解法1
def fun(rank):#rank递归第几个人
    if rank ==1:
        return 10
    else:
        return 2+fun(rank-1)
print(fun(5))

#解法2
def age(n):
    return 10 if not n-1 else age(n-1)+2
print(age(5))