# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:13:33 2018

"""
'''
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法
'''
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )
#输出结果：My name is Zara and weight is 21 kg!

'''   python字符串格式化符号:
     符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
 '''
 
 ''' 格式化操作符辅助指令:
     符号	      功能
     *          定义宽度或者小数点精度
     -	          用做左对齐
     +	        在正数前面显示加号( + )
   <sp>	     在正数前面显示空格
   #	     在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'
              (取决于用的是'x'还是'X')
   0	       显示的数字前面填充'0'而不是默认的空格
   %	       '%%'输出一个单一的'%'
  (var)	     映射变量(字典参数)
   m.n.	 m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''