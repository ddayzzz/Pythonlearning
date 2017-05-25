# coding=gb2312
# �����Ĺ�����2 ʹ�ÿ�
from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

    def __getattr__(self, att):
        if att == 'error':
            raise RuntimeError('�û�����Ĵ���')
        else:
            return 'no problem'


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('hahaha') as qq:
    qq.query()
    print(qq.nanananan)
    #print(qq.error)


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h2'):
    print('6666', '7777')

# �����ĵȼ۵Ĺ���
from contextlib import closing
from urllib.request import urlopen


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)