# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск писанины')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск зарисовки')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск корректировки')


stat_1 = Stationery('Циркуль')
stat_2 = Pencil('Ручка')
stat_3 = Pen('Карандаш')
stat_4 = Handle('Маркер')

stat_1.draw()
stat_2.draw()
stat_3.draw()
stat_4.draw()
