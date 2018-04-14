'''统计句子中的词频次数
题目内容：
用字典编写程序统计某个已分词的句子中词频次数
程序参考框架
def countfeq(s):
   ... ...
   return a dict
if __name__ == "__main__":
   s = input()
   ... ...
   s_dict = countfeq(s)
   print(len(s_dict.keys()))
'''


def countfeq(s):
    list = s.split('/')#以/为分界
    [list.remove(item) for item in list if item in ',.!):']
    #remove() 函数用于移除列表中某个值的第一个匹配项
    dict={}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return  dict
if __name__ == '__main__':
    s = input()
    s_dict = countfeq(s)
    print(len(s_dict.keys()))

