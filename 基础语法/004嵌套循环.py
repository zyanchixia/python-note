# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:39:32 2018

"""
'''
嵌套循环：在一个循环体里面嵌入另一个循环，可以在while循环体中嵌套for循环
循环控制语句：
break 语句：在语句块执行过程中终止循环，并且跳出整个循环
continue 语句：在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
pass 语句：pass是空语句，是为了保持程序结构的完整性
Python for 循环嵌套语法：
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
   
Python while 循环嵌套语法：
while expression:
   while expression:
      statement(s)
   statement(s)
'''
#使用嵌套循环输出2~100之间的素数：除了1和它本身以外不再有其他因数
l = []
i = 2
for i in range(2,100):#迭代2~100之间的数字
    j = 2
    for j in range(2,i):   #根据因子迭代
        if (i%j==0):   #确定第一个因子
            break     #跳出循环
    else:
        l.append(i)
print(l)

#求[a,b]之间的质数(即素数),除了1和它本身以外不再有其他因数
a = 1000
b = 10000
s = []
for num in range(a,b+1):
    snum = int(num*0.5+1)
    for i in range (2,snum):
        if num%i ==0:
            break
    else:
        s.append(num)
print(a,'到',b,'的质数有',s)
print(a,'到',b,'有',len(s),'个质数')