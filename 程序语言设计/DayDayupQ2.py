
#DayDayupQ2:每天进步(退步)5‰ 和 1% 的结果呢

dayfactor =0.005 #使用变量的方便性
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print('向上:{:.2f},向下:{:.2f}'.format(dayup,daydown))
