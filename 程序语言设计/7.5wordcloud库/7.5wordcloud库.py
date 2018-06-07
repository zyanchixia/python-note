#wordcloud应用实例 之英文

import wordcloud
txt = 'life is short,you need python'
w =wordcloud.WordCloud(background_color = 'white')
w.generate(txt)
w.to_file('pywcloud.png')



#wordcloud应用实例 之中文
import jieba
import wordcloud
txt = '程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\动进行各种运算处理。'
w = wordcloud.WordCloud(width=1000,\
                        font_path='msyh.ttc',height=700)
w.generate(' '.join(jieba.lcut(txt)))
#先分词，再用空格关联词语后赋值给wordcloud
w.to_file('cpywcloud.png')
