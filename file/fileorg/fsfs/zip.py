#coding=gb2312
#zip
import zipfile
import pprint
zf=zipfile.ZipFile('zip.zip','r')
print(zf.namelist())
#zf.write('gaibian.pdf',compress_type=zipfile.ZIP_DEFLATED)
print(zf.namelist())
for fl in zf.namelist():
    finfo=zf.getinfo(fl)
    #if finfo.__dir__():
    #    print('dirname:'+fl)
    #else:
    print('filename:'+fl+',size:'+str(finfo.compress_size))
zf.close()
