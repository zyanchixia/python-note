# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:54:50 2018
# 局部变量和全局变量 规则2
局部变量为组合数据类型且未创建，等同于全局变量

"""
ls = ['F','f'] #使用列表真实创建一个全局变量列表ls
def func(a):
    ls.append(a) #此处ls是列表类型，未真实创建，等同于全局变量
    return
func('C') #全局变量ls被修改
print(ls)
#运行结果为 ['F', 'f', 'C']