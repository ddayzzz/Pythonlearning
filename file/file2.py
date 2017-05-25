#file shelve usage
#coding=gb2312
import shelve
"""
fptr=open('file.txt','r')
print(fptr.read())
fptr.close()
fptr=open('file.txt','a')
fptr.write('hh的v阿达v阿飞vvv热加工纳入监控功能软件管家看能够看见人家看个人\n')
fptr.close()
"""
#shelve 保存变量数据
"""
shelveself='self'
fptr=shelve.open(shelveself)
cats=['lala','liuliu','fdfdf']
fptr['cats']=cats
fptr.close()
"""
shelveself='self'
fptr=shelve.open('self')
for i in fptr['cats']:
    print(i)