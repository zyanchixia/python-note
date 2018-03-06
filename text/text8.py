# -*- coding: utf-8 -*-
'''
Created on Mon Mar  5 16:04:56 2018
'''
'''
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列
'''
#解法0：
for i in range(1,10):
    for j in range(1,i+1):
        k = i*j
        print('{}*{}={}'.format(j,i,k),end = ' ')
print('')
#解法1：for循环
for i in range (1,10):
    for j in range(1,10):
        print(j,'*',i,'=',i*j,'\t',end='')
        if i ==j:
            print('')
            break
#解法2：
for j in range(9):
    i = 1
    j = j+1
    while (i<=j):
        k = j*i
        print('%d*%d=%d'%(i,j,k),end = ' ')
        i+=1
    print('')
