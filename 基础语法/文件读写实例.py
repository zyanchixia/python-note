# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:25:42 2018
向本地文件的字符串前加上序号1,2,3...后写到另一个文件中 
"""
with open('cs.txt') as f1:
    cNames = f1.readlines()
for i in range(0,len(cNames)):
    cNames[i] = str(i+1) + ':' + cNames[i]
with open('tt.txt','w') as f2:
    f2.writelines(cNames)
    