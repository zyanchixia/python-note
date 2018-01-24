import requests #调用库

def getHTMLText(url):#定义
    try:
        r = requests.get(url,timeout = 30) #请求url链接,限时30秒
        r.raise_for_status()#判断返回的内容是否正常
        #若状态不是200，引发httperror异常
        r.encoding = r.apparent_encoding#替代，使返回的解码是正确的
        return r.text
    except:
        return "异常"

if __name__ == "__main__":#前后都是双下划线
    url = "http://www.baidu.com"
    print(getHTMLText(url))
