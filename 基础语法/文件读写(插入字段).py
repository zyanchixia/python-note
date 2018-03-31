# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:51:14 2018

"""
'''
file_obj.seek(offset,whence=0),在文件中移动文件指针，
从whence（0表示文件头部，1表示当前位置，2表示文件尾部）
偏移offset个字节；
whence参数可选，默认为0
'''
s = 'Today is a good day,do you think so?'
with open (r'C:\Users\ningkang\Desktop\companies.txt','a+') as f:
    #a+以读和追加模式打开
    f.writelines('\n')
    f.writelines(s)
    f.seek(0)#从文件头部开始读取
    cNames = f.readlines()
    print(cNames)
