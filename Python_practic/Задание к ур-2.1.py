# Задание к Ур 2.1
# Встроенные типы и операции с ними
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list('Обычная строка')
print(list('Обычная строка'))
list('12345678990')
print(list('12345678990'))
print('12345678990')
print('_________')

list('123 456 789 90')
print(list('12345678990'))
print('123 456 789 90'.split())
# Определить тип элементов
print(type(list('123 456 789 90')))

print(type('12345678990'))
print(type('a'))
print(type(9))
print(type(9.1))

# В двоичном формате_тип
print(bin(17))  # -> 0b10001
print(type(bin(17)))

# В восьмеричном формате_тип
print(oct(17))  # -> 0o21
print(type(oct(17)))

# В шестнадцатеричном формате_тип
print(hex(17))  # -> 0x11
print(type(hex(17)))

# В комплексных числах_тип
n_1 = complex(5, 6)
print(n_1)  # (5+6j)
print(type(n_1))


# Результаты вычислений
# ['О', 'б', 'ы', 'ч', 'н', 'а', 'я', ' ', 'с', 'т', 'р', 'о', 'к', 'а']
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']
# 12345678990
# _________
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']
# ['123', '456', '789', '90']
# <class 'list'>
# <class 'str'>
# <class 'str'>
# <class 'int'>
# <class 'float'>
# 0b10001
# <class 'str'>
# 0o21
# <class 'str'>
# 0x11
# <class 'str'>
# (5+6j)
# <class 'complex'>
