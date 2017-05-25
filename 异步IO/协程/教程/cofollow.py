# coding=utf-8
# 协程教程 program like tail -f in unix-like
import time


def follow(thefile, target):
    thefile.seek(0, 2)  # 文件流定位 (offset,where) 0 for head 1 for current position 2 for EOF
    while True:
        line = thefile.readline()  # in python 3.x str hasn't decode attribute https://zhidao.baidu.com/question/1958303036751247620.html
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)  # 发送给协程的处理程序


# 设置一个函数包裹器 发挥一个打包的函数 参数自动解开 
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)  # 迭代cr对象，在这个例子中printer就是一个yield的对象
        return cr
    return start


@coroutine
def printer():
    while True:
        line = (yield) # 接受一个项目
        print(line)


print(dir(str))
f = open('CBS.log')
ff = follow(f, printer())
for i in ff:
    pass  # 循环监控
f.close()