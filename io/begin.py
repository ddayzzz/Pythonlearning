# coding=gb2312
# IOʹ��

with open('test1.txt', 'r+') as fptr:  # ʹ�������Ĺ�����
    print(fptr.read())

# ָ������ ��ѡ������
f = open('test1.txt', 'r', encoding='ascii', errors='ignore')
print(f.read(5))

# stringIO
from io import StringIO
si = StringIO()
print(si.write('hello\n6666\n777'))
print(si.getvalue())
# si�൱��C++���sstream 
while(True):
    s = si.readline()
    if s == '':
        break
    print(s.strip())

# BytesIOд��
from io import BytesIO
bi = BytesIO()
bi.write('�й�'.encode('utf-8'))
print(bi.getvalue())
fwtr = open('test1_save.txt', 'a')
fwtr.write(si.getvalue())  # ֻ��д���ַ��� ����д���ֽ��� �ַ�����
fwtr.close()