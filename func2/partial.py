#coding=utf-8
#Æ«º¯Êý
import functools
int2 = functools.partial(int, base=2)
print(int2('1011'))
max2=functools.partial(max)
print(max2(4,5,10,-5))  