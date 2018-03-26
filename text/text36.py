# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:47:21 2018

"""
#题目：求100之内的素数
#解法0：
num1 = int(input('请输入区间最小值'))
num2 = int(input('请输入区间最大值'))
for num in range(num1,num2+1):
    if num >1: #素数大于1
        for i in range(2,num):
            if (num % i )==0:
                break
        else:
            print(num)
            
#解法1
for i in range(2,100):
    if 0 not in [i % n for n in range(2,i)]:
        print(i)
            
#解法2
import numpy as np
num = np.arange(101)
for i in num[2:101]:
    c = 0
    mod1 = []
    mod1.append(np.mod(i,num[1:101]))
    c = np.count_nonzero(mod1) #得到非0元素
    if (np.size(mod1)-c <=2):
        print (i)
#mod 元素级的求模计算，除法的余数