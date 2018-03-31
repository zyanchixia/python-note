# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:25:42 2018

"""
import math

def isprime(n): #判断是否为素数
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n % i ==0:
            return False
    return True

def prime(n):
    if n == 1:
        return 2
    k = 1
    i = 1
    while (k<n):
        i+=2
        if isprime(i)==True:
            k+=1
    return i

def monisen(no):
    k=0
    i=1
    t=0
    while(k<no):
        t=prime(i)#t是第i个素数
        if isprime(2**t-1) == True:
            k+=1 #如果2**t-1也是素数
        i+=1
    return 2**t-1#跳出while循环时,k==num,直接输出2**t-1的值，即为第no个默尼森数

print(monisen(4))
        
            
