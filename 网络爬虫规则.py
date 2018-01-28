# requests 库的简单介绍和安装
#可以在http://www.python-requests.org网站上详细了解
#requests 库安装：用管理员权限启动cmd---pip install requests 回车，即可安装成功

#测试requests库安装效果，启动IDLE，import requests
r = requests.get("http://baidu.com")
r.status_code #执行，看状态码是否为200，200则说明访问成功
r.encoding = 'utf-8' 
r.text#打印网页内容
'''
requests库7个主要方法
1：requests.request() 构造一个请求，支撑以下各方法的基础方法；
2：requests.get() 获取html网页的主要方法，对应于http的get
3：requests.head() 获取html网页头信息的方法，对应于http的head
4：requests.post() 向html网页提交post请求的方法，对应于http的post
5：requests.put() 向html网页提交put请求的方法，对应http的put
6：requests.patch() 向html网页提交局部修改请求，对应http的patch
7：requests.delete() 向html页面提交删除请求，对应http的delete


requests.get(url,params= None,**kwargs)
url：拟获取页面的url链接
params：url中的额外参数，字典或字节流格式，可选
**kwargs：12个控制访问的参数
'''

#response 对象,包含服务器返回的所有信息，也包含请求的response信息
'''
response 对象的属性
r.status_code：http请求的返回状态，200表示链接成功，404表示失败
r.text： http响应内容的字符串形式，即url对应的页面内容
r.encoding：从http header中猜测的响应内容编码的方式
r.apparent_encoding：从内容中分析出的响应内容编码方式
r.content：http响应内容的二进制形式

requests 库的异常情况
1：requests.ConnectionError:网络链接错误异常，如DNS查询失败，拒绝连接等
2：requests.HTTPError：http错误异常
3：requests.URLRequired：url缺失异常
4：requests.TooManyRedirects：超过最大重定向次数，产生重定向异常
5：requests.Timeout：请求url超时，产生超时异常 

理解response的异常：
r.raise_for_status(),如果不是200，产生异常，requests.HTTPError
r.raise_for_status() 在方法内部判断r.status_code是否等于200，不需要增加额外的if语句，
该语句便利用try-except进行异常处理
'''

