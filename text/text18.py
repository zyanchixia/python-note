# -*- coding: utf-8 -*-
'''
Created on Tue Mar  6 15:14:44 2018
'''
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值
'''
#解法0：
n = int(input('n='))
a = int(input('a='))
sum = 0
total = 0
for i in range(n):
    sum += (10**i)
    total += sum * a
print(total)

#解法1：
from functools import reduce
total=0
sum=[]
n = int(input('n='))
a = int(input('a='))
for count in range(n):
    total =total + a
    a = a*10
    sum.append(total)
    print(total)
sum = reduce(lambda x,y : x+y,sum)#reduce() 函数会对参数序列中元素进行累积
print('计算结果为:',sum)