def num_translate(s=''):
    """
    Translate numbers from 0 to 10 from English into Russian
    with the same first char case and lowercase other char

    :param s: string-numbers in English
    :return: string-numbers in Russian or None
    """
    my_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    _res = my_dict.get(s.lower())
    if _res is None or s[0].islower():
        res = _res
    else:
        res = _res[0].upper() + _res[1:]
    return res


print('num_translate :', num_translate('TeN'))
