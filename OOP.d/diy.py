#coding=utf-8
#slot
class Animal(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return' Student object (name : %s)' % self.name
    def __repr__(self):
        return'Debug Student object (name : %s)' % self.name
    def __getattr__(self,n):
        if n=='score':
            return lambda: 25
a=Animal('ghh')
print(a.score())
#迭代对象
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
    #支持下标和切片
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        elif isinstance(n,slice):#并不支持负数和步长
            s=n.start
            e=n.stop
            if s is None:
                s=0
            if e is None:
                e=100#默认的大小
            a,b=1,1
            L=[]
            for x in range(e):
                if x >=s:
                    L.append(a)
                a,b=b,a+b
            return L
"""
for i in Fib():
    print(i)
"""
f=Fib()
print(f[8:10])