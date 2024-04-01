# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict)
print(my_dict['k_1'])
print(my_dict['k_2'])
print(my_dict['k_3'])
print(my_dict.get('k_4'))
result_my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(result_my_dict)
print('__________')

list = (2, 'text', 456, 45.3, True)
print(list)

result_list = [2, 'text', 456, 45.3, True]
result_list.reverse()
print(result_list)
print('__________')
result_list.insert(3, 1)
print(result_list.insert(3, 1))


