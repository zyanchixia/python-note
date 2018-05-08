# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:36:09 2018
5.3 字符串反转

将字符串s反转后输出：切片操作
s[::-1]
理解：将s的全部，按照-1的步长输出，即反转
"""
def rvs(s):
    if s == '':#s为空，则返回s本身
        return s
    else:
        return rvs(s[1:])+s[0]
    #除首字母之外的其他进行反转，首字符放最后