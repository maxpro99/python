from random import shuffle, choice, randint

# Вариант функции без проверок входящих данных
def get_jokes(n):
    return  [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for x in range(n) ]


# Вариант функции без проверок входящих данных, но зато с флагом и именованным аргументом
# Тут всё-таки не будем трогать глобальные переменные
def get_jokes1(n, rep=True):
    w_1, w_2, w_3 = nouns, adverbs, adjectives
    shuffle(w_1)
    shuffle(w_2)
    shuffle(w_3)
    return [f'{choice(w_1)} {choice(w_2)} {choice(w_3)}' if rep else f'{w_1[x]} {w_2[x]} {w_3[x]}' for x in range(n)]


# Идём на усложнение задачи
# Вариант функции с неограниченным кол-вом слов.
# Всё-таки в такой функции намоного логичнее
# использовать передачу аргументов в функцию,
# и не трогать глобальные переменные.
# И в месте вызова функции это будет выглядеть нагляднее.
# Также озаботимся и проверкой аргументов на ошибки
def get_jokes2(n, *args):
    """
    Return n strings from string with random *word parameters from lists of strings

    :param n: number of strings
    :param args: string with text and '*word's , lists of strings
    :return: list of strings
    """

    jokes = []
    if n and len(args) and isinstance(n,int) and isinstance(args[0],str):

        jokes.append[x for x in range]



    if len(args):
        for num_joke in range(n):
            joke = ''
            for num_words in args:
                joke += choice(num_words) + ' '
            joke.rstrip(' ')
            jokes.append(joke)
    else:
        jokes.append('Нет вариантов слов в виде перечисляемых аргументов, нет и шуток!')
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(3))
print(get_jokes1(3, rep=False))
print(get_jokes2(4, 'мой *word еще *word очень *word ', nouns, adverbs,adjectives))
