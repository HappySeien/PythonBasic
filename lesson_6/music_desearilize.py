# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json
# и group.pickle, прочитать из них информацию. И получить объект:
# словарь из предыдущего задания.


import json
import pickle


with open('group.json', 'r', encoding='utf-8') as f:
    a = json.load(f)

print(a)

with open('group.txt', 'rb') as file:
    b = pickle.load(file)

print(b)
