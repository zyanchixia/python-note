#plt.scatter(x,y)绘制散点图，其中，x和y长度相同

import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')

ax.set_title('Smiple Scatter')

plt.show()
