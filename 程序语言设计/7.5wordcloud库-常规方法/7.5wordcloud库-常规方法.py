'''wordcloud.WordCloud() 代表一个文本对应的词云
可根据文本中词语出现的频率等参数绘制词云
w = wordcloud.WordCloud()
1:w.generate(txt) :向WordCloud对象中加载文本txt
w.generate('python and WordClouod')
2:w.to_file(filename) :将词云输出为图像文件，.png或.jpg格式
w.to_file('outfile.png')

wordcloud库常规方法
步骤1：配置对象参数
步骤2：加载词云文本
步骤3：输出词云文件
'''
import wordcloud
c = wordcloud.WordCloud()
c.generate('wordcloud by python lalalala')
c.to_file('pywordcloud.png')

'''
1：分割：以空格分隔单词
2: 统计：单词出现的次数并过滤掉太短的单词
3：字体：根据统计配置字号
4：布局：颜色环境尺寸
'''
