#coding=gb2312
"""
#装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def plus(x,y):
    return x+y
print(plus(2,3))
"""
#高级的使用
import functools
def recorder(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper1(*args):
            print(args)
            return func(args)
        return wrapper1
    return decorator
def now(*a):
    return True
nowa = recorder('execute')(now) #第一层返回返回decorator ， decorator需要一个函数作为参数。然后返回wrapper1他也要接受参数
print(nowa(*[7,8,9]))
print(nowa.__name__)
#functools.wrap的使用：

