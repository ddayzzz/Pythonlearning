# coding=gb2312
# IO使用

with open('test1.txt', 'r+') as fptr:  # 使用上下文管理器
    print(fptr.read())

# 指定编码 可选错误处理
f = open('test1.txt', 'r', encoding='ascii', errors='ignore')
print(f.read(5))

# stringIO
from io import StringIO
si = StringIO()
print(si.write('hello\n6666\n777'))
print(si.getvalue())
# si相当于C++里的sstream 
while(True):
    s = si.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO写入
from io import BytesIO
bi = BytesIO()
bi.write('中国'.encode('utf-8'))
print(bi.getvalue())
fwtr = open('test1_save.txt', 'a')
fwtr.write(si.getvalue())  # 只能写入字符串 不能写入字节流 字符串流
fwtr.close()