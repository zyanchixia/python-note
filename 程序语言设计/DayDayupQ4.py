#DayDayupQ4 工作日模式要努力到什么水平，才能和每天努力1%一样

def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1-0.01)
        else:
            dayup = dayup * (1+df)
    return dayup #工作日进步1%，双休日退步1%的结果
dayfactor = 0.01
dayup1 = pow(1.01,365) #每天进步1%的值
while dayup(dayfactor) < dayup1:
    dayfactor += 0.001

print('工作日的努力参数是:{:.3f}'.format(dayfactor))


