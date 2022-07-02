'''
Пользователь вводит через дефис две буквы, Ваша задача написать программу, которая будет возвращать все символы между ними включительно.
Никаких проверок на ошибку делать не надо, минимальное значение всегда
меньше или равно максимальному.

Пример:
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
'''
import string

alphabet = string.ascii_letters
final_string = ''

user_string = input('Введите через дефис 2 буквы : ')
start = alphabet.index(user_string[0])
end = alphabet.index(user_string[len(user_string) - 1])
while start < end + 1:
    final_string += alphabet[start]
    start += 1
print(final_string)
