#绘制一条蟒蛇
import turtle
turtle.setup(650,350,200,200)
turtle.penup() #拿起笔
turtle.fd(-250)
turtle.pendown() #放下笔
turtle.pensize(25) #画笔型号
turtle.pencolor('blue') #画笔颜色
turtle.seth(-40)#方向
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()

