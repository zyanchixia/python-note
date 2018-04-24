# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:49:11 2018

"""
import matplotlib.pyplot as plt
fig,(ax0,ax1) = plt.subplots(2,1) #2行1列

ax0.plot(range(7),[3,4,7,6,2,8,9],color= 'r',marker='o')
#x轴是0-6，y轴上的数字分别是列表中的7个数字，红色，圆点
ax0.set_title('subplot1')#设置子图的标题
plt.subplots_adjust(hspace=0.5)
#调整两个子图之间的距离，这里是垂直方向距离
ax1.plot(range(7),[5,1,8,2,6,9,4],color='g',marker='o')
ax1.set_title('subplot2')

