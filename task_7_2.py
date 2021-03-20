# 2. * (вместо 1) Написать скрипт, создающий из config.yaml
# стартер для проекта со следующей структурой:
# Примечание: структуру файла config.yaml придумайте сами,
# его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
# - длина больше 255
# - Память кончилась
# - Совершенно непонятно как файлы от папок отличать
# - Надо бы обрабатывать комментарии

# Не ясно почему yaml.
# Не разбирали его, ни ссылок не видел на него...
# Да и в самом стандарте
# https://yaml.org/spec/1.2/spec.html
# описание приведенного примера не нашел
# Например "|--" - что за покемон?
# Непонятно также почему на первом уровне
# продолжается часть этого знака во всех строках
# а на нулевом нет? и на втором и на третьем нет?
# Непонятно как файлы от папок отличать

import os

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = f.readlines()

path = []
last_level = -1
for line in data:
    level = line.count('   ') + line.count('|  ')
    if level > last_level:
        path.append(line.strip().replace('|--', '').replace('|  ', '').replace('   ', ''))
    else:
        path[level] = line.strip().replace('|--', '').replace('|  ', '').replace('   ', '')
        for i in range(level, last_level):
            path.pop()

    # Папки от файфлов в данном примере будем различать наличием точки
    # И это опять плохая практика
    if '.' in path[level]:
        with open(os.path.join(*path), 'x', encoding='utf-8') as f:
            f.write('я файлик')
    else:
        if not os.path.exists(os.path.join(*path)):
            os.mkdir(os.path.join(*path))
    last_level = level

