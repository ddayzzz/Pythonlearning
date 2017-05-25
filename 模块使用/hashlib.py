# coding=utf-8
# hashlib算法
import hashlib
"""
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
"""


# 设计一个保存用户登录信息的程序
userinfo = dict({})
class UserInfo(object):

    def login(self, username, passwd):
        global userinfo
        if username in userinfo.keys():
            md = hashlib.md5()
            md.update(username.encode('utf-8'))
            md.update(passwd.encode('utf-8'))
            md.update('_the_salt'.encode('utf-8'))
            comp = md.hexdigest()
            if comp == userinfo[username]:
                print('Welcome!')
            else:
                print('Incorrect password')
        else:
            print('No such username')

    def __setitem__(self, username, passwd):
        global userinfo
        md = hashlib.md5()
        md.update(username.encode('utf-8'))
        md.update(passwd.encode('utf-8'))
        md.update('_the_salt'.encode('utf-8'))
        comp = md.hexdigest()
        userinfo[username] = comp

    def display(self):
        global userinfo
        for k, v in userinfo.items():
            print('Username : ', k, ',Password(MD5) : ', v)


if __name__ == '__main__':
    i = UserInfo()
    i['shu'] = 'abc'
    i['fang'] = 'bbc'
    i.login('shu', 'abc')
    i.display()
