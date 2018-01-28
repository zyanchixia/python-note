#京东商品爬取实例
import requests #引入requests库

url = 'https://item.jd.com/12539078422.html' #给定url链接地址

try: #用try ...except框架
    r = requests.get(url,timeout = 30) #get引入url链接，设定时间30秒
    r.raise_for_status()#判断状态码是否为200
    r.encoding = r.apparent_encoding 
    print(r.text[:1000]) #打印前1000行信息
except:
    print('抓取失败')
    
