# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:25:04 2018
七段数码管绘制
1：绘制单个数字对应的数码管
2：获得一串数字，绘制对应的数码管
3：获得当前系统时间，绘制对应数码管
数码管有固定的顺序
"""
import turtle
def drawLine(draw):#绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    #函数draw控制画笔，如果draw true则画笔落下，否则画笔抬起
    turtle.fd(40) #向前进方向行进40像素
    turtle.right(90) #右转90度
def drawDigit(digit):#根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False) #第一笔
    drawLine(True) if digit in [0,1,3,5,6,7,8,9] else drawLine(False) #第二笔
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False) #第三笔
    drawLine(True) if digit in [0,2,6,8] else drawLine(False) #第四笔
    turtle.left(90)#回到起点，调整笔头90度向左（即继续向上）
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False) #第无笔
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False) #第六笔
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False) #第七笔
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20) #为绘制后续数字确定位置
    
def drawDate(date):
    for i in date:
        drawDigit(eval(i)) #通过eval()函数将数字变为整数

def main(): #定义主函数信息
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20180507')
    turtle.hideturtle()
    turtle.done()
    
main()
        

    
    