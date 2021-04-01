# 3. Осуществить программу работы с органическими клетками,
# состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки
# арифметических операторов:
# сложение (__add__()),
# вычитание (__sub__()),
# умножение (__mul__()),
# деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и округление до целого числа деления клеток соответственно.
#
# Сложение.
# Объединение двух клеток. При этом число ячеек общей
# клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение.
# Создаётся общая клетка из двух. Число ячеек общей клетки —
# произведение количества ячеек этих двух клеток.
#
# Деление.
# Создаётся общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15
# , а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, cellule):
        self.cellule = cellule

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    # Логично для клеток сделать по модулю)
    # Но будем согласно заданию
    def __sub__(self, other):
        if self.cellule <= other.cellule:
            raise Exception('Result is below zero. brrr...')
        return Cell(self.cellule - other.cellule)

    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)

    def __truediv__(self, other):
        return Cell(self.cellule // other.cellule) if self.cellule // other.cellule > 0 else 1/0

    def make_order(self, n):
        return ''.join([((('*' * n + '\n') * (self.cellule // n)) + '*' * (self.cellule % n)).rstrip()])


my_cell_0 = Cell(6)
print('my_cell_0 = Cell(6) --> my_cell_0.make_order(3)')
print(my_cell_0.make_order(3))

my_cell_1 = Cell(7)
print('my_cell_1 = Cell(7) --> my_cell_1.make_order(2)')
print(my_cell_1.make_order(2))

my_cell_2 = Cell(2)
print('my_cell_2 = Cell(2) --> my_cell_2.make_order(4)')
print(my_cell_2.make_order(4))

print('(my_cell_2 + my_cell_0).make_order(10)')
print((my_cell_2 + my_cell_0).make_order(10))

my_cell_3 = my_cell_1 - my_cell_2
print('my_cell_3 = my_cell_1 - my_cell_2 --> my_cell_3.make_order(2)')
print(my_cell_3.make_order(2))

print('(my_cell_2 * my_cell_0).make_order(10)')
print((my_cell_2 * my_cell_0).make_order(10))

print('((my_cell_0 + my_cell_2) * my_cell_1 / my_cell_0).make_order(10)')
print(((my_cell_0 + my_cell_2) * my_cell_1 / my_cell_2).make_order(10))
