# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам
# и путь к выходному файлу со словарём. Проверить работу
# скрипта для случая, когда все файлы находятся в разных папках.


# я так понял, что задаём именно пути, а не имена файлов с путями
# и что делать, если указано одна, две, три или четыре папки??
# Решение такое:
#
# 1. не указано папок - ищем все файлы в текущей директории
# Если третий файл есть, то спрашиваем (R)ewrite file /(A)dd info
#
# 2. Указана одна папка. Ищем файлы для чтения там.
# Файл для записи - ищем в текущей, если такой файл есть, то спрашиваем (R)ewrite file /(A)dd info
# Если файла нет, то пишем его в текущую директорию
#
# 3. Указано две папки.
# Ищем первый файл для чтения в первой папке,
# Второй файл для чтения ищем во второй папке,
# файл для записи - ищем в текущей, если третий файл есть, то спрашиваем (R)ewrite file /(A)dd info
# Если файла нет, то пишем его в текущую директорию
#
# 4. Указано три папки.
# Ищем первый файл для чтения в первой папке,
# Второй файл для чтения ищем во второй папке,
# файл для записи - ищем в третей папке, если третий файл есть, то спрашиваем (R)ewrite file /(A)dd info
# Если файла нет, то пишем его в третью директорию
#
# 5. Указано четыре и более папки.
# Пишем ошибку.

import sys
import os.path
import json

path_users = ''
path_hobby = ''
path_users_hobby = ''
if len(sys.argv) > 4:
    print('Слишком много параметров')
    exit(1)
elif len(sys.argv) < 2:
    path_users = ''
    path_hobby = ''
    path_users_hobby = ''
elif len(sys.argv) == 2:
    path_users = sys.argv[1]
    path_hobby = sys.argv[1]
    path_users_hobby = ''
elif len(sys.argv) == 3:
    path_users = sys.argv[1]
    path_hobby = sys.argv[2]
    path_users_hobby = ''
elif len(sys.argv) == 4:
    path_users = sys.argv[1]
    path_hobby = sys.argv[2]
    path_users_hobby = sys.argv[3]
path_users += 'users.csv'
path_hobby += 'hobby.csv'
path_users_hobby += 'users_hobby.txt'

if os.path.isfile(path_users) and os.path.isfile(path_hobby):
    users_hobby_method = 'w'
    if os.path.isfile(path_users_hobby):
        if input('File "users_hobby.txt" already exist. '
                 'Do you want Rewrite file(default - press Enter) or (A)dd info to file: ').lower() == 'a':
            users_hobby_method = 'a'
    # Вариант без создания переменных
    # Работа проверена только на вложенных папках.
    # При этом необходимо папки заканчивать обратным слэшем.
    # with open(path_users, 'r', encoding='utf-8') as users_f, \
    #         open(path_hobby, 'r', encoding='utf-8') as hobby_f, \
    #         open(path_users_hobby, users_hobby_method, encoding='utf-8') as users_hobby_f:
    #     for line in users_f:
    #         users_hobby_f.write(f'{line.rstrip()}:zzz {hobby_f.readline().rstrip() or None}\n')
    #     if hobby_f.readline():
    #         exit(1)
# Присмотримся к заданию: В какой раз? В 6_5 раз выходит.
# Реальнро странная история.
# В предыдущих заданиях чаще вопрос программирования,
# алгоритмирования был.
# А нынче вопрос именно обращения с языком.
# НО!
# По факту так и не было глубокого изучения ни структур данных,
# ни базы по языку.
# Как работает интерпретатор, сколько памяти занимают какие структуры.
# Как работает с оперативкой? не ясно....
# может хранить переменных на 50 Gb при оперативке 16?
# Смысл задания, если мы из файла, который должен занимать больше,
# чем оперативка запишем все в переменные, которые будут занимать памяти тоже больше,
# чем оперативка?
# Для чего выбирать тип хранения? Для каких условий?
# Искать его один раз(словарь), или составлять общую статистику (множество)?
# Или составлять иерархически сложную структуру (тогда наверное list)?
# Конкретно такая инфа вообще не может быть больше
# 5 млрд. людей на 100 байт (завышенная средняя) = 500 Gb)))))
# И ещё еинтересно, что после строчки в задании:
#
# "Преобразовать в какой-нибудь контейнерный тип
# (список, кортеж, множество, словарь).
# Обосновать выбор типа."
#
# Идёт строчка:
#
# "В СЛОВАРЕ должны храниться данные, полученные в результате парсинга."
#
# Пока делал данную работу было много вопросов,
# часть из которых просто повисла в воздухе,
# а часть решена. НО с большей долей вероятности неправильно, костылями.
#
# И получилось, что вместо разбора сложного на составные,
# и разбора реальных задач, мы занимаемся изобретением велосипеда.


    # Словарь хороший способв хранения данных для поиска по ключу,
    # но ставить ФИО на ключ ненормальная идея.
    # Один и тот же ключ может встретися с большой вероятностью.
    # Да и поиск в данном случае желательно иметь созможность вести по всем полям.
    # Поэтому логично для очень быстрого поиска использовать в таких случаях
    # взаимосвязанные избыточные словари с идентификаторами.
    # т.е. основные словари с ключом идентификатором,
    # и списком ссылок на все остальные словари.
    # Подозреваю, что примерно так устроены базы данных.
    # Но мои потуги реализовать это несмотря на алгоритмический
    # выигрыш, уверен, будут проигрывать и в скорости и в памяти
    # каким-то правильным способам, которые уже есть, но
    # мне не сказали.
    # Тем более, что файл, по условиям задачи, и так слишком большой,
    # И создавать большую структуру данных,
    # сопоставимую с размером файла в памяти не получится.
    # Что делать? Как правильно решать?
    # Дай ответ. Не даёт ответа....

    with open(path_users, 'r', encoding='utf-8') as users_f, \
            open(path_hobby, 'r', encoding='utf-8') as hobby_f:
        users_hobby_dict = {line[0]: [*line[1].rstrip().split(','), hobby_f.readline().rstrip().split(',') or None] for line in enumerate(users_f, 10000)}
        # Проверяем что получилось)))
        print(users_hobby_dict)
        # Запишемся в файл
        # Использоую JSON
        # Хотя на уроке сказали, что раз в задании ничего про библиотеки,
        # То подразумевается, что ничего и не надо использовать.
        # Но вроде как JSON проходили,
        # и именно его понимание надо показать в задании.
        # Опять задание не четко сформулировано.
        with open(path_users_hobby, users_hobby_method, encoding='utf-8') as users_hobby_f:
            users_hobby_f.write(json.dumps(users_hobby_dict))

        # Если еще остались хобби, то выход с кодом 1
        # Кстати вопрос:
        # в task_6_4 после очередных переделок
        # эта срочка оказалась в def
        # Но работает))) А как транслирует код?
        if hobby_f.readline():
            exit(1)





else:
    print('Не хватает исходных данных.')



