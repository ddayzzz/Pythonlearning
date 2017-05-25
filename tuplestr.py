#python
# coding=gb2312
import pprint
dic={'apple':'red','pear':'yellow','grape':'green'}
for v in dic.keys():#打印key
    print(v)
for k,v in dic.items():#打印key和value
    print('key :'+str(k)+' value :'+str(v),end='\n')
#默认替换：
print(dic.setdefault('nut','brown'))
print(dic.setdefault('apple','green'))
#打印

socket={'shu':{'school':['TJPU','XGYZ','JS'],'sex':'male'},'Liu':{'school':['XTU','JS'],'sex':'female'}}
print(socket)#这个不美观 使用pprint就很好，可以处理嵌套的value
pprint.pprint(socket)
print(pprint.pformat(socket))#等价语句