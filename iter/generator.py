#coding=gb2312
#������
"""
g=(x*x for x in range(1,10))
for i in g:
    print(i)
"""
#�����汾��쳲�����
"""
def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    print('Done')
f=fib(8)
print(f) f��һ������������
for s in f:
    print(s)
"""
#�������
def triangles(n):
     L=[1]#����һ��list[1]
     while True:
        yield L#��ӡ����list
        L=[L[x]+L[x+1] for x in range(len(L)-1)]#������һ���м��ֵ����ȥ���ߵ�1��
        L.insert(0,1)#�ڿ�ͷ����1
        L.append(1)#�ڽ�β���1
        if len(L)>10:#�����10��
            break
a=triangles(10)
for i in a:
    print(i)