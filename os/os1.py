# coding=gb2312
import os


# ��дһ��������ls��С����
path1 = '.'
filelist = [x for x in os.listdir(path1)]
for i in filelist:
    if os.path.isdir(i):
        print('<DIR> %s' % i.ljust(10))
        for sub in os.listdir(os.path.sep.join((path1, i))):
             print('    <SUB> %s' % sub.ljust(10))
    elif os.path.isfile(i):
        print('<FLE> %s' % i.ljust(10))
    elif os.path.islink(i):
        print('<LNK> %s' % i.ljust(10))