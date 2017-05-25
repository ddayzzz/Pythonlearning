#coding=utf-8
#参数：
def def_para(l=[]):
    l.append('END')
    return l
#print(def_para())
#print(def_para())#默认参数必须是不变的对象
#可变的参数
"""
def accumulate(*nums):
    sum=0
    for n in nums:
        sum=sum+n
    return sum
print(int(accumulate(2,3,5,5)))
"""
"""
def person(name,age,**kw):
    print('name:',name,' age:',age,' other:',kw)
    print(str(type(kw)))
person('Shu',19,city='Xiangtan',sex='Male')
"""
#命名关键字参数 需要制定全部的关键字
def job(ty,*salary,days):
    print(ty,salary,days)
job('Cleaner')
job('Traveler',days=7)
def f1(x,y=56):
    print(x,y)
f1(5)
f1(6,7)
#Python对尾递归没有优化
