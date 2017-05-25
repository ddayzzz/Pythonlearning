# coding=utf-8
# 替换所有的Agent
# regular match demo 2
import re
str1 = r'Agent \w*'  # 替换Agent 且后面要接一个空格
rep = re.compile(str1)
print(rep.sub('***', 'Agent ffggg Agent dfafrdfdf Agent '))
# sub替换2 保留第一个字符
str2 = r'Agent (\w)w*'
print(re.compile(str2).sub(r'\1***', 'Agent Liu Agent Wang Agent Fang'))

