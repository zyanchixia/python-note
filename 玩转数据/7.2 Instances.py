#7.2 面向对象实例 Instances
class Dog(object):
    def greet(self):
        print('HI')
        
dog = Dog
dog.greet()

'''
实例的创建----通过调用类对象
1.定义类---Dog
2.定义一个实例----dog
3.通过实例使用属性或方法----dog.greet
'''
