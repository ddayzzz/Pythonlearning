#coding=utf-8
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,sc):
        if sc>100:
            print('Too high')
        elif sc <0 :
            print('Too low')
        else:
            self._score=sc
s=Student()
s.score=10
#print(s.score)
#pratice
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,w):
        if w<0:
            raise ValueType('negative width')
        self._width=w
    @height.setter
    def height(self,h):
        if h<0:
            raise ValueType('negative height')
        self._height=h
    @property
    def resolution(self):
        return self.width*self.height
s=Screen()
#s.width=-98 #will raise error
#s.height=-99
s.width=1024
s.height=768
print(s.resolution)