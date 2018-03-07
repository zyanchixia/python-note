# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:03:00 2018

"""
'''
=  #c = a + b 将 a + b 的运算结果赋值为 c
+= #c += a 等效于 c = c + a
-= #c -= a 等效于 c = c - a
*= #c *= a 等效于 c = c * a
/= #	c /= a 等效于 c = c / a
%= #c %= a 等效于 c = c % a
**= #	c **= a 等效于 c = c ** a
//= #c //= a 等效于 c = c // a
'''
a ,b,c= 21,10,0

c = a + b
print("1 - c 的值为：", c) #1 - c 的值为： 31
 
c += a
print("2 - c 的值为：", c ) #2 - c 的值为： 52
 
c *= a
print ("3 - c 的值为：", c ) #3 - c 的值为： 1092
 
c /= a 
print( "4 - c 的值为：", c ) #4 - c 的值为： 52.0
 
c = 2
c %= a
print( "5 - c 的值为：", c) #5 - c 的值为： 2
 
c **= a
print ("6 - c 的值为：", c) #6 - c 的值为： 2097152
 
c //= a
print ("7 - c 的值为：", c) #7 - c 的值为： 99864

