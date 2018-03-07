# -*- coding: utf-8 -*-
'''
Created on Wed Mar  7 11:32:14 2018

'''
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
求出这个数列的前20项之和
程序分析：请抓住分子与分母的变化规律
'''
#解法0：
sum = 0 #前20项的和
a,b = 2,1#第一个分母，分子
for i in range(1,21):
    sum += a/b
    b,a = a,a+b #分子是前一个分数的分子分母之和，将分子分母交换
print(sum)

#解法1：#reduce() 函数会对参数序列中元素进行累积
from functools import reduce
a ,b =2,1
l = []
l.append(a/b)
for i in range(1,20):
    b,a = a,a+b
    l.append(a/b)
print(reduce(lambda x,y:x+y,l)) #匿名函数