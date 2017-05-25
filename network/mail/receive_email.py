# coding=gb2312
# POP3协议收邮件
# 途径MUA ->MDA(邮件代理) ->(访问)MUA
import poplib
from email.parser import Parser
# 解析邮件
from email.header import decode_header
from email.utils import parseaddr
import random

"""EMAIL原始文本
--===============4557463990664328221==
Content-Type: text/html; charset="utf-8"  《头》
MIME-Version: 1.0  《头》
Content-Transfer-Encoding: base64  《头》

PGh0bWw+PGJvZHk+PGgxPkhlbGxvPC9oMT48cOS6uuWRkCrjg7vvv6Xvv6UlYGA8YSBocmVmPSJo
dHRwOi8vd3d3LmJhaWR1LmNvbSIgYWx0PSLnmb7luqYiPuiuv+mXrueZvuW6pjwvYT48L3A+PHNw
YW4+PGgxPumZhOS7tuWcsOWbvueJh+S/oeaBrzxpbWcgc3JjPSJjaWQ6MCI+PC9oMT48L3NwYW4+
PC9ib2R5PjwvaHRtbD4=

--===============4557463990664328221==
Content-Type: image/jpeg
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="attach_banner.jpg"
Content-ID: <0>
X-Attachment-Id: 0

/9j/4QrbRXhpZgAATU0AKgAAAAgAEAEAAAMAAAABDMAAAAEBAAMAAAABCZAAAAECAAMAAAADAAAA
zgEGAAMAAAABAAIAAAEOAAIAAAAEYnNoAAEPAAIAAAAHAAAA1AEQAAIAAAAQAAAA2wESAAMAAAAB
AAEAAAEVAAMAAAAxxxxBASE64编码。忽略。。。
--===============4557463990664328221==--
"""


def decode_str(s):
    value, charset = decode_header(s)[0]  # 解析头的第一个类型 值就是Content-Type的值
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()  # 这个是什么情况呢？可能是防止其他的类型没有getchar这个选项 如果没有返回的是None就不怎么好看了。所以我只在text html中用
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 缩进显示
def print_info(msg, indent=0):
    if indent == 0:  # 用来区别是否是邮件信息的变量 如果是在解析附件包的情况 就需要+1 因此加入了一定数量的TAB
        for header in ['From', 'To', 'Subject']:  # 处理邮件的信息
            value = msg.get(header, '')  # 获取每一个信息
            if value:
                if header == 'Subject':  # 主题特殊处理
                    value = decode_str(value)  # 解码
                else:
                    hdr, addr = parseaddr(value)  # 解析邮箱的地址
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, value)  # name是发件者或者是收件者
            print('%s%s: %s' % ('   ' * indent, header, value))  # 打印信息
    if (msg.is_multipart()):  # 是否是附件包
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))  # 每一个附件包需要单独拿出来 这个主要用于标注包的编号
            print_info(part, indent + 1)  # 递归 显示这个包的内容
    else:
        content_type = msg.get_content_type()  # 这个才是分解每一个附件包的过程
        if content_type == 'text/pain' or content_type == 'text/html':  # 文本或者HTML文本
            content = msg.get_payload(decode=True)  # 解码就可以了
            charset = guess_charset(msg)  # 获取可能的编码
            if charset:
                content = content.decode(charset)  # 指定编码解码
            print('%sText: %s' % ('   ' * indent, content + '...'))  # 显示出来
        else:
            print('%sAttachment: %s' % ('   ' * indent, content_type))  # 其他的格式打印信息
            content = msg.get_payload(decode=True)  # 解码就可以了
            with open(('ATTACH_%d' % random.randint(0, 12)), 'wb') as fptr:  # 防止文件冲突
                fptr.write(content)  # 直接下载文件


# 获取账户信息
em = '2419940233@qq.com'
passwd = 'pykhxqxdwjfpdjge'  # 我开启了授权码 所以用授权码登陆
pop3_server = 'pop.qq.com'
# 连接pop服务器
ser = poplib.POP3_SSL(pop3_server, 995)
ser.set_debuglevel(1)
print(ser.getwelcome().decode('utf-8'))
# 登录服务器
ser.user(em)
ser.pass_(passwd)
# stat获取邮件数量和占用空间
print('Messages:%s, Size:%s' % ser.stat())
# 返回所有邮件的编号
resp, mails, octets = ser.list()
print(mails)
# 最新的一封
index = len(mails)  # 注意是从1开始的
resp, lines, octets = ser.retr(index)  # https://www.ibm.com/developerworks/cn/linux/l-cn-socketftp/
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
ser.quit()
