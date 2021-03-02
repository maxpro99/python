import utils

# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
#
# Написали, перенесли, создали, импортировали
# Что-то происходит!!!!
# Вроде ничего лишнего

print(*utils.currency_rates('AZN', 'AMD'))
print(*utils.currency_rates('tmt', 'AMD'))
print(utils.currency_rates('uah', 'uzs', 'krw'))
print(utils.currency_rates('uah', 'czK'))
print(*utils.currency_rates('uah'))
print(*utils.currency_rates('xxx'))
print(utils.currency_rates('xxx'))
print(utils.currency_rates())
print(*utils.currency_rates())
