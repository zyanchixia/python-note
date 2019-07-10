import requests
import re
import jieba
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
#在显示窗口移除InsecureRequestWarning信息
from requests.packages.urllib3.exceptions import InsecureRequestWaring
requests.packages.urllib3.disable_warings(InsecureRequestWarning)


def get_page(page):
    url = r'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv271779&productId=1135611&score=0&sortType=5&page='
    res = requests.get(
