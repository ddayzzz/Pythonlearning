# coding=gb2312
# �����Ĺ�����


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin....')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

    def __getattr__(self, att):
        if att == 'error':
            raise RuntimeError('�û�����Ĵ���')
        else:
            return 'no problem'


with Query('hahaha') as qq:
    qq.query()
    print(qq.nanananan)
    print(qq.error)