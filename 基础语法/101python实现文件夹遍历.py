# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:42:12 2018

"""
#python实现文件夹遍历
#os.path.exists(path) 判断文件路径是否存在
import os
dir = 'E:\报表\退款'
if os.path.exists(dir):
    print('dir exists')
else:
    print('no exists')
    
#os.path.isfile(path) 判断path是否是文件
dir = r'E:\报表\退款\退款\20110301\2011-03-01.xls'#r的使用
if os.path.isfile(dir):
    print('file exists')
else:
    print('no exists')
    
#os.path.getsize(path) 获取path文件的大小   
size = os.path.getsize(dir)
print(size/1024)

'''os.path.walk(path) 遍历path，
返回一个三元组（dirpath, dirnames, filenames). dirpath表示遍历到的路径,
 dirnames表示该路径下的子目录名，是一个列表, 
 filesnames表示该路径下的文件名，也是一个列表
 例如: 当遍历到c:\windows时，dirpath="c:\windows",
 dirnames是这个路径下所有子目录名的列表，dirnames是这个路径下所有文件名的列表
 '''
 #列出windows目录下的所有文件和文件名
for (root,dirs,files) in os.walk('C:\Windows'):
    for filename in files:
        print(os.path.join(root,filename))
    for dirc in dirs:
        print(os.path.join(root,dirc))
#实例
dir = r'E:\报表\退款\20110301'
for (root,dirs,files) in os.walk(dir):
    for filename in files:#路径+文件名
        print(os.path.join(root,filename))
    for dirc in dirs:#路径+文件夹名
        print(os.path.join(root,dirc))