# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:20:27 2018
题目：对10个数进行排序
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，
下次类推，即用第二个元素与后8个进行比较，并进行交换
"""
a = []
for n in range(10):
    a.append(int(input('请输入一个数字:\n')))
a.sort()
print(a)
