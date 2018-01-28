# BeautifulSoup 库
#安装： win平台，以管理员身份运行cmd，执行 pip install beautifulsoup4即可
#安装测试：演示html地址：http:python123.io/ws/demo.html，文件名：demo.html
#手工获取：浏览器右键，查看源代码
#requests库获取
import requests
url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
print(r.text)

demo = r.text #  即可获得

#1：Tag标签
#标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾

from bs4 import BeautifulSoup #从bs4库导入一个叫做BeautifulSoup的类
soup = BeautifulSoup(demo,'html.parser')#对demo的html的解析
#soup变量代表了解析后的demo页面
print(soup.prettify())
      
soup.title#title是页面在浏览器左上角的显示信息位置的地方
tag = soup.a
#定义一个tag变量获取页面中.a标签，也就是链接标签的内容
tag
#任何存在于HTML语法中的标签都可以用soup.<tag>访问获得
#当HTML文档中存在多个相同<tag>对应内容时，soup.<tag>返回第一个

#2：Tag的name（名字）
#标签的名字，<p>…</p>的名字是'p'，格式：<tag>.name

#获取标签的名字
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
soup.a.name #即可获得a标签的名字
soup.a.parent.name#a标签父标签的名字
soup.a.parent.parent.name #a标签父标签的父标签的名字

#3：Tag的attrs（属性）
#标签的属性，字典形式组织，格式：<tag>.attrs

tag = soup.a
tag.attrs#获取标签的属性
{'href': 'http://www.icourse163.org/course/BIT-268001',
 'class': ['py1'], 'id': 'link1'}
#打印出一个字典，给出了标签属性中标签名字，属性名字，属性的值之间的对应关系
tag.attrs['class']#获取class属性的值
['py1']#是一个列表类型，列表类型中的第一个值是py1
tag.attrs['href']#获取a标签的链接属性
'http://www.icourse163.org/course/BIT-268001'#这是一个课程链接地址
type(tag.attrs)#标签属性的类型
<class 'dict'>#字典类型
type(tag) #标签的类型
<class 'bs4.element.Tag'> #标签类型
#一个tag可以有0个或者多个属性，字典类型


#4：Tag的NavigableString
#基本元素
#NavigableString
#说明：标签内非属性字符串，<>…</>中字符串，格式：<tag>.string

soup.a #/获取a标签的信息
<a class="py1" href="http://www.icourse163.org/course/BIT-268001"
id="link1">Basic Python</a>
soup.a.string#a的字符串信息
'Basic Python'
>>> soup.p
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>> soup.p.string
'The demo python introduces several python courses.'
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>

#5：Tag的Comment
#说明：标签内字符串的注释部分，一种特殊的Comment类型
newsoup = BeautifulSoup('<b><!--this is a comment--></b><p>thin is not a comment</p>','html.parser')
            #<!表示一个注释的开始，b标签是一个注释类型，p不是
>>> newsoup.b.string
'this is a comment'
>>> type(newsoup.b.string)
<class 'bs4.element.Comment'>
>>> newsoup.p.string
'thin is not a comment'
>>> type(newsoup.p.string)
<class 'bs4.element.NavigableString'>
