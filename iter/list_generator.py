#coding=utf-8
#列表生成式
lis=[x*x for x in range(1,11) if x % 2==0]
print(lis)
#全排列
lis2=[m+n for m in 'ABC' for n in 'XYZ']
print(lis2)
#全部转换为小写
lis3=[m.lower() for m in ['FGFG','HREHR','SHTTR']]
print(lis3)