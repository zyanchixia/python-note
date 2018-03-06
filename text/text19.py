# -*- coding: utf-8 -*-
'''
Created on Tue Mar  6 15:41:33 2018

'''
'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"
例如6=1＋2＋3.编程找出1000以内的所有完数
完数定义:某自然数除它本身以外的所有因子之和等于该数,则该数被称为完数
'''
#解法0:#结果为6,28,496
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)
#解法1:
 '''结果
 6 [1, 2, 3]
28 [1, 2, 4, 7, 14]
496 [1, 2, 4, 8, 16, 31, 62, 124, 248]
'''
import numpy as np
for m in range(1,1001):
    n = [1]
    for i in range(2,m):
        if m % i == 0:
            n.append(i)
    if m == np.sum(n):
        print(m,n)