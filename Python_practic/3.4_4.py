# First way using operator ** (kwargs)
def my_func_1(x, y):
    result = x ** y
    return result

# Second way without using operator **
# Первый способ: возведение в степень с помощью оператора kwargs
def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result

# ________________________________________________

# Второй способ: более сложная реализация без оператора kwargs, предусматривающая использование цикла
# Input numbers x and y
x = float(input("Enter a positive number x: "))
y = int(input("Enter a negative number y: "))

# Calculate the result using both ways
result_1 = my_func_1(x, y)
result_2 = my_func_2(x, y)

# Print the results
print("Result using operator **: ", result_1)
print("_____________________________________________")
print("Result without using operator **: ", result_2)