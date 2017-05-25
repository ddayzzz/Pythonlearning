#python
def spam():
    try:
        global eggs
        e=eggs / 0
    except:
        print('DIVIDE BY ZERO')
eggs=0
spam()
print(eggs)