# coding=gb2312
# ���л��Ĳ���
"""
import pickle
d = dict(name='Bob', age=20, score=88)
f = open('pickling\pickle.txt', 'rb')
print(pickle.load(f))
f.close()
"""

# json�汾�Ĵ洢
import json
rdr = open('pickling/json_read.json', 'r')  # ���ļ��д�JSON�ļ�
reader = json.load(rdr)  # ��json�ļ��ж�ȡ
print(type(reader), '\n', reader)
# д�뵽������json�ļ�
rdr.close()
writer = open('pickling/json_store.json', 'a')
json.dump(reader, writer)

# json.dump(json.loads('{"Country":"China"}'), writer)
writer.close()