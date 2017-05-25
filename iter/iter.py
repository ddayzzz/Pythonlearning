#coding=utf-8
#迭代的使用
dic={'haha':'6','sb':'250'}
for i in dic.items():
    print(i)
#判断是否是迭代类型
import collections
from collections import Iterable
print(str(isinstance(5535,Iterable)))
lis=['a','b','c']
for i in enumerate(lis):
    print(i)
lis2=[('a','A'),('b','B')]
for l1,l2 in lis2:
    print(l1+':'+l2)
