in_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Согласно заданию  дополняем только до двух! целочисленных разрядов
# Знак перед десятичным числом берем любой (*, +, -, x)
print(' '.join([f'"{x:0>2}"' if x.isnumeric() else
                f'"{x[0]}{x[1:]:0>2}"' if len(x) > 1 and x[1:].isnumeric()
                else x for x in in_list]))

# В данном задании пример немного изменен
# чтобы показать, что новое условие только знаки '+' и '-' подходят для определения числа
in_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', 'x5', 'градусов']
print(' '.join([f'"{x:0>2}"' if x.isnumeric() else
                f'"{x[0]}{x[1:]:0>2}"' if len(x) > 1 and (x[0] == '+' or x[0] == '-') and x[1:].isnumeric()
                else x for x in in_list]))

