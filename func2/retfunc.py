#coding=utf-8
#���غ���
def ss(l):
    def sum():
        ss=0
        for i in l:
            ss+=i
        return ss
    return sum
r1=ss([2,6,5,9])
r2=ss([2,6,5,9])
l=[2,6,5,9]
r3=ss(l)
r4=ss(l)
print(r1)
print(r2)
print(r1==r2)
print(r3)
print(r4)
print(r3==r4)
print(r1()==r2())
print(r3()==r4())
#�հ������ⲿ����������
def power():
    lis=[]
    for i in range(1,4):
        def ii():
            return i*i
        lis.append(ii)#��ӱհ�
    return lis
f1,f2,f3=power()
print(f1(),'\n',f2(),'\n',f3())#���9 9 9
#��������
def plus():
    return lambda x,y:x+y
print(plus()(45,5))
def ret():
    lis=[]
    for i in range(1,4):
        lis.append(lambda j=i:j*j)
    return lis
s1,s2,s3=ret()#���ظ�ֵ���ܶ�
print(s1())#1
print(s2())#4
print(s3())#9
    