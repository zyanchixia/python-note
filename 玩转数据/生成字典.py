#根据如下数据：在以下现有数据中生成字典

'''想得到以下字典，将plist中的每个元素的二级元素分别取出

{'AXP': '86.40', 'BA': '122.64', 'CVX': '115.91',
'CAT': '99.44', 'CSCO': '23.78'}
'''

pList = [('AXP', 'American Express Company', '86.40'),
      ('BA', 'The Boeing Company', '122.64'),
      ('CAT', 'Caterpillar Inc.', '99.44'),
      ('CSCO', 'Cisco Systems,Inc.', '23.78'),
      ('CVX', 'Chevron Corporation', '115.91')]
      

aList = []
bList = []
for i in range (5):#遍历元素
    aStr = pList[i][0]#取二级元素
    bStr = pList[i][2]#取二级元素
    aList.append(aStr)
    bList.append(bStr)
aDict = dict(zip(aList,bList))
print(aDict)
         
'''
zip将两个列表对应的元素分别组合起来
dict将组合成组的数据转成字典
