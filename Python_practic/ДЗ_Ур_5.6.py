"""
    6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
    наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.

    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# Импорт модуля re для работы с регулярными выражениями
import re

# Инициализация пустого словаря для отчета
report = {}

# Открытие файла 'task06.txt' для чтения в режиме UTF-8
with open('task06.txt', 'r', encoding='UTF-8') as file:
    # Чтение всего содержимого файла в переменную text
    text = file.read()

    # Возврат указателя чтения на начало файла
    file.seek(0)

    # Построчное чтение файла
    for row in file:
        # Разделение строки на две части: название предмета и описание занятий
        row_items = row.split(': ')

        # Поиск всех чисел в описании занятий с помощью регулярного выражения
        hours = re.findall(r"\d+", row_items[1])

        # Обновление словаря: название предмета и общее количество часов занятий
        report.update({row_items[0]: sum([int(i) for i in hours])})

# Вывод исходного содержимого файла
print(f"Исходный файл:\n{text}\n")

# Вывод словаря, содержащего название предмета и общее количество часов занятий
print(f"Словарь:\n{report}")

# ___________________________
#результаты вычислений
# Исходный файл:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) - 10(лаб)
# Физкультура: - 30(пр)
#
# Словарь:
# {'Информатика': 170, 'Физика': 40, 'Физкультура': 30}