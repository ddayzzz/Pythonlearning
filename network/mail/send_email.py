# coding=gb2312
# SMTPЭ�鷢���ʼ�
# ԭ���û������ʼ�->MUA->MTA->.....��MTA
from email.mime.text import MIMEText
import smtplib  # for SMTP


# ���ġ�MIME��subtype(plain�Ǵ��ı�MIME/plain)  UTF-8�ַ���
msg = MIMEText('hello!ffewfefe', 'plain', 'utf-8')
from_addr = input('From:')
passwd = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')
# �����Ǳ������ ��������554���� ref http://blog.csdn.net/smart55427/article/details/48783393
msg['subject'] = 'Python STMP'
msg['From'] = from_addr
msg['To'] = to_addr
# ��ʼ�����ʼ�
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
