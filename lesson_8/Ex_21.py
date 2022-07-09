"""
Ваша задача — написать функцию, которая будет проверять, является ли предложение палиндромом. Палиндромом — предложение,
 которое читается одинаков слева на право и справа налево.
Функция принимает на вход строку, а возвращает булевое значение True\False
Пример:
is_palindrome('A man, a plan, a canal: Panama') -> True
is_palindrome('0P') -> False
is_palindrome('a.') -> True
"""


import string


def is_palindrome(work_string):
    for el in work_string:
        if el in string.punctuation or el == ' ':
            work_string = work_string.replace(el, '')
    work_string = work_string.lower()
    reversed_string = ''.join(reversed(work_string))
    if work_string == reversed_string:
        palindrome = True
    else:
        palindrome = False
    return palindrome


user_string = input('Введите строку для проверки : ')
# для проверки
# user_string = 'Муза, ранясь шилом опыта, ты помолишься на разум'
print('Введеная строка палиандром? - ', is_palindrome(user_string))
