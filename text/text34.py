# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:51:31 2018

"""
#练习函数调用

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()
