# coding=utf-8
# 这个是使用正则表达式的字符切分
import re
str1 = 'abc   bc   v h,hj,hh'
print(re.split('[\s,]+', str1))  # 可以按照任意的空格数量和逗号分割