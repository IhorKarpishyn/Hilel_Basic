"""
Вам необходимо написать функцию, которая будет принимать список из чисел и находить среди них уникальное число.
Пример:
find_unique_value([1, 2, 1, 1]) -> 2
find_unique_value([2, 3, 3, 3]) -> 2
find_unique_value([5, 5, 5, 0.5]) -> 0.5
"""

# возвращаю уникальные из списка
def find_unique_value(work_list):
    unique = set(work_list)
    unique_list = []
    count = 0
    for i in unique:
        count = work_list.count(i)
        if count == 1:
            unique_list.append(i)
    return unique_list


unique_numbers = find_unique_value([5, 5, 5, 0.5])
print('Уникальные номера : ', *unique_numbers)
