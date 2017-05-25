#coding=utf-8
#继承与多态
class Animal(object):
    def run(self):
        print('Animal is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')
class Dog(object):
    def run(self):
        print('Dog is running')
class LikeDuck(object):
    def run(self):
        print('I am a duck! Hahaha')
def pp(an):
    an.run()
a=Animal()
c=Cat()
d=Dog()
du=LikeDuck()
pp(a)
pp(c)
pp(d)
pp(du)
#类型判断 isinstance
print(isinstance(du,LikeDuck))
print(dir(str))
gh=getattr(du,'run',401)
gh()

