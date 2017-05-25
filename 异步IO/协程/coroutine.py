# coding=utf-8
# 协程


def consumer():
    r = ''
    while True:
        n = yield r  # 返回下一个生成对象
        if not n:
            return
        print('[CONSUMER] Cosuming %s....' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s....' % n)
        r = c.send(n)  # 发送参数给生成器 设置生成器的输入 返回输出
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()  # 首先生成一个生成器 不需要r=''的情况
produce(c)
