# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:15:54 2018

"""
'''
#python条件语句是通过一条或多条语句的执行结果(True 或False)来决定执行的代码块
python程序语言指定任何非0或非空(null)值为true，0或null值为false
'''
'''
1：基础应用
if 判断条件:
    执行语句
else:
    执行语句
'''
flag = False
name ='luren'
if name == 'python':#判断变量是都为python
    flag = True #条件成立时设置标志为真
    print('welcome boss') #输出信息
else:
    print(name)#条件不成立时输出变量名称
#输出结果为 luren
'''
2:判断多条件时
if 判断条件1:
    执行语句1
elif 判断条件2:
    执行语句2
elif 判断条件3:
    执行语句3
else:
    执行语句4
'''
num =5
if num ==3:#判断num的值
    print ('boss')
elif num ==2:
    print('user')
elif num ==1:
    print('worker')
elif num <0:#值小于0时的输出
    print('error')
else:
    print('roadman')#条件不成立时输出

#如果需要多个条件同时判断时，可以用or，and
num = 9
if num >=0 and num <=10:#判断是否在0到10之间
    print('hello')

num = 8
if (num >=0 and num <=5) or (num >=10 and num<=15):#判断是否在0~5或者10~15之间
    print('hello')
else:
    print('undefine')

