# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:24:33 2018

"""
#按逗号分隔列表
#解法0
L = [1,2,3,4,5]
s = ','.join(str(n) for n in L)
print(s)
#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#解法1：
L = [1,2,3,4,5]
L1 = repr(L)[1:-1]
print(L1)
#repr() 函数将对象转化为供解释器读取的形式

#解法2：
numbers = list(range(1,9))
for i in numbers:
    if(i == numbers[-1]):
        print(i) #打印最后一位数，不需要加逗号
    else:
        print(i,end=',')