#coding= gb2312
l='.'.join(['a','b','c'])
print(l)
#分解
s1='''666
Shu
32
66
777'''
print(s1.split('\n'))#['666', 'Shu', '32', '66', '777']
#rjust
s2='fdf'
print(s2.rjust(10,'*'))
#clipboard usage
import pyperclip
#pyperclip.copy('Hello')
print(pyperclip.paste())