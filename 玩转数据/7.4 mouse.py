# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:56:39 2018
7.4 mouse
"""

import wx
class Frame1(wx.Frame):
    def _init_(self,superior):
        wx.Frame._init_(self,parent=superior,title='Example',
                        pos=(100,200),size=(350,200))
        self.panel = wx.Pane(self)
        self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick)
        #鼠标左键点击，抬起
    
    def onClick(self,event):
        posm = event.GetPosition()
        wx.StaticText(parent = self.panel,label='Hello World',
                      pos = (posm.x,posm.y))

if __name__=='__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    
    
#执行报错 Kernel died, restarting....
