# Реализовать функцию int_func(), принимающую слова из маленьких
# латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    if word.islower() and word.isalpha():
        return word.capitalize()
    else:
        return "Ошибка. Пожалуйста, введите слово из маленьких латинских букв без пробелов и специальных символов."

# Ввод текстовой строки
user_input = input("Введите слово из маленьких латинских букв: ")
print(int_func(user_input))