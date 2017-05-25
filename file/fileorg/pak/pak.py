#coding=gb2312
#文件改名+打包
#将所有的美国风格的日期转换为中国的日期并添加前缀信息
#支持的日期 yu月日年(mm-dd-yyyy)
import zipfile,sys,os,re
pakfle='package.zip'
reg=r'''
^[0-9]{2,2}[-/\s]?[0-9]{2,2}[-/\s]?[0-9]{4,4}$
'''
regex=re.compile(reg,re.VERBOSE)
re.search('fefefeefe02221996fedfd')