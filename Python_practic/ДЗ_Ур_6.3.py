"""
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
    position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
    дохода с учетом премии (get_total_income).

    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        # Инициализация атрибутов класса Worker
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}  # Создание словаря с окладом и премией для дохода


class Position(Worker):
    def get_full_name(self):
        # Метод для получения полного имени сотрудника
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        # Метод для расчета общего дохода с учетом премии
        return sum(self._income.values())  # Суммирование всех значений в словаре для получения общего дохода


vasya = Position('Вася', 'Иванов', 'Программист', 100000, 20000)
print(vasya.get_full_name())  # Вывод полного имени сотрудника
print(vasya.position)  # Вывод должности сотрудника
print("Вася Иванов - оклад =", vasya._income['wage'])  # Вывод оклада сотрудника
print("Вася Иванов - bonus =", vasya._income['bonus'])  # Вывод премии сотрудника
print("Общий доход сотрудника =", vasya.get_total_income())  # Вывод общего дохода сотрудника

#____________________________________
# результаты вычислений
# Вася Иванов
# Программист
# Вася Иванов - оклад = 100000
# Вася Иванов - bonus = 20000
# Общий доход сотрудника = 120000