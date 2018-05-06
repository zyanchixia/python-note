# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:08:45 2018
显示helloworld字符串
"""

import wx 
class Frame1(wx.Frame):
   def __init__(self,parent,title):
        wx.Frame.__init__(self, parent, title = title, 
                          pos = (100,200), size = (200,100))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value = "Hello, World!",
                            size = (200,100))
        self.Show(True)
if __name__ == '__main__': 
    app = wx.App()
    frame = Frame1(None, "Example")
    app.MainLoop()
    
    
'''
在Anaconda中运行程序如果出现
“NoAppError: The wx.App object must be created first!”这样的错误，
请在Python Shell中执行del app即可
'''