# coding=gb2312
# 发送邮件2 完整地发送
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart  # 打包附件
from email.mime.base import MIMEBase  # 添加图片类型 ref to http://blog.csdn.net/offbeatmine/article/details/51790654
from email.mime.image import MIMEImage
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), adr))


from_add = 'wangshu175@163.com'
passwd = 'ws19971222'
to_add = '2419940233@qq.com'
smtp_server = 'smtp.163.com'
smtp_port = 465  # SMTP SSL加密 需要建立SSL安全连接 然后再使用SMTP协议 后面需要startssl
# 构建正文
msg = MIMEText('<html><body><h1>Hello</h1><p人呐*·￥￥%``<a href="http://www.baidu.com" alt="百度">访问百度</a></p><span><h1>附件地图片信息<img src="cid:0"></h1></span></body></html>', 'html', 'utf-8')
"""
msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = Header('Greeting from Python', 'utf-8').encode()
"""
# 我需要添加附件：也就是发送一个打包地包裹给MUP 将正文、附件打包即可
msgpack = MIMEMultipart()
msgpack.attach(msg)
with open('attach_banner.jpg', 'rb') as fptr:
    # mime = MIMEBase('image', 'jpeg', filename='attach_banner.jpg')  # 可以直接使用MIMEImage #REF https://zhidao.baidu.com/question/201405089515383405.html
    mime = MIMEImage(fptr.read())
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='attach_banner.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 从流中读取数据
    # mime.set_payload(fptr.read())
    # Base64编码
    #encoders.encode_base64(mime)
    # 打包
    msgpack.attach(mime)
# 一定要添加信息
msgpack['From'] = from_add
msgpack['To'] = to_add
msgpack['Subject'] = Header('你好呀！Greeting from Python with attachments', 'utf-8').encode()
# 连接服务器
# 普通地发送不建立SSL server = smtplib.SMTP(smtp_server, smtp_port) smtp_port一般为25
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_add, passwd)
server.sendmail(from_add, [to_add], msgpack.as_string())  # for attachments use msgpack
server.quit()
