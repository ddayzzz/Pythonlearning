#pattern match and regular expression
#coding=gb2312
import re
reg_str=r'\d\d\d-\d\d\d-\d\d\d\d'#regular expression
reg_obj=re.compile(reg_str)#regular expression(RegEx) object
mo=reg_obj.search('My phone:568-777-3333')
mo2=reg_obj.search('vaild : 5555-555-6666')
mo3=reg_obj.search('invaild : a12a-222-33')
print(mo.group())
print(mo2.group())#555-555-6666
#print(mo3.group())#error None does not have group()
#�ڶ��� group() �ȼ���group(0)
reg_str2=r'(\d\d)-(\d\d)-(\d\d\d\d)'
reg_obj2=re.compile(reg_str2)
mo4=reg_obj2.search('23-66-6666')
print('1st:'+mo4.group(1)+'\n2nd'+mo4.group(2)+'\n3rd:'+mo4.group(3))
"""�ȼ۵���䣺g1,g2,g3=mo4.groups()
print('groups():'+'1st:'+g1+'\n2nd'+g2+'\n3rd:'+g3)"""
#�ܵ�ʶ��������
app=r'app(ly|le|etite)'
regexapp=re.compile(app)
print('app'+regexapp.search('apply for porfessor').group(1))
#̰�ĵı��ʽƥ��
greed=r'(Ha\?){3,5}'#3<=Ha?<=5�γ���
regexgreed=re.compile(greed)
print(regexgreed.search('Ha?Ha?Ha?Ha?Ha?').group(0))#����ж����ԣ���ô�ͻ�ƥ�����
#��̰�ĵ�ƥ��
nogreed=r'(Ha\?){3,5}?'#3<=Ha?<=5�γ��� ע��ĩβ�ġ�?��
regexnogreed=re.compile(nogreed)
print(regexnogreed.search('Ha?Ha?Ha?Ha?Ha?').group(0))#�ҵ���ƥ��ľͻ�ֹͣ���� ���Ha?Ha?Ha?
#findall��ʹ��
sub=r'(\d\d\d)-(\d\d)'
nosub=r'\d\d\d-\d\d'
regexsub=re.compile(sub)
regexnosub=re.compile(nosub)
print(regexsub.findall('555-22��666-22'))#�������ӵ�ƥ�������������ƥ����ÿһ��ƥ�����һ��Ԫ�飺[('555', '22'), ('666', '22')]
print(regexnosub.findall('555-22��666-22'))#����û����ƥ���Ҳ�᷵��һ���б�ÿһ��Ԫ�ؾ���һ���ַ���
#.*��ƥ�� .��ʾƥ��һ����������е��ַ� *����>=0   Ĭ��̰��
dotstar=r'File:(.*),Extra:(.*)'
mo5=re.compile(dotstar).search('File:hahaha,Extra:txt')
print(mo5.group(1)+'.'+mo5.group(2))
#��̰�ĵ�ƥ��
dotstarnogreed=r'<.*?>'#ȥ���ʺžͿ���ƥ��<abcd>dfvdvd>
print(re.compile(dotstarnogreed).search('<abcd>dfvdvd>').group())
