# coding=utf-8
# 处理三个URL
"""
GET / 首页
GET /signin 登录页面
POST /signin 处理登录表单显示登录结果
"""
from flask import Flask as fk
from flask import request


app = fk(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello</h1>'


@app.route('/signin', methods=['GET'])
def sigin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="passwd" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def sigin():
    if request.form['username'] == 'admin' and request.form['passwd'] == 'password':  # Flask通过request.form['name']来获取表单的内容。
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()