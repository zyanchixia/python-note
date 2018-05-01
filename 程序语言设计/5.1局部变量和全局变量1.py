# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:09:07 2018
#局部变量和全局变量 规则1
局部变量和全局变量是不同的变量
--局部变量是函数内部的占位符，与全局变量可能重名但不同
--函数运算结束后，局部变量被释放
--可以使用global保留字在函数内部使用全局变量
"""
n,s = 10,100 # 全局变量s
def fact(n):
    s = 1 #此处的s是局部变量与全局变量s不同
    for i in range(1,n+1):
        s *= i #此处s是fact()函数的运行结果
    return s
print(fact(n),s) #此处s = 100
#运行结果  3628800 100


n,s = 10,100
def fact(n):
    global s 
    #fact()函数中使用global保留字声明，此处s是全局变量s
    for i in range(1,n+1):
        s *= i #全局变量
    return s
print(fact(n),s)#全局变量s被函数修改
#运行结果 362880000 362880000