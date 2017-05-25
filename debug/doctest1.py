# coding=gb2312
# 文档测试
# 注意：有两个地方可以放doctest测试用例，一个位置是模块的最开头，另一个位置是函数声明语句的下一行（就像上面的例子这样）。除此之外的其它地方不能放，放了也不会执行。

def mul(x, *more):
    '''
    >>> mul(1, 2, 3)
    6
    >>> mul(2, 2, 2, 2, 2)
    31
    '''
    pro = x
    for k in more:
        pro *= k
    return pro


if __name__ == '__main__':
    import doctest
    doctest.testmod()
