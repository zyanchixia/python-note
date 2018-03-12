# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:41:39 2018

"""
'''
字典是另一种可变容器模型，且可存储任意类型对象
典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，
整个字典包括在花括号 {} 中,键必须是唯一的，但值则不必;
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组;
d = {key1 : value1, key2 : value2 }
'''
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict3['Name']:",dict3['Name']) #dict3['Name']: Zara
print("dict3['Age']:",dict3['Age']) #dict3['Age']: 7

#修改字典：向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8
dict['School'] = 'DPS School'
print("dict['Age']:",dict['Age']) #dict['Age']: 8
print("dict['School']:",dict['School']) #dict['School']: DPS School

#删除字典元素：能删单一的元素也能清空字典，清空只需一项操作
 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空词典所有条目
del dict        # 删除词典
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#字典键的特性：
'''
值可以没有限制地取任何python对象，既可以是标准的对象，
也可以是用户定义的，但键不行
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
'''
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name']) #dict['Name']:  Manni

dict = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name']) #list objects are unhashable