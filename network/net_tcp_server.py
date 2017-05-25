# coding=gb2312
# TCP���
import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)  # print(type(addr)) addr ��һ��tuple
    sock.send(b'Welcome!')  # ����welcome���ͻ���
    while True:
        data = sock.recv(1024)  # �ӿͻ��˽���1024�ֽڵ��ַ�
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':  # ����̻��Ϸ������˳���ָ�� ��ô�ͻ�رջỰ
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  # ����ӭ��Ϣ���ͻ�ȥ
    sock.close()
    print('Connection from %s:%s closed' % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(10)  # ��������ָʾ�������ӵ����󣩵������г��ȱ�����Ϊ backlog ���������������ʱ�յ�����ָʾ����ܾ������ӡ�
    print('LISTENING....')
    while True:
        soc, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(soc, addr))  # ÿ������һ������ ����һ���µ��߳�
        t.start()
