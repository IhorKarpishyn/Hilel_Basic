'''
Даны 2 строки. Необходимо найти индекс второго вхождения искомой строки в строке для поиска.
Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims".
Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать,
что "s" – это самый первый символ в слове "sims", а значит индекс первого вхождения равен 0. Но нам необходимо найти
вторую "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.
Строка, которую нужно найти, может состоять из нескольких символов.
Input: Две строки (String).
Output: Int or None
Примеры:
second_index("sims", "s") == 3
second_index("find the river", "e") == 12
second_index("hi", " ") is None
'''


def second_index(string1, string2):
    count = 0
    index = None
    i = 0
    if len(string2) > 0:
        while i < len(string1):
            if string1[i] == string2[0]:
                count += 1
                if count == 2:
                    tmp_string = string1[i:i + len(string2)]
                    if string2 == tmp_string:
                        index = i
                    else:
                        count -= 1
            i += 1
    if index is not None:
        print(index)
    else:
        print('is None')


user_string = input('Введите строку : ')
find_string = input('Введите что будем искать : ')

second_index(user_string, find_string)
