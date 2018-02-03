'''
包含yield语句的函数是一个生成器
生成器每次产生一个值(yield语句)，然后函数被冻结，被唤醒后再产生一个值
生成器是一个不断产生值的函数

'''
#生成器写法
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    print(i,"",end ="")



#普通写法

def square(n):
    ls = [i**2 for i in range(n)]
    return ls

for i in square(5):
    print(i,"",end='')



#生成器优势：1）更节省存储空间 2）响应更迅速 3）使用更灵活
    
