# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:39:06 2018

"""
'''
for循环：重复执行语句,可以遍历任何序列的项目，如一个列表或者一个字符串
循环控制语句：
break 语句：在语句块执行过程中终止循环，并且跳出整个循环
continue 语句：在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
pass 语句：pass是空语句，是为了保持程序结构的完整性
'''
for letter in 'python':
    print('当前字母:',letter)
fruits = ['banana','apple','mango']
for fruit in fruits:
    print('当前水果:',fruit)
print ('over')

#通过序列索引迭代
fruits = ['banana','apple','mango']
for index in range(len(fruits)):#内置函数len(),range()
    print('当前水果:',fruits[index])

#循环使用else语句
    '''
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
while … else 也是一样'''
for num in range(10,20):#迭代10~20之间的数字
    for i in range(2,num):#根据因子迭代
        if num%i ==0:     #确定第一个因子
            j = num /i    #计算第二个因子
            print('%d 等于%d*%d'%(num,i,j))
            break    #跳出当前循环
    else:            #循环的else部分
        print(num,'是一个质数')
        
#输出2-100之间的质数
l =[]
for num in range(2,100): #迭代2~100之间的数字
    for i in range(2,num):  #根据因子迭代
        if num%i ==0:    #确定第一个因子
            break   #跳出循环
    else:
        l.append(num)   #循环else部分
print(l)
 

