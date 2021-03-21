# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
# -------
# Задача хорошая, но почему сохраниение в словарь?
# Словарь - это хэш-таблица, и отсортировать её нельзя.
# В случае в методичке данные выведены по порядку, поэтому видно вторую границу
# А в общем случае такого не будет(((((((((

import os
import random
import json

# создадим папку для задания
my_dir = 'folder_to_task_7_5'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

# Но проверили и на других папках
# my_dir = '../../'


# Наполним ёё файлами
# Если их там мешьше 500
if len(os.listdir(my_dir)) < 500:
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    extensions = ['zip', 'txt', 'my', 'py', 'xxx', 'bin']
    for _ in range(10 ** 3):
        f_name_tuple = (''.join(random.sample(letters, random.randint(4, 8))), '.', random.choice(extensions))
        f_name = ''.join(f_name_tuple)
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
        with open(os.path.join(my_dir, f_name), 'wb') as f:
            f.write(f_content)

summary = [[0 for _ in range(6)], [[] for _ in range(6)]]
for root, dirs, files in os.walk(my_dir):
    for file in files:
        key_size = len(str(os.stat(os.path.join(root, file)).st_size)) - 1
        if key_size > 5:
            key_size = 5
        summary[0][key_size] += 1
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        if ext not in summary[1][key_size]:
            summary[1][key_size].append(ext)
summary_dict = {10 ** (i + 1): (summary[0][i], summary[1][i]) for i in range(6)}

with open(f'{my_dir}_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary_dict, f)
