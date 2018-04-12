# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:30:06 2018
利用turtle库画图
The Legend of The Blue Sea
"""
#画出蓝色大海的传说，91度漩涡
import turtle
t = turtle.Pen()
t.pencolor('blue')
for i in range(0,1000,5):
    t.forward(i)
    t.left(91)
