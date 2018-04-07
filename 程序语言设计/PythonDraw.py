#绘制一条蟒蛇
import turtle
turtle.setup(650,350,200,200)
turtle.penup() #拿起笔
turtle.fd(-250)#倒退前进250
turtle.pendown() #放下笔
turtle.pensize(25) #画笔型号
turtle.pencolor('blue') #画笔颜色
turtle.seth(-40)#将海龟方向指向坐标系中绝对40方向 
for i in range(4):#产生循环计数序列
    turtle.circle(40,80)#以40为半径，80度为弧度
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)#向前行进40，脖子部分
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()#去掉，则运行完自动关闭

