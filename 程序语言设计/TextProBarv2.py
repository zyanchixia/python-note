#TextProBarv2 文本进度条单行进度刷新
'''
刷新的本质：用后打印的字符覆盖之前的字符
不能换行：print()需要被控制
要能回退:打印后光标退回到之前的位置\r
'''

import time
for i in range(101):# 0%到100%
    print('\r{:3}%'.format(i),end = '')
    #\r 默认表示将输出的内容返回到第一个指针,这样的话，后面的内容会覆盖前面的内容
    #end = ''不换行
    time.sleep(0.1)
