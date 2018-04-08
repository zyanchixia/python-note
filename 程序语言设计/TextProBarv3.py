##TextProBarv3 文本进度条完整效果
import time
scale = 50
print('执行开始'.center(scale//2,'-'))#将-填充在"执行开始"字符串的两侧
start = time.perf_counter()#增加计时效果,开始时间
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start#记录每一次需要打印文本进度条时所用的时间
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end = '')
    #3.0表示输出格式为3位数据，小数点后0位,
    #时间 {:.2f}s 时间小数点后2位；end =''不换行
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,'-'))
#\n  回车，光标在下一行
