#coding=utf-8
#元类的使用
#type创建类型
def fn(self,name='world'):
    print('hello,%s' % name)
class local(object):
    pass
hello=type('hello',(object,),dict(hello=fn))#创建hello类，继承object 有函数hello表示为fn
h=hello()
print(type(h))#<class '__main__.hello'>
print(type(hello))#<class 'type'>
h.hello('fdfdf')
print(hello.__bases__)
#定义一个元类 使用函数
def pr(self):
    print(self.name)
def new(name, parent,attr):
    l={}
    for key,value in attr.items():
        if not key.startswith('__'):
            l[key.upper()]=value
        else:
            l[key]=value
    return type(name,parent,l)

__metaclass__=new
class A(object):
    pass
pw=new('ffe',(A,),{'pp':pr})#pw是一个类 而不是对象
print(hasattr(pw,'pp'))
print(hasattr(pw,'PP'))
pw.name='egge'
pppp=pw()
pppp.PP()
#使用元类
class Metaclass(type):
    def __new__(self,name,obj,attr):
        l={}
        for key,value in attr.items():
            if not key.startswith('__'):
                l[key.upper()]=value
            else:
                l[key]=value
        #return type(name,parent,l)
        return super(Metaclass,self).__new__(self,name,obj,l)
class Tri(object):
    bar=12
    money='grgrg'
tt=Metaclass('Tri',(),{'bar':Tri.bar,'money':Tri.money})
print(dir(tt))
print(tt.BAR)
#REF http://blog.jobbole.com/21351/
#init new http://www.jb51.net/article/48044.htm