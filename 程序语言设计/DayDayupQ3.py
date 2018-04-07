
#DayDayupQ3 工作日的力量

dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:#每周7天，余数为6或0时表示双休日
        dayup = dayup*(1-dayfactor)#双休日退步1%
    else:
        dayup = dayup*(1+dayfactor)#工作日进步1%
print('工作日的力量:{:.2f}'.format(dayup))
        
