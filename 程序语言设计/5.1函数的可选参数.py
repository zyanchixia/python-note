# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:47:40 2018
1:
函数可以有参数也可以没有，但必须要保留括号
def <函数名>():
    <函数体>
    return <返回值>

2:函数定义时可以为某些参数指定默认值，构成可选参数
def <函数名>(<非可选参数>,<可选参数>):
    <函数体>
    return <返回值>

3:可变参数传递
函数定义时可以设计可变数量参数，即不确定参数总数量
def <函数名>(<参数>,*b):
    <函数体>
    return <返回值>
"""

#计算n!//m
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m
a = fact(10,5)
print(a)

#计算n!乘数
def fact1(n,*b): #*b可变参数
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s *= item
    return s

b = fact1(10,3,5,8)
print(b)