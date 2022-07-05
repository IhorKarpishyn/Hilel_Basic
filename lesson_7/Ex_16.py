'''Написать функцию, которая представит человека по переданным параметрам.
Входные данные: Два аргумента строка(str) и положительное число(int)
Функция должна вернуть строку.

say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
'''


def say_hi(n, a):
    n = n.capitalize()
    if a.isdigit() and int(a) > 0:
        hello_text = 'Hi. My name is {name} and I\'m {age} years old'.format(name=n, age=a)
    else:
        hello_text = 'Вы ввели не верно возраст'
    return hello_text


name = input('Введите имя : ')
age = input('Введите возраст : ')

hello = say_hi(name, age)
print(hello)
