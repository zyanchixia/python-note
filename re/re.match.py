
#match对象介绍：Match对象是一次匹配的结果，包含匹配的很多信息
>>> match = regex.search('bit 100081')
>>> if match:
	print(match.group(0))

	
100081
>>> type(match)
<class '_sre.SRE_Match'>
#match对象的属性
'''
属性说明
.string待匹配的文本
.re匹配时使用的patter对象（正则表达式）
.pos正则表达式搜索文本的开始位置
.endpos正则表达式搜索文本的结束位置

match对象的方法：
.group(0) 获得匹配后的字符串
.start() 匹配字符串在原始字符串的开始位置
.end() 匹配字符串在原始字符串的结束位置
.span() 返回(.start(), .end())

'''
>>> import re
>>> regex = re.compile(r'[1-9]\d{5}')#将正则表达式的字符串形式编译成正则表达式对象
>>> m = regex.search('bit100081 bin299981')
>>> m.string #匹配文本
'bit100081 bin299981'
>>> m.re #匹配正则表达式
re.compile('[1-9]\\d{5}') #系统认为只有通过compile之后的才是正则表达式
>>> m.pos #正则表达式搜索文本的开始位置
0
>>> m.endpos #正则表达式搜索文本的结束位置
19
>>> m.group(0)#获得匹配后的字符串
'100081'
>>> m.start()#匹配字符串在原始字符串的开始位置
3
>>> m.end()#匹配字符串在原始字符串的结束位置
9
>>> m.span()#返回（.start()  .end())
(3, 9)


