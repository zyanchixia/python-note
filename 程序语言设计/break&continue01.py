#一个栗子看break和continue之间的差异

for c in 'PYTHON':
    if c == 'T':
        continue #当遇到T则跳过并继续执行语句
    print(c,end='')
else:
    print('正常退出')
    
#输出结果：PYHON正常退出

    
for c in 'PYTHON':
    if c == 'T':
        break #当遇到T则退出程序
    print(c,end = '')
else:
    print('正常退出')
    
#输出结果：PY
