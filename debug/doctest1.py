# coding=gb2312
# �ĵ�����
# ע�⣺�������ط����Է�doctest����������һ��λ����ģ����ͷ����һ��λ���Ǻ�������������һ�У��������������������������֮��������ط����ܷţ�����Ҳ����ִ�С�

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
