#coding=gb2312
"""
#װ����
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
#�߼���ʹ��
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
nowa = recorder('execute')(now) #��һ�㷵�ط���decorator �� decorator��Ҫһ��������Ϊ������Ȼ�󷵻�wrapper1��ҲҪ���ܲ���
print(nowa(*[7,8,9]))
print(nowa.__name__)
#functools.wrap��ʹ�ã�

