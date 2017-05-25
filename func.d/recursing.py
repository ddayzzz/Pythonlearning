#coidng=utf-8
#递归
import types
def f(n,pre=1):
    if n==1 or n==0 :
        return 1*pre
    else:
        return f(n-1,n*pre)
def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g=g.next()
    return g
print(tramp(f, 996))