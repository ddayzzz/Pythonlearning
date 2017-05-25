# coding=gb2312
from multiprocessing.managers import BaseManager
import queue
import logging
import sys
import time
logging.basicConfig(level=logging.DEBUG)


class QueueManager(BaseManager):
    pass


def main():
    # �������QueueManagerֻ�������ϻ�ȡQueue������ע��ʱֻ�ṩ����:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # ���ӵ���������Ҳ��������task_master.py�Ļ���:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    # �˿ں���֤��ע�Ᵽ����task_master.py���õ���ȫһ��:
    m = QueueManager(address=(server_addr, 1080), authkey=b'abc')
    # ����������:
    m.connect()
    # ��ȡQueue�Ķ���:
    task = m.get_task_queue()
    result = m.get_result_queue()
    # ��task����ȡ����,���ѽ��д��result����:
    for i in range(1, 11):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except task.Empty:
            print('task queue is empty.')
    # �������:
    print('worker exit.')


if __name__ == '__main__':
    
    main()
