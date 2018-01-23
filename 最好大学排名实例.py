#最好大学排名实例
#功能描述：输入：大学排名URL链接
#输出：大学排名信息的屏幕输出（排名，大学名称，总分等信息）
#技术路线：requests-bs4
#定向爬虫：仅对输入的URL进行爬取，不做扩展爬取
#查看robots协议 http://www.zuihaodaxue.cn/robots.txt
#程序结构设计
#步骤1：从网上获取最好大学排名网页内容  getHTMLText()
#步骤2：提取网页内容中信息并合适的数据结构  fillUnivList()
#步骤3：利用数据结构展示并输出结果  printUnivList()


import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout =30)#get函数获取url信息，并设定时间30秒
        r.raise_for_status()#判断产生异常信息
        r.encoding = r.apparent_encoding #修改编码
        return r.text#将网页信息内容返回给程序的其他部分
    except:
        return''
    
  #将一个html页面信息中关键数据放入一个list列表中
def fillUnivList(ulist,html):

    
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        #查找tbody标签，并将子节点做遍历
        #每一个tr就是一所大学对应的信息
        if isinstance (tr,bs4.element.Tag):#检测tr标签的类型，如果不是bs4库定义的
            #tag类型，就过滤掉
            tds = tr('td')
#对tr标签中的td标签做查询，将所有的td标签存为一个名为tds的列表类型
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
#在ulist中增加所需字段
            
#观察源代码可知，所有学校信息被封装在一个表格中，表格的标签为tbody，在tbody中
#每一个大学的信息又被封装在一个标签tr中，即每一个tr标签包含了当前所有大学信息
#每个tr标签中的信息又被td标签所包围
#所以要先找到tbody标签，获取所有大学的相关信息---然后tr标签获取每个大学的信息
#---然后每个td标签获取更详细的信息----用遍历和查找方法获得
#右键查看网页源代码可知跟每个学校相关的是使用tr标签来索引的一段信息
#可以看到我们需要的信息在里边都是可以得到的

def printUnivList(ulist,num):#num表示将列表中的多少个信息打印出来
    print('{:^10}\t{:^6}\t{:^10}\t{:^10}'.format('排名','学校名称','城市','总分'))
    for i in range(num):
        u = ulist[i]
        print('{:^10}\t{:^6}\t{:^10}\t{:^10}'.format(u[0],u[1],u[2],u[3]))
 #格式化输出：.format方法       

def main():
    uinfo = []#定义一个uinfo列表，将大学信息放在其中，设置为空
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url) #将url转换成html
    fillUnivList(uinfo,html) #将html信息提取后放在uinfo列表中
    printUnivList(uinfo,20)
main()

