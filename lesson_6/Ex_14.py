'''
Ваша задача — написать программу, которая перемножает все цифры, введенного пользователем целого числа, пока оно не
 станет меньше либо равной 9. Число вводит пользователь с клавиатуры, и оно всегда должно быть больше нуля.

Примеры:
999 -> 2 # 999 -> 9 * 9 * 9 = 729 -> 7 * 2 * 9 = 126 -> 1 * 2 * 6 = 12 -> 1 * 2 = 2
1000 -> 0
423 -> 8
1 -> 1
'''

number = input('Введите число : ')

if number.isdigit() and int(number) > 0:
    while int(number) > 9:
        result = 1
        for i in number:
            result *= int(i)
        number = str(result)
    print(number)
else:
    print('Вы не следуете требованиям -  число > 0 ')
