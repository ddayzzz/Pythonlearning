# coding=utf-8
# server 端
from wsgiref.simple_server import make_server
from resp_hello import application


httpd = make_server('', 8000, application)
print('Server HTTP on port 8000')
# 监听请求
httpd.serve_forever()
