# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:26:21 2018
Python 列表函数&方法
"""
'''
#python 包含以下函数
len(list)  #列表元素个数
max(list) #返回列表元素最大值
min(list) #返回列表元素最小值
list(seq)  #将元组转换为列表

#python包含以下方法
list.append(obj) #在列表末尾添加新的对象
list.count(obj) #统计某个元素在列表中出现的次数
list.extend(seq)
#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)
#从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) #将对象插入列表
list.pop(obj=list[-1])
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) #移除列表中某个值的第一个匹配项
list.reverse() #反向列表中元素
list.sort([func]) #对原列表进行排序
list.clear() #清空列表
list.copy() #复制列表
'''
#python 包含以下函数
l = [2018, 1952, 1997, 2000]
t = (123, 'xyz', 'zara', 'abc')
print(len(l))
print(max(l))
print(min(l))
tl = list(t)
print('元组转列表:',tl)#输出 元组转列表: [123, 'xyz', 'zara', 'abc']
#python包含以下方法
l.append(1314)
print ('添加之后输出:',l) #[2018, 1952, 1997, 2000, 1314, 1314]
print('计算出现次数:',l.count(1997)) #计算出现次数: 1
#list.extend
l2 = list(range(3)) #创建0-2的列表
l.extend(l2) #扩展列表
print("扩展后的列表:",l)
#扩展后的列表: [2018, 1952, 1997, 2000, 1314, 1314, 0, 1, 2]
#list.index(obj)
l1 =['Google', 'Runoob', 'Taobao']
print('Runoob索引值为:',l1.index('Runoob')) #Runoob索引值为: 1
print('Taobao索引值为:',l1.index('Taobao')) #Taobao索引值为: 2
#list.insert(index, obj) #将对象插入列表
l1.insert(1,'baidu')
print('列表插入元素后为:',l1)
#列表插入元素后为: ['Google', 'baidu', 'Runoob', 'Taobao']
#list.pop(obj=list[-1]) 移除列表中的元素
l1.pop() #无特殊标注即默认移除最末一个元素
print('列表默认移除最后一个元素:',l1) #['Google', 'Runoob']
l1.pop(1)
print('列表移除第1个索引元素之后:',l1) # ['Google']
#list.remove(obj) #移除列表中某个值的第一个匹配项
l1 =['Taobao','Google', 'Runoob',  'Taobao','Baidu']
l1.remove('Taobao')
print('移除淘宝后:',l1)#移除返回的第一个匹配项
l1.remove('Baidu')
print('移除百度后:',l1)
#list.reverse() #反向列表中元素
l1.reverse()
print("列表反转后: ",l1) #将列表中元素倒置
#list.sort([func]) #对原列表进行排序
l1.sort()
print("列表排序后: ",l1)
#列表排序后:  ['Baidu', 'Google', 'Runoob', 'Taobao', 'Taobao']
#list.copy() #复制列表
l2 = l1.copy()
print("l2列表: ",l2) #将其他表复制一份
# list.clear() #清空列表
l2 = l1.clear()
print("l2列表: ",l2) #输出结果none