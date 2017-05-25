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
#第二段 group() 等价于group(0)
reg_str2=r'(\d\d)-(\d\d)-(\d\d\d\d)'
reg_obj2=re.compile(reg_str2)
mo4=reg_obj2.search('23-66-6666')
print('1st:'+mo4.group(1)+'\n2nd'+mo4.group(2)+'\n3rd:'+mo4.group(3))
"""等价的语句：g1,g2,g3=mo4.groups()
print('groups():'+'1st:'+g1+'\n2nd'+g2+'\n3rd:'+g3)"""
#管道识别多个分组
app=r'app(ly|le|etite)'
regexapp=re.compile(app)
print('app'+regexapp.search('apply for porfessor').group(1))
#贪心的表达式匹配
greed=r'(Ha\?){3,5}'#3<=Ha?<=5次出现
regexgreed=re.compile(greed)
print(regexgreed.search('Ha?Ha?Ha?Ha?Ha?').group(0))#如果有二义性，那么就会匹配最长的
#非贪心的匹配
nogreed=r'(Ha\?){3,5}?'#3<=Ha?<=5次出现 注意末尾的“?”
regexnogreed=re.compile(nogreed)
print(regexnogreed.search('Ha?Ha?Ha?Ha?Ha?').group(0))#找到能匹配的就会停止搜索 输出Ha?Ha?Ha?
#findall的使用
sub=r'(\d\d\d)-(\d\d)'
nosub=r'\d\d\d-\d\d'
regexsub=re.compile(sub)
regexnosub=re.compile(nosub)
print(regexsub.findall('555-22：666-22'))#由于有子的匹配项，所以有两个匹配项每一个匹配项构成一个元组：[('555', '22'), ('666', '22')]
print(regexnosub.findall('555-22：666-22'))#由于没有子匹配项，也会返回一个列表，每一个元素就是一个字符串
#.*的匹配 .表示匹配一个任意除换行的字符 *出现>=0   默认贪心
dotstar=r'File:(.*),Extra:(.*)'
mo5=re.compile(dotstar).search('File:hahaha,Extra:txt')
print(mo5.group(1)+'.'+mo5.group(2))
#非贪心的匹配
dotstarnogreed=r'<.*?>'#去掉问号就可以匹配<abcd>dfvdvd>
print(re.compile(dotstarnogreed).search('<abcd>dfvdvd>').group())
