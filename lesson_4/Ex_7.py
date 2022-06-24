'''
Написать программу, которая перемещает все нули в конец списка.
Ваша задача — изменить список так, что бы нули оказались в конце списка.
Порядок ненулевых чисел должен сохранится.
'''

import random

start_list = []
tmp_list = []
y = 0
while y < 10:
    start_list.append(random.randint(0, 3))
    y += 1
print('Начальный список : ', start_list)
i = 0
while i < len(start_list):
    if start_list[i] == 0:
        tmp_list.append(start_list[i])
        start_list.pop(i)
        i -= 1
    i += 1
start_list += tmp_list
print('Список с нулями в конце : ', start_list)
