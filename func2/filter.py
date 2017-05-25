#coding=gb2312
#筛选器：
#筛选出奇数列表
def isodd(u):
    return u % 2==1
print(list(filter(isodd,[7,5,3,6,9])))
#埃拉托色尼筛选法求素数：(不会)
import math
def filter_div(n):
    for i in range(2,math.sqrt(n)):
        if n % i:
            return False
    return True
def filter_prime():
   res=[]

