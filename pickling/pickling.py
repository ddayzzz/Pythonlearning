# coding=gb2312
# 序列化的操作
"""
import pickle
d = dict(name='Bob', age=20, score=88)
f = open('pickling\pickle.txt', 'rb')
print(pickle.load(f))
f.close()
"""

# json版本的存储
import json
rdr = open('pickling/json_read.json', 'r')  # 从文件中打开JSON文件
reader = json.load(rdr)  # 从json文件中读取
print(type(reader), '\n', reader)
# 写入到其他的json文件
rdr.close()
writer = open('pickling/json_store.json', 'a')
json.dump(reader, writer)

# json.dump(json.loads('{"Country":"China"}'), writer)
writer.close()