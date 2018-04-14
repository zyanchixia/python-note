# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:25:13 2018

"""
'''统计句子中的词频次数（3分）
题目内容：

对于一个已分词的句子（可方便地扩展到统计文件中的词频）：
可以用collections模块中的Counter()函数方便地统计词频，例如可用如下代码：
'''
from collections import Counter
s = "我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！/"
s_list = s.split('/')
[s_list.remove(item) for item in s_list
 if item in '，！,.?!""']#中英文状态下还有空格
print(Counter(s_list))#出现的词及次数明细
print(len(Counter(s_list)))

