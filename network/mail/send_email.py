# coding=gb2312
# SMTP协议发送邮件
# 原理：用户发送邮件->MUA->MTA->.....个MTA
from email.mime.text import MIMEText
import smtplib  # for SMTP


# 正文、MIME的subtype(plain是纯文本MIME/plain)  UTF-8字符集
msg = MIMEText('hello!ffewfefe', 'plain', 'utf-8')
from_addr = input('From:')
passwd = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')
# 以下是必须填的 否则会出现554错误 ref http://blog.csdn.net/smart55427/article/details/48783393
msg['subject'] = 'Python STMP'
msg['From'] = from_addr
msg['To'] = to_addr
# 开始发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
