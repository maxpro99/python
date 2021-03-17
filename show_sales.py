def show_sales(*args):
    """
    Print lines from first args (0 if absent)
    to seconf args (end if absent) from *args
    to file bakery.csv
    in utf-8 code
    :param args: tuple of str
    :return: None
    """

    # По хорошему файл тоже передавать надо,
    # тогда будет логично, что скрипт вынесен

    # А еще хорошо бы было, если бы передавать можно было и int

    # Тут надо бы проверку введеных аргументов сделать
    # но ведь задание не совсем про это?
    start_pos = 0
    finish_pos = 0
    if len(args) > 2:
        exit(1)
    elif len(args) == 2:
        start_pos = int(args[0])-1
        finish_pos = int(args[1])
    elif len(args) == 1:
        start_pos = int(args[0])-1
    if start_pos < 0:
        start_pos = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if finish_pos:
            print(''.join(f.readlines()[start_pos:finish_pos]))
            # Не факт, что такой итератор не читайет все равно больше, чем память)))))))))))
        else:
            print(''.join(f.readlines()[start_pos:]))


if __name__ == '__main__':
    import sys

    exit(show_sales(*sys.argv[1:]))
