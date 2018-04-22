
from turtle import Turtle #引入turtle库的turtle模块
p = Turtle()
p.speed(2) #设置速度
p.pensize(3) #设置线条粗细
p.color('black','yellow') #笔的颜色及填充颜色
p.begin_fill() #开始填充
for i in range(5):#5条线
    p.fd(200)#向前200
    p.right(144)#向右144度 与向左216度的结果是一样的
p.end_fill()#结束填充
