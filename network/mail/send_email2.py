# coding=gb2312
# �����ʼ�2 �����ط���
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart  # �������
from email.mime.base import MIMEBase  # ���ͼƬ���� ref to http://blog.csdn.net/offbeatmine/article/details/51790654
from email.mime.image import MIMEImage
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), adr))


from_add = 'wangshu175@163.com'
passwd = 'ws19971222'
to_add = '2419940233@qq.com'
smtp_server = 'smtp.163.com'
smtp_port = 465  # SMTP SSL���� ��Ҫ����SSL��ȫ���� Ȼ����ʹ��SMTPЭ�� ������Ҫstartssl
# ��������
msg = MIMEText('<html><body><h1>Hello</h1><p����*������%``<a href="http://www.baidu.com" alt="�ٶ�">���ʰٶ�</a></p><span><h1>������ͼƬ��Ϣ<img src="cid:0"></h1></span></body></html>', 'html', 'utf-8')
"""
msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = Header('Greeting from Python', 'utf-8').encode()
"""
# ����Ҫ��Ӹ�����Ҳ���Ƿ���һ������ذ�����MUP �����ġ������������
msgpack = MIMEMultipart()
msgpack.attach(msg)
with open('attach_banner.jpg', 'rb') as fptr:
    # mime = MIMEBase('image', 'jpeg', filename='attach_banner.jpg')  # ����ֱ��ʹ��MIMEImage #REF https://zhidao.baidu.com/question/201405089515383405.html
    mime = MIMEImage(fptr.read())
    # ���ϱ�Ҫ��ͷ��Ϣ:
    mime.add_header('Content-Disposition', 'attachment', filename='attach_banner.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # �����ж�ȡ����
    # mime.set_payload(fptr.read())
    # Base64����
    #encoders.encode_base64(mime)
    # ���
    msgpack.attach(mime)
# һ��Ҫ�����Ϣ
msgpack['From'] = from_add
msgpack['To'] = to_add
msgpack['Subject'] = Header('���ѽ��Greeting from Python with attachments', 'utf-8').encode()
# ���ӷ�����
# ��ͨ�ط��Ͳ�����SSL server = smtplib.SMTP(smtp_server, smtp_port) smtp_portһ��Ϊ25
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_add, passwd)
server.sendmail(from_add, [to_add], msgpack.as_string())  # for attachments use msgpack
server.quit()
