#coding=utf8
#zip
import zipfile
import pprint
zf=zipfile.ZipFile('password.zip','r')
print(zf.namelist())
#zf.write('gaibian.pdf',compress_type=zipfile.ZIP_DEFLATED)
print(zf.namelist())
zf.extractall('fsfs',pwd=str('19971222').encode('utf_8'))
zf.close()
