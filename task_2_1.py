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
for num in range(1, 100, 2):
    odd_numbers_cube.append(num ** 3)

# Решение a
print(sum_only_div(odd_numbers_cube, 7))

# Решение b и c (новый список не создавался)
for num in range(len(odd_numbers_cube)):
    odd_numbers_cube[num] += 17

print(sum_only_div(odd_numbers_cube, 7))
