# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:09:24 2018

"""
#题目：按相反的顺序输出列表的值。
#解法0
a = ['one','two','three']
for i in a [::-1]:
    print(i)

#解法1：
list = ['a','b','c','d']
list.reverse()
print(list)


#解法2
a = ['one','two','three','four','five']
def reverse(a):
    if len(a) <=1:
        print(a[0],end =' ')
    else:
        print(a[-1],end=' ')
        reverse(a[0:-1])
reverse(a)