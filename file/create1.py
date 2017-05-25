#coding=gb2312
import pprint,shelve
print(pprint.pformat(shelve.open('createfile')['dic']))