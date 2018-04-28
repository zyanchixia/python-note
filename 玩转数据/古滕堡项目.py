path= '英文版《暮光之城》1-5小说全集.txt'

from nltk.corpus import gutenberg
allwords = gutenberg.words(path)
#将文档中所有字符，包含标点符号，全部放入allwords中
len(allwords) #计算长度
len(set(allwords)) #计算不重复的单词和标点符号个数
allwords.count('Bella') #计算bella出现的次数

A=set(allwords)
longwords = [w for w in A if len(w) >12]
#单词长度大于12的单词
print(sorted(longwords))
#对这些单词进行排序
