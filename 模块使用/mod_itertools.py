# coding=utf-8
# itertools 的使用
import itertools
natuls = itertools.count(1) # 间隔位1的无限的序列
end = itertools.takewhile(lambda x: x <= 10, natuls)  # 限制了范围
for n in end:
    print(n)
# chain工具 连接：
for c in itertools.chain('ABC', 'XYZ'):
        print(c)
# groupby : 把相邻的重复的元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCaaaAAAa', lambda x: x.upper()):
    print(key, list(group))
