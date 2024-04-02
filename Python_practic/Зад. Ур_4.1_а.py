# Написать скрипт, в котором должна быть предусмотрена
# функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.
def calculate_salary(hours_worked, hourly_rate, bonus):
    salary = (hours_worked * hourly_rate) + bonus
    return salary

import sys

if len(sys.argv) != 4:
    print("Пожалуйста, введите три параметра: выработка в часах, "
          "ставка в час, премия")
    hours_worked = float(input("Введите количество отработанных часов: "))
    hourly_rate = float(input("Введите почасовую ставку: "))
    bonus = float(input("Введите размер премии: "))
else:
    hours_worked = float(sys.argv[1])
    hourly_rate = float(sys.argv[2])
    bonus = float(sys.argv[3])

total_salary = calculate_salary(hours_worked, hourly_rate, bonus)
print("Заработная плата сотрудника составляет:", total_salary)

# Пример расчета заработной платы при условии отработки 40 часов, ставке 1770 руб. в час и премии
example_salary = calculate_salary(40, 1770, 5000)
print("Пример расчета заработной платы: 40 часов * 1770 руб. + 5000 руб. премии =", example_salary)