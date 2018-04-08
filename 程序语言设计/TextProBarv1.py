#TextProBarv1  文本进度条，利用time的sleep函数

import time

scale = 10#文本进度条的宽度为10

print('------执行开始------')
for i in range(scale+1):
    a = '*' * i # *号被复制i遍，当前百分比表达的信息
    b = '.' * (scale - i ) #剩余进度条百分比的信息
    c = (i/scale)*100 #输出与当前进度条和进度相关的百分比
    print ('{:^3.0f}%[{}->{}]'.format(c,a,b))#居中对齐
     #3.0表示输出格式为3位数据,小数点后0位,3个{}分别对应cab
    time.sleep(0.1)#定义休眠时间
print('------执行结束------')
