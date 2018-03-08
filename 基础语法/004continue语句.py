# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:37:06 2018

"""
'''
 continue 语句跳出本次循环，然后继续进行下一轮循环,而break跳出整个循环
 '''
for letter in 'python':
    if letter =='h': #当等于h时，继续下一轮循环
        continue
    print('当前字母:',letter)
#输出结果当前字母: p 当前字母: y 当前字母: t 当前字母: o 当前字母: n

var = 10
while var >0:
    var = var-1
    if var ==5:
        continue
    print('当前变量值:',var)
print ('over')
#输出结果是除5之外的数字