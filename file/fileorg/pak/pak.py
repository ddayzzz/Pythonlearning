#coding=gb2312
#�ļ�����+���
#�����е�������������ת��Ϊ�й������ڲ����ǰ׺��Ϣ
#֧�ֵ����� yu������(mm-dd-yyyy)
import zipfile,sys,os,re
pakfle='package.zip'
reg=r'''
^[0-9]{2,2}[-/\s]?[0-9]{2,2}[-/\s]?[0-9]{4,4}$
'''
regex=re.compile(reg,re.VERBOSE)
re.search('fefefeefe02221996fedfd')