#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 19:27
# @Site    : 
# @File    : 微信群发消息.py
# @Software: PyCharm
import itchat
import time
from itchat.content import  *

gname = 'we are 伐木累'#微信群名字
context = '这是我的测试消息' #发送消息的内容
def SendChatRoomsMsg(gname,context):
    #获取所有群的相关消息，update = True信息更新
    myroom = itchat.get_chatrooms(update = True)
    global username
    #传入指定群名进行搜索，之所以搜索，是因为群员的名称信息也在里面
    myroom = itchat.search_chatrooms(name = gname)
    for room in myroom:
        if room['NickName'] == gname:
            #遍历所有NickName为键值的信息进行匹配群名
            username = room['UserName']
            # 得到群名的唯一标识，进行信息发送
            itchat.send_msg(context,username)
        else:
            print('No groups found')

#监测谁发消息给我
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send("自动回复：你的消息我收到了...我现在有事，晚上回复你，如果有急事，打电话给我"%
    # "您发送了:\'%s\'\n这是自动回复的消息啦啦啦...我现在有事，晚上回复你消息呀"%
                (msg['Text']),toUserName=msg['FromUserName']
                )
# 登录微信enableCmdQR表示的是当完全的命令行界面可以弹出文本绘制的二维码
# 生成二维码，需扫码登陆，hotReload= True表示的连续几次运行不需要再次扫码
itchat.auto_login(hotReload = True)
# 调用函数发送群消息
SendChatRoomsMsg(gname,context)

# 保持登录状态
itchat.run()




