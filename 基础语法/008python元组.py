# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:06:01 2018

"""
'''
Python的元组与列表类似，不同之处在于元组的元素不能修改;
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可;
下标索引从0开始，可以进行截取，组合等
'''
tup1 = (50,) #元组中只包含一个元素时，需要在元素后面添加逗号
#访问元组
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print('tup1[1]:',tup1[1]) #输出chemistry
print('tup2[1:5]:',tup2[1:5])#输出(2, 3, 4, 5)

#修改元组：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1+tup2
print(tup3)#输出(12, 34.56, 'abc', 'xyz')

#删除元组：可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000);
print(tup)
del(tup)
print('after deleting tup :',tup)#输出结果name 'tup1' is not defined

#元组运算符：元组之间可以使用 + 号和 * 号进行运算
'''
Python 表达式	结果	描述
len((1, 2, 3))	3	计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	True	元素是否存在
for x in (1, 2, 3): print x,	1 2 3	迭代
'''
#元组索引，截取:访问元组中的指定位置的元素，也可以截取索引中的一段元素
L = ('spam', 'Spam', 'SPAM!')
'''
Python 表达式	结果	描述
L[2]	'SPAM!'	读取第三个元素
L[-2]	'Spam'	反向读取；读取倒数第二个元素
L[1:]	('Spam', 'SPAM!')	截取元素
'''

#无关闭分隔符:任意无符号的对象，以逗号隔开，默认为元组
print('abc', -4.24e93, 18+6.6j, 'xyz')
x,y = 1,2
print("Value of x , y : ", x,y)
#输出abc -4.24e+93 (18+6.6j) xyz
#Value of x , y :  1 2

#元组内置函数
cmp(tuple1, tuple2) #比较两个元组元素
len(tuple) #计算元组元素个数
max(tuple) #返回元组中元素最大值
min(tuple) #返回元组中元素最小值
tuple(seq) #将列表转换为元组