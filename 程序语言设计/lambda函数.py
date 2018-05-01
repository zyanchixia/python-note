# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:22:16 2018
lambda 函数返回函数名作为结果
--lambda 函数是一种匿名函数，即没有名字的函数
--使用lambda保留字定义，函数名是返回结果
--lambda函数用于定义简单的，能够在一行内表示的函数
<函数名> = lambda<参数>:<表达式>
"""

f = lambda x,y:x+y
f(10,15)
#返回结果25
f1 = lambda : 'lambda函数'
print(f1())
#返回结果 lambda函数