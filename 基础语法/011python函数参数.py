# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:28:26 2018

"""
'''
python参数:
1：必备参数:
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
2：关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
使用关键字参数允许函数调用时参数的顺序与声明时不一致，顺序不重要
因为 Python 解释器能够用参数名匹配参数值
3：缺省参数
调用函数时，缺省参数的值如果没有传入，则被认为是默认值
4：不定长参数
你可能需要一个函数能处理比当初声明时更多的参数
这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名
语法：加了星号（*）的变量名会存放所有未命名的变量参数
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
5:匿名函数：python 使用 lambda 来创建匿名函数
lambda只是一个表达式，函数体比def简单很多
lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，
后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法：lambda [arg1 [,arg2,.....argn]]:expression

6：return语句
return语句[表达式]退出函数，选择性地向调用方返回一个表达式
不带参数值的return语句返回None

7:全部变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

'''
#必备参数+关键字参数
def printme(str):
    print(str)
    return
print(str) #输出为错
printme(str = 'my string')#关键字参数，输出为 my string

#缺省参数
def printinfo(name,age=35):
    print('name:',name)
    print('age:',age)
    return
printinfo(age=50,name = 'miki')#输出 name: miki，age: 50
printinfo(name='lala') #输出 name: lala age: 35缺省参数没传入，则被认为是默认值

#不定长参数
def printinfo(arg1,*vartuple):
    print('输出:')
    print(arg1)
    for var in vartuple:
        print (var)
    return
printinfo(10)
printinfo(70,60,50)

#匿名函数
sum = lambda arg1,arg2:arg1+arg2
print('相加后的值为:',sum(10,20)) #相加后的值为: 30
print('相加后的值为:',sum(20,20)) #相加后的值为: 40

#return 语句
def sum(arg1,arg2):
    total = arg1+arg2
    print('函数内:',total)
    return total
total = sum(10,20) #函数内: 30

#全部变量和局部变量
total = 0 #这是一个全局变量
#可写函数说明
def sum (arg1,arg2): #返回2个参数的和
    total = arg1+arg2 #total在这里是局部变量
    print('函数内是局部变量:',total)
    return total
#调用sum函数
sum(10,20) #函数内是局部变量: 30
print('函数外是全局变量:',total) #函数外是全局变量: 0