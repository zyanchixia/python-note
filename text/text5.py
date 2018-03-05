# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:29:56 2018

@author: zhangyanhong
"""
'''题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换
，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小
'''
#解法0：
x= int(input('请输入一个整数:\n'))
y= int(input('请输入一个整数:\n'))
z= int(input('请输入一个整数:\n'))
if x>y:
    x,y = y,x
if y>z:
    y,z = z,y
print('3个整数从小到大排列顺序为:',(x,y,z))

#解法1：
x= int(input('请输入一个整数:\n'))
y= int(input('请输入一个整数:\n'))
z= int(input('请输入一个整数:\n'))
num = [x,y,z]
num.sort() #对列表进行升序排列
print('3个整数从小到大排列顺序为:',num)
rnum = [x,y,z]
rnum.sort(reverse = True) #降序排列
print('3个整数从大到小排列顺序为',rnum)