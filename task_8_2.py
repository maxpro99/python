# 2. * (вместо 1) Написать регулярное выражение для парсинга
# файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/
# Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>,
# <request_datetime>,
# <request_type>,
# <requested_resource>,
# <response_code>,
# <response_size>),
# например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = (
# '188.138.60.101',
# '17/May/2015:08:05:49 +0000',
# 'GET',
# '/downloads/product_2',
# '304',
# '0')
# Примечание: вы ограничились одной строкой
# или проверили на всех записях лога в файле?
# Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

parsed_row = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # Вариант 3
        parsed_row.append(re.sub(r' - - \[|] "| HTTP/1.1" | ', '~', line).split('~')[:7])

        # Вообще для логов записанных с определнной структурой
        # нет большого смысла использовать регулярные выражения
        # И распарсить можно был-бы поэлегантнее
        # Но согласно практическому заданию будем делать именно
        # с помощью регулярных выражений

        # Сейчас закомментим, но вообще проверили строки на то,
        # что еще бывает в них, нет ли особенных строк?
        # if 'HTTP/1.1"' not in line.split():
        #     print(line)
        # if '+0000]' not in line.split():
        #     print(line)
        # if '"GET' not in line.split():
        #      print(line)

        # Вариант 1
        # parsed_row.append(re.sub(r' - - \[|] "| HTTP/1.1" | ".+"', ' ', line).split())
        # Надо уточнить, что тут часть строки +0000
        # видимо смещение часового пояса
        # записана в отдельную переменную, что не совсем соответсвует заданию

        # Вариант 2
        # parsed_row.append(re.sub(r' - - \[|] "| HTTP/1.1" | ".+"| ', '~', line).split('~')[:7])

        # Вариант 4
        # Пока дописывать не буду,
        # но следуя логике урока тут
        # надо представить регулярные
        # выражения для каждой переменной
        # Например
        remote_addr = re.findall(r'\d+\.\d+\.\d+\.\d+\b', line)
        print(f'Remote address: {remote_addr}')
        request_datetime = re.findall(r'\d+\/\w+\/.+ \+\d{4}', line)
        print(f'Request datetime: {request_datetime}')
        # Ну так же можно продолжать и дальше,
        # Но это неправильный подход,
        # Поскольку не ясно чего мы оттуда выдираем,
        # Ведь исходим уже из просмотра файла,
        # Из порядка в нём.
        # В очередной раз повторю свою мысль,
        # что задания должны быть, примерно, как в codewars
        # Загрузил, и получи результат с автопроверкой.
        # И учителя не грузить, и ученик не сомневается в себе,
        # И на множество условий может автоматика проверить.
        request_type = re.findall(r'GET|HEAD', line)
        print(f'Request type: {request_type}')
        # requested_resource = re.findall(r'\/w+d+.\d+.\d+.\d+.\b', line)
        # print(f'requested_resource: {requested_resource}')
        # response_code = re.findall(r'\d+.\d+.\d+.\d+.\b', line)
        # print(f'response_code: {response_code}')
        # response_size = re.findall(r'\d+.\d+.\d+.\d+.\b', line)
        # print(f'response_size: {response_size}')

print(parsed_row)
