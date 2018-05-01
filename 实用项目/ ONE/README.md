# python-note

ONE主要内容是每日一句话,一幅图片,一篇文章,一个问题
目标:爬取ONE往期所有的每日一句,并保存下来
思路:
  1.由于是所有的往期,所以要先确定每期页面的url的规律 
  2.查看页面源代码,确定要爬取内容的位置 
  3.写爬虫程序,爬取内容并保存

1.确定URL规律 
  要爬取页面中的三个关键部分：URL,期次,每日一句
观察URL,每一期的URL公共部分是http://wufazhuce.com/one/,
期次不同,后边跟的数字不同,可测,根据规则可知
URL = http://wufazhuce.com/one/+num（num范围是14-2043）,到2018年4月11号的
2.右键--查看源代码,定位目标
期次和每日一句所在的标签分别是****class属性为“one-titulo”和”fp-one-cita”的div

3.写爬虫程序
  开发工具和开发环境,IDE：Windows,Python3+,Spyder；
  技术路线:requests---BeautifulSoup---re
