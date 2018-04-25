# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:10:19 2018
# pandas excel和csv格式文件的存取
"""
#读取
import pandas as pd

path_c = qj.csv
result1 = pd.read_csv(path_c)
print(result1['字段a'][:5])#如果数据量太大，可以直接打印某列和前n行


result2 = pd.read_excel('jxz.xlsx')#改为自己的路径
print(result2['字段a']) #只打印某列数据