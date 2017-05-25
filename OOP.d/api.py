#coding=utf-8
#API的调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        if path=='user':
            return lambda x:Chain('%s/%s' %(self._path,x))
        else:
            return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
    def __call__(self):#相当于C++里的重载调用运算符
        print('fwwsf')
print(Chain('http://api.com').user('shusagsa').copy) #http://api.com/shusage/copy
print(callable(Chain))
print(callable(Chain()))