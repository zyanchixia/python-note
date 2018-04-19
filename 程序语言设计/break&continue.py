#循环控制保留字

s = 'PYTHON'
while s != '':
    for c in s:
        print(c,end='')
    s = s[:-1]
    
#结果  PYTHONPYTHOPYTHPYTPYP

'''
双层循环：
在外层循环中，s!='',每次执行完将s切片的最后一个字符去掉
内层循环:当s!=''时，将s中每个字符打印出来
'''

s = 'PYTHON'
while s != '':
    for c in s:
        if c =='T':
            break #当c==T时，仅跳出最内层循环
        print(c,end = '')
    s = s [:-1]
#结果 PYPYPYPYPYP
