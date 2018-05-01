# -*- coding: utf-8 -*-
'''
Created on Wed Apr 11 15:01:35 2018


ONE主要内容是每日一句话,一幅图片,一篇文章,一个问题
目标:爬取ONE往期所有的每日一句,并保存下来
思路:
  1.由于是所有的往期,所以要先确定每期页面的url的规律 
  2.查看页面源代码,确定要爬取内容的位置 
  3.写爬虫程序,爬取内容并保存

1.确定URL规律 
  要爬取页面中的三个关键部分：URL,期次,每日一句
观察URL,每一期的URL公共部分是http://wufazhuce.com/one/,
期次不同,后边跟的数字不同,可测,根据规则可知
URL = http://wufazhuce.com/one/+num（num范围是14-2043）,到2018年4月11号的
2.右键--查看源代码,定位目标
期次和每日一句所在的标签分别是****class属性为“one-titulo”和”fp-one-cita”的div

3.写爬虫程序
  开发工具和开发环境,IDE：Windows,Python3+,Spyder；
  技术路线:requests---BeautifulSoup---re
'''
import requests
import re
from bs4 import BeautifulSoup
url = 'http://wufazhuce.com/one/'#链接的公共部分
words = ['0'] *3800 #定义一个长度3800的列表,以保存每句话,并初始为0,防止字段过长溢出
for i in range(14,2043):#2043是2018年4月11日的页面对应
    #14之前的页面都不存在了,而且，这个区间内也有失效页面，代码执行期间会报错，所以用continue
    s = str(i) #数字类型转换成字符串类型
    currenturl = url +s #当前期的链接
    try:
        res = requests.get(currenturl)#获取url
        res.raise_for_status()
    except requests.RequestException as wrong : #异常处理
        print(wrong)
    else:
        html = res.text #页面内容
        soup = BeautifulSoup(html,'html.parser') #html字符串创建BeautifulSoup对象
        a = soup.select('.one-titulo')#查找期次所在的标签
        b = soup.select('.one-cita') #查找每日一句所在标签
        index = re.sub('\D','',a[0].string.split()[0])
        #re.sub用于替换字符串中的匹配项,\D:匹配一个非数字字符，等价于[^0-9]
        #从“vol.xxx”提取期次数值作为下标,这一句要理解正则表达式
        if(index == ''):
            continue
        words[int(index)] = b[0].string.split() #将该期每日一句存入列表
        
f = open('one20.txt','a',encoding='utf-8')#将每句话写入这个txt文件中,先打开
#默认存放在你脚本放的位置
for i in range(1,2043):
    if(words[i]=='0'):
        continue
    else:
        f.writelines('VOL.'+str(i)+'\n') #写入期次和换行
        f.writelines('    ') #每句话开始空四格
        f.writelines(words[i]) #写入该句话
        f.writelines('\n\n') #换行,并空一行写入下一句
f.close()

        

