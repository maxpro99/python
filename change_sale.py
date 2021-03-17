def change_sale(*args):
    """
    Set new value from args[1]
    to lines from args[0]
    in file bakery.csv
    in utf-8 code
    :param args: tuple of str value, lines
    :return: None
    """

    # По хорошему файл тоже передавать надо,
    # тогда будет логично, что скрипт вынесен

    # А еще хорошо бы было, если бы передавать можно было и int

    # Тут надо бы проверку введеных аргументов сделать
    # но ведь задание не совсем про это?
    start_pos = 0
    if len(args) != 2:
        print('При запуске введите два аргумента: номер записи и новое значение')
        exit(1)
    else:
        start_pos = int(args[0])-1
        new_value = args[1]
    if start_pos < 0:
        start_pos = 0
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        if len(new_value) < 16:
            f.seek(17 * start_pos)
            f.write(new_value)
        else:
            # Тут моржно было бы реализовать вырывание пробелов из нескольких следующих строк.
            # И совместить это с записью вообще всего в другой файл
            # И только после окончания всех работ затереть им существующий.
            # Но мы просто поругаемся
            print('Вы хотите продать слишком много булочек.\n'
                  'Налицо признаки коррупционной составляющей\n'
                  'Ждите! За вами уже выехала бригада быстрого реагирования ФСБ!')


if __name__ == '__main__':
    import sys

    exit(change_sale(*sys.argv[1:]))