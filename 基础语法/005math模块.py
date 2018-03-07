# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:53:51 2018

"""
'''
Python数学函数 math模块,cmath模块
'''
import math
dir (math)
['__doc__', '__loader__', '__name__', '__package__', 
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 
 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 
 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 
 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 
 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
 'log2', 'modf', 'nan', 'pi', 'pow', 'radians',
 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

import cmath
dir (cmath)
['__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
 'atanh', 'cos', 'cosh', 'e', 'exp', 'isclose', 'isfinite', 
 'isinf', 'isnan', 'log', 'log10', 'phase', 'pi', 'polar', 
 'rect',  'sin', 'sinh', 'sqrt', 'tan', 'tanh']
#python 数学函数
abs(x)	 #返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	#返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	#如果 x < y 返回 -1, 如果 x == y 返回 0, 
           #如果 x > y 返回 1
exp(x)	#返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)#返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	#返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)#	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	#返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	#返回给定参数的最大值，参数可以为序列
min(x1, x2,...)	#返回给定参数的最小值，参数可以为序列
modf(x)#返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
pow(x, y)	#x**y 运算后的值。
round(x [,n])	#返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	#返回数字x的平方根