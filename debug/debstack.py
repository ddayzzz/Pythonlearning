# coding=gb2312
# ���ö�ջ
# Ref : http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
import logging  # ������־��¼ģ��
import os,sys

# ��¼����־���ļ�
logging.basicConfig(level=logging.INFO,  # ����
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # ��ʽ
                    datefmt='%a, %d %b %Y %H:%M:%S',  # ���ڸ�ʽ
                    filename=os.getcwd()+os.path.sep.join((os.path.sep, 'debug', 'myapp.log')),  # �ļ�·�����������Ǳ�������Ŀ��Īiһ����Ŀ¼
                    filemode='w')  # ��д�Ĳ�������open��flag����

# �����������
console = logging.StreamHandler()  # ��
console.setLevel(logging.INFO)  # ����
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)  # ����Ϊһ��ָ���ĸ�ʽ�Ķ���
logging.getLogger('').addHandler(console)  # ����һ����logger����getLoger�Ĳ���Ϊ''��
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