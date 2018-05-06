# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:03:22 2018
7.6 布局管理
"""
import wx

class Frame1(wx.Frame):

    def _init_(self,superior):
        wx.Frame._init_(self,parent=superior,title = 'Hello World in wxPython')
        panel = wx.Panle(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel,value='hello,world',
                                 size=(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP|wx.EXPAND)
        button = wx.Button(panel,label='Click Me')
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
        self.Show(True)
    def OnClick(self,text):
        self.text1.AppendText('\nHello,World')

if __name__=='__main__':
    app = wx.App()
    frame = Frame1(None,'Hello World in wxPython')
    app.MainLoop()

#EOL while scanning string literal 报错，是因为引号没有成对出现
#The wx.App object must be created first!  要记得 del app