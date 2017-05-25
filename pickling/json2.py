# coding=gb2312
# json 的高级使用
import json


class student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2json(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def json2student(d):
    return student(d['name'], d['age'], d['score'])


s = student(name='Fang', age=25, score=99)
di = json.dumps(s, default=student2json)
s1 = json.loads(di, object_hook=json2student)
print(type(s1))
