#信息标记与提取方式：XML,JSON,YAML


#XML：
#<name> … </name> 有内容的正常书写形式
#<name /> 无内容空元素的缩写形式
#<!‐‐‐‐> 注释的书写形式

#JSON：有类型的键值对的 key:value，增加双引号
#“key”:“value” 有类型的键值组织起来
#“key”:[“value1”,“value2”]如果值多，就用逗号，中括号
#“key”:{“subkey”:“subvalue”}新的键值对作为值的一部分，放在键值对中，用大括号来嵌套

#YAML  无类型键值对 key:value ，无双引号形式，
#缩进表达所属关系，减号-表示并列关系，|表达整块数据，#表示注释
#key :value 无类型的键值对，没有双引号
#key :#Comment 表注释
#‐value1 表并列
#‐value2 
#key : 键值对之间可以嵌套，所属关系
 #   subkey:subvalue 


#XML  最早的通用信息标记语言，可扩展性好，但繁琐；Internet上的信息交互与传递
 
#JSON 信息有类型，适合程序处理(js)，较XML简洁；移动应用云端和节点的信息通信，无注释

#YAML 信息无类型，文本信息比例最高，可读性好；各类系统的配置文件，有注释易读


#实例：提取HTML中所有URL链接
#思路：1) 搜索到所有<a>标签 2)解析<a>标签格式，提取href后的链接内容

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
for link in soup.find_all('a'):#找到所有的a标签
    print(link.get('href')) #标签的 href 属性用于指定超链接目标的 URL
    
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001

#基于bs4库的html内容查找方法：

#find_all(name,attrs,recursive, string, **kwargs)
#返回一个列表类型，存储查找的结果
#1：∙ name:对标签名称的检索字符串
soup.find_all('a')#返回列表类型，所有a标签

soup.find_all(['a','b']) #返回的是一个列表类型，所有a b标签

for tag in soup.find_all(True):
	print(tag.name)  #返回所有标签信息

import re #正则表达式库
for tag in soup.find_all(re.compile('b')):
    print(tag.name)# 只显示以b开头的所有信息
#2：attrs：对标签属性值的检索字符串，可标注属性检索
     soup.find_all('p','course')#查找所有p标签的包含course字符串的信息，返回字符串类型
     soup.find_all(id = 'link1')#直接标注属性检索，查找id=link1的值为查找元素的
     soup.find_all(id = 'link')#并没有一个id属性为link的标签，但有link1的
     #所以要引入正则表达式进行模糊查找
>>> import re
>>> soup.find_all(id = re.compile('link'))
#3:∙recursive:是否对子孙全部检索，默认True,布尔型值
>>> soup.find_all('a') #查找a标签返回2个结果
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001"
 id="link1">Basic Python</a>, <a class="py2"
 href="http://www.icourse163.org/course/BIT-1001870001"
 id="link2">Advanced Python</a>]

soup.find_all('a',recursive=False)
[]#查找a标签当下儿子节点时，可以赋值recursive为false，返回值为空，
#说明儿子节点中没有a标签，a标签或许在其他子孙节点中

#4：∙string: <>…</>中字符串区域的检索字符串

>>> soup.find_all(string = 'Basic Python')
['Basic Python']#精确查找字符串

#利用正则表达式模糊查找带有某个字符串的信息
>>> import re
>>> soup.find_all(string = re.compile('python'))
['This is a python demo page',
 'The demo python introduces several python courses.']

#扩展方法，简化
<tag>(..) 等价于<tag>.find_all(..)
soup(..) 等价于soup.find_all(..)
