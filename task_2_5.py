# заполняем случайными ценами

from random import randint

# Заполним "от руки" для проверки "крайних" случаев
price_in_penny = [0, 1, 100, 101, 1000]
for var_i in range(11):
    price_in_penny.append(randint(0, 100000))


# задание A
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# Мы возьмём форматЪ 00 руб. 00 коп.
for price in price_in_penny:
    print(f"{price//100:0>2} руб. {price%100:0>2} коп.", end=', ')
print()
print('----------------')


# задание B
# Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print('Сортируем по возрастанию в том же списке')
print('price_in_penny id before sort():', id(price_in_penny))
price_in_penny.sort()
print('price_in_penny id after sort() :', id(price_in_penny))
for price in price_in_penny:
    print(f"{price//100:0>2} руб. {price%100:0>2} коп.", end=', ')
print()
print('----------------')


# задание C
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('Сортируем по убыванию в новом списке')
print('price_in_penny id before sort():', id(price_in_penny))
price_in_penny_sorted = sorted(price_in_penny, reverse=True)
print('price_in_penny_sorted id       :', id(price_in_penny_sorted))
for price in price_in_penny_sorted:
    print(f"{price//100:0>2} руб. {price%100:0>2} коп.", end=', ')
print()
print('----------------')


# задание D
# Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
for price in price_in_penny_sorted[4::-1]:
    print(f"{price//100:0>2} руб. {price%100:0>2} коп.", end=', ')
