from requests import get, utils
from datetime import datetime

# >Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
#
# >Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
# Подумали, реализовали список.
#
# Подумали еще немного, и поняли, что в задании не хватает работы с валютами
# Справка об используемых Сокращениях и валютах
# Так как передаем строку, то могли бы и просто "манаты" писать, например
# Работы с номиналами курсов - те же сумы номинируются в рубли от 10 000 сумов
#
# Подумали еще немного, и решили не додумывать задание)

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
        answer.append(
            datetime.strptime(content[content.find('Date=') + 6:content.find('Date=') + 16], "%d.%m.%Y").date())
        return answer
    else:
        return None


print(currency_rates('Usd','eur'))