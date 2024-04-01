# Задание_3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл  #число 3. Считаем 3 + 33 + 333 = 369.

number = int(input())
a = int(10 * number + number)
b = int(100 * number + a)
summa = int(number) + a + b

print(summa)