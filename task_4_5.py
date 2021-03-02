# >Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# >Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# >Убедиться, что ничего лишнего не происходит.
# Там так и сделали
# в модуле utils и task_4_4
#
# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
#
# А вот тут в задании опять небольшая путаница:
# создаём модуль utils или всё-таки task_4_5
# Я доработал именно utils сначала, теперь скопировал всё в task_4_5
# Они индентичны и должны работать как при импорте, так и из консоли
# Но из-за формата результата, и его вывода
# чтобы было как в примере - добавил принт, сменил list на tuple
# НО! Чтобы возвращала функция именно как в примере:
# без скобок с запятой дата через черточки
# У меня не вышло((((((
# Круто, если подскажете как (Ну если только не строку возвращает, а то так и я смогу)

def currency_rates(*args):
    """
    Return currency exchange rates to ruble for today.
    currency_rates(usd, eur): [02/02/2021, {'USD': 744373}]

    :param args: tuple of str
    :return: list [date, {currency: currency exchange rates}
    """

    from requests import get, utils
    from datetime import datetime

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    answer = ()
    for currency in args:
        start_pos = content.find(currency.upper())
        if start_pos == -1:
            answer += (None,)
        else:
            answer += (float(content[content.find('ue>', start_pos) + 3:
                                        content.find('</V', start_pos)].replace(',', '.')),)
    if len(answer):
        answer += (
            datetime.strptime(content[content.find('Date=') + 6:content.find('Date=') + 16], "%d.%m.%Y").date(),)
        print(*answer)
        return answer
    else:
        print('А где ваши аргуметы?')
        return (None)

if __name__ == '__main__':
    import sys

    exit(currency_rates(*sys.argv[1:]))
