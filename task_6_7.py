import add_sale, show_sales, change_sale
import random

# Возьмём пустой bakery.csv
# Добавим случайных продаж
add_sale.add_sale(*[str(random.randint(1, 10000)/100) for _ in range(15)])
# Добавим конкретных продаж
add_sale.add_sale('1','2', '3', '4')
# Посмотрим на наши продажи и работу функции show_sales()
print('Продажи:')
show_sales.show_sales()
print('Продажи c 5ой:')
show_sales.show_sales('5')
print('Продажи cо 2ой по 4ю:')
show_sales.show_sales('2', '4')
print('Добавим продажу на 323424,6')
add_sale.add_sale('323424,6')
print('Продажи с 12й:')
show_sales.show_sales('12')
# Пдовертим-подкрутим-подшаманим наши продажи
# и посмотрим  работу функции change_sale()
print('Изменим 5ю продажу на 123456789,22')
change_sale.change_sale('5','123456789,22')
print('Посмотрим на 5ю продажу:')
show_sales.show_sales('5','5')
print('Изменим 5ю продажу на 1234567890123456,22)))')
change_sale.change_sale('5','1234567890123456,22')
print('Посмотрим на 5ю продажу:')
show_sales.show_sales('5','5')


