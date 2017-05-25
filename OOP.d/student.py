#coding=utf-8
#OOP
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('Selfid:%s Name:%s Score:%d' %(id(self),self.__name,self.__score))
    def printage(self):
        print(self.age)
b=Student('Shu',88)
c=Student('Shu',88)
c.print_score()
b.print_score()
b.age=55#居然可以独立的添加变量 但是不能添加私有的变量
c.age=555
b.printage()
c.printage()