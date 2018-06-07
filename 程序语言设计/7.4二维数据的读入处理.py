#二维数据的读入处理
#从csv格式的文件中读入数据
fo = open(fname)
ls = []
for line in fo:
    line = line.replace('\n','')
    ls.append(line.split('.'))

fo.close()





#将数据写入csv格式的文件
ls = [[],[],[]] #二维列表
f = open(fname,'w')
for item in ls:
    f.write(','.join(item) + '\n')

f.close()
