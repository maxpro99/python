# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/
# master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>).
#
# Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# Примечание: код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
#

# Не факт, что код будет работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
# Поскольку и данных просто списка может быть очень много.
# Т.е. по хорошему их тоже надо в файл, а не в оперативку программы

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    answer = [(line.split()[0], line.split()[5][1:], line.split()[6]) for line in f]

print(answer)
