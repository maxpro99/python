import time


def no_problem(num, val):
    # переписать процедуру универсальнее
    answer = True
    # проверим строку
    if val in [x[1] for x in enumerate(field) if x[0] // 9 == num // 9 and x[0] != num]:
        answer = False
    # проверим столбец
    if answer and val in [x[1] for x in enumerate(field) if x[0] % 9 == num % 9 and x[0] != num]:
        answer = False
    # проверим мини-квадратик
    if answer and val in [x[1] for x in enumerate(field) if x[0] % 9 == num % 9 and x[0] != num]:
        answer = False
    return answer


field = [0 for _ in range(81)]
chek_fields = []
# chek_fields.append() = [x for x in range(81) if x]
# chek_fields.append() = []
# chek_fields.append() = []
el = 0

while 0 <= el < len(field):
    while el < len(field) and field[el] < 9:
        field[el] += 1
        # time.sleep(0.1)
        print(f'\b\b\b', end='')
        print(f' {field[el]} ', end='')
        if no_problem(el, field[el]):
            print('XXX', end='')
            el += 1
    if el < len(field):
        field[el] = 0
        # time.sleep(0.1)
        print(f'\b\b\b', end='')
        el -= 1
if el > 0:
    print('Solved')
    # Надо печать сделать поуниверсальнее для любых полей
    print(' ', '  '.join([str(el[1]) + '\n' if (el[0] + 1) % 9 == 0 else str(el[1]) for el in enumerate(field)]))
else:
    print('No have solve')