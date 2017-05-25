# coding=utf-8
# task封装
import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
"""output
Hello world! (<_MainThread(MainThread, started 7924)>)
Hello world! (<_MainThread(MainThread, started 7924)>)
Hello again! (<_MainThread(MainThread, started 7924)>)
Hello again! (<_MainThread(MainThread, started 7924)>) 同一个线程
"""