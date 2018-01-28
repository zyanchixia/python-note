#基于bs4库的html内容遍历方法：下行遍历，上行遍历，平行遍历
#标签树的下行遍历：
#.contents 子节点的列表，将<tag>所有儿子节点存入列表
#.children 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
#.descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
#BeautifulSoup类型是标签树的根节点

>>> import requests
>>> r = requests.get('http://python123.io/ws/demo.html')
>>> demo = r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p
class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p
class="course">Python is a wonderful general-purpose programming language. You
can learn Python from novice to professional by tracking the following
courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1"
id="link1">Basic Python</a> and <a href="http://www.icourse163.org
/course/BIT-1001870001" class="py2"
id="link2">Advanced Python</a>.</p>\r\n</body></html>'
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo,'html.parser')
>>> soup.head#获取soup的head标签
<head><title>This is a python demo page</title></head>
>>> soup.head.contents#head标签的子节点
[<title>This is a python demo page</title>]
>>> soup.body.contents#body标签的子节点，对于一个标签的儿子节点并不仅仅包括
#标签节点，也包括字符串节点
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
>>> len(soup.body.contents)#获取儿子节点的数量
5
>>> soup.body.contents[1]#检索第二个相关节点
<p class="title"><b>The demo python introduces several python courses.</b></p>

>>> for child in soup.body.children:
	print(child)#遍历儿子节点

>>> for child in soup.body.descendants:
	print(child) #遍历子孙节点
	

#标签树的上行遍历
#.parent节点的父亲标签
#.parents节点先辈标签的迭代类型，用于循环遍历先辈节点

soup = BeautifulSoup (demo,'html.parser')
>>> soup.title.parent #遍历title的父亲标签
<head><title>This is a python demo page</title></head>
>>> soup.html.parent#遍历html的父亲标签，是最高级的，所以是它本身
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
>>> soup.parent#无结果，表明为空

soup = BeautifulSoup (demo,'html.parser')
for parent in soup.a.parrents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
p
body
html
[document]
#遍历所有先辈节点，包括soup本身，所以要区别判断




#标签树的平行遍历：必须发生在同一个父节点下的各个节点之间
#平行标签获得的不一定是标签类型，所以需要做判断
#如下：

#.next_sibling返回按照HTML文本顺序的下一个平行节点标签
#.previous_sibling返回按照HTML文本顺序的上一个平行节点标签
#.next_siblings迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
#.previous_siblings迭代类型，返回按照HTML文本顺序的前续所有平行节点标签

for sibiling in soup.a.next_sibilings:# 遍历后续节点
	print(sibiling)


for sibiling in soup.a.previous_sibilings: #遍历前续节点
	print(sibiling)



