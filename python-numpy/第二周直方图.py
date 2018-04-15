#plt.hist(x,bins,normed)绘制直方图

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)#一个随机种子为0

mu,sigma = 100,20 #均值和标准差

a = np.random.normal(mu,sigma,size=100)
#用random.normal生成一个均值，方差已给定的元素是正态分布特点的数组a

#绘制数组a的直方图
plt.hist(a,20,normed = 1,histtype = 'stepfilled',facecolor = 'b',alpha=0.75)
'''
第二个参数20即为bins值，把数组a的最大值和最小值之间
  平均切割成bins个直方，可改为其它数看显示结果
normed =1，将每个直方中出现元素的个数规划为出现的概率，所以纵坐标是个小数
如果normed=0，那么纵坐标就是在这个直方区域之间出现的a的元素的个数
histtype 绘制类型，
facecolor 颜色，
alpha 尺寸比例

'''
plt.title('Histogram')#定义标题名称

plt.show()
