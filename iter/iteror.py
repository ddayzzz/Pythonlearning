#coding=utf-8
#��������ʹ��
#����������Iterator
li=['ge','gewghr','gfhf']
print(type(li))
print(type(iter(li)))
fi=iter(li)
while True:
    try:
        i=next(fi)
        print(i)
    except StopIteration:
        break