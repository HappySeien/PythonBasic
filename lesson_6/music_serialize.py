# 1: Создать модуль music_serialize.py. В этом модуле определить словарь
# для вашей любимой музыкальной группы, например:

import json
import pickle

my_favourite_group = {
    'name': 'Король и шут',
    'tracks': ['лесник', 'марионетки', 'добрые люди'],
    'Albums': [{'name': 'король и шут', 'year': '1999'},
               {'name': 'продовец кошмаров', 'year': '2006'},
               {'name': 'TODD act 1', 'year': '2011'}]
}

# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json,
# group.pickle соответственно. В файле group.json указать кодировку utf-8.

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

print(f)

with open('group.txt', 'wb') as file:
    pickle.dump(my_favourite_group, file)

print(file)
print('Записано')
