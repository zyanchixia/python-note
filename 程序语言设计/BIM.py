#多分支程序编写：注意条件之间的覆盖；程序可运行但不正确，要注意分支条件

height,weight = eval(input('请输入身高(cm）和体重(kg),用逗号隔开:'))
bim = weight/pow(height/100,2)#身高厘米转换成米
print('BIM数值为:{:.2f}'.format(bim))#结果保留两位小数

who,nat='',''#国际BIM值和国内BIM值初始值为空
if bim < 18.5:
    who,nat = '偏瘦','偏瘦'
    
elif 18.5<= bim < 24:
    who,nat = '正常','正常'
    
elif 24<= bim < 28:
    who,nat = '正常','偏胖'
    
elif 28<= bim < 30:
    who,nat = '偏胖','肥胖'
    
else:
    who,nat = '肥胖','肥胖'
print ("BIM指标为:国际'{0}',国内'{1}'".format(who,nat))
    
'''

分类    国际BIM值      国内BIM值
偏瘦    <18.5          <18.5
正常  18.5~25         18.5~24
偏胖   25~30           24~28
肥胖   >=30            >=28


'''
