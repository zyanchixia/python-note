#百度/360搜索关键词提交
#百度关键词接口
# http://www.baidu.com/s?wd=keyword
#360的关键词接口
# http://www.so.com/s?q=keyword

# 百度关键词搜索提交
import requests
keyword = 'python'
url = 'http://www.baidu.com/s'
try:
    kv = {'wd':keyword}
    r = requests.get(url,params = kv) #params:字典或字节序列，作为参数增加到url中
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')

#实例分步骤解析：
import requests 
url = 'http://www.baidu.com/s'
kv = {'wd':'python'} #定义键值对，查找关键字python的信息
r = requests.get(url,params = kv)#params可作为参数增加到url中
r.status_code
200
r.request.url#返回查找关键字的url的具体信息
'http://www.baidu.com/s?wd=python'
len(r.text)#查看一下长度
286333

#360关键词搜索提交代码
import requests
url = 'http://www.so.com/s'
keyword = 'python'
try:
    kv = {'q':keyword}
    r = requests.get(url,params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('抓取失败')

    
