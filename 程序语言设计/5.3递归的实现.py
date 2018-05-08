# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:27:16 2018
5.3 代码复用与函数递归
"""

#递归的实现
def fact(n):
    if n == 0 :
        return 1
    else:
        return n * fact(n-1)
    
#调用函数 进行计算  
fact(5)