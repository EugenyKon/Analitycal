#1.Создать программный файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
# Запрашиваем у пользователя имя файла для сохранения данных
file_name = "Prob_2.txt"  # Вводим имя файла

# Открываем файл для записи
with open(file_name, 'a') as file:
    print("Введите данные для записи в файл. Введите пустую строку, чтобы завершить:")

    # Ввод данных для записи
    data_to_write = "Сегодня пятница, да,да"
    file.write(data_to_write + "\n")
    print("Ввод данных завершен.")

print(f"Данные были и успешно записаны в файл '{file_name}'.")


# Результаты вычислений:
# Введите данные для записи в файл.
# Введите пустую строку, чтобы завершить:
# Ввод данных завершен.
# Данные были успешно записаны в файл 'Prob_2.txt'
# Сегодня пятница
# Сегодня пятница
# Сегодня пятница
# Сегодня пятница
# Сегодня пятница
# Сегодня пятница
# Сегодня пятница, да,да
