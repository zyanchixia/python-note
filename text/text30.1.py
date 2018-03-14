# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:15:57 2018

"""
'''
题目：一个5位数，判断它是不是回文数
即12321是回文数，个位与万位相同，十位与千位相同
'''
def num():
    n = input('请输入一个数字:')
    x = list(n)
    l = len(x) #输入数字是几位数
    if l % 2 != 0:#判断输入的数字是偶数还是奇数
        med = int((l+1) /2) #定位该数字的中间位置
        i = x[:med-1] #12321
        x.reverse()
        j = x[:med-1]
        if i == j:
            print('{0}是回文数'.format(n))
        else:
            print('{0} 不是回文数'.format(n))
    else:
        med = int(l/2)
        i = x[:med]
        x.reverse()
        j = x[:med]
        if i == j:
            print('{0}是回文数'.format(n))
        else:
            print('{0} 不是回文数'.format(n))
num()
        