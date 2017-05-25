# coding=utf-8
# filter 的示例
import time
import re
import coroutine


@coroutine.coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        print(type(line))
        g = pattern.search(line)
        if g is not None:
            print('Matched:', line)


@coroutine.coroutine
def printer():
    while True:
        line = (yield)  # 接受一个项目
        print(line)


def follow(thefile, target):
    thefile.seek(0, 2)  # 文件流定位 (offset,where) 0 for head 1 for current position 2 for EOF
    while True:
        line = thefile.readline()  # in python 3.x str hasn't decode attribute https://zhidao.baidu.com/question/1958303036751247620.html
        if not line or line is None:
            time.sleep(0.1)
            continue
        target.send(line)  # 发送给协程的处理程序


if __name__ == '__main__':
    f = open('CBS.log')
    reg = re.compile(r'(http(s)?://)(www\.)?([a-zA-Z0-9]+\.(com|org|cn))')
    ff = follow(f, grep(reg, printer()))
    for i in ff:
        pass
