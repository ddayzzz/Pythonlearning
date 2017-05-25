#file
#coding=gb2312
import os
print(os.path.realpath('c:\\windows'))
#获取文件夹的大小
for  f in os.listdir('c:\\windows\\winsxs'):
    print(f+' size is '+str(os.path.getsize(os.path.join('c:\\windows\\winsxs',f))))