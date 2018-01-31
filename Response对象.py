import requests #调用库
r = requests.get('http://www.baidu.com') #get方法访问百度主页
print(r.status_code)#检测请求的状态码
200 #200表示成功，非200即为失败
type(r)#检测r的类型
<class 'requests.models.Response'>#返回一个名为Response的类
r.headers#返回头部信息
{'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Content-Encoding': 'gzip'
 
