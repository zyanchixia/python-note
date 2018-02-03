# 淘宝商品比价定向爬虫
#功能描述：目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格
#理解：1：淘宝的搜索接口，2：翻页处理
#技术路线：requests -re
#通过淘宝网页第一页与第二页与第三页等的对比可以看出，每页有44个商品
#定向爬虫可行性：http://s.taobao.com/robots.txt
#程序的设计结构：
#步骤1：提交商品搜索请求，循环获取页面
#步骤2：对于每个页面，提取商品名称和价格信息
#步骤3：将信息输出到屏幕上


import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('步骤1出错')
    
def parsePage(ilt,html):#一个结果的列表类型，一个相关的html信息
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#商品价格
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)#商品名称
#.*?最小匹配，匹配的是"raw_tital"作为键,""作为值的键值对,
#最小匹配表明取到最后一个""为止的内容,来约束匹配的内容就是商品本身的名称
        delt = re.findall(r'\"item_loc\"\:\".*?\"',html)#发货地
        salt = re.findall(r'\"view_sales\"\:\".*?\"',html) #付款人数
        nlt = re.findall(r'\"nick\"\:\".*?"',html)# 店铺名称
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#eval将获得字符串的最外层的""或''去掉
            title = eval(tlt[i].split(':')[1])#split用:来分割字符串,获得键值对的1部分
            delivery = eval(delt[i].split(':')[1])
            sales = eval(salt[i].split(':')[1])
            shoptitle = eval(nlt[i].split(':')[1])
            ilt.append([price,title,delivery,sales,shoptitle])
    except:
        print('解析出错')
#先#用split(':')方法将字符串以":"开割形成一个字符串数组
       # 然后再通过索引[1]取出所得数组中的第二个元素的值
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t{:32}\t{:4}\t{:64}"
    #{}定义槽函数,第一个位置长度为4,第二个位置长度为8....
    print(tplt.format('序号','价格','商品名称','发货地','付款人数','店铺名称'))
    count = 0 #定义输出信息的接收器，表示序号
    for g in ilt:
        count = count +1
        print(tplt.format(count,g[0],g[1],g[2],g[3],g[4]))
        
def main():
    goods = '进口蓝莓'
    depth = 1 #向下一页爬取的深度
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' +str(44*i)#每页44个商品
            #查看每页的url链接可找到规律,每个页面起始以&s开头
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
    
main()

            
      # delt = re.findall(r'\"item_loc\"\:\".*?\"',html)#发货地
       # salt = re.findall(r'\"view_sales\"\:\"[\d\]*\"',html) #付款人数
        #    delivery = eval(delt[i].split(':')[1])
        #    sales = eval(salt[i].split(':')[1])
         #tplt = "{:4}\t{:8}\t{:16}\t{:32}\t{:64}\t{:128}"
