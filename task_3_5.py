from random import shuffle, choice, randint

# Вариант функции без проверок входящих данных
def get_jokes(n):
    return  [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for x in range(n) ]


# Вариант функции без проверок входящих данных, но зато с флагом и именованным аргументом
# Тут всё-таки не будем трогать глобальные переменные
def get_jokes1(n, rep=True):
    """
    Return list of random jokes string

    :param n: int number of jokes
    :param rep: Bool flag to allow repeat words in jokes
    :return: List of jokes string
    """
    w_1, w_2, w_3 = nouns, adverbs, adjectives
    shuffle(w_1)
    shuffle(w_2)
    shuffle(w_3)
    return [f'{choice(w_1)} {choice(w_2)} {choice(w_3)}' if rep else f'{w_1[x]} {w_2[x]} {w_3[x]}' for x in range(n)]


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(3))
print(get_jokes1(3, rep=False))
