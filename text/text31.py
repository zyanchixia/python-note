# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:47:08 2018

"""
'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，
则继续判断第二个字母;
程序分析：用情况语句比较好，如果第一个字母一样，
则判断用情况语句或if语句判断第二个字母
'''
#解法0：构建数据字典，用键值对来匹配信息
weeklist = {'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wedensday',
            'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
letter1 = input('请输入首字母:') #千万注意中英文状态
letter1 = letter1.upper() #将字母转换成大写
if (letter1 in ['T','S']):
    letter2 = input('请输入第二个字母:')
    print(weeklist[letter1][letter2])
else:
    print(weeklist[letter1])