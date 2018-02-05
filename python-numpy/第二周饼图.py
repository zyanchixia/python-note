#plt.pie(data, explode)绘制饼图函数（数据，字符分割）

import matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs'#给出4个品项

sizes = [15,30,45,10]#给出分别的尺寸

explode = (0,0.1,0,0)#将Hogs在饼图中的显示突出出来

plt.pie(sizes,explode = explode,labels = labels,autopct ='%1.1f%%',
        shadow =False ,startangle = 90)

'''size 尺寸，explode 突出部分，labels 每块对应的标签，
autopct 显示百分数的方式，
shadow 饼图是二维饼图还是带阴影的,可以尝试改为ture看效果
startangle 开始角度90  '''

plt.axis('equal')
plt.show()
