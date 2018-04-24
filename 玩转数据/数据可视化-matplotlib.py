# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:55:16 2018
python数据可视化:
 matplotlib,pandas绘图，直方图，散点图，柱状图，折线图，箱线图
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#两组来自正太分布的随机数的散点图，bo指用蓝色圆点绘图
#plt.plot(np.random.normal(size=100),np.random.normal(size=100),'bo')
with mpl.rc_context(rc={'font.family':'serif','font.weight':'bold','font.size':8}):
    fig = plt.figure(figsize=(6,3))#定义一个长6宽3的画布
    ax1 = fig.add_subplot(121) #将画布分为1行2列，从左到右从上到下取第1个
    ax1.set_xlabel('some random numbers')#x轴名
    ax1.set_ylabel('more random numbers')#y轴名
    ax1.set_title('Random scatterplot')#标题名
    plt.plot(np.random.normal(size=100),np.random.normal(size=100),'r.')
    #作一个散点图
    
    ax2 = fig.add_subplot(122)
    ax2.set_xlabel('sample')
    ax2.set_ylabel('sumulative sum')
    ax2.set_title('Nomal distrubution')
    plt.hist(np.random.normal(size=100),bins=15)
    #作一个柱状图, bins 设置分组的个数
    plt.tight_layout()
    #紧凑显示图片
    plt.savefig('normalvars.png',dpi=150)
    #保存以上图片,dpi图片精度