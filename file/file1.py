#file
#coding=gb2312
import os
print(os.path.realpath('c:\\windows'))
#��ȡ�ļ��еĴ�С
for  f in os.listdir('c:\\windows\\winsxs'):
    print(f+' size is '+str(os.path.getsize(os.path.join('c:\\windows\\winsxs',f))))