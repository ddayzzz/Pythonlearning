# coding=utf-8
# web开发入门
# WSGI(Web Server Gateway Interface)


# 符合WSGI的响应HTTP的请求的函数 environ包含所有HTTP请求信息的dict；start_response是一个响应的函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    hello = '<h1>Hello!,%s' % (environ['PATH_INFO'][1:] or 'web')
    hello2 = '<p>'
    for inf in environ:
        hello2 = hello2 + inf + ', Value is ' + str(environ[str(inf)]) + '&nbsp;<br>'
    hello2 = hello2 + '</p>'
    hello = hello + hello2
    return [hello.encode('utf-8')]






