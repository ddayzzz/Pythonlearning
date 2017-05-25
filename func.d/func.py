#coding=utf-8
#这个是函数的使用的PY示例
#检查函数的数据类型
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('错误的数据类型'+str(type(x)))
    else:
        if x>=0:
            return x
        else:
            return -x
i=235
str1='ggrgrg'
f=0.963
tuple1=('j','hjh')
dic={'lk':'fgf','gr':'grrefe'}
lis=['fdfe','grgrgr']
print(my_abs(i))
print(my_abs(str1))
print(my_abs(f))
print(my_abs(tuple1))
print(my_abs(dic))
print(my_abs(lis))

