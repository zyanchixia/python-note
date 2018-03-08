# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:44:43 2018

"""
'''
pass语句：pass 不做任何事情，一般用做占位语句
Python pass是空语句，是为了保持程序结构的完整性

'''
for letter in 'python':
    if letter == 'h':
        pass
        print('这是pass块')
    print('当前字母:',letter)
'''输出结果
当前字母: p
当前字母: y
当前字母: t
这是pass块
当前字母: h
当前字母: o
当前字母: n
'''