import jieba
import wordcloud

f = open(鹿鼎记.txt','r',encoding='gb18030')
#文本中出现的一些特殊符号超出了gbk的编码范围，可以选择编码范围更广的‘gb18030’
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='msyh.ttc',\
                        width=1000,height=700,background_color='white',\
                        )
w.generate(txt)
w.to_file('ludj.png')
