# coding=utf-8
# 这个是协程的包裹器


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)  # 迭代cr对象，在这个例子中printer就是一个yield的对象
        return cr
    return start
