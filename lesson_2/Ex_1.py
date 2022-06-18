'''
Пользователь вводит 4-хзначное число с клавиатуры. Написать программу, которая выводит цифры, из которого это число состоит. Например пользователь вводит 1234, а программа выводит:
1
2
3
4
Задачу необходимо решить используя методы деления (подсказка // и % или divmod).
Число ВСЕГДА 4-хзначное!
'''
# Вариант 1
number = int(input('Enter a four-digit number:'))

if 999 < number < 10000:
    for i in [1000, 100, 10, 1]:
        print(number // i)
        number %= i
else:
    print('Number must be four digits. Bye!')

# Вариант 2
number = input('Enter a four-digit number:')
for i in number:
    print(i)
