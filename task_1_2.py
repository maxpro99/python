odd_numbers_cube = []


# Вынесенная функция подсчёта суммы цифр входящего числа
def digit_sum(in_number):
    digit_sum_var = 0
    rank = 1
    while in_number:
        digit_sum_var += in_number % 10 ** rank / 10 ** (rank - 1)
        in_number -= in_number % (10 ** rank)
        rank += 1
    return digit_sum_var


def sum_only_div(array, div):
    out_sum = 0
    for current_num in array:
        # на 0 % 7 проверять в данном случае не будем - массив начинается с 1
        if not digit_sum(current_num) % div:
            out_sum += current_num
    return out_sum


# Задание 2: Создаём список, состоящий из кубов нечетных чисел
# Позволю себе с вами не согласиться
# Основной код ниже И читается он явно и просто.
# В данном случае я доверяю вашему мнению больше, чем своему
# Поэтому прошу указть нга трудночитаемые места
# Задачу я решил неверно - ошибка в кол-ве элементов
# У меня в цикле было 100, а необходимо 1000
# Полностью согласен, что поставленная задача не была решена
# Сожалею, переделываю и отправляю снова.
# Работу фунций проверил - все работает как задумано

for num in range(1, 1000, 2):
    odd_numbers_cube.append(num ** 3)


# Решение a
print(sum_only_div(odd_numbers_cube, 7))
print('-------------')
print('-------------')
print('-------------')


# Решение b и c (новый список не создавался)
for num in range(len(odd_numbers_cube)):
    odd_numbers_cube[num] += 17
print(sum_only_div(odd_numbers_cube, 7))


# Решил сделать еще один вариант решения
# Также он желателен для проверки результатов
# Данное решение не соответствует условию задачи
# определять сумму цифр ТОЛЬКО арифметическими выражениями
print('oneline')
print(sum([x**3 for x in range(1, 1000, 2) if not sum([int(z) for z in list(str(x**3))]) % 7]))

# Но с моими функциями можно так сделать
print(sum([x**3+17 for x in range(1, 1000, 2) if not digit_sum(x**3) % 7]))
# И вариант c
print(sum([x**3+17 for x in range(1, 1000, 2) if not digit_sum(x**3+17) % 7]))
