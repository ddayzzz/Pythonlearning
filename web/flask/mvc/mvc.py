# coding=utf-8
# MVC结构初探
from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    passwd = request.form['password']
    if username == 'admin' and passwd == '123':
        return render_template('signin-ok.html', username=username)
    # 错误记录一下
    if os.path.exists('record.json') == False:
        data = {'count': 1}
        jsfptr = open('record.json', 'w')
        jsfptr.write(json.dumps(data))
        jsfptr.close()
        return render_template('form.html', message='Bad username or password!', count=range(1, 2), username=username)
    jsfptr = open('record.json', 'r')
    data = json.load(jsfptr)
    jsfptr.close()
    cnt = data['count']
    data['count'] = data['count'] + 1
    jsfptr = open('record.json', 'w')
    jsfptr.write(json.dumps(data))
    jsfptr.close()
    return render_template('form.html', message='Bad username or password!', count=range(1, cnt + 2), username=username)


if __name__ == '__main__':
    app.run()