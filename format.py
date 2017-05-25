# coding= gb2312 注释需# 后面需要空格

# dunders名称（我猜是double underscores的缩写 :D），应该放在
# 模块的说明字符串后，import的前面除了 from __future__


import shutil

__author__ = 'shu'

import sys  # 模块要在第一行或者第一个注释后
import os  # 不是import sys,os 而且模块要被使用 否则就是F401错误 
shutil.copy2('ggrg', 'ege')
sys.argv  # 要使用
os.P_WAIT


def fcn(  # 需要空两行 inline的注释需要距离两个空格
        var_one, var2, var3,
        var4):
    print('6666')  # 居然需要和fcn对齐 也就是4个spaces


li = [  # 距离函数、类定义有两个空白行
     1, 2, 3,
     4, 5, 6,
]  # 多行定义一个列表 ,后面记得空格
result = fcn(
        'a', 'b', 'c',
        'd',
)
""" 只要方便就可以了 多行注释不要用\作为分隔。长的导入语句、http链接可以不满足长度限制
一行列数 : PEP 8 规定为 79 列，这有些苛刻了。根据自己的情况，比如不要超过满屏时编辑器的显示列数。这样就可以在不动水平游标的情况下，方便的查看代码。
一个函数 : 不要超过 30 行代码, 即可显示在一个屏幕类，可以不使用垂直游标即可看到整个函数。
一个类 : 不要超过 200 行代码，不要有超过 10 个方法。
一个模块 不要超过 500 行。
"""

num1 = 52
num2 = 33
income = (num1
          + 55  # 建议和num1对齐
          + (num1 - num1)
          - num2)


class clas(object):
        _name = '55'

        def meth1(self):
                pass

        def meth2(self, pa=' '):  # 两个方法之间用一个空行隔开 默认参数要不用分开
                pass


"""编码：
标识符、字符串字面值、注释必须是ASCII。除了测试其他的边，作者名称提供拉丁音译名(transliteration)
"""

# 不要使用空格的情况
# 1 ：不要在括号后空格
spam = ({'66': 6}, {'888': 8})
# 2：不要元组、列表结尾后空格
spam2 = (56,)
# 3 : 在逗号、分号（semicolon，用于一行多语句的分隔）、冒号（colon）前使用空格
x = 666
y = 99
if x == 4:
        print(x, y)
else:
        x, y = y, x
# 4 :参数列表、索引、切片的左括号不加空格，默认参数赋值不要用空格
liuliu = ['123', '256', '6666']
h1 = liuliu[1::3]
h2 = liuliu[x+y:x:]  # 这个地方和doc的不同，怪事

"""
Always surround these binary operators with a single space on either side: assignment ( = ), augmented assignment ( += , -= etc.), comparisons ( == , < , > , != , <> , <= , >= , in , not in , is , is not ), Booleans ( and , or , not ).
如果两个运算符的优先级不同，可以给较低的运算符添加空格
"""
z = x*x + y*y
z1 = (x+x) * (y+y)
"""
函数的注释
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
当混合有参数时，注解需要的=两边要有空格
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): 
"""
# 模块的名称一般是小写
# 小驼峰式命名法 firName
# 大驼峰式命名法 FirstName 单词都大写
# 但是缩写都大写 例如HTTPEror
# 驼峰式大小写StudlyCaps
# _一般用来表示强调连接的结构性

# 下划线使用
# _xxxx : 私有的成员 不会被导入
# xxxx_ : 用来避免关键字冲突 Tkinter.Toplevel(master, class_='ClassName')
# __xxxx : 命名类的属性等 例如inside class FooBar, __boo becomes _FooBar__boo
# __xxxx__ : 魔术对象。比如构造方法等

# 异常名：加上后缀Error
# 全局变量名：__all__是一个列表可以指定导出的名称。如果没有列表导出所有不以_开头的名称

# 函数与方法的参数
# 实例方法：第一个参数为self
# 类的方法：第一个参数为cls
# 参数建议后面添加一个单下划线
# 函数名建议小写，适当添加下划线可以提高可读性

# 常量全大写

# 继承设计
"""
 对简单的公开数据属性 (data attribute)，最好只暴露属性名，没有复杂的访问
 @property 装饰器可以让函数的行为像直接使用属性
"""

# 编程建议
"""
1.对 a+=b or a=a+b 形式的语句，不要依赖 CPython 对就地 (in-place) 字 符串连接的高效实现。那些语句在 Jython 中运行很慢。对库的性能敏感部分，应 该改用 ''.join() 语句。这将保证对不同的实现，字符串连接表现为线性时间。
2.对于比较单件（singletons ）例如None  建议使用 is is not 而不是用==或!=比较
3.捕获异常之后不建议使用空语句。如果想捕获所有异常，使用StandardError
4.使用def而不是赋值来返回一个可调用对象
5.异常类从Exception类派生而不是BaseException
6.空的字符串、元组、列表为空，总是表示他们为False
7.确保if的所有情况返回值
8.建议使用tartswith endswith而不是切片来判断字符串的开头和结尾
9.不要使用==比较布尔值
10.==是比较值（Value） 而 is是判断对象本身（Type）
"""