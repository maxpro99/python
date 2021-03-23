# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево).
# А также методы:
# go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'{self.name} Поехала')


    def stop(self):
        print(f'{self.name} Остановилась')


    def turn(self, direction):
        print(f'{self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.direction} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            print(f'Скорость {self.name} составляет {self.direction} км/ч')
        else:
            print(f'Скорость {self.name} превысила порог 60 км/ч')


class SportCar(Car):
    def _(self):
        pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            print(f'Скорость {name} составляет {self.direction} км/ч')
        else:
            print(f'Скорость {name} превысила порог 40 км/ч')


class PoliceCar(Car):
    def _(self):
        pass


car_1 = TownCar(100, 'Red', 'Leaf', is_police=False)
car_2 = SportCar(110, 'Color', 'MarkII', is_police=True)
car_3 = WorkCar(120, 'Orange', 'Kamaz', is_police=False)
car_4 = PoliceCar(130, 'Blue', 'Vesta', is_police=True)

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()

