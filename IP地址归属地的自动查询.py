# IP地址归属地的自动查询

'''http://m.138.com 是一个可以查询ip地址的网站，可以通过输入随意一个ip地址来观察链接发生的变化
http://m.ip138.com/ip.asp?ip=202.204.80.112
由此来得知ip地址查询的接口模式
http://m.ip138.com/ip.asp?ip= 
import requests
url = 'http://m.138.com/ip.asp?ip=' #定义url链接
r = requests.get(url + '202.204.80.112')#get方法得到ip地址
r.status_code#返回状态200
print(r.text[-500:])#输出最后500个字符
'''

#全代码可写为
import requests
url = 'http://m.ip138.com/ip.asp?ip='
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('解析错误')

    
    
