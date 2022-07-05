'''
Напишите программу, которая сгенерирует два списка с разным количеством элементов (кол-во формируется рандомно).
Один список с числами кратными 3, другой с числами кратными 5.
С помощью множеств создайте список с числами, которые есть в обоих множествах.
'''
import random


def generate(multiplicity):
    new_list = []
    i = 0
    # Чтобы было больше вхождений взял минимум 20
    while i < random.randint(20, 50):
        if i > 0:
            new_list.append(multiplicity * i)
        i += 1
    return new_list

# сгенерирует два списка с разным количеством элементов
first_list = generate(3)
second_list = generate(5)
# С помощью множеств
first_set = set(first_list)
second_set = set(second_list)
# создайте список с числами, которые есть в обоих множествах
the_same = first_set.intersection(second_set)
final_list = list(the_same)
final_list.sort()

print('Сгенерированный список кратный 3 : ', first_list)
print('Сгенерированный список кратный 5 : ', second_list)
print('Список с числами, которые есть в обоих множествах : ', final_list)
