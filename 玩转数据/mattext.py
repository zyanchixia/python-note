# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:24:10 2018

"""
path = '222.xlsx'
import pandas as pd
result = pd.read_excel(path)
#print(result) #打印表中数据结果

import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
x = result.date
y = result.amont

plt.title('Function 20180423')
plt.xlabel('date')
plt.ylabel('amont')
plt.plot(x,y)#折线图
plt.bar(x,y) #柱状图
plt.savefig(r'C:\Users\zhangyanhong\Desktop\1.jpg')#保存图片
