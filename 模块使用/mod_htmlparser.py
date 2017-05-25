# coding=gb2312
# html������
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attr):  # ��ǩ����ʼ
        # pass  # print('<%s>' % tag)
        if tag == 'title':
            # print('Event��', attr, end='')
            pass
        elif tag == 'a':
            # ��ȡԪ�����Ϣ
            print('Event��%s, Link��%s, Event info��' % (attr[1][1], attr[0][1]), end='')

    def handle_endtag(self, tag):  # ��ǩ����ֹ
        pass  # print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):  # ����Ԫ��
        pass  # print('<%s/>' % tag)

    def handle_data(self, data):  # �����ǩ��ֵ
        print(data)

    def handle_comment(self, data):  # ����ע��
        pass  # print('<!--', data, '-->')

    def handle_charref(self, name):  # ����ת����ַ�
        pass  # print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''
<ul class="subnav menu" role="menu" aria-hidden="true">
<li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li></ul>
''')
