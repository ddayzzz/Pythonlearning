#coding=utf-8
class p1(object):
    def __init__(self):
        print('p1')
        self.geg='egege'
class c1(p1):
    def __init__(self):
        #super(c1,self).__init__()
        p1.__init__(self)
        print('c1')
class c2(p1):
    def __init__(self):
        #super(c2,self).__init__()
        p1.__init__(self)
        print('c2')
class c3(c1,c2):
    def __init__(self):
        super(c3,self).__init__()
        #c1.__init__(self)
        #c2.__init__(self)
        pass
c=c3()
print(c.geg)
"""
不使用super
p1
c1
p1
c2
使用super
p1
c2
c1
"""
#ref http://blog.csdn.net/u011467044/article/details/52205961