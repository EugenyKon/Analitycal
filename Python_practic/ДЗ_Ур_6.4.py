"""
    4. Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

# Создаем базовый класс Car
class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        # Инициализируем атрибуты speed, color, name, is_police
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    # Метод для старта движения машины
    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    # Метод для остановки машины
    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    # Метод для поворота машины
    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')

# Создаем дочерние классы: TownCar, SportCar, WorkCar, PoliceCar
class TownCar(Car):
    def __init__(self, color: str, name: str):
        # Инициализация атрибутов для TownCar
        self.speed = 0
        self.color = color
        self.name = name

    # Переопределение метода show_speed для TownCar
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')

class WorkCar(Car):
    def __init__(self, color: str, name: str):
        # Инициализация атрибутов для WorkCar
        self.speed = 0
        self.color = color
        self.name = name

    # Переопределение метода show_speed для WorkCar
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')

# Дополнительный класс PoliceCar не содержит переопределения метода show_speed


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(f"Тест-драйв {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Kia Optima', False)
test_drive(car)

polo = TownCar('коричневый', 'Volkswagen Polo')
test_drive(polo)

veyron = SportCar('желтый', 'Bugatti Veyron')
test_drive(veyron)

largus = WorkCar('красный', 'Lada Largus')
test_drive(largus)

mondeo = PoliceCar('синий', 'Ford Mondeo')
test_drive(mondeo)

#_____________________________________
# Результаты вычислений
# Тест-драйв гражданского автомобиля Kia Optima, цвет белый
# Разгоняемся до 40 км/ч
# Скорость 40 км/ч
# Поворачиваем направо
# Останавливаемся
# Скорость 0 км/ч
# Не можем повернуть - мы стоим на месте
# Разгоняемся до 60 км/ч
# Скорость 60 км/ч
# Разгоняемся до 120 км/ч
# Скорость 120 км/ч
# Останавливаемся
# Тест-драйв окончен
#
# Тест-драйв гражданского автомобиля Volkswagen Polo, цвет коричневый
# Разгоняемся до 40 км/ч
# Скорость 40 км/ч
# Поворачиваем направо
# Останавливаемся
# Скорость 0 км/ч
# Не можем повернуть - мы стоим на месте
# Разгоняемся до 60 км/ч
# Скорость 60 км/ч
# Разгоняемся до 120 км/ч
# Внимание! Превышение скорости 120 км/ч
# Останавливаемся
# Тест-драйв окончен
#
# Тест-драйв гражданского автомобиля Bugatti Veyron, цвет желтый
# Разгоняемся до 40 км/ч
# Скорость 40 км/ч
# Поворачиваем направо
# Останавливаемся
# Скорость 0 км/ч
# Не можем повернуть - мы стоим на месте
# Разгоняемся до 60 км/ч
# Скорость 60 км/ч
# Разгоняемся до 120 км/ч
# Скорость 120 км/ч
# Останавливаемся
# Тест-драйв окончен
#
# Тест-драйв гражданского автомобиля Lada Largus, цвет красный
# Разгоняемся до 40 км/ч
# Скорость 40 км/ч
# Поворачиваем направо
# Останавливаемся
# Скорость 0 км/ч
# Не можем повернуть - мы стоим на месте
# Разгоняемся до 60 км/ч
# Внимание! Превышение скорости 60 км/ч
# Разгоняемся до 120 км/ч
# Внимание! Превышение скорости 120 км/ч
# Останавливаемся
# Тест-драйв окончен
#
# Тест-драйв полицейского автомобиля Ford Mondeo, цвет синий
# Разгоняемся до 40 км/ч
# Скорость 40 км/ч
# Поворачиваем направо
# Останавливаемся
# Скорость 0 км/ч
# Не можем повернуть - мы стоим на месте
# Разгоняемся до 60 км/ч
# Скорость 60 км/ч
# Разгоняемся до 120 км/ч
# Скорость 120 км/ч
# Останавливаемся
# Тест-драйв окончен