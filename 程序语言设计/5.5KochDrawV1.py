# -*- coding: utf-8 -*-
"""
Created on Wed May  9 06:17:18 2018
5.5 科赫雪花小包裹 KochDrawV1
科赫曲线：
1.给定线段AB，科赫曲线可以由以下步骤生成:
2.将线段分成三等份(AC,CD,DB)
3.以CD为底，向外(内外随意)画一个等边三角形DMC
4.将线段CD移去
分别对AC,CM,MD,DB重复1~3。
""" 
import turtle
def koch(size,n):
    if n == 0 :
        turtle.fd(size) #当=0时绘制的图形是一条直线
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,400)#窗体大小
    turtle.penup()
    turtle.goto(-200,100)#将画笔移动到这个位置
    turtle.pendown()
    turtle.pensize(2)#画笔宽度2
    level = 3 #3阶科赫雪花
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()