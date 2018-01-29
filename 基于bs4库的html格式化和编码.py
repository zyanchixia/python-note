#基于bs4库的html格式化和编码
import requests
url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
soup.prettify()#给html的文本，标签，内容增加换行符，也可以为每个标签做处理
'<html>\n <head>\n  <title>\n   This is a python demo page\n
</title>\n </head>\n <body>\n  <p class="title">\n   <b>\n
The demo python introduces several python courses.\n   </b>\n
</p>\n  <p class="course">\n   Python is a wonderful general-purpose
programming language. You can learn Python from novice to professional
by tracking the following courses:\n   <a class="py1"
href="http://www.icourse163.org/course/BIT-268001" id="link1">\n
Basic Python\n   </a>\n   and\n   <a class="py2"
href="http://www.icourse163.org/course/BIT-1001870001" id="link2">\n
Advanced Python\n   </a>\n   .\n  </p>\n </body>\n</html>'
#bs4库的prettify()方法
#.prettify()为HTML文本<>及其内容增加更加'\n'
#.prettify()可用于标签，方法：<tag>.prettify()
