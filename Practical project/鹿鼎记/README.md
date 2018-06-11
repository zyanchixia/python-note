# python-ludj

鹿鼎记是最喜欢的金庸小说之一了，每个人看似没有特点，却又深藏大智慧                                                                

目标:将鹿鼎记做成词云图，看看在讲什么  

遇到问题：
UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 11126: illegal multibyte sequence         
                                                             
解决方法：
使用python的时候经常会遇到文本的编码与解码问题，其中很常见的一种解码错误如题目所示，下面介绍该错误的解决方法，将‘gbk’换成‘utf-8’也适用。 
（1）、首先在打开文本的时候，设置其编码格式，如：open(‘1.txt’,encoding=’gbk’)； 
（2）、若（1）不能解决，可能是文本中出现的一些特殊符号超出了gbk的编码范围，可以选择编码范围更广的‘gb18030’，如：open(‘1.txt’,encoding=’gb18030’)； 
（3）、若（2）仍不能解决，说明文中出现了连‘gb18030’也无法编码的字符，可以使用‘ignore’属性进行忽略，如：open(‘1.txt’,encoding=’gb18030’，errors=‘ignore’)； 
（4）、还有一种常见解决方法为open(‘1.txt’).read().decode(‘gb18030’,’ignore’)
                                                              

