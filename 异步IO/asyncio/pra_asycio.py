# coding=utf-8
# asyncio的使用
import asyncio


@asyncio.coroutine  # 装饰器标记为coroutine
def hello():
    print('Hello, world!')
    r = yield from asyncio.sleep(5)  # 线程不会等待执行完sleep 这个yield可以从这个操作中获取数据
    print('Hello again')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()