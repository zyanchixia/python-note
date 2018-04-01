# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:08:38 2018
定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数
（允许输入大写字符，并且计数时不区分大小写）
"""
#解法0
def countchar(str):
    s = []#创建空列表以存放结果 
    str = str.lower()#将输入字符串中的字母转化为小写
    for i in range(26):#列表赋初值26个0
        s.append(0)
    for i in str:#遍历字符串
        if ord('a') <=ord(i) <=ord('z'):#判断在26个字母之间
            s[ord(i)-ord('a')] += 1#统计个数
    return s

if __name__ == "__main__":
    str = input()
    print(countchar(str))
    
    
 #解法1   
def countchar(str):
    num = [0]*26    
    str = str.lower()#支持输入大写字符，统一转换为小写
    for i in range(len(str)):#遍历字符串
        if str[i].isalpha():#检测字符串是否只由字母组成
            temp = ord(str[i]) - ord('a')#计算个数
            num[temp] += 1#将个数累计
    return num

if __name__=="__main__":
    str = input()
    print(countchar(str))