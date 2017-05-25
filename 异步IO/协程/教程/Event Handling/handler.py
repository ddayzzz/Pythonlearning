# coding=utf-8
# JSONReader
import json


class Handler(object):

    def __init__(self, jsonfile, target):
        self.target = target
        jsonptr = open(jsonfile, 'r')
        self.data = json.load(jsonptr)
        jsonptr.close()

    def attr_start(self, name):
        self.target.send(('start', name))

    def attr_end(self, name):
        self.target.send(('end', name))

    def attr_text(self, name):
        self.target.send(('text', name))

    def attr_print(self, name):
        self.target.send(('print', name))



