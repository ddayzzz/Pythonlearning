#coding=utf-8
#�б�����ʽ
lis=[x*x for x in range(1,11) if x % 2==0]
print(lis)
#ȫ����
lis2=[m+n for m in 'ABC' for n in 'XYZ']
print(lis2)
#ȫ��ת��ΪСд
lis3=[m.lower() for m in ['FGFG','HREHR','SHTTR']]
print(lis3)