# coding=gb2312
# debug2
# pdb debug usng pdb module

import pdb

def foo(s):
    n = int(s)
    pdb.set_trace()
    return 10 / n


def main():
    foo('4')


main()