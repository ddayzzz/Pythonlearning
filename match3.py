#match email and phone from clipboard
#coding=gb2312
import re
import pyperclip
str_phone=r'(\d{,3})(\s|-|.)(\d{,11})'

str_email=r'''(
[0-9a-zA-Z-_]+#usename
@#symbol
[0-9a-zA-Z-_]+#domain name
(\.[0-9a-zA-Z-_]{2,4}))
'''
stre=str(pyperclip.paste())
print('剪贴板内容：'+stre)
regex_phone=re.compile(str_phone)
regex_email=re.compile(str_email,re.VERBOSE)
mo1=regex_phone.search(stre)
mo2=regex_email.search(stre)
print('Phone Number:'+mo1.group())
print('Email:'+mo2.group())