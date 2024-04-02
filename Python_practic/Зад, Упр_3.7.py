# Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Используйте написанную
# ранее функцию int_func().
def int_func(word):
    if word.islower() and word.isalpha():
        return word.capitalize()
    else:
        return "Ошибка. Пожалуйста, введите слово из маленьких латинских букв без пробелов и специальных символов."

def capitalize_words_in_string(input_str):
    words = input_str.split()
    capitalized_words = [int_func(word) for word in words]
    return ' '.join(capitalized_words)

# Ввод текстовой строки
user_input = input("Введите строку из слов, разделённых пробелом: ")
print(capitalize_words_in_string(user_input))