# 3. Создать структуру файлов и папок, как написано в
# задании 2(при помощи скрипта или «руками» в проводнике).Написать
# скрипт, который собирает все шаблоны в одну папку templates, например:
# | --my_project
# ...
# | --templates
# | | --mainapp
# | | | --base.html
# | | | --index.html
# | | --authapp
# | | --base.html
# | | --index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html - файлы расположены в родительских папках(они
# играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

# И опять не понятно что делать
# Предположу, что надо объединить папки templates
# Но их повсюду искать, или объедиять только с конкретного уровня.
# Будем искать везде.
# И конкретно эта модель создана изначально "с пространтвом имён"
# Но ведь в общем случае названия внутренних папок и файлов
# в templates могут совпадать. Тут это исключение предусматривать не стал
# Тем более не понятно что делать - то-ли склевать папки, то-ли давать имена +'(n)'
# или ещё что-то
#
# Структуру папок и файлов берем после выполнения task_7_3

import os
import shutil


def copy_dir(from_dir, to_dir):
    for root, dirs, files in os.walk(from_dir):
        for n_dirs in dirs:
            if not os.path.exists(os.path.join(to_dir, n_dirs)):
                os.mkdir(os.path.join(to_dir, n_dirs))
        for n_file in files:
            shutil.copy2(os.path.join(root, n_file), os.path.join(to_dir, root.replace(from_dir, "")[1:], n_file))


root_dir = 'my_project'
dir_name = 'templates'
if not os.path.exists(os.path.join(root_dir, dir_name)):
    os.mkdir(os.path.join(root_dir, dir_name))

# идем по всем папкам, кроме той, в которую копируем
# Если находим такое-же имя, то копируем всё в нашу папку
for root, dirs, files in os.walk(root_dir):
    if dir_name in dirs and root != root_dir:
        copy_dir(os.path.join(root, dir_name), os.path.join(root_dir, dir_name))
