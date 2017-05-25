# coding=gb2312
# TCP编程
import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)  # print(type(addr)) addr 是一个tuple
    sock.send(b'Welcome!')  # 发送welcome给客户端
    while True:
        data = sock.recv(1024)  # 从客户端接受1024字节的字符
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':  # 如果刻划断发送了退出的指令 那么就会关闭会话
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  # 将欢迎信息发送回去
    sock.close()
    print('Connection from %s:%s closed' % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(10)  # 输入连接指示（对连接的请求）的最大队列长度被设置为 backlog 参数。如果队列满时收到连接指示，则拒绝该连接。
    print('LISTENING....')
    while True:
        soc, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(soc, addr))  # 每监听到一个请求 创建一个新的线程
        t.start()
