#file shelve usage
#coding=gb2312
import shelve
"""
fptr=open('file.txt','r')
print(fptr.read())
fptr.close()
fptr=open('file.txt','a')
fptr.write('hh��v����v����vvv�ȼӹ������ع�������ܼҿ��ܹ������˼ҿ�����\n')
fptr.close()
"""
#shelve �����������
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