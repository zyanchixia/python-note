# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:25:18 2018
创建一个简单的wxpython程序
#firstwxPython

"""
import wx
app = wx.App() #创建一个应用程序对象
frame = wx.Frame(None,title = 'hello world')
#创建一个frame对象
frame.Show(True) #显示窗体
app.MainLoop()#进入事件循环

