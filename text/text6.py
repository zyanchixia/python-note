# -*- coding: utf-8 -*-
'''
Created on Mon Mar  5 14:46:42 2018

'''

'''题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
#解法0：
def fib(n):
    a,b= 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(10)) # 输出了第10个斐波那契数列

#解法1：使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))# 输出了第10个斐波那契数列
#解法2：
def fib(n):
    if n==1 or n==2:
        return 1
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib(10)) #输出前10个斐波那契数列
#解法3：
def fib(n):
    a,b = 0,1
    while n:
        a,b,n = b,a+b,n-1
        print(a)
fib(10)#输出前10个斐波那契数列
#解法4：使用生成器
def fib(max):
    n,a,b=0,0,1
    while n <max:
        yield b
        a,b = b,a+b
        n +=1
max = int(input('input max num:'))
for n in fib(max):
    print(n)#输出前10个斐波那契数列