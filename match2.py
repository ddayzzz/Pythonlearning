# coding=utf-8
# �滻���е�Agent
# regular match demo 2
import re
str1 = r'Agent \w*'  # �滻Agent �Һ���Ҫ��һ���ո�
rep = re.compile(str1)
print(rep.sub('***', 'Agent ffggg Agent dfafrdfdf Agent '))
# sub�滻2 ������һ���ַ�
str2 = r'Agent (\w)w*'
print(re.compile(str2).sub(r'\1***', 'Agent Liu Agent Wang Agent Fang'))

