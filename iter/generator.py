#coding=gb2312
#生成器
"""
g=(x*x for x in range(1,10))
for i in g:
    print(i)
"""
#函数版本的斐波那契
"""
def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    print('Done')
f=fib(8)
print(f) f是一个生成器对象
for s in f:
    print(s)
"""
#杨辉三角
def triangles(n):
     L=[1]#定义一个list[1]
     while True:
        yield L#打印出该list
        L=[L[x]+L[x+1] for x in range(len(L)-1)]#计算下一行中间的值（除去两边的1）
        L.insert(0,1)#在开头插入1
        L.append(1)#在结尾添加1
        if len(L)>10:#仅输出10行
            break
a=triangles(10)
for i in a:
    print(i)