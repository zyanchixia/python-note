# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:43:37 2018

题目：利用递归方法求5!。

程序分析：递归公式：fn=n * fact(n-1)
5！=4！×5=3！*4*5=2！*3*4*5=1！*2*3*4*5

n！=1（n=0，1）
n！=n*（n-1）！（n>1）
"""
#解法0
def fact(j):
    sum = 0
    if j == 0 :
        sum = 1
    else:
        sum = j *fact(j-1)
    return sum
print(fact(5))

#解法1
def fact(n):
    if n ==1:
        fn = 1
    else:
        fn = n *fact(n-1)
    return fn
print(fact(5))

#解法2
def fact(n):
    if n ==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

