#网上图片资源爬取
#网络图片链接的格式： http://www.example.com/picture.jpg
#国家地理：http://www.nationalgeographic.com.cn/
#选择一个图片Web页面：
#http://www.nationalgeographic.com.cn/photography/photo_of_the_ day/3921.html
#网上找一张图片，右键，属性，得到该图片的地址链接如下

#步骤详解
import requests
path = 'D://abc.jpg'#定义一个存储地址在d盘，爬取下来的图片命名为abc
url ='http://image.nationalgeographic.com.cn/2017/0331/20170331042952894.jpg'
r = requests.get(url) 
r.status_code
#图片是一个二进制格式
with open(path,'wb') as f:#打开存储的文件，并将它定义为文件标识符f
    f.write(r.content)#将返回的内容写到这个文件中，r.content表示响应内容的二进制形式
    
f.close()#关闭文件，在d盘查看abc即为网上爬取下来的

#代码更新
import requests
import os
url = 'http://image.nationalgeographic.com.cn/2017/0331/20170331042952894.jpg'
root = 'D://pics//' #定义一个根目录
path = root + url.split('/')[-1]#将文件路径标识为根目录+网络文件名称
#截取最后一个/之后的内容，也就是.jpg之前的信息
try:
    if not os.path.exists(root):#判断根目录是否存在
        os.mkdir(root) #若不存在，则创建一个
    if not os.path.exists(path):#判断文件是否存在
        r = requests.get(url)#若不存在，则通过get方式在网上获取
        with open(path,'wb') as f:#打开文件，并定义为f
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
