from requests import get, utils


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
            print(answer)


    # print(content)
    # print(type(content))


currency_rates('usd', 'eur')
