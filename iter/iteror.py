#coding=utf-8
#迭代器的使用
#迭代器类型Iterator
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