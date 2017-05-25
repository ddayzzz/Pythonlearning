#coding=utf-8
class Student(object):
    def score(self):
        return self._score
    def set_score(self,sc):
        if sc>100:
            print('Too high')
        elif sc <0 :
            print('Too low')
        else:
            self._score=sc
s=Student()
s.set_score(55)
s.set_score(-8)