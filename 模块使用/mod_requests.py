# coding=gb2312
# ref http://www.cnblogs.com/jackyspy/p/6027385.html
# requests的使用
import requests


print(type(requests.get('http://httpbin.org/ip', proxies={'http':'127.0.0.1:1080'}).json()))

