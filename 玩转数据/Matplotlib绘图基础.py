# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:27:18 2018

"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1)
y = np.sin(4*np.pi*x)*np.exp(-5*x)
plt.plot(x,y) #折线图
plt.plot(x,y,'r.') #红色圆点的散点图
plt.bar(x,y) #柱状图

#栗2 
import pylab as pl
t = np.arange(0.,4.,0.1)
pl.plot(t,t,t,t+2,t,t**2)