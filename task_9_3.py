# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}

class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


python_student = Position('Ivanov', 'Ivan', 'Firestarter', 0, 1000000)
manual_writer = Position('Stupidov', 'Purga-ogly', '-', 100000000, -100000001)

print(python_student.get_full_name())
print(python_student.get_total_income())
print(manual_writer.get_full_name())
print(manual_writer.get_total_income())
