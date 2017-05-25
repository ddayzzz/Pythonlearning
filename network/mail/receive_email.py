# coding=gb2312
# POP3Э�����ʼ�
# ;��MUA ->MDA(�ʼ�����) ->(����)MUA
import poplib
from email.parser import Parser
# �����ʼ�
from email.header import decode_header
from email.utils import parseaddr
import random

"""EMAILԭʼ�ı�
--===============4557463990664328221==
Content-Type: text/html; charset="utf-8"  ��ͷ��
MIME-Version: 1.0  ��ͷ��
Content-Transfer-Encoding: base64  ��ͷ��

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
AAEAAAEVAAMAAAAxxxxBASE64���롣���ԡ�����
--===============4557463990664328221==--
"""


def decode_str(s):
    value, charset = decode_header(s)[0]  # ����ͷ�ĵ�һ������ ֵ����Content-Type��ֵ
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()  # �����ʲô����أ������Ƿ�ֹ����������û��getchar���ѡ�� ���û�з��ص���None�Ͳ���ô�ÿ��ˡ�������ֻ��text html����
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# ������ʾ
def print_info(msg, indent=0):
    if indent == 0:  # ���������Ƿ����ʼ���Ϣ�ı��� ������ڽ�������������� ����Ҫ+1 ��˼�����һ��������TAB
        for header in ['From', 'To', 'Subject']:  # �����ʼ�����Ϣ
            value = msg.get(header, '')  # ��ȡÿһ����Ϣ
            if value:
                if header == 'Subject':  # �������⴦��
                    value = decode_str(value)  # ����
                else:
                    hdr, addr = parseaddr(value)  # ��������ĵ�ַ
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, value)  # name�Ƿ����߻������ռ���
            print('%s%s: %s' % ('   ' * indent, header, value))  # ��ӡ��Ϣ
    if (msg.is_multipart()):  # �Ƿ��Ǹ�����
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))  # ÿһ����������Ҫ�����ó��� �����Ҫ���ڱ�ע���ı��
            print_info(part, indent + 1)  # �ݹ� ��ʾ�����������
    else:
        content_type = msg.get_content_type()  # ������Ƿֽ�ÿһ���������Ĺ���
        if content_type == 'text/pain' or content_type == 'text/html':  # �ı�����HTML�ı�
            content = msg.get_payload(decode=True)  # ����Ϳ�����
            charset = guess_charset(msg)  # ��ȡ���ܵı���
            if charset:
                content = content.decode(charset)  # ָ���������
            print('%sText: %s' % ('   ' * indent, content + '...'))  # ��ʾ����
        else:
            print('%sAttachment: %s' % ('   ' * indent, content_type))  # �����ĸ�ʽ��ӡ��Ϣ
            content = msg.get_payload(decode=True)  # ����Ϳ�����
            with open(('ATTACH_%d' % random.randint(0, 12)), 'wb') as fptr:  # ��ֹ�ļ���ͻ
                fptr.write(content)  # ֱ�������ļ�


# ��ȡ�˻���Ϣ
em = '2419940233@qq.com'
passwd = 'pykhxqxdwjfpdjge'  # �ҿ�������Ȩ�� ��������Ȩ���½
pop3_server = 'pop.qq.com'
# ����pop������
ser = poplib.POP3_SSL(pop3_server, 995)
ser.set_debuglevel(1)
print(ser.getwelcome().decode('utf-8'))
# ��¼������
ser.user(em)
ser.pass_(passwd)
# stat��ȡ�ʼ�������ռ�ÿռ�
print('Messages:%s, Size:%s' % ser.stat())
# ���������ʼ��ı��
resp, mails, octets = ser.list()
print(mails)
# ���µ�һ��
index = len(mails)  # ע���Ǵ�1��ʼ��
resp, lines, octets = ser.retr(index)  # https://www.ibm.com/developerworks/cn/linux/l-cn-socketftp/
# lines�洢���ʼ���ԭʼ�ı���ÿһ��,
# ���Ի�������ʼ���ԭʼ�ı�:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# �Ժ�������ʼ�:
msg = Parser().parsestr(msg_content)
print_info(msg)
# ���Ը����ʼ�������ֱ�Ӵӷ�����ɾ���ʼ�:
# server.dele(index)
# �ر�����:
ser.quit()
