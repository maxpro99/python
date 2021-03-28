# 1.	Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенныхв виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31	22
# 37	43
# 51	86
#
# 3     5	    32
# 2	    4	    6
# -1	64	    -8
#
# 3	    5	    8	    3
# 8	    3	    7	    1
#
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.


class Matrix:
    def __init__(self, *args, rows=None, cols=None):
        # Возьмем по умолчанию rows = 1
        if rows is None and cols is None:
            self.rows = 1
            self.cols = len(args)
        elif rows is not None and cols is None:
            self.rows = rows
            self.cols = len(args) // rows
        elif rows is None and cols is not None:
            self.cols = cols
            self.rows = len(args) // cols
        else:
            self.cols = cols
            self.rows = rows

        # Проверим размерность данных
        if len(args) != self.rows * self.cols:
            raise Exception(f'Invalid matrix dimension '
                            f'row:{self.rows} * col:{self.cols} != {len(args)} (number of elements)')

        # Заполним матрицу
        self.matrix_list = [list(args[x * self.cols:x * self.cols + self.cols]) for x in range(self.rows)]

    # Перегрузим преобразование в строку.
    # Можно было сделать одной строкой,
    # Но так мне читается попроще. Если нет, то надо править.
    def __str__(self):
        matrix_str = ''
        for row in range(self.rows):
            matrix_str += ' '.join(str(_).center(6)
                                   if len(str(_)) < 7 else
                                   str(_)[:5] + '~'
                                   for _ in self.matrix_list[row])
            matrix_str += '\n'
        return matrix_str

    # Перегрузим сложение
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception('Not the same dimension of args Matrix.')
        return Matrix(*[s + o for rs, ro in zip(self.matrix_list, other.matrix_list)
                        for s, o in zip(rs, ro)], rows=self.rows, cols=self.cols)

    # Сделано симпатично
    # B думаю, что такую симпатичность надо делать именно
    # в отдельной функции
    # А в __str__ попроще
    def matrix_table_view(self, length_element=6):
        if length_element < 2:
            raise Exception('Length_element is small, than 2.')
        matrix_str = '\n'
        for row in range(self.rows):
            matrix_str += '-' * ((length_element + 2) * self.cols + 1)
            matrix_str += '\n'
            matrix_str += '| '
            matrix_str += '| '.join(str(_).center(length_element)
                                    if len(str(_)) < (length_element + 1) else
                                    str(_)[:(length_element - 1)] + '~'
                                    for _ in self.matrix_list[row])
            matrix_str += '|'
            matrix_str += '\n'
        matrix_str += '-' * ((length_element + 2) * self.cols + 1)
        matrix_str += '\n'
        return matrix_str



my_matrix_0 = Matrix(1.15366345354, 2, 3, 4, 5, 6, 7, 8, 9, rows=3)
my_matrix_1 = Matrix(31, 22, 37, 43, 51, 86, cols=2)
my_matrix_2 = Matrix(3, 5, 32, 2, 4, 6, -1, 64, -8, rows=3)
my_matrix_3 = Matrix(3, 5, 8, 3, 8, 3, 7, 1, rows=2)

print(my_matrix_0)
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_3)

print(my_matrix_0.matrix_table_view())
print(my_matrix_0.matrix_table_view(2))
print(my_matrix_0.matrix_table_view(15))
print(my_matrix_1.matrix_table_view())
print(my_matrix_2.matrix_table_view())
print(my_matrix_3.matrix_table_view())
print(my_matrix_3.matrix_table_view(2))

print((my_matrix_0 + my_matrix_0).matrix_table_view())

my_matrix_4 = my_matrix_2 + my_matrix_2
print(my_matrix_4.matrix_table_view(4))
