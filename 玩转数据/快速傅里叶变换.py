# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:40:34 2018

"""

#一组数据的快速傅里叶变换

import scipy as sp
import pylab as pl
listA = sp.ones(500) #成黄建一个有500个1的数组
listA[100:300] = -1 #把这些元素设置为-1
f = sp.fft(listA)#对这个数组进行傅里叶变换
pl.plot(f)
pl.show()
