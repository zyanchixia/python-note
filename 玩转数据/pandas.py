# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:45:48 2018

"""

import pandas as pd
import numpy as np
excel_path = r'C:\Users\zhangyanhong\Desktop\麒麟瓜.xlsx'
df= pd.read_excel(excel_path)
一：查看数据
1.查看前n行或后n行
#print(df.head(2)) #取表的前2行
#print(df.tail(2)) #取最后2行
2.查看index，columns及values
df.index,df.columns,df.values
3.describe()函数对于数据的快速统计汇总
#print(df.describe())
#对每一列数据进行统计：计数，均值，std，各个分位数等
4.对数据转置
#print(df.T) #对数据进行转置
5.对轴进行排序
#print(df.sort_index(axis=1,ascending=False))
'''axis=1表示对所有columns进行排序，
ascending=False表示按降序排列，参数缺失时默认升序
可分别将这个两个条件执行，看效果
'''
6.对DataFrame中的值排序
#print(df.sort(columns = '订单'))
#只对这一列从小到大排序
二：选择对象
1.选择特定行和列数据
#print(df[0:3]) #通过切片来选择前n行数据
2.loc是通过标签来选择数据
df.loc['x']#默认选取行为x的行数据
#print(df.loc[:,['订单','商品名称']])
#选取所有行及column为这两个的列
#print(df.loc[6])
#选取行为6的行数据
#print(df.loc[[6,7],['订单','商品名称']])
#选取6,7行和订单，商品名称列的数据
3.iloc直接通过位置来选择数据
df.iloc[1:2,1:2] #显示第一行第一列的数据，切片后面的值取不到
df.iloc[1:2]#表示列的值没有时，默认选取行位置为1的所有数据
df.iloc[[0,2],[1,2]]#自由选取行位置和列位置的对应数据
4.使用条件来选择
df[df.订单>500] #取订单列大于500的数据
df[df['仓库'].isin(['青岛流亭仓','上海黄渡仓'])]
#isin选出特定列中包含特定值的行数据
三：设置值（赋值）
赋值操作在上述选择操作的基础上直接赋值即可
df.loc[:,['订单','商品名称']]=9
#将订单和商品名称两列的所有行数据全部赋值为9
df.iloc[:,[1,3]]=9
#效果同上