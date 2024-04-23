"""
    1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
    в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода.
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""
#  Создается класс Date, который будет использоваться для работы с датами.
import re
#  Задаются списки максимального количества дней в каждом месяце для обычных и високосных годов.
class Date:
    max_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_days_in_month_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# В конструкторе класса Date происходит инициализация объекта,
    # проверка корректности формата переданной даты и разбиение даты на составные части.
    def __init__(self, date_string):
        match_result = re.match(r'^\d\d-\d\d-\d\d\d\d$', date_string)
        if match_result is None:
            raise Exception(f"{date_string} - incorrect date format, use dd-mm-yyyy format")
        self.date_string = date_string
        self.day, self.month, self.year = map(int, date_string.split('-'))
# Метод extract класса Date с декоратором @classmethod извлекает числа-день, месяц, год из переданной даты.
    @classmethod
    def extract(cls, date_string):
        date = cls(date_string)
        return [date.day, date.month, date.year]
# Метод validate класса Date с декоратором @staticmethod проводит валидацию числа, месяца и года.
    @staticmethod
    def validate(date_string):
        date = Date(date_string)
        is_not_zero = date.day > 0 and date.month > 0 and date.year > 0
        if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month_ly[date.month - 1]
        else:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month[date.month - 1]
        return is_not_zero and is_fit_boundaries

# В блоке if __name__ == '__main__' начинается исполнение скрипта.
# Задаются указанные тестовые даты: правильная, невалидная и некорректная.
# Создается объект для правильной даты и выводятся извлеченные числовые данные.
# Создается объект для невалидной даты и выводятся извлеченные числовые данные.
# Обрабатывается исключение, возникающее при передаче некорректной даты.
# Проводится проверка валидности правильной даты и выводится результат.
# Проводится проверка валидности невалидной даты и выводится результат.
if __name__ == '__main__':
    real_date_str = '22-12-1983'
    not_valid_date_str = '29-02-2019'
    incorrect_date_str = '9-02/*019'

    real_date = Date(real_date_str)
    print(f"{real_date.extract(real_date_str)} - extracted numbers")

    not_valid_date = Date(not_valid_date_str)
    print(f"{real_date.extract(not_valid_date_str)} - extracted numbers")

    try:
        incorrect_date = Date(incorrect_date_str)
    except Exception as e:
        print(e)

    if Date.validate(real_date_str):
        print(f"{real_date_str} - valid date")
    else:
        print(f"{real_date_str} - invalid date")

    if Date.validate(not_valid_date_str):
        print(f"{not_valid_date_str} - valid date")
    else:
        print(f"{not_valid_date_str} - invalid date")