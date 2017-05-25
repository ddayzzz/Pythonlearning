# coding=gb2312
# windows 可以使用的分布式
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import queue
import logging
import random
import sys
from threading import Thread


class QueueManager(BaseManager):
    pass


task_queue = queue.Queue()
result_queue = queue.Queue()


def get_task_queue():
    global task_queue
    return task_queue


def get_result_queue():
    global result_queue
    return result_queue


def main():
    QueueManager.register('get_result_queue', callable=get_result_queue)
    QueueManager.register('get_task_queue', callable=get_task_queue)
    iManager = QueueManager(address=('127.0.0.1', 1080), authkey=b'abc')
    logging.info('服务器创建完成')
    iManager.start()
    logging.info('服务器启动')
    taskQueue = iManager.get_task_queue()
    resultQueue = iManager.get_result_queue()
    for i in range(1, 11):
        print('Put task %d...' % i)
        taskQueue.put(random.randint(0, 10000))
    for i in range(1, 11):
        r = resultQueue.get(timeout=10)
        print('Result: %s' % r)
    iManager.shutdown()


if __name__ == '__main__':
    print(sys.argv)
    freeze_support()  # 测试 https://hg.python.org/cpython/file/d9893d13c628/Lib/multiprocessing/forking.py#l302
    main()
