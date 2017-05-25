# coding=gb2312
# tcp 用户
import socket
import threading
import random
import os


def gen_str():
    fr = chr(random.randint(65, 90))
    se = chr(random.randint(65, 90))
    th = chr(random.randint(65, 90))
    return ''.join((fr, se, th)).encode('utf-8')


def send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [bytes(gen_str()), bytes(gen_str()), bytes(gen_str())]:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


for i in range(0, 6):
    th = threading.Thread(target=send)
    th.start()
os.system("pause")
# ref http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html
# ref https://zhidao.baidu.com/question/1302029005675079579.html