# coding=gb2312
# 调用堆栈
# Ref : http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
import logging  # 导入日志记录模块
import os,sys

# 记录到日志的文件
logging.basicConfig(level=logging.INFO,  # 级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 格式
                    datefmt='%a, %d %b %Y %H:%M:%S',  # 日期格式
                    filename=os.getcwd()+os.path.sep.join((os.path.sep, 'debug', 'myapp.log')),  # 文件路径，我这里是保存在项目的莫i一个子目录
                    filemode='w')  # 读写的参数，与open的flag无异

# 输出到错误流
console = logging.StreamHandler()  # 流
console.setLevel(logging.INFO)  # 级别
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)  # 设置为一个指定的格式的对象
logging.getLogger('').addHandler(console)  # 创建一个根logger对象（getLoger的参数为''）
# default path is cwd path


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


logging.debug('DEBUG MESSAGES')
logging.info('INFO MESSAGES')
main()
print('END')