#已知有员工姓名和工资信息表，如何单独输出员工姓名和工资金额
aInfo = {'Wangdachui':3000,'Niuyun':2000,'Linling':4500,'Tianqi':8000}
#names = aInfo.keys()
#salary = aInfo.values()
for k,v in aInfo.items():#item把字典中每对键和值组成一个元祖
    print(k,v)
