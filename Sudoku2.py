import time
import copy

len_field = 81
links_field = [set.union(
    {x for x in range(i // 9 * 9, i // 9 * 9 + 9) if x != i},
    {x for x in range(i % 9, len_field, 9) if x != i},
    {x for x in range(i // 9 // 3 * 27 + i % 9 // 3 * 3, i // 9 // 3 * 27 + i % 9 // 3 * 3 + 3) if x != i},
    {x for x in range(i // 9 // 3 * 27 + i % 9 // 3 * 3 + 9, i // 9 // 3 * 27 + i % 9 // 3 * 3 + 3 + 9) if x != i},
    {x for x in range(i // 9 // 3 * 27 + i % 9 // 3 * 3 + 18, i // 9 // 3 * 27 + i % 9 // 3 * 3 + 3 + 18) if x != i})
    for i in range(len_field)]
start_field = [0 for _ in range(len_field)]
start_field[0] = 8
start_field[11] = 3
start_field[12] = 6
start_field[19] = 7
start_field[22] = 9
start_field[24] = 2
start_field[28] = 5
start_field[32] = 7
start_field[40] = 4
start_field[41] = 5
start_field[42] = 7
start_field[48] = 1
start_field[52] = 3
start_field[56] = 1
start_field[61] = 6
start_field[62] = 8
# далее 17 заполненная
start_field[65] = 8
# start_field[66] = 5
start_field[70] = 1
start_field[73] = 9
start_field[78] = 4

field = copy.deepcopy(start_field)
start_field.append(0)

cell, solved = 0, 0
start_time = time.time()
step = 1
iteration = 0
print(f'Iteration: {iteration:<16,}', end='')
while cell >= 0:
    iteration += 1
    if iteration % 100000 == 0:
        print('\b'*16 + f'{iteration:<16,}', end='')

    if start_field[cell] != 0:
        while start_field[cell] != 0 and 0 <= cell < len_field:
            cell += step
    else:
        field[cell] += 1
        while field[cell] < 10 and field[cell] in {field[x] for x in links_field[cell]}:
            field[cell] += 1
        if field[cell] < 10:
            step = 1
            cell += step
        else:
            field[cell] = 0
            step = -1
            cell += step
    if cell == len_field:
        solved += 1
        print()
        print(f'Solved: {solved} in {time.time() - start_time} in iteration {iteration:<8}')
        print(' ',
              '  '.join([str(el[1]) + '\n' if (el[0] + 1) % 9 == 0 else str(el[1]) for el in enumerate(field)]))
        print(f'Iteration: {iteration:<16,}', end='')
        step = -1
        cell += step
print(f'Done. Solved: {solved} in {time.time() - start_time}')
