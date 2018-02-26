#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

#解法0：根据题意，直接写出过程并打印出结果
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j and j != k and i != k):
                print(i,j,k)
'''


#解法1：指出三位数的数量，添加无重复三位数的数量
'''
d = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (b!=c) and (a!=c):
                d.append([a,b,c])
print("总数量:",len(d))

print (d)
'''


#解法2：将for循环和if语句综合成一句，直接打印出结果
'''
list_num = [1,2,3,4]
list = [i *100+ j *10 +k for i in list_num for j in list_num for k in list_num if(j != k and  i!=k and j!=i)]
print (list)
                        
'''
#解法3：用python自带函数permutations
'''
from itertools import permutations
for i in permutations([1,2,3,4],3):
    print(i)
'''

#解法4：对解法3的补充,执行结果好像不对
'''
from itertools import permutations
for i in permutations([1,2,3,4],3):
    k =''
    for j in range(0,len(i)):
        k = k +str(i[j])
print(int(k))
'''
#解法5：
'''
num = [1,2,3,4]
i = 0
for a in num:
    for b in num:
        for c in num:
            if(a!=b and a!=c and b!=c):
                i +=1
                print(a,b,c)
print('总数是:',i)
'''
#解法6：考虑减少冗余判断和循环，做出以下优化
'''
for i in range(1,5):
    for j in range(1,5):
        if (j ==i):
            continue;
        for k in range(1,5):
            if (k==i or k ==j):
                continue;
            print(i,j,k)
'''
