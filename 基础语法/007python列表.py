# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:15:06 2018

"""
'''
python 列表 list 创建一个列表，只要把逗号分隔的不同的数据项使用[]括起来即可
'''
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
#访问列表中的值
#与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等
print('list1[1]:',list1[0])
print('list2[1:5]:',list2[1:5])

#更新列表：可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
list =[] #一个空列表
list.append('google') #用append()添加元素
list.append('runoob')
print(list)

#删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000]
del list1[2] #删除元素
print('after deltting value at index 2:',list1)

#列表脚本操作符
'''
Python 表达式	结果	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	迭代
'''

#列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
'''
Python 表达式	结果	描述
L[2]	'Taobao'	读取列表中第三个元素
L[-2]	'Runoob'	读取列表中倒数第二个元素
L[1:]	['Runoob', 'Taobao']	从第二个元素开始截取列表
'''