'''
Для списка целых чисел нужно найти сумму элементов с четными индексами [0-й, 2-й, 4-й итд],
затем перемножить эту сумму на последний элемент исходного массива.
Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 [ноль].
[0, 1, 2, 3, 4, 5] => (0 + 2 + 4) * 5 = 30
'''

import random

start_list = []
y = 0
while y < 10:
    start_list.append(random.randint(0, 100))
    y += 1
summa = 0
print('Начальный список : ', start_list)
if start_list:
    for i, el in enumerate(start_list):
        if i % 2 == 0:
            summa += el
    result = summa * start_list[len(start_list) - 1]
else:
    result = 0
print('Сумма элементов с четными индексами : ', summa)
print('Сумма умноженная на последний элемент : ', result)
