# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:50:04 2018

"""
'''
python基础语法:
python 最具特色的就是用缩进来写模块,缩进的空白数量是可变的，
但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行
'''
if True:
    print('True')
else:
    print('Flase')

#python 引导:单引号，双引号，三引号
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落，
包含了多个语句"""
#python注释 用#
# 第一个注释
print "Hello, Python!";  # 第二个注释
#Python空行，函数之间或类的方法之间用空行分隔，表示一段新的代码的开始
#等待用户输入
input('按下enter键退出，其他任意键显示...\n')
#同一行显示多条语句
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys;x='runoob';sys.stdout.write(x+'\n')
#print 输出：print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
x= 'a'
y = 'b'
print(x) #换行输出x
print(y) #换行输出y
print(x,y) #不换行输出x,y