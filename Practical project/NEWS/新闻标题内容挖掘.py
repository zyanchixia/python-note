

#爬取新浪新闻标题，将时间，标题，网址链接保存至本地，并形成词云保存

import requests,time
from bs4 import BeautifulSoup
from  wordcloud import  WordCloud
import matplotlib.pyplot as plt

def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding #中文
        return r.text #获取其text文本
    except:
        return '第一步出错'
'''
右键查看源代码，所需数据保存在  
<div class="news-item first-news-item img-news-item"> 的<h2>标签中
print(h2)
可以看到所需内容
[<h2><a href="http://news.sina.com.cn/c/xl/2018-05-14/doc-ihapkuvk7011058.shtml"
suda-uatrack="key=newschina_index_2014&amp;value=news_link_1"
target="_blank">汪洋:委员积极资政建言是对共产党领导负责的表现</a></h2>]
'''
def getContent(url):
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'html.parser')#解析
    for news in soup.select('.news-item'):
        h2 = news.select('h2')
        if len(h2)>0: #h2长度大于0
            time = news.select('.time')[0].text #找到时间，获取其text文本
            title = h2[0].text #标题
            href = h2[0].select ('a')[0]['href']#网址
            print(time,title,href)                          
    #将爬取数据写入文件
        with open ('tt.txt','a',encoding='utf-8') as f:
            f.write('新闻标题:%s\n时间:%s\n链接地址:%s\n'%(time,title,href))


def main():
    url = r'http://news.sina.com.cn/china/' #url链接地址
    getContent(url)
    
main()

#最后词云也要封包，时间来不及了，先提交了作业，后续会跟进
dd = open('tt.txt','r', encoding='UTF-8').read()
wordcloud = WordCloud(background_color='white',width=1000,height=860,margin=2).generate(dd)
#规范画布底色大小高度
plt.show(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('text.png')    
