# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:14:29 2018

"""
'''
Python 函数：是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段
函数能提高应用的模块性，和代码的重复利用率

定义一个函数:
你可以定义一个由自己想要功能的函数，以下是简单的规则：

    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方,
    不带表达式的return相当于返回 None;
语法:
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]


'''
#传不可变对象实例
def changeint(a):
    a = 10
    
b = 2
changeint(b)
print(b) #输出结果是2

#传可变对象实例
def changeme(mylist):
    mylist.append([1,2,3,4])
    print('函数内取值:',mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print('函数外取值:',mylist)
#输出结果 函数内取值: [10, 20, 30, [1, 2, 3, 4]]
 #       函数外取值: [10, 20, 30, [1, 2, 3, 4]]