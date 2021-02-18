answer = 'Wrong answer'

#
# duration_names = [['дн','час','мин','сек'],[24,60,60,1],[0,0,0,0]]

while not answer.isdigit():
    answer = input('Введите промежуток времени в секундах (цифрами целое число от 0 до 64000):')

duration = int(answer)
print(duration, 'секунд - это :')

# вариант в котором будут печататься и 0 дней и 0 часов и 0 минут
print(f"{duration // (24 * 60 * 60)} дн {duration // (60 * 60) % 24} час {duration // 60 % 60} мин {duration % 60} сек")

# вариант в котором 0 не будут печататься кроме секунд, но даже в середине(
print(f"{duration // (24 * 60 * 60)} дн " * bool(duration // (24 * 60 * 60)) +
      f"{duration // (60 * 60) % 24} час " * bool(duration // (60 * 60) % 24) +
      f"{duration // 60 % 60} мин " * bool(duration // 60 % 60) +
      f"{duration % 60} сек")

# вариант в котором 0 не будут печататься, но даже в середине(
print(f"{duration // (24 * 60 * 60)} дн " * bool(duration // (24 * 60 * 60)) +
      f"{duration // (60 * 60) % 24} час " * bool(duration // (60 * 60) % 24) +
      f"{duration // 60 % 60} мин " * bool(duration // 60 % 60) +
      f"{duration % 60} сек" * bool(duration % 60))

# вариант в котором 0 не будут печататься согласно заданию
print(f"{duration // (24 * 60 * 60)} дн " * bool(duration // (24 * 60 * 60)) +
      f"{duration // (60 * 60) % 24} час " * bool(
    bool(duration // (60 * 60) % 24) or bool(duration // (24 * 60 * 60))) +
      f"{duration // 60 % 60} мин " * bool(
    bool(duration // 60 % 60) or bool(duration // (60 * 60) % 24) or bool(duration // (24 * 60 * 60))) +
      f"{duration % 60} сек")

# print(duration//(24 * 60 * 60), ' дн ', duration//(60 * 60)%24, ' час ', duration//60%60, ' мин ', duration%60, ' сек')
