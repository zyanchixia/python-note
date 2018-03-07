# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:20:15 2018

"""
#6 python列表：list[]是使用最频繁的数据类型,
#加号 + 是列表连接运算符，星号 * 是重复操作
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)           # 输出完整列表
print (list[0])          # 输出列表的第一个元素 runoob
print (list[1:3])         # 输出第二个至第三个元素 [786, 2.23]
print (list[2:])         # 输出从第三个开始至列表末尾的所有元素[2.23,'john',70.2]
print (tinylist * 2)      # 输出列表两次
print (list + tinylist)   # 打印组合的列表

#7:元组 用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])         # 输出第二个至第三个的元素 (786, 2.23)
print (tuple[2:])          # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组
#8：字典 无序的对象集合，用"{ }"标识，由索引(key)和它对应的值value组成
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])            # 输出键为 2 的值
print (tinydict)            # 输出完整的字典
#{'name': 'john', 'code': 6734, 'dept': 'sales'}
print (tinydict.keys())     # 输出所有键 dict_keys(['name', 'code', 'dept'])
print (tinydict.values())    # 输出所有值 dict_values(['john', 6734, 'sales'])


