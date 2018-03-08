# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:37:47 2018

"""
'''
while循环：在给定的判断条件为true时执行循环体，否则退出循环体
循环控制语句：
break 语句：在语句块执行过程中终止循环，并且跳出整个循环
continue 语句：在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
pass 语句：pass是空语句，是为了保持程序结构的完整性
'''
#在某条件下循环执行某段程序，以处理需要重复处理的相同任务
'''
while 判断条件:
    执行语句...
 '''
count = 0
while (count<9):
    print('the count is :',count)
    count +=1
print('over')
#continue 用于跳过该次循环
i = 1
while i<10:
    i +=1
    if i%2>0: #非双数时跳过输出
        continue
    print(i)#输出双数2,4,6,8,10
# break 则是用于退出循环
i = 1
while 1: #循环条件为1必定成立
    print (i)#输出1~10
    i +=1
    if i >10:#当i大于10时跳出循环
        break#输出1~10

#无限循环：如果条件判断语句永远为true，循环将会无限执行下去，用ctrl+c来中断循环
var=1
while var ==1:#该条件永远为true，循环将无限执行下去
    num = input('enter a number:')
    print('you entered:',num)
print('over')

#循环使用else语句，循环条件为flase时，执行else语句
count=0
while count<5:
    print(count,'is less than 5')
    count +=1
else:
    print(count,'is not less than 5')

