# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:57:31 2018

"""
'''
爬取ONE的图片：
通过页面源代码，找到目标图片所在标签是img标签，用bs4的find_all()函数查找
目标图片在第2个img标签中,
http://wufazhuce.com/one/2043
'''
import re
import requests
from bs4 import BeautifulSoup
import urllib.request
url = 'http://wufazhuce.com/one/'
Path = r'C:\测试图片保存\\'#图片保存路径，改为你自己的路径
#注意最后有\\，是指把照片保存在了该文件夹中
num = 0#记录爬取照片的个数
for i in range (14,20):#想要多少图片自己定义
    s = str(i)
    currenturl = url +s
    try:
        res = requests.get(currenturl)
        res.raise_for_status()
    except requests.RequestException as e:#异常处理
        print(e)
    else:
        html = res.text
        soup = BeautifulSoup(html,'html.parser')
        a = soup.select('.one-titulo')#期次
        h = soup.find_all('img') #图片标签
        imgUrl = h[1].get('src')#获取图片的链接，目标图片在第2个img标签中，所以取第1个
        index = re.sub('\D','',a[0].string.split()[0])
        if(index==''):
            continue
        imgName = Path + 'VOL.'+index+'.jpg'#图片完整路径含图片名
        urllib.request.urlretrieve(imgUrl,imgName) #保存图片
        #python3+的写法，与2不同 
        num += 1
        print('图片已爬取%d张'%num)
print('爬取结束')
            
