#coding=utf-8
#slot
class Animal(object):
    __slots__=('age','typ')
    def run(self):
        print('Animal is running')
    
a1=Animal()
a2=Animal()
from types import MethodType
def set_age(self,age):
    self.age=age
"""
a1.set_age=MethodType(set_age,a1)
a1.set_age(222)
"""
Animal.set_age=set_age
a1.set_age(88)
a2.set_age(99)
print(a1.age)
print(a2.age)
