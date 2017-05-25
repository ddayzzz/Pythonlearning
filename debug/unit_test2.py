# coding=gb2312
# ��Ԫ����2
import unittest


class People(object):  # ����ǲ��Ե���

    def __init__(self, name, age):  # ��Ҫ���Եĳ�ʼ������
        self._name = name
        self._age = age

    def __getattr__(self, key):  # ����Ƿ��������
        if key is not dir(self):
            raise AttributeError('No attribute : %s' % key)
        return key


class Test(unittest.TestCase):  #��Ԫ���Ե���
    def test_init(self):  # test_��ͷ����ʾһ�����Եĺ��� �������������Ҫ���Է�����
        p = People('Shu', 19)
        self.assertEqual(p._name, 'Shu')  # ���� �Ƿ����
        self.assertEqual(p._age, 19)
        print('OK???')

    def setUp(self):  # ����ǿ�ʼ����ǰ��ִ�е����
        print('setup...')

    def tearDown(self):  # �������Ե�ִ�����
        print('teardown...')


if __name__ == '__main__':
    unittest.main()