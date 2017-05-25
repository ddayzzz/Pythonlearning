# coding=utf-8
# boardcast
import filter


@filter.coroutine.coroutine
def boardcast(target):
    while True:
        item = (yield)
        for tar in target:
            tar.send(item)  # 将获得的内容全部转发


if __name__ == '__main__':
    m1 = r'Python'
    m2 = r'AMD[a-zA-Z0-9]+'
    m3 = r'AMDI do(es)? [a-zA-Z]'

    f = open('CBS.log')  # 只需要一个printer就可以打印值
    pp = filter.follow(f, boardcast([
        filter.grep(filter.re.compile(m1), filter.printer()),
        filter.grep(filter.re.compile(m2), filter.printer()),
        filter.grep(filter.re.compile(m3), filter.printer())
    ]))
    f.close()

