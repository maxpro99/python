def add_sale(*args):
    """
    Write new lines from *args to file
    bakery.csv
    in utf-8 code
    :param args: tuple of str
    :return: None
    """

    # По хорошему файл тоже передавать надо,
    # тогда будет логично, что скрипт вынесен

    # А еще хорошо бы было, если бы передавать можно было и int

    with open('bakery.csv', 'a', encoding='utf-8') as f:
        for sale in args:
            #  Была идея для перезаписи и индексации
            #  использовать ровное кол-во символов в строке:
            f.write(f'{sale}{" "*(15 - len(sale))}\n')
            # f.write(f'{sale}\n')


if __name__ == '__main__':
    import sys

    exit(add_sale(*sys.argv[1:]))
