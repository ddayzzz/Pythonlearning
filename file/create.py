#create py
#coding=gb2312
import os,shelve,pprint
selffile='createfile'
selfptr=shelve.open(selffile)
dic=[{'name':'名字'},{'USSR':'former soviet'},{'China':{'1':'china','2':'Chinese'}}]
selfptr['dic']=dic
crepy='create1.py'
fptr=open(crepy,'a')
fptr.write('#coding=gb2312\nimport pprint,shelve\nprint(pprint.pformat(shelve.open(\'createfile\')[\'dic\']))')