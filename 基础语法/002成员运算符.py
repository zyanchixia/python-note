# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:50:49 2018

"""
'''
#python 成员运算符：
in:如果在指定的序列中找到值返回 True，否则返回 False
   x 在 y 序列中 , 如果 x 在 y 序列中返回 True
not in :如果在指定的序列中没有找到值返回 True，否则返回 False
   x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")#
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")#
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")#
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")