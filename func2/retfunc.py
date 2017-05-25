#coding=utf-8
#返回函数
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
#闭包引用外部参数的问题
def power():
    lis=[]
    for i in range(1,4):
        def ii():
            return i*i
        lis.append(ii)#添加闭包
    return lis
f1,f2,f3=power()
print(f1(),'\n',f2(),'\n',f3())#输出9 9 9
#匿名函数
def plus():
    return lambda x,y:x+y
print(plus()(45,5))
def ret():
    lis=[]
    for i in range(1,4):
        lis.append(lambda j=i:j*j)
    return lis
s1,s2,s3=ret()#多重赋值不能多
print(s1())#1
print(s2())#4
print(s3())#9
    