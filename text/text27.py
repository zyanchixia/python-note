# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:07:46 2018
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
题解：Python List reverse()方法:用于反向列表中元素
"""
#解法0
S = input('请输入一个字符串:')
L=list(S)
L.reverse() #反向列表中元素
for i in range(len(L)):
    print(L[i])
    
#解法1   
def output(s):
    s = list(s)
    if len(s) == 0:
        return
    print(s[len(s)-1])
    s.pop() #默认移除列表中的最后一个元素，并且返回该元素的值
    output(s)
output('abcde')