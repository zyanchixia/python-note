# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:09:32 2018

"""
'''break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，
也会停止执行循环语句
break语句用在while和for循环中
'''
#实例1
for letter in 'python':
    if letter == 'h':
        break
    print('当前字母:',letter)  #当前字母: p 当前字母: y 当前字母: t

#实例2
var = 10
while var >0:
    print('当前变量值:',var)
    var = var -1
    if var ==5: #当变量var等于5时，退出循环
        break
print ('over')