'''
Создайте список случайных чисел, со случайным количеством элементов от 3 до 10.
Ваше задача - создать новый список из 3 элементов начального списка -  первым, третьим и вторым с конца .

Пример:
[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
'''

import random

start_list = []
final_list = []
i = 0
while i < random.randint(3, 10):
    start_list.append(random.randint(0, 100))
    if i == 0 or i == 2:
        final_list.append(start_list[i])
    i += 1
final_list.append(start_list[len(start_list)-2])
print('Сгенерированный список: ', start_list)
print('Список - элементы первый, третий и второй с конца: ', final_list)
