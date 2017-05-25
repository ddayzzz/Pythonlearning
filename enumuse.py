#coding=utf-8
#枚举类型
from enum import Enum,unique
Animal = Enum('Animal', {'ANT':2,'HJ':3},module=__name__)#创建一个枚举Animal 包含ANT BEE。。。
print(Animal.ANT==1)
@unique #不允许有重复值
class Job(Enum):#使用类 继承自Enum
    COOK=1
    DRIVER=2
print(Job)#<enum 'Job'>
print(Job.COOK)
#迭代
print(list(Animal))
for name,member in Animal.__members__.items():
    print(name,'->',member,':',member.value)#获取枚举的信息
""" 输出的信息
ANT -> Animal.ANT : 2
HJ -> Animal.HJ : 3
"""
print(Animal is not Job)#True
print(Animal.ANT==Job.DRIVER)#False
#使用值访问
print(Animal(3))
print(Animal['HJ'])
print(Animal.HJ > Animal.ANT)