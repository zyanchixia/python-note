#RE库的基本使用

#re.search(pattern,string,flags=0)
#re.search 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象

import re
match = re.search(r'[1-9]\d{5}','bit 100081')#定义match变量
if match:
    print(match.group(0))
 #返回的结果   100081

    
#re.match()从一个字符串的开始位置起匹配正则表达式，返回match对象
    #re.match(pattern,string,flags=0)
import re
match  = re.match(r'[1-9]\d{5}','100081 bit')
if match:
    print(match.group(0))
 #返回的结果   '100081' ----要注意起始位置与正则表达式是一致的，否则为空

   
#re.findall()搜索字符串，以列表类型返回全部能匹配的子串
    #re.findall(pattern,string,flags=0)
import re
ls = re.findall(r'[1-9]\d{5}','bit100081 fin2900012')
ls
#返回结果['100081', '2900012'] 全部能匹配到的信息


#re.split()将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
 #re.split(pattern,string,maxsplit=0,flags=0)
#maxsplit: 大分割数，剩余部分作为后一个元素输出
re.split(r'[1-9]\d{5}','bit100081 fin290009')
#返回结果 ['bit', ' fin', ''] 默认全部分割
re.split(r'[1-9]\d{5}','bit100081 fin290009 jia272415',maxsplit = 1)

#返回结果['bit', ' fin290009 jia272415'] #只分割了第一个，剩下的部分还是完整的


#re.finditer()搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
#re.finditer(pattern,string,flags=0) 适合用在 for循环中
for m  in re.finditer(r'[1-9]\d{5}','bit100081 fin290021'):
	if m :
		print(m.group(0))

#返回结果，返回的是迭代类型，适合用在for循环中		
#100081
#290021

#re.sub()在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
#re.sub(pattern,repl, string,count=0,flags=0)
re.sub(r'[1-9]\d{5}',':zipcode','bit100081 fin290012 hun123453',count=2)
#'bit:zipcode fin:zipcode hun123453'  替换所有符合的，count是最大替换次数
∙ pattern : 正则表达式的字符串或原生字符串表示
∙ repl: 替换匹配字符串的字符串
∙ string : 待匹配字符串
∙ count : 匹配的大替换次数
∙ flags : 正则表达式使用时的控制标记


#re库的另一种等价方法
regex=re.compile(r'[1‐9]\d{5}') #编译后可多次操作
a = regex.search('bit100081 fin100089') #直接写内容了
if a :
    print(a.group(0))

100081


