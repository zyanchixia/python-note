# 亚马逊网页爬取实例
import requests
url = 'https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki'
try:
    kv = {'user-agent':'Mozilla/5.0'}#定义一个标准浏览器
    r = requests.get(url,headers = kv)#重新定义headers信息
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
    



#实例分步骤解析：
import requests
url = 'https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki'
r = requests.get(url,timeout=30)
r.status_code
503#而实际上我自己写的时候却返回了200，我也不知道是为什么
r.encoding
'ISO-8859-1'
r.encoding = r.apparent_encoding
r.text
#由于之前状态不是200，这里返回提示Marktplace APIS意外错误
r.requests.headers #查看发给亚马逊的到底是什么信息
{'User-Agent': 'python-requests/2.13.0', 'Accept': '*/*',
 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate'}
#可以看到uesr-agent是requests，说明爬虫忠实的告诉了亚马逊我们是通过程序产生的访问
#亚马逊就可以不支持这样的访问，所以要更改头部信息，模拟浏览器向亚马逊发送信息
kv = {'user-agent':'Mozilla/5.0'}#是一个标准浏览器，也可以用其他的浏览器，这是举例
#重新定义user-agent的内容，


