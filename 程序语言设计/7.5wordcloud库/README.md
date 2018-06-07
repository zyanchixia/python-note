
'''wordcloud.WordCloud() 代表一个文本对应的词云
可根据文本中词语出现的频率等参数绘制词云

w = wordcloud.WordCloud()
方法：
1:w.generate(txt) :向WordCloud对象中加载文本txt
w.generate('python and WordClouod')
2:w.to_file(filename) :将词云输出为图像文件，.png或.jpg格式
w.to_file('outfile.png')
参数：
1：width:指定词云对象生成图片的宽度，默认400像素
w = wordcloud.WordCloud(width = 600)
2：height: 指定词云对象生成图片的高度，默认200像素
w=wordcloud.WordCloud(height=400)

配置对象参数：
1:min_font_size:指定词云中字体的最小字号，默认4号
w = wordcloud.WordCloud(min_font_size = 10)
2:max_font_size:指定词云中字体的最大字号，根据高度自动调节
w = wordcloud.WordCloud(max_font_size=20)
3:font_size:指定词云中字体字号的步进间隔，默认为1
w = wordcloud.WordCloud(font_step=2)
4:font_path:指定字体文件的路径，默认None
w = wordcloud.WordCloud(font_path='msyh.ttc')--微软雅黑
5:max_words:指定词云显示的最大单词数量，默认200
w = wordcloud.WordCloud(max_words=20)
6:stop_words:指定词云的排除词列表，即不显示的单词列表
w = wordcloud.WordCloud(stop_words={'python'})
7:mask:指定词云形状，默认为长方形，需要引用imread()函数
from scipy.misc import imread
mk = imread('pic.png')
w =  wordcloud.WordCloud(mask=mk)
8:background_color:指定词云图片的背景颜色，默认为黑色
w = wordcloud.WordCloud(background_color='white')


wordcloud库常规方法
步骤1：配置对象参数
步骤2：加载词云文本
步骤3：输出词云文件
'''
import wordcloud
c = wordcloud.WordCloud()
c.generate('wordcloud by python lalalala')
c.to_file('pywordcloud.png')
