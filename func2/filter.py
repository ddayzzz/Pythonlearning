#coding=gb2312
#ɸѡ����
#ɸѡ�������б�
def isodd(u):
    return u % 2==1
print(list(filter(isodd,[7,5,3,6,9])))
#������ɫ��ɸѡ����������(����)
import math
def filter_div(n):
    for i in range(2,math.sqrt(n)):
        if n % i:
            return False
    return True
def filter_prime():
   res=[]

