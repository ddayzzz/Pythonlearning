# coding=utf-8
# aync/await
import asyncio


async def wget(host):
    print('wget : %s...' % host)
    connect = asyncio.open_connection(host, 80)  # 打开连接 访问www服务端口
    reader, writer = await connect  # for detail https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host  # GET请求
    writer.write(header.encode('utf-8'))
    await writer.drain()  # yield from writer.drain()  # 刷新底层传输的写缓冲区也就是把需要发送出去的数据，从缓冲区发送出去。没有手工刷新，asyncio为你自动刷新了。当执行到reader.readline()时，asyncio知道应该把发送缓冲区的数据发送出去了。ref：http://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/001467709310657d35aab1ece384720ba5f341c5503a224000
    # drain ref2 : https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter
    while True:
        line = await reader.readline()
        # yield from asyncio.sleep(2) 交替执行 不会等待这个暂停两秒结束继续执行其他可以执行的协程
        if line == b'\r\n':
            break
        print('%s header> %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.baidu.com', 'www.bing.com', 'www.microsoft.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()