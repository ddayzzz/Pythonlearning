# coding=gb2312
# 单元测试2
import unittest


class People(object):  # 这个是测试的类

    def __init__(self, name, age):  # 需要测试的初始化函数
        self._name = name
        self._age = age

    def __getattr__(self, key):  # 检查是否存在属性
        if key is not dir(self):
            raise AttributeError('No attribute : %s' % key)
        return key


class Test(unittest.TestCase):  #单元测试的类
    def test_init(self):  # test_开头，表示一个测试的函数 后面的内容是需要测试方法名
        p = People('Shu', 19)
        self.assertEqual(p._name, 'Shu')  # 断言 是否相等
        self.assertEqual(p._age, 19)
        print('OK???')

    def setUp(self):  # 这个是开始测试前的执行的语句
        print('setup...')

    def tearDown(self):  # 结束测试的执行语句
        print('teardown...')


if __name__ == '__main__':
    unittest.main()