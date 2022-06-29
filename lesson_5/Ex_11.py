'''
Пользователь вводит строку. Ваша задача - проверить, может ли эта строка, быть именем переменной.
Переменная не может начинаться с цифры, состоять только из цифр, не может содержать заглавные буквы и знаки пунктуации,
кроме нижнего подчеркивания "_" . Также, она не может быть ни одним из зарегистрированных слов. При этом имя переменной,
может состоять только из одного нижнего подчеркивания "_" .
Зарегистрированные слова можно взять из keyword.kwlist.
В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
_ => True
x => True
get_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
'''
import keyword
import re
import string

is_valid = None
punct_valid = None
count_ = 0
user_string = input('Введите строку ')

# получаю список пунктуации
punct = string.punctuation
# убираю из него '_'
for el in punct:
    if el == '_':
        punct = punct.replace(el, '')
# проверяю есть ли в строке неразрешенные знаки пунктуации из переменной punct
for i in user_string:
    for y in punct:
        if i in y:
            punct_valid = False
    # считаю в этом же цикле количество _ в строке
    if i == '_':
        count_ += 1
# проверяю является ли строка зарезервированным словом
if user_string in keyword.kwlist:
    is_valid = False
# проверяю есть ли Заглавные буквы в строке
elif re.search(r'[A-Z]', user_string) is not None:
    is_valid = False
# "Переменная не может начинаться с цифры, состоять только из цифр...."
# Если будет состоять только из цифр, тогда и первая будет так же цифра, а если первая не цифра тогда и строка уже не состоит только из цифр. Наверное только этой проверки хватит
elif re.search(r'[0-9]', user_string[0]) is not None:
    is_valid = False
# проверяю что знаков _ не более 1 в строке
elif count_ > 1:
    is_valid = False
elif punct_valid is not None:
    is_valid = False
else:
    is_valid = True
print('Вы ввели имя переменной : ', user_string)
print('Валидное ли имя переменной : ', is_valid)
