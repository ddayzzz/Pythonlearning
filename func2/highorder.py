#coding=utf-8
import math
import functools 
def lis(num,*funcs):
    li=[func(num) for func in funcs]
    return li
print(lis(-5,abs,math.sin))
#map/reduce
def s(a,b):
    return a+b
print(functools.reduce(s,[3,6,9,6]))
print(list(map(str,[1,2,3,5])))
#可以将字符串变为数字
def char2num(c):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
def num2int(d,d1):
    return d *10 +d1
print(functools.reduce(num2int,[1, 3, 5, 7, 9]))
print(functools.reduce(num2int,map(char2num,'55663')))#可以将字符串转换为数字
#浮点数的转换
def num2xiaoshu(d,d1):
    return d*0.1+d1
s='55663.3558'
zheng=s[:s.index('.')]
xiao=s[s.index('.')+1:][::-1]
print(functools.reduce(num2int,map(char2num,zheng))+functools.reduce(num2xiaoshu,map(char2num,xiao)) /10.0)#可以将字符串转换为数字



