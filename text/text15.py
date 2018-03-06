# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:27:56 2018

@author: zhangyanhong
"""
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子
'''
#解法0：
score = int(input('请输入分数:\n'))
if score >=90:
    grade = 'A'
elif score >=60:
    grade = 'B'
else:
    grade = 'C'
print('%d 属于 %s'%(score,grade))
#解法1：
score = int(input('请输入分数:\n'))
print('A' if score>=90 else ('B' if score >=60 else 'C'))
#解法2：
s = int(input('请输出分数:'))
ar = [90,60,0]
gra = ['A','B','C']
for idc in range(0,3):
    if s >= ar[idc]:
        print(gra[idc])
        break