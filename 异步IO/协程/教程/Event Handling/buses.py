# coding=utf-8
# 公交车管理模块
import coroutine
import handler


@coroutine.coroutine
def buesemgr(target):
    event, value = (yield)
    # event 是消息的类型 value
    if event == 'start':
        busdict = {}
        fragments = []
        while True:
            event, value = (yield)
            if event == 'start':
                fragments = []
            elif event == 'text':
                fragments.append(value)
            elif event == 'end':
                if value != 'bus':
                    busdict[value] = ''.join(str(fragments))
                else:
                    target.send(busdict)
                    break


@coroutine.coroutine
def filter_on_field(fieldname, value, target):
    while True:
        d = (yield)
        if d.get(fieldname) == value:
            target.send(d)


@coroutine.coroutine
def bus_location():
    while True:
        bus = (yield)
        print('%(route)s,%(id)s,"%(direction)s,%(latitude)s,%(logitude)s' % bus)


f = handler.Handler(r'异步IO\协程\教程\Event Handling\buses.json', buesemgr(
        filter_on_field('route', '22', 
            filter_on_field('direction', 'North Bound', 
            bus_location())))
)
f.attr_start(7574)
f.attr_text(7574)
f.attr_end('bus')
