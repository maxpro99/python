# 2. *(вместо 1)
# Ну тут "вместо" не получится, толкько а добавочку
# Найти IP адрес спамера и количество отправленных им
# запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше
# всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_list = [line.split()[0] for line in f]

# Очень долгий метод
# res = (0, 1)
# for x in ip_list:
#     print(x)
#     if ip_list.count(x) > res[1]:
#         print(f'{x}:{ip_list.count(x)}')
#         res = x, ip_list.count(x)
# print(ip_list)
# print(res)

# Алгоритм быстрее, НО
# уверен, что есть и более простой, быстрый
# и более "пайтонистый" способ
# но после того, как начинаешь искать,
# вопросов больше чем ответов
# Так и не оговорены сколько памяти и времени
# что кушает
ip_list.sort()
len_ip_list = len(ip_list)
res = (0, 1)
current_num_ip = 0
while current_num_ip < len_ip_list:
    if ip_list.count(ip_list[current_num_ip]) > res[1]:
        res = ip_list[current_num_ip], ip_list.count(ip_list[current_num_ip])
        print(res)
    current_num_ip += res[1]
print(f'C {res[0]} пришло {res[1]} запросов, и это максимальное кол-во в этом логе')


# print(sorted(answer, key=lambda answer_el: answer_el[0]))
