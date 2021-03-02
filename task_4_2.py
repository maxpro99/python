from requests import get, utils

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
#
# >Можно ли, используя только методы класса str, решить поставленную задачу?
# Да. Решено.
#
# >Функция должна возвращать результат числового типа, например float.
# >Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Да.
#
# >Сильно ли усложняется код функции при этом?
# Нет, можно сразу считать в сотых долях копейки, т.е. 1 рубль 12 копеек считать как 11200 сотых копейки
# Может даже упростится код в некоторых местах.
#
# >Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Добавили проверку
#
# >Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# Да. Сделали.
#
# >В качестве примера выведите курсы доллара и евро.
# Вывели.
def currency_rates(*args):
    """
    Return currency exchange rates to ruble for today.
    currency_rates(usd, eur): [02/02/2021, {'USD': 744373}]

    :param args: tuple of str
    :return: list [date, {currency: currency exchange rates}
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    answer = []
    for currency in args:
        start_pos = content.find(currency.upper())
        if start_pos == -1:
            answer.append(None)
        else:
            answer.append(float(content[content.find('ue>', start_pos) + 3:
                                        content.find('</V', start_pos)].replace(',', '.')))
    if len(answer):
        return answer
    else:
        return None


print(currency_rates('usd', 'eur'))
