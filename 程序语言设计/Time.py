
'''
时间获取:
time()  #获取当前时间戳，即计算机内部时间值，浮点数
ctime()  #获取当前时间并以易读方式表示，返回字符串
gmtime() #获取当前时间，表示计算机可处理的时间格式
'''

import time

time.time()
#1523106574.2408912

time.ctime()
#'Sat Apr  7 21:09:57 2018'

time.gmtime()
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=7, tm_hour=13,
                 tm_min=15, tm_sec=31, tm_wday=5, tm_yday=97, tm_isdst=0)

'''
时间格式化:strftime(tpl,ts):tpl是格式化模板字符串，用来定义输出效果
                            ts是计算机内部时间类型变量
strptime(str,tpl):str 是字符串形式的时间值
                  tpl是格式化模板字符串，用来定义输入效果
'''
t = time.gmtime()
time.strftime('%Y-%m-%d %H:%M:%S',t)
#输出结果  '2018-04-07 13:20:32'


timeStr = '2018-04-07 13:20:32'
time.strptime(timeStr,'%Y-%m-%d %H:%M:%S')
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=7, tm_hour=13, tm_min=20,
                 tm_sec=32, tm_wday=5, tm_yday=97, tm_isdst=-1)


'''
程序计时:是指测量起止动作所经历时间的过程
sleep(a)产生时间,s拟休眠的时间，单位秒，可以是浮点数

perf_counter() 测量时间，返回一个cpu级别的精确时间计数值，单位为秒
由于这个计数值起点不确定，连续调用差值才有意义

'''
start = time.perf_counter()
end = time.perf_counter()
end-start
#输出结果 26.444938623020814


def wait():
	time.sleep(3.3)

	
wait()#程序将等待3.3秒后再退出

