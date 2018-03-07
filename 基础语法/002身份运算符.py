# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:54:06 2018

"""
'''
python身份运算符:用于比较两个对象的存储单元
is:判断两个标识符是不是引用自一个对象
x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not :判断两个标识符是不是引用自不同对象
x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，
否则返回 False
'''
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")#
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print( "2 - a 和 b 没有相同的标识")
else:
   print( "2 - a 和 b 有相同的标识")#
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")#
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")#
else:
   print( "4 - a 和 b 有相同的标识")