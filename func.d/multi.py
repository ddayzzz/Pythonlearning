#coding=utf-8
#返回多个值示例：
import math
def solve_formula(a,b,c):
    delta=math.sqrt(b*b-4*a*c)
    return float((-b+delta)/(2*a)),float((-b-delta)/(2*a))
a=int(input())
b=int(input())
c=int(input())
r1,r2=solve_formula(a,b,c)
print('root1 is %f,root 2 is %.2f' %(r1,r2))