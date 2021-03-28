# 2. Реализовать проект расчёта суммарного
# расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта —
# одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов
# проекта и проверить работу декоратора @property.


import abc


class AbstractClothes(abc.ABC):
    @abc.abstractmethod
    def tissue_consumption(self):
        pass


class Coat(AbstractClothes):
    def __init__(self, size):
        self.size = size

    # @property
    def tissue_consumption(self):
        return self.size/6.5 + 0.5


class Suite(AbstractClothes):
    def __init__(self, height):
        self.height = height

    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.2


my_coat = Coat(54)
my_suite = Suite(185)
print(my_coat.tissue_consumption())
print(my_suite.tissue_consumption)

# т.е. абстрактные методы не спасают интерфейс от неодинаковости))))))))))
# декораторы... получается портят код?
