#python
# coding=gb2312
import pprint
dic={'apple':'red','pear':'yellow','grape':'green'}
for v in dic.keys():#��ӡkey
    print(v)
for k,v in dic.items():#��ӡkey��value
    print('key :'+str(k)+' value :'+str(v),end='\n')
#Ĭ���滻��
print(dic.setdefault('nut','brown'))
print(dic.setdefault('apple','green'))
#��ӡ

socket={'shu':{'school':['TJPU','XGYZ','JS'],'sex':'male'},'Liu':{'school':['XTU','JS'],'sex':'female'}}
print(socket)#��������� ʹ��pprint�ͺܺã����Դ���Ƕ�׵�value
pprint.pprint(socket)
print(pprint.pformat(socket))#�ȼ����