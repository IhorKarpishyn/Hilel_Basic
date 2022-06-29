'''
Пользователь вводит строку, Ваша задача — преобразовать строку в hashtag.
Парочка правил:
никаких символов из набора string.punctuation быть не должно, в том числе и пробелов;
итоговая длина hashtag должна быть не более 140 символов.
Каждое слово начинается с заглавной буквы.
Если длина хэштега более 140 символов - обрезать итоговую строку до 140 символов.

Примеры:
'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
'''

import string

hashtag = '#'
user_string = input('Введите строку : ')
tmp = user_string[:]
for el in tmp:
    if el in string.punctuation:
        tmp = tmp.replace(el, '')
tmp = list(tmp.split())
for el in tmp:
    hashtag += el.capitalize()
#Если длина хэштега более 140 символов - обрезать итоговую строку до 140 символов.
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print('Вы ввели строку : ', user_string)
print('Ваш хэштег : ', hashtag)
