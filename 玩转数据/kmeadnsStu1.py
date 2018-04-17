#聚类分析

import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]

data = np.array([list1,list2,list3,list4,list5,list6])
whiten = whiten(data)#whiten算出各列元素的标准差
centroids,_=kmeans(whiten,3)#kmeans对数据进行聚类，2是聚成两类，指学霸和非学霸,可调整
#kmeans的返回结果是一个元祖，其中指需要用到第一个值，,_表示第二个不需要
result,_=vq(whiten,centroids)
#vq是一个矢量量化函数，可以对每一个数据进行归类
print(result)
#[1 0 0 1 1 0] 结果如此，list6的同学是学霸，list2和3也属于一类
