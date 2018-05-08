# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:43:59 2018
5.3 斐波那契数列
"""
def f(n):
    if n ==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
    
f(5)