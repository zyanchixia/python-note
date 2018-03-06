# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:56:39 2018

"""
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''
#解法0：递归
def fib(n):
    if n ==1 or n ==2:#第一个月和第二个月都是1
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(7))
#解法1：
def r(num):
    f1=1
    f2=1
    if num ==1 or num ==2:
        return 1
    else:
        for i in range(num-1):
            f1,f2 = f2,f1+f2
    return f1
print(r(6))