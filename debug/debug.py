# coding=utf8
# debug segmentation usage
try:
    print('try...')
    jk = len(2)
    print('rest...')
except ZeroDivisionError as e:
    print('ZeroDivision...', e)
except ValueError as e:
    print('Value exception...')
except BaseException as e:
    print('standard error...', e.__class__)  # catch all potential erro and print the erorr's type
else:
    print('no errors...')
finally:
    print('finally...')
print('END')