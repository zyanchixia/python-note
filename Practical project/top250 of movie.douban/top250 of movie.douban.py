# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:52:39 2018
爬取豆瓣top250的电影
影片名称，导演演员信息，评分，评论人数，上映日期，制片国家

"""
import requests
from lxml import html
k = 1
for n in range(10):
    url = r'https://movie.douban.com/top250?start={}&filter='.format(n*25)
    con = requests.get(url).content
    sel = html.fromstring(con)


# 所有的信息都在div class="info"标签里
for i in sel.xpath('//div[@class="info"]'):
    #影片名称
    title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
    #导演，演员，制片国家，影片类型等放进info
    info = i.xpath('div[@class="bd"]/p[1]/text()')
    
    info_1 = info[0].replace(" ","").replace("\n","") #导演
    date = info[1].replace(" ","").replace("\n","").split("/")[0]#上映日期
    country = info[1].replace(" ","").replace("\n","").split("/")[1]#制片国家
    geners = info[1].replace(" ","").replace("\n","").split("/")[2] #影片类型
    rate = i.xpath('//span[@class="rating_num"]/text()')[0]#评分
    comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0] #评论人数
    print('TOP%s'%str(k))
    print(title,info_1,date,country,geners,rate,comCount)
    with open(r'C:\Users\ningkang\Desktop\top250.txt','a',encoding='utf-8') as f:
        f.write('TOP%s\n影片名称:%s\n评分:%s %s人评论\n上映日期:%s\n上映国家:%s\n导演:%s\n'
                %(k,title,rate,comCount,date,country,info_1))
        f.write("=============================\n")
    k +=1
    
    
