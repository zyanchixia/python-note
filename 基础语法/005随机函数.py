# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:21:32 2018

"""
'''
python 随机函数
'''
choice(seq)#从序列的元素中随机挑选一个元素，
 #如random.choice(range(10)),从0到9随机挑选一个整数
import random
randrange()#返回指定递增基数集合中的一个随机数，基数缺省值为1
 #语法：randrange([start,]stop [,step])
print('randrange(1,100,2):',random.randrange(1,100,2))

print(random.randrange(100))

random()#随机生成一个实数，在[0,1])范围内，random.random()
seed([x]) #改变随机数生成器的种子seed
shuffle(lst) #将序列的所有元素随机排序
uniform(x,y) #随机生成下一个实数，它在[x,y]范围内 random.uniform(2,8)

