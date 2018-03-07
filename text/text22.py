# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:09:59 2018

"""
'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人
已抽签决定比赛名单。有人向队员打听比赛的名单
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
'''
#解法0：
for a in ['x','y','z']:
    for b in ['x','y','z']:
        for c in ['x','y','z']:
            if((a!=b) and (b!=c) and (c!=a) and (a!='x')
            and (c!='x') and (c!='z')):
                print('a和%s比赛,b和%s比赛,c和%s比赛'%(a,b,c))
#解法1：
n = ['a','b','c']
m = []
for i in range(3):
    if n[i] != 'a' and n[i] != 'c':#i非a非c，即b=x
        m.insert(i,'x')
    elif n[i] != 'c':#a=z
        m.insert(i,'z')
    else:
        m.insert(i,'y')#c=y
print('a--%s,b--%s,c--%s'%(m[0],m[1],m[2]))
                   