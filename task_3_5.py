from random import choice, randint, shuffle

# Вариант функции без проверок входящих данных
def get_jokes(n):
    return  [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for x in range(n) ]


# Вариант функции без проверок входящих данных с флагом и именованным аргументом
def get_jokes1(n, rep=True):
    w_1, w_2, w_3 = nouns, adverbs, adjectives
    w_1.shuffle()
    w_2.shuffle()
    w_3.shuffle()
    return [f'{choice(w_1)} {choice(w_2)} {choice(w_3)}' if rep else f'{w_1[x]} {w_2[x]} {w_3[x]}' for x in range(n)]


# Вариант функции с неограниченным кол-вом слов
# и проверкой аргументов на ошибки
def get_jokes2(n, *args, rep=True):



    jokes = []
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
# print(get_jokes(3, [], [], [], rep=True))
